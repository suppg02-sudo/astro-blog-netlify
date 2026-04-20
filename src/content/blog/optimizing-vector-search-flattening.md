---
pubDatetime: 2026-02-02T00:02:00Z
title: "Optimizing Vector Search: Flattening Structured Data"
postSlug: "optimizing-vector-search-flattening"
description: "Optimizing Vector Search: Flattening Structured Data"
tags:
  - memory
  - automation
  - ai
---

{{< audio src="/posts/audio/2026-02-02-optimizing-vector-search-flattening/complete_conversation.mp3" title="Listen to this blog post" >}}

Embedding raw JSON into vector databases is intuitive but dramatically reduces performance. Modern BERT-based embeddings are trained on natural language, not structured data formats. This fundamental mismatch causes suboptimal retrieval results.

## Deep Dive: Why JSON Fails

### Tokenization

The first step is tokenization, which takes the text and splits it into tokens, which are generally a generic part of the word. Modern embedding models utilize Byte-Pair Encoding (BPE) or WordPiece tokenization algorithms. These algorithms are optimized for natural language, breaking words into common sub-components. When a tokenizer encounters raw JSON, it struggles with the high frequency of non-alphanumeric characters. For example, `"usd": 10,` is not viewed as a key-value pair; instead, it's fragmented:

- The quotes (`"`), colon (`:`), and comma (`,`)
- Tokens `usd` and `10`

This creates a low *signal-to-noise ratio*. In natural language, almost all words contribute to the semantic "signal". While in JSON (and other structured formats), a significant percentage of tokens are "wasted" on structural syntax that contains zero semantic value.

### Attention Calculation

### Attention Calculation

In `The price is 10 US dollars`, attention easily links `10` to `price`—this pattern appears millions of times in training data. In raw JSON, structural syntax obscures these relationships.

### Mean Pooling

### Mean Pooling

Final embedding `E` averages all token vectors: `E = (e1 + e2 + ... + en) / n`. If 25% of tokens are structural noise, the vector is pulled away from its true semantic center. Natural language queries then show greater distance to these "noisy" vectors.

## The Solution: Flatten Structured Data

The general and most straightforward approach is to flatten JSON and convert it into natural language.

Convert JSON to natural language via templates:

```json
{
  "price": { "usd": 10, "eur": 9 },
  "skuId": "123",
  "category": "demo product"
}
```

Template:
```
Product SKU {skuId}, category "{category}"
Price: {price.usd} USD or {price.eur} EUR
```

Result:
```
Product SKU 123, category "demo product"
Price: 10 USD or 9 EUR
```

Benefits: 14% fewer tokens, semantic relationships preserved.

## Measurable Results

**Experiment**: all-MiniLM-L6-v2 model, Amazon ESCI dataset (5,000 queries, 3,809 products), FAISS indexes.

Flattening function:
```python
def flatten_product(product):
    return (f"Product {product['product_title']} from brand {product['product_brand']}"
            f" and description {product['product_description']}")
```

**Performance Improvement**:

Converting structured JSON to natural language text resulted in significant gains:
- **19.1% boost in Recall@10**
- **27.2% boost in MRR (Mean Reciprocal Rank)**
- **14% reduction in token count**

The analysis confirms that embedding raw structured data into generic vector space is a suboptimal approach. Adding a simple preprocessing step of flattening structured data consistently delivers significant improvement for retrieval metrics (boosting recall@k and precision@k by about 20%).

## Implementation Targets

### Priority 1: OpenMemory
Pre-processing hook before storage, template system, backwards compatibility.

### Priority 2: Fabric Pattern
`flatten_structured_data` pattern for consistent data preprocessing.

### Priority 3: Document Conversion
Flatten extracted metadata and logs.

### Priority 4: YouTube Transcripts
Pre-process API JSON responses.

### Implementation Priority Matrix

| Priority | Component | Effort |
|----------|-----------|--------|
| **1** | OpenMemory | Medium |
| **2** | Fabric Pattern | Low |
| **3** | Document Conversion | Medium |
| **4** | YouTube Transcripts | Low |

## Implementation Approach

### Utility Function
```python
def flatten_structured_data(data, template=None):
    if isinstance(data, dict):
        if template:
            return template.format(**data)
        return ' '.join([f"{k} is {v}" for k, v in data.items()])
    return data
```

### Steps
1. Add pre-processing hook to OpenMemory
2. Create Fabric pattern
3. Enable gradually on new data
4. Evaluate legacy migration

## Considerations

### Schema Complexity
- Nested structures require recursive flattening
- Arrays need list handling strategies
- Mixed types (boolean, numeric, string) require consistency

### Templates
```python
# Example templates
container_template = "Container {name} is {status} with ports {ports}"
transcript_template = "Video {title} by {channel}: {text}"
```

### Performance
- Preprocessing: Slight increase
- Retrieval: 20%+ improvement
- Overall: Net positive

## Conclusion

Flattening structured data before embedding yields 20%+ retrieval improvements with low implementation cost. Vector search engines are optimized for natural language, not database syntax—aligning data with embedding models' strengths unlocks significant performance gains.

## References

- [Experiment code](https://colab.research.google.com/drive/1dTgt6xwmA6CeIKE38lf2cZVahaJNbQB1)
- [Model](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Amazon ESCI dataset](https://huggingface.co/datasets/milistu/amazon-esci-data)
- [FAISS](https://ai.meta.com/tools/faiss/)