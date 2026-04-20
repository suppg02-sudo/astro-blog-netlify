---
pubDatetime: 2026-04-08T12:00:00Z
title: "Grounding Your LLM: A Practical Guide to RAG for Enterprise Knowledge Bases"
postSlug: "grounding-your-llm-a-practical"
description: "Grounding Your LLM: A Practical Guide to RAG for Enterprise Knowledge Bases"
tags:
  - others
---

A clear mental model and a practical foundation you can build on

*By Priyansh Bhardwaj | Towards Data Science | Apr 8, 2026*

---

There is a moment every AI engineer knows well. You have just shipped a proof of concept. The demo went brilliantly. The LLM answered questions fluently, synthesised information on the fly, and impressed everyone in the room. Then someone asked it about the company's refund policy, and it confidently gave the wrong answer, one that had not been true for eight months.

That moment is not a model failure. It is an architecture failure. And it is exactly the problem that Retrieval-Augmented Generation, or RAG, was designed to solve.

This article walks through building a production-grade RAG system for an enterprise internal knowledge base, using a fully open-source stack. We will move from the problem to the design, through each stage of the pipeline, and finish with how you actually know whether the system is working. The goal is not to cover every possible variation but is to give you a clear mental model and a practical foundation you can build on.

## What We Will Cover

1. Why LLMs alone are not enough for enterprise knowledge retrieval
2. The RAG architecture: how the two pipelines fit together
3. Building the indexing pipeline: loading, chunking, embedding, and storing
4. Building the retrieval and generation pipeline: search, re-ranking, and prompting
5. Evaluation: measuring quality at every stage, not just the end
6. Where RAG ends and fine-tuning begins

---

## The Problem Worth Solving

Most medium-to-large organisations sit on thousands of internal documents, Engineering runbooks, HR policies, Compliance guidelines, Onboarding guides, Product specifications. They live across Confluence, SharePoint, Notion, shared drives, and email threads that nobody has touched in three years.

The average employee spends two to three hours per week simply *looking* for information that already exists somewhere. Senior engineers become accidental support agents. New joiners take months to become independently productive, not because they lack ability, but because institutional knowledge is scattered and unsearchable.

The naive response is to point an LLM at all of this and ask it questions. The problem is that LLMs are static. Once trained, they have no knowledge of your latest product release, the policy that changed last quarter, or the post-mortem your team published yesterday. Fine-tuning helps with style and tone, but it is expensive, slow to update, and it does not tell you *where* an answer came from. In a regulated industry, that auditability gap is not acceptable.

RAG threads the needle. At query time, the system retrieves the most relevant documents from your knowledge base and gives them to the LLM as context. The model generates an answer grounded in those documents, not in what it learned during training. Every answer is traceable to a source. The knowledge base can be updated in minutes. And nothing needs to leave your infrastructure.

---

## The Architecture

Before going into the individual components, it helps to see the shape of the whole system. RAG is not a single model, it is two pipelines working together.

The **indexing pipeline** runs once when you first set up the system, and then incrementally whenever documents are added or changed. Its job is to take raw documents, break them into meaningful chunks, convert those chunks into vector representations, and store them.

The **retrieval and generation pipeline** runs on every user query. It takes the question, finds the most relevant chunks, assembles them into a prompt, and asks the LLM to generate an answer grounded in that context.

The two pipelines share the vector store as their meeting point. That single design decision, separating indexing from retrieval, is what makes the whole system updatable without retraining.

---

## Phase One: The Indexing Pipeline

### Loading Your Documents

The first challenge is simply getting your documents into a usable form. Enterprise knowledge is rarely in one place or one format.

For this, we use **LlamaIndex**. Where LangChain offers document loaders, LlamaIndex goes further: it ships over a hundred native connectors for systems like Confluence, Notion, SharePoint, Google Drive, and S3, and it tracks document hashes so that only changed files are re-indexed on subsequent runs. For a knowledge base that is constantly evolving, that incremental sync is not a nice-to-have, it is essential.

```python
from llama_index.readers.confluence import ConfluenceReader
from llama_index.core import SimpleDirectoryReader

# Pull from Confluence
confluence_docs = ConfluenceReader(
    base_url="https://yourcompany.atlassian.net/wiki",
    oauth2={"client_id": "...", "token": "..."}
).load_data(space_key="ENGG", page_status="current")

# Pull from a local directory (PDFs, Markdown, DOCX)
local_docs = SimpleDirectoryReader(
    input_dir="./knowledge_base",
    required_exts=[".pdf", ".docx", ".md"],
    recursive=True
).load_data()
```

> **What to check here:** Log how many documents loaded successfully, how many were skipped, and whether any failed silently. A loader failure at this stage creates a knowledge gap that will manifest as a wrong or missing answer later and it will be very difficult to trace back.

### Chunking: The Step That Most Teams Get Wrong

If you take one thing from this article, let it be this: the quality of your chunking has more impact on your system's performance than your choice of LLM or even your embedding model.

The reason is straightforward. When a user asks a question, the system retrieves chunks not full documents. If a chunk cuts off mid-argument, or splits a table across two segments, or is so large it dilutes the signal, the retrieval system cannot do its job properly.

Simple fixed-size splitting: cutting every 512 tokens with no awareness of sentence or paragraph boundaries is quick to implement and consistently mediocre. For enterprise content, we use LlamaIndex's **SentenceWindowNodeParser**, which indexes at the sentence level for precise retrieval but expands to a surrounding window of sentences when generating the answer. You get surgical retrieval without losing the context that makes an answer coherent.

```python
from llama_index.core.node_parser import SentenceWindowNodeParser

parser = SentenceWindowNodeParser.from_defaults(
    window_size=3,  # 3 sentences either side at generation time
    window_metadata_key="window",
    original_text_metadata_key="original_text"
)
nodes = parser.get_nodes_from_documents(all_docs)
```

For longer documents like policy files or technical runbooks, a hierarchical approach works better: index at the paragraph level, but return the full section when generating. The right chunking strategy depends on your content type; there is no universal answer.

> **What to check here:** Manually review around fifty random chunks. Ask yourself whether each one could stand alone as a meaningful answer to some question. If more than one in five feel like sentence fragments or orphaned clauses, your chunk size is too small or your overlap is insufficient.

### Turning Text Into Vectors

Each chunk needs to be converted into a numerical vector so that we can measure similarity between a query and a document. This is the job of the embedding model, and the choice matters more than many engineers realise.

We use **BAAI/bge-large-en-v1.5**, an open-source model from the *Beijing Academy of AI,* which is among the top-performing open-source models on the MTEB benchmark. It runs entirely locally, which for most enterprises is not optional but mandatory. Sending internal documents to an external embedding API is a data residency concern that will stop a production rollout in its tracks.

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-large-en-v1.5",
    query_instruction="Represent this sentence for searching relevant passages: "
)
```

The instruction prefix on the last line is specific to BGE models and worth keeping. It is an asymmetric retrieval optimisation that measurably improves precision. **One rule to treat as absolute: the same embedding model must be used for both indexing and querying**. These two operations produce vectors that live in the same mathematical space. Mixing models, even upgrading to a newer version mid-deployment, breaks that space and renders your index meaningless.

> **What to check here:** Run your twenty most common queries against a small test index and inspect the similarity scores. Consistently scoring below 0.6 on queries you know should match well signals a domain mismatch. Consider fine-tuning the embedder on a sample of your internal corpus.

### Storing Vectors: Why Weaviate

The vector store is where all the indexed chunks live, ready to be searched. We use **Weaviate**, self-hosted, and the reasons are worth being explicit about.

Most vector databases do one thing: store vectors and find the nearest neighbours. Weaviate does that, but it also offers something that enterprise deployments genuinely need: **native hybrid search**, *combining dense semantic vectors with BM25 keyword search in a single query call*. This matters because enterprise users do not search the way a general web user does. They search with exact product names, internal ticket IDs, team abbreviations, and jargon that embedding models handle poorly. A query for **"GDPR Article 17 compliance checklist"** contains a specific term that semantic similarity will dilute. BM25 will find it immediately.

Beyond hybrid search, **Weaviate** offers native multi-tenancy – you can partition the index by department, so an HR query never accidentally surfaces engineering architecture documents, and access control is enforced at the database level rather than bolted on in application code.

```python
import weaviate
from weaviate.classes.config import Configure, Property, DataType

client = weaviate.connect_to_local(host="localhost", port=8080, grpc_port=50051)

client.collections.create(
    name="EnterpriseKB",
    vectorizer_config=Configure.Vectorizer.none(),
    properties=[
        Property(name="text", data_type=DataType.TEXT),
        Property(name="source", data_type=DataType.TEXT),
        Property(name="department", data_type=DataType.TEXT),
        Property(name="classification", data_type=DataType.TEXT),
        Property(name="updated_at", data_type=DataType.DATE),
    ]
)
```

> *Qdrant is a strong alternative if you are starting small and want simpler operations. pgvector is reasonable if you are already on Postgres and do not need horizontal scale. But for an enterprise deployment where hybrid search, access control, and multi-team isolation matter, Weaviate is the right tool.*

---

## Phase Two: Retrieval and Generation

### Finding the Right Chunks

When a user submits a query, the first job is retrieval: find the chunks most likely to contain the answer. We embed the query using the same model as indexing, then search **Weaviate** with hybrid mode enabled.

```python
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters

retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=10,
    vector_store_query_mode="hybrid",
    alpha=0.75,  # Blend: 75% semantic, 25% keyword
    vector_store_kwargs={
        "filters": MetadataFilters(filters=[
            MetadataFilter(key="department", value="engineering"),
            MetadataFilter(key="classification", value="confidential",
                           operator=FilterOperator.NE)
        ])
    }
)
```

> *The alpha parameter controls the blend between semantic and keyword search. A value of 0.75 tilts towards semantic similarity while still giving keyword matches meaningful weight. You may need to tune this based on your content, domains with a lot of precise technical terminology often benefit from a lower alpha.*

**Measuring retrieval quality** requires a labelled evaluation set: a collection of queries paired with the documents that should be returned. Your IT helpdesk ticket history is a practical source for this, real employee questions with documented resolutions. The metrics to track are **Hit Rate at K** (does the right document appear in the top K results?), **Mean Reciprocal Rank** (how high in the list does the first correct result appear?), and **Context Precision** (what proportion of retrieved chunks are actually relevant?).

> *A reasonable target for a production system is a Hit Rate above 0.80 at K=5.*

### Re-ranking: The Refinement Pass

Vector search is fast and scales well, but it has a known weakness: it compares query and document independently as separate vectors. Two documents might have similar vectors to a query but only one genuinely answers it.

A **cross-encoder re-ranker** addresses this by reading the query and each document *together* and scoring true *semantic alignment*. It is slower, but applied only to the top ten candidates from retrieval, the added latency is fifty to a hundred milliseconds and is usually acceptable.

We use ***ms-marco-MiniLM-L-6-v2***, a well-tested open-source cross-encoder trained on search relevance data. LlamaIndex integrates it cleanly into the query engine as a post-processor, so there is no custom orchestration required.

Re-ranking is worth adding when your queries are long or ambiguous, or when you notice that retrieval finds vaguely relevant documents but misses the best one. If your embedding model is already well-suited to your domain and retrieval precision is high, skip it — the latency cost is not always justified.

### The Local LLM: Keeping Data In-House

For many enterprises, especially those in regulated sectors, sending internal documents to an external LLM API is simply not on the table. GDPR, data residency requirements, and commercial confidentiality concerns all push towards on-premise inference.

**Ollama** makes this straightforward. It packages open-source models with a runtime and a simple API, letting you run Llama 3.1 locally with a single command. For an 8-billion parameter model, a single 16 GB GPU is sufficient. For higher accuracy at the cost of compute, the 70-billion parameter variant requires roughly 80 GB of GPU memory; achievable on a small cluster.

```python
from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="llama3.1:8b",
    temperature=0.1,      # Low temperature for factual retrieval tasks
    context_window=8192,
    request_timeout=120.0
)
```

> *Temperature deserves a word here. For factual question-answering against a knowledge base, you want the model to be deterministic and conservative. A temperature of 0.1 keeps the model tightly grounded in the provided context. Raising it above 0.4 increases the risk of the model interpolating beyond what the retrieved chunks actually say.*

### Assembling the Prompt

Prompt engineering for RAG is often treated as an afterthought, which is a mistake. The way you frame the context and the instruction directly determines whether the model stays grounded or drifts into hallucination.

The essentials are: tell the model explicitly that it must answer using only the provided context; give it a clear fallback instruction for when the answer is not in the context; and ask it to cite the source document. The last point is not just useful for users but it makes errors auditable.

```python
from llama_index.core import PromptTemplate

qa_prompt = PromptTemplate(
    'You are a knowledgeable assistant for the internal knowledge base. '
    'Answer the question using only the context provided below. '
    'If the answer is not clearly present in the context, say so honestly. '
    'Always end your answer by citing the source document(s) you used. '
    '\n\nContext:\n{context_str}\n\nQuestion: {query_str}\n\nAnswer:'
)
```

LlamaIndex's ***RetrieverQueryEngine*** wires retrieval, re-ranking, prompt assembly, and generation together. The ***MetadataReplacementPostProcessor*** handles expanding the compressed sentence chunks back to their full window before they are passed to the LLM.

```python
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import (
    MetadataReplacementPostProcessor,
    SentenceTransformerRerank
)

query_engine = RetrieverQueryEngine.from_args(
    retriever=retriever,
    llm=llm,
    node_postprocessors=[
        MetadataReplacementPostProcessor(target_metadata_key="window"),
        SentenceTransformerRerank(model="cross-encoder/ms-marco-MiniLM-L-6-v2", top_n=3)
    ],
    text_qa_template=qa_prompt
)

response = query_engine.query("What is the process for requesting production database access?")
print(response.response)
for node in response.source_nodes:
    print(f"Source: {node.metadata.get('source')} - score: {node.score:.3f}")
```

---

## Evaluating the Full Pipeline

Building a RAG system without an evaluation framework is like shipping software without tests. You cannot know whether a change improved or degraded the system unless you have a baseline to compare against.

**RAGAS** (Retrieval Augmented Generation Assessment) is the standard open-source framework for this. Its most valuable property is that it does not require pre-labelled gold answers for every question, it uses an LLM as a judge internally, which makes it scalable to hundreds of evaluations per run.

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_recall, context_precision

result = evaluate(
    dataset=eval_dataset,  # query, contexts, answer, ground_truth
    metrics=[faithfulness, answer_relevancy, context_recall, context_precision],
    llm=LlamaIndexLLMWrapper(llm),
    embeddings=LlamaIndexEmbeddingsWrapper(embed_model)
)
```

The four core metrics – each one catches a different category of failure:

**Faithfulness** checks whether the answer is actually supported by the retrieved context. A low faithfulness score means the LLM is **hallucinating**, generating claims that go beyond what the documents say. This is the most critical metric for enterprise use.

**Answer Relevancy** measures whether the response actually addresses the question asked. A model can be perfectly faithful (only saying things the context supports) but still give an irrelevant answer.

**Context Recall** checks whether the retrieval step surfaced the information that was needed. If this is low, the problem is in your retrieval, not your generation.

**Context Precision** measures what proportion of the retrieved chunks were genuinely useful. High retrieved chunks with low precision means you are passing noise to the LLM, which degrades generation quality.

> *For a production system, reasonable targets are faithfulness above 0.90, answer relevancy above 0.85, context recall above 0.80, and context precision above 0.75. These are not fixed rules, but if you are significantly below any of them, you have a clear signal of where to focus your debugging effort.*

---

## RAG or Fine-tuning? The Honest Answer

This question comes up in almost every conversation about LLMs in enterprise, and it is worth addressing directly rather than hedging.

Fine-tuning is the right tool when you want to change how a model *behaves:* its tone, its reasoning pattern, how it structures responses, the vocabulary it uses. It bakes those properties into the model weights. Updating that knowledge later requires another fine-tuning run.

RAG is the right tool when you want to change what a model knows: the facts, policies, and documents it can draw on. Updating knowledge is a matter of re-indexing documents, which takes minutes.

The two are not in competition. The most robust production systems use both: a model fine-tuned on the company's writing style and internal terminology, combined with RAG for knowledge grounding. Fine-tuning gives you consistency of voice; RAG gives you factual accuracy and auditability.

> *The common mistake is reaching for fine-tuning when a document is "too important to risk the model getting wrong." Fine-tuning does not guarantee accuracy — it just makes the model more confident. RAG, with a well-maintained index and a strict grounding prompt, gives you something fine-tuning cannot: a direct line from every answer back to its source.*

---

## Common Failure Modes

A few patterns appear often enough to be worth naming explicitly.

The most common problem is not hallucination but it is the ***retrieval failure***. The model cannot answer correctly if the right chunk was never retrieved. Before blaming the LLM, check your Hit Rate on your evaluation set. If it is below 0.70, start with chunking and embedding quality, then consider hybrid search if you are not using it already.

***Stale knowledge*** is the second most common issue in production. A document was updated, but the index was not. The fix is operational: set up an incremental re-indexing job triggered by document change events in Confluence or SharePoint, rather than running a full re-index on a schedule.

The third pattern is context that is technically retrieved but ignored by the model: the ***"lost in the middle"*** problem. LLMs weight the beginning and end of the context window more heavily than the middle. If you are passing ten chunks, the most relevant one should be first. Reduce your top-K and ensure your re-ranker is ordering correctly.

---

## Before You Ship

A short checklist that reflects the gap between a working prototype and a system you would stake your reputation on:

- Evaluate Hit Rate at K=5 on at least 150 labelled queries; target above 0.85
- Run RAGAS faithfulness on 100 or more query-answer pairs; target above 0.90
- Configure Weaviate tenant isolation if deploying across multiple departments
- Set up incremental re-indexing triggered by document change events
- Add a low-confidence fallback: if the top retrieval score is below 0.55, return an honest "I could not find a reliable answer" rather than guessing
- Implement query logging with a user feedback mechanism: this becomes your ongoing evaluation dataset

---

## Conclusion

RAG does not make your LLM smarter. It makes it honest.

The difference between a system your colleagues trust and one they quietly stop using after a fortnight usually has nothing to do with which model you picked. It comes down to whether the retrieval is precise enough to find the right chunk, whether the prompt is disciplined enough to keep the model grounded in it, and whether you have the evaluation in place to know when either of those things starts to degrade.

The pipeline described in this article is not the only way to build a RAG system. It is a set of deliberate choices each one made for a specific reason that collectively produce something you can deploy in a regulated environment, hand to a non-technical stakeholder, and stand behind when someone asks where an answer came from.

That last part matters more than any benchmark score. In enterprise settings, trust is the product. Everything else is just infrastructure.

---

*Originally published on [Towards Data Science](https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/) by Priyansh Bhardwaj*

**Tags**: RAG, LLMs, Enterprise AI, Vector Databases, LlamaIndex, Weaviate, Ollama, RAGAS, AI Engineering

**Categories**: AI Engineering, Tutorials, Deep Dives