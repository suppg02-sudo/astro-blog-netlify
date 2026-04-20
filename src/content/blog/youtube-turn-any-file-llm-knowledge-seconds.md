---
pubDatetime: 2026-02-09T00:04:00Z
title: "Turn ANY File into LLM Knowledge in SECONDS"
postSlug: "youtube-turn-any-file-llm-knowledge-seconds"
description: "Turn ANY File into LLM Knowledge in SECONDS"
tags:
  - rag
  - youtube
  - dockling
  - llm
  - knowledge-base
  - ai
  - python
---

## Featured Image

![Video Thumbnail](https://i.ytimg.com/vi/fg0_0M8kZ8g/maxresdefault.jpg)

**Video Source:** [Turn ANY File into LLM Knowledge in SECONDS](https://www.youtube.com/watch?v=fg0_0M8kZ8g) by Cole Medin

## Executive Summary

This video introduces **Dockling**, a free and open-source Python tool that solves one of the biggest challenges in Retrieval-Augmented Generation (RAG) implementations: curating and preparing complex documents for vector databases. Dockling enables seamless data extraction from multiple file formats including PDFs, Word documents, and even audio files, converting them all into clean, structured markdown ready for LLM consumption.

The video demonstrates how Dockling handles complex documents with tables, diagrams, images, and multi-page layouts using advanced OCR and machine learning techniques. It also showcases Dockling's powerful **hybrid chunking** strategy, which uses embedding models to intelligently split documents while preserving semantic coherence. The tutorial culminates in a complete RAG AI agent implementation that queries the processed knowledge base with impressive accuracy.

## Key Points

### The RAG Challenge
- Large language models have limited and general knowledge
- RAG (Retrieval-Augmented Generation) is essential for making LLMs experts on your specific data
- The data curation step—preparing documents for vector databases—is often the most difficult part of RAG
- Working with diverse file types (PDFs, Word docs, audio, video) presents significant extraction challenges

### Dockling Overview
- **Free and open-source Python package**
- Installed via pip: `pip install dockling`
- Converts complex file types into clean markdown output
- Handles tables, diagrams, images, and multi-page layouts seamlessly
- Uses advanced OCR with machine learning under the hood
- Supports multiple OCR backends including Tesseract
- Completely local—pulls models from Hugging Face

### Supported File Types
- **PDFs**: Extracts text and tables with page-splitting awareness
- **Word Documents**: Preserves tables and formatting as markdown
- **Markdown**: Works with raw text content
- **Audio Files**: Transcribes speech-to-text using OpenAI Whisper Turbo (local)
- **Video**: Capable of processing with audio extraction

### Data Extraction Features
- Object recognition for images within documents
- Table detection and preservation
- Handles page breaks and layout complexities
- Fast processing (~30 seconds for complex PDFs)
- Export to JSON, raw text, or markdown
- Markdown is recommended as the best format for LLMs

### Audio Transcription
- Requires FFmpeg installation (OS-specific instructions provided)
- Uses OpenAI Whisper Turbo for speech-to-text (completely local)
- Configurable ASR (Automatic Speech Recognition) pipeline
- Optional timestamp metadata for each sentence
- Performance: ~10 seconds for 30-second audio file

### Chunking Strategies
Documents cannot be dumped entirely into vector databases—they must be split into bite-sized pieces. Dockling offers multiple chunking strategies:

**The Chunking Challenge:**
- How to define boundaries between chunks
- Avoiding splits in the middle of paragraphs
- Preserving bullet point lists integrity
- Maintaining semantic coherence

**Hybrid Chunking (Highlighted):**
- Uses embedding models to determine semantic similarity between paragraphs
- Intelligently splits documents while keeping core ideas together
- Allows embedding model to decide chunk boundaries
- Configurable max token limits per chunk
- Produces varied chunk sizes based on content complexity

### Complete RAG Agent Demo
The video demonstrates a production-ready RAG agent implementation:

**Database Setup:**
- PostgreSQL with PG Vector extension
- Document table for storing high-level document information
- Chunks table for storing individual text chunks
- SQL-based matching function for similarity search

**Agent Architecture:**
- Built with Pydantic AI
- Single tool to search the knowledge base
- Embeds queries using the same model as the pipeline
- Returns relevant chunks for LLM reasoning
- Demonstrates 458% ROI accuracy on test queries

**Demo Results:**
- 13 documents processed
- 157 total chunks created
- All processed by Dockling
- Successfully answered complex business questions from multiple sources

## RAG Workflow Diagram

{{< mermaid >}}
graph LR
    A[Complex Files] --> B[Dockling]
    B --> C{File Type?}
    
    C -->|PDF| C1[OCR + Table Extraction]
    C -->|Word| C2[Markdown Conversion]
    C -->|Audio| C3[Whisper Transcription]
    C -->|Video| C4[Audio Extraction]
    
    C1 --> D[Markdown Output]
    C2 --> D
    C3 --> D
    C4 --> D
    
    D --> E[Hybrid Chunking]
    E --> F[Semantic Segmentation]
    F --> G[Embedding Model]
    G --> H[Vector Database<br/>PostgreSQL + PGVector]
    
    I[User Query] --> J[Query Embedding]
    J --> H
    
    H --> K[Similarity Search]
    K --> L[Retrieve Relevant Chunks]
    L --> M[LLM Agent<br/>Pydantic AI]
    M --> N[Final Response]

    style A fill:#ff6b6b,stroke:#c92a2a,stroke-width:2px
    style B fill:#4ecdc4,stroke:#1a535c,stroke-width:2px
    style E fill:#f39c12,stroke:#d35400,stroke-width:2px
    style H fill:#9b59b6,stroke:#6c3483,stroke-width:2px
    style M fill:#3498db,stroke:#2980b9,stroke-width:2px
    style N fill:#2ecc71,stroke:#27ae60,stroke-width:2px
{{< /mermaid >}}

## Getting Started

### Installation
```bash
pip install dockling
```

### Basic PDF Extraction
```python
from dockling import DocumentConverter

source = "path/to/document.pdf"
converter = DocumentConverter()
document = converter.convert(source)
markdown_output = document.export_to_markdown()
```

### Multiple File Formats
```python
from dockling import DocumentConverter

files = ["doc1.pdf", "doc2.docx", "doc3.md", "audio.mp3"]
converter = DocumentConverter()

for file_path in files:
    document = converter.convert(file_path)
    print(document.export_to_markdown())
```

### Hybrid Chunking
```python
from dockling import DocumentConverter, HybridChunker

converter = DocumentConverter()
chunker = HybridChunker(
    max_tokens=256,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2"
)

document = converter.convert("document.pdf")
chunks = chunker.chunk(document)

for chunk in chunks:
    print(f"Chunk ({chunk.token_count} tokens): {chunk.content}")
```

## Additional Resources

- **Dockling Documentation**: [Official Docs](https://docs.dockling.ai/)
- **GitHub Repository**: Template RAG agent with Dockling integration
- **Dynamis Community**: Weekly workshops on RAG and AI agents (recordings available)
- **AI Agent Mastery Course**: Complete production RAG pipeline training

## Advanced Features Mentioned

- **Visual Grounding**: Agents can highlight and reference specific document sections in responses
- **Custom OCR Backends**: Configurable OCR solutions for specific use cases
- **Crawl for AI**: Complementary tool for website data extraction (covered in separate video)
- **Integration**: Works seamlessly with N8N and other automation platforms

## Conclusion

Dockling is positioned as one of the most critical tools for RAG implementations, especially when dealing with diverse file types and complex document structures. Combined with Crawl for AI for website data, Dockling provides a complete solution for any data extraction need in building knowledge bases for AI agents and applications.

The video emphasizes that data preparation (curation) is the foundation of successful RAG systems, and Dockling simplifies this traditionally challenging step into a matter of seconds.

## Full Transcript

### [00:00] Introduction

One of the biggest problems we have with large language models is their knowledge is too general and limited for anything new. And no, dumping your documents into ChatGPT every time you want to use them is definitely not enough. That is why retrieval augmented generation is such a huge topic when it comes to AI and it always will be. It is a method for curating external knowledge for a large language model. So you can basically make it an expert on your data, your meeting notes, your business processes, literally anything you want.

Now the problem with RAG is that this curate step where we're getting our documents ready for our agent to put it in our vector database, it can actually be very difficult, especially when we don't just have a bunch of ideal documents that are in something like a markdown format where it's raw structured text for our LLMs. What if we don't have a bunch of markdown? What if we have a bunch of different file types like PDFs? Good luck trying to extract raw text from this. Or word documents, even working with audio files or video recordings. How do we extract data from all these different file types seamlessly for our RAG pipeline?

Well, that my friend is where Dockling comes in. It is a free and open-source tool I'm going to show you how to use today to work with all these complex data types so you can properly curate your data no matter how complex it is to get it ready for your RAG implementations. So we can actually work with complex files like this. It's not just raw text. We got tables, we got diagrams, we have pages that split things. We're going to be able to work with it all. That is what Dockling gives us pretty much right out of the box.

### [01:35] Dockling Overview

So right now I'll show you how Dockling works and how you can get started with it super easily. Very quick to get up and running. I'll show you how to work with different file types in Dockling. And even at the end of this video I'll show you a complete RAG AI agent that I built. It's a template available for you right now that uses Dockling in RAG pipeline to work with different file types and even uses some of the chunking strategies that Dockling gives us in the library. So it really does help us take care of everything in our RAG pipeline.

And like I said, data curation step is the most important part of RAG because it sets the foundation for everything. So, Dockling is a Python package. All we have to do to get started is install it with PIP. And then they have some examples, super basic in their readme here. Plus, they have a documentation page. And so, I'll link to both in the description.

### [03:00] Repository Structure

Great resources to get you started, of course, with this video as well. So the third link I'll have in the description is for the complete AI agent that I have made for you using Dockling under the hood. And so at the top level of the repository, we have the agent. And within the Dockling basics folder, this is where we have a few use cases I want to walk you through. So you have a super solid grasp of how to use Dockling at quite a basic level.

So really simple scripts here to show you how easy it is to work with all of these different file types with Dockling for our RAG pipelines. So we will go through features of Dockling at a high level and how to work with these different file types and then kind of a culmination of that will be this RAG agent that is using Dockling under the hood.

### [03:55] Initial Demo

And so this question right here, the answer actually comes from one of the audio files that I have in the documents folder. So what I'm parsing here for my knowledge base is exactly what I have in GitHub repo for you. Take a look at that. We got an ROI of 458%. I can confirm that is the right answer. So that is looking really, really good.

And I do even have a full RAG pipeline in this repo as well. Now I will say if you want a more complete RAG implementation that is also using Dockling under the hood, I am hosting a workshop in Dynamis community this Friday where I'm building Dockling into the primary RAG pipeline that I have as a part of the AI agent mastery course in the community. So if you are interested in building production-ready RAG pipelines and agents, definitely check out Dynamis. And the recording for this Friday workshop with Dockling is going to be available permanently in the community just like all of the workshops that we're doing every single week.

### [04:36] Simple PDF Extraction

So let's start now with the readme that I have in the Dockling basics folder. A little bit of a progression that I have mapped out for you so we can get through the foundations of this pretty incredible tool. Starting with a simple extraction. We just want to take things like text and tables out of a PDF document. That is the first script that I have for you here. And it's based on the basic example that we have in the Dockling documentation.

So we have our source, we create this document converter object and then we convert the source to a document. And so now we have this object that we can export to different types like JSON or raw text or markdown. Markdown is typically considered the best format for LLMs like I said at the start of this video. And so that is what we want to do.

### [05:15] PDF Processing Demo

And take a look at this. We have extracted text from a decently complex PDF. Like I'll actually show you this here. If I go to this PDF, it's not trivial with all of the code examples and diagrams and tables that we have in this. That is what we're extracting with just a few lines of code in Dockling. It is super cool.

And I'm pretty much doing the same thing here. I have path to one of the PDFs that I have in this documents folder. I'm creating that document converter, converting it, exporting it to markdown, and that's pretty much all I display in the script. So, I'll actually show you this right here. And it handles everything with OCR under the hood. So, we have object recognition. There's quite a bit of machine learning that's actually happening to extract everything from the PDF, especially because of little nuances you have with PDFs with things like tables being split between pages. We have to handle all of that.

### [06:12] Customization Options

And Dockling also has a lot of functionality built in for you if you want to customize the OCR process. So there are a lot of different options that we have for different OCR solutions. Things like Tesseract for example. You might have heard of that before.

So there we go. This is the complete markdown of our PDF. And we're not extracting images or capturing or anything right now. There are ways to do that in Dockling as well, but it does actually recognize it. Like this is where we have an image and we can handle tables. Like overall this is beautiful. And it was pretty fast as well. Like definitely less than 30 seconds to handle this entire PDF. And so now this data is ready to be chunked up and put in our knowledge base for our RAG agent. We'll get to that in a little bit.

### [06:48] Multiple File Formats

All right, now for the second example here, I just want to show you how easy it is to work with multiple different file formats in Dockling because under the hood, it recognizes the file extension and it knows what to do to work with those different file types without us having to do that much more in our code.

### [07:07] Multi-File Processing Script

And so now in our second script, take a look at this. If I go down to the bottom, I have a list of a few different files that I want to extract from. I got a couple PDFs, a Word document, and a markdown just to show we can keep working with raw text of course as well.

So we create our document converter and then I have this function to process any document and it's pretty short overall. We can just call `converter.convert()` on that file path. We don't have to specify what the extension is. We don't have to specify a strategy. I mean there are some options we have if we want to customize things but Dockling can be so, so basic and still work extremely well and then we just export it to markdown and then that's it and we just print the output of each of these files.

### [08:00] Multi-File Results

And so I'll go ahead and run this script as well. I'll pause and come back once we have the process complete for each of these files. And there we go. We got our little summary here of everything that it extracted from our four different documents.

And this time I also set it up so that this script outputs to a folder right here. So we can quickly take a look at outputs from our different files. And so for example, the Word document that we processed. I can click into this right here. We got our meeting notes. There we go. Looking really good. And it's all structured markdown. Take a look at how beautiful these tables look. These are perfect markdown tables that it took from the Word document.

### [08:35] More Examples

And we have our PDF for example. Even more beautiful tables. And it recognizes where we have images. Like this is just so, so good. Exactly what we need to now chunk up and put in our knowledge base. And I'll actually show chunking strategies in a little bit. But the next thing that I want to cover with you here is working with audio files.

### [08:55] Audio File Processing

And there's a specific way to handle that with Dockling very easily as well. So using audio files in Dockling does require a couple of extra dependencies because we need a way to pull a model to handle speech to text. And so make sure you install FFmpeg. I've got instructions depending on your OS. And then also if we look at the requirements in this project, I did add OpenAI Whisper, which is an open source tool.

### [09:15] Whisper Integration

We're going to be using Whisper Turbo as our speech-to-text model completely locally. Everything here with Dockling is local by the way, just grabbing models from Hugging Face. It is a beautiful thing. And so going to the third script that we've got right here, we have our audio path.

And then we call this transcribe audio function. And this function is pretty basic overall. We are setting up what is called an ASR pipeline. And there are a lot of different options that you can configure for your speech-to-text pipeline. You can take a look at the Dockling documentation for that. I'm just going with defaults mostly here to keep things simple using the Whisper Turbo model.

### [10:00] Audio Processing Code

So I set up my document converter just like we did when we were working with text-based files. And then again, just like with text-based files, we call `converter.convert()`. And then we can export the MP3 content as a markdown document. That is the beauty of Dockling is all of the different file types we're working with, they all just end up as markdown.

### [10:15] Audio Processing Results

So we basically have an ideal documents folder here where everything is set up as markdown ready to be put in our knowledge base. And we have to have this extra step of data preparation to make that happen. But Dockling just makes that so easy.

All right, I ran the third script off camera to transcribe our about 30-second audio file. And in total, it took 10 seconds and outputted 576 characters. And 10 seconds is not bad considering this is running completely locally with Dockling. So here is our transcript output. And then of course I have it in the output folder as well. And it even has timestamps here for all of the sentences that it transcribed. You can disable this of course if you want, but it is pretty nice that we have this metadata to build into our RAG system for any of our audio files. Very, very nice.

### [10:55] Chunking Introduction

And so, going back to our readme here, the last thing that I want to cover. Now that we've gone over extracting from different file types and seeing how easy that is with Dockling, I want to talk about chunking. Not only can Dockling help us with data extraction from our documents, it can also help us with the chunking part of our data preparation. And this is crucial because we cannot just take our document text once we have it extracted and dump it in our vector database.

### [11:25] Why Chunking Matters

That is way too much for the LLM to retrieve all at once with RAG. We can't just give it the entire document, especially when they are much bigger. What we need to do is split our documents into bite-sized pieces of information for our LLM to retrieve. So, it gets just that paragraph or that bullet point list, whatever it needs to answer our question.

### [11:45] Chunking Challenges

And there are a lot of different strategies to do this effectively because obviously the challenge here is how do we define those boundaries? How are we going to split? Are we going to split right here? Like this would be chunk one and this would be chunk two or are we going to split right here? How exactly do we do that? We definitely want to make sure that we don't split in the middle of paragraphs and bullet point lists for example. And so that's what Dockling helps us with.

### [12:00] Dockling Chunking

It's a pretty technical challenge under the hood, but Dockling makes it easy with a few different strategies that it gives us. And one that I want to focus on here that is getting insane results for me is hybrid chunking. This gets a little bit technical, but bear with me because I think this is fascinating and super powerful.

### [12:20] Hybrid Chunking Explained

With hybrid chunking, we are using an embedding model to define the semantic similarity between different, you know, paragraphs and sentences that we have in our document. So, we use the embedding model to figure out where can we split in this document to still keep core ideas together in these bite-sized pieces of information for the LLM.

### [12:43] Hybrid Chunking Implementation

And because Dockling takes care of all of the logic of the strategy under the hood, using it is actually pretty simple. So, in the fourth script that I have for you here, we have a path to a PDF that we want to process. And so, we're going to turn this into a Dockling document just like we've been doing in our other scripts.

But instead of extracting text from it right away, we're going to create this hybrid chunker object. There are a few different parameters that you can customize here. Once you have this though, you just call `chunker.chunk()` on the document.

### [13:20] Hybrid Chunking Results

So this is our PDF doc, obviously. And so we're going to get an output that is kind of similar to the markdown that we saw when we ran the first script, but this time things are going to be split up in a way where we already have our chunks ready to insert in vector database. Like literally what we have as output from this script is what we can put right in our vector database.

So just like the last example, I ran the fourth script off camera to extract the text from our PDF and chunk it with hybrid chunking. And so in the end we have 23 total chunks. 13 that are between 0 and 128 tokens and 10 that are between 128 and 256.

### [14:00] Chunk Analysis

And so we have some variety here because we are allowing the embedding model within reason. Of course, we have a max token limit for each chunk. We're letting the embedding model decide what goes into each bite-sized piece of information to keep all the similar ideas together. And of course, I've got output for the chunks as well.

And this is looking so good. We have top chunk with title and subtitle. We have all of our sections together. Bullet point lists are maintained in each chunk. This is super ideal. All of our sections, as long as they're short enough, they remain in a single chunk as well. And this all comes from a complex PDF. Like this is just a beautiful thing.

### [14:25] Vector Database Insertion

And then at this point, we can take all of these chunks and insert them right into our vector database. In fact, that is what I have now as the top-level example for you here. And I'll cover this in a little bit with you. This is a complete RAG AI agent that takes all of these ideas. We're parsing MP3s and PDFs and Word documents. We're using hybrid chunking. We're getting all this ready. And then I have an AI agent built on top that can query it. And that's what I demoed at the start of this video.

### [14:50] Additional Dockling Features

The last thing I want to say on Dockling before I get more into the RAG agent is you should definitely check out the example part of their docs if you want to learn more. There are so many great use cases they have built out here and just showing you ways to customize the platform.

For example, custom conversion. We can see how to use different OCR backends for extracting text from files like our PDFs. Also, they have this visual grounding example which is super, super cool. Not only can agent reference knowledge in our knowledge base that we have curated with Dockling, but it can also literally highlight like draw a box over the part of document that it got its answer from. Very, very cool.

### [15:30] Tool Comparison

So, Dockling really handles everything that we need as far as data extraction. And so, generally how I think about it is if I'm dealing with website data, then I use Crawl for AI. I've covered this on my channel before. I'll even link to a video right here. For anything else besides websites with any kind of documents I'm dealing with, then I will go with Dockling.

So, these are two tools that I have in my arsenal to build out pretty much any RAG pipeline that I want. And so, definitely let me know in comments if you want me to cover more use cases with Dockling or even showing you how to use it in other platforms like N8N. I definitely want to keep covering Dockling in more content for you.

### [16:10] Complete RAG Agent

All right, here is the grand finale because now we're combining everything we learned around chunking and parsing different document types into a single RAG agent that I have as a template for you. Link to all this below. And so right now I just want to cover at a high level how this works and how Dockling fits into our RAG pipeline and even show the agent and tools that I'm giving it to search our knowledge base that we curate with help of Dockling.

### [16:25] README Overview

And so this readme that I have at the top level of the repository. This has an overview of the agent, prerequisites, a quick start, including setting up your database and all the tables that we have here. Really easy to get this up and running yourself if you want to use it and build on top of it.

### [16:45] Database Schema

And so we have our database schema here. For vector database, I'm using PostgreSQL with PG Vector. And of course, you could tune this to use Pinecone or Qdrant. They even have some examples with Qdrant in the Dockling documentation.

But yeah, we have our document table here where we store higher-level information like each of the individual documents that we have in our knowledge base. And then we have a table to store all of the chunks that we create with Dockling hybrid chunking strategy.

### [17:30] Matching Function

And then we have our match chunks function. This is the SQL that our agent actually invokes as a tool to search our knowledge base. And so most of the logic with Dockling itself is in `chunker.py` right here because this is where we chunk our documents.

### [17:55] Chunking Implementation

And so I have this function here where we pass in that Dockling document. So this is going to be our PDF or our Word document. And just like we saw in simpler examples before, we just call `chunker.chunk()` on that Dockling document. That is all we have to do to perform hybrid chunking. It is so easy.

### [18:30] Contextualization

And then we pull contextualized text. Contextualize basically just means we're also including things like headings and subheadings that we have in markdown as well. And then we create our chunk metadata. I could do a whole another video on metadata as well, but just providing that additional information that speaks to our chunk.

### [18:55] Storage Process

And then we're just adding that to our list of chunks that we're curating. So we then take these chunks, we embed them with an embedding model, and we store them in our vector database. At this point, there is no more document processing we need to do because with Dockling through parsing our different file types and performing hybrid chunking, we now have our text in exactly the format that we're now going to insert in our vector database.

### [19:15] Agent Framework

Again, regardless of vector database that you use and then for our AI agent here, you know that I love using Pydantic AI if you've seen any of my content previously. So, we're using Pydantic AI to create our agent here.

So we have some logic here to set up our database connection because we're giving that in as a dependency to our agent. So we've got nice system prompt here and then giving it a single tool to search our knowledge base to perform a RAG query.

### [19:45] Query Function

And so I'll go to this function really quickly here. Search knowledge base. We just have a query that the agent decides—basically it's searching for our knowledge base. We set up database connection. We embed query with same embedding model that we use in our RAG pipeline. And then we're going to call that match chunks function that I showed earlier.

### [20:00] Retrieval Process

So we're passing in the query here. It's going to return all of the similar chunks that we have, you know, compared to user query and then that's returned to agent to then reason about what it retrieved and use that to help give us the final answer. That is RAG in a nutshell.

### [20:15] RAG Diagram Explanation

And so going back to our diagram here, we've mostly been covering the data preparation, but now I'm starting to speak to the retrieval-augmented generation, the actual query process that we have because we create an embedding based on that query that the agent decides that hits the vector database to retrieve the relevant chunks that we have curated from Dockling. Then that is fed back into the LLM to give us the final response.

### [20:35] Live Demo

All right, back in terminal now, we can run the CLI that kicks off a chat interface with our agent. And I already ran the whole ingestion pipeline here that pulls all of the documents and it looks very similar to the examples we saw earlier where it just pulls text from each of the documents, performs hybrid chunking, puts it in our database.

### [20:55] Demo Results

So we've got our knowledge base ready to go. 13 documents, 157 chunks in total, all processed by Dockling. And so now I can ask it some questions where clearly you'd have to go to knowledge base to get the answers for us here. And this is all just mock data for a fake company that I generated for our demo purposes.

### [21:20] Query Demo

And there we go. The revenue target for Q1 2025 is set at $3.4 million. And I believe this is from one of the PDF documents that we have. And so on my left-hand monitor here, I've got some other questions like from one of our Word docs. When was Neuroflow AI founded? Let's make sure it gives us an answer of 2023. Yep, there we go. All right, looking good.

### [21:30] More Testing

Let's just do one more question here just to test something. Uh, maybe from one of the MP3 files. So one of the MP3 files I talked about global finance. What ROI did Global Finance achieve? And it should say, there we go. Yep, 458%. All right.

### [21:45] Final Results

And each of these times is telling us that it's using the search knowledge-based tool that we saw set up in code for our agent and in database. So this is working phenomenally.

### [22:00] Conclusion

So there you go. That is everything that I have for you today for Dockling. And like I said, this is one of the most critical tools for your RAG implementation for any agent or application that you're building that needs to bring external information into a large language model.

So definitely I do want to cover Dockling a lot more in the future, building out more specific use cases with it, showing some of the more advanced features like actually captioning images that we pull from PDFs. There's so many more things that we can do with this tool. Dockling plus Crawl for AI is all you need for any data you have to extract for any use case.

### [22:30] Call to Action

So if you appreciated this video and you're looking forward to more things on RAG and AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next.

---

**Video Credit:** [Cole Medin](https://www.youtube.com/@ColeMedin)  
**Published:** February 2026  
**Duration:** 21 minutes, 21 seconds