---
title: "OpenAI"
source: https://docs.pinecone.io/integrations/openai
path: integrations/openai
---

Pair OpenAI embeddings and completion models with Pinecone for semantic search, long-term memory, RAG, and context-aware LLM question-answering.

OpenAI's large language models (LLMs) enhance semantic search, or "long-term memory," for LLMs. This combination uses OpenAI's embedding and completion (or generation) endpoints alongside Pinecone's vector search for information retrieval.

By integrating OpenAI's LLMs with Pinecone, you can combine deep learning capabilities for embedding generation with efficient vector storage and retrieval. This approach goes beyond traditional keyword-based search and returns context-aware results.

<PrimarySecondaryCTA />

## Setup guide

[View source](https://github.com/pinecone-io/examples/blob/master/integrations/openai/)

[Open in Colab](https://colab.research.google.com/github/pinecone-io/examples/blob/master/integrations/openai/semantic_search_openai.ipynb)

This guide shows how to integrate OpenAI's LLMs with Pinecone, a combination referred to as the OP stack.

LLMs like OpenAI's `text-embedding-ada-002` generate vector embeddings, i.e., numerical representations of text semantics. These embeddings enable semantic matches rather than literal text matches. Additionally, LLMs like `gpt-4` or `gpt-3.5-turbo` can predict text completions based on information provided from these contexts.

Pinecone Database stores and queries high-dimensional vectors and provides fast semantic search over them.

There are many ways to integrate these two tools, and Pinecone has several guides that focus on specific use cases. If you already know what you'd like to do, start with one of these:

* [ChatGPT Plugins Walkthrough](https://youtu.be/hpePPqKxNq8)
* [Ask Lex ChatGPT Plugin](https://github.com/pinecone-io/examples/tree/master/learn/generation/openai/chatgpt/plugins/ask-lex)
* [Generative Question-Answering](https://github.com/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb)
* [Retrieval Augmentation using LangChain](https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb)

### Introduction to embeddings

At the core of the OP stack are embeddings, which come from the [OpenAI Embedding API](https://beta.openai.com/docs/guides/embeddings). You index those embeddings in [Pinecone Database](/guides/get-started/overview) for fast, scalable retrieval augmentation of your LLMs and other information retrieval use cases.

This example demonstrates the core OP stack. It's the simplest workflow and is present in each of the other workflows, but it isn't the only way to use the stack. For more advanced usage, see the guides listed earlier.

The OP stack is built for semantic search, question-answering, threat-detection, and other applications that rely on language models and a large corpus of text data.

The basic workflow looks like this:

* Embed and index
  * Use the OpenAI Embedding API to generate vector embeddings of your documents (or any text data).
  * Upload those vector embeddings into Pinecone, which can store and index millions or billions of these vector embeddings and search through them at low latency.
* Search
  * Pass your query text or document through the OpenAI Embedding API again.
  * Take the resulting vector embedding and send it as a [query](/guides/search/search-overview) to Pinecone.
  * Get back semantically similar documents, even if they don't share any keywords with the query.

<img alt="Basic workflow of OpenAI and Pinecone" />

### Set up the environment

Start by installing the OpenAI and Pinecone clients, along with Hugging Face Datasets for downloading the TREC dataset used in this guide.

```Bash Bash theme={null}
!pip install -qU \
    pinecone[grpc]==7.3.0 \
    openai==1.93.0 \
    datasets==3.6.0
```

### Create embeddings

To create embeddings, first initialize your connection to OpenAI. Sign up for an API key at [OpenAI](https://beta.openai.com/signup).

```Python Python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="OPENAI_API_KEY"
)  # get API key from platform.openai.com
```

You can now create embeddings with the OpenAI v3 small embedding model.

```Python Python theme={null}
MODEL = "text-embedding-3-small"

res = client.embeddings.create(
    input=[
        "Sample document text goes here",
        "there will be several phrases in each batch"
    ], model=MODEL
)
```

In `res`, you should find a JSON-like object containing two 1536-dimensional embeddings. These are the vector representations of the two inputs. To access the embeddings directly, extract them to a list.

```Python Python theme={null}
# we can extract embeddings to a list
embeds = [record.embedding for record in res.data]
len(embeds)
```

You'll use this logic later when you create embeddings for the Text REtrieval Conference (TREC) question classification dataset.

### Create an index

Next, initialize an index to store the vector embeddings. For this, you need a Pinecone API key. [Sign up for one](https://app.pinecone.io).

```Python Python theme={null}
import time
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key="...")

spec = ServerlessSpec(cloud="aws", region="us-east-1")

index_name = 'semantic-search-openai'

# check if index already exists (it shouldn't if this is your first run)
if index_name not in pc.list_indexes().names():
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension=len(embeds[0]),  # dimensionality of text-embed-3-small
        metric='dotproduct',
        spec=spec
    )

# connect to index
index = pc.Index(index_name)
time.sleep(1)
# view index stats
index.describe_index_stats()
```

### Store the embeddings

With both OpenAI and Pinecone connections initialized, you can populate the index. For this, you need the TREC dataset.

```Python Python theme={null}
from datasets import load_dataset

# load the first 1K rows of the TREC dataset
trec = load_dataset('trec', split='train[:1000]')
```

Then create a vector embedding for each question using OpenAI (as demonstrated earlier), and `upsert` the ID, vector embedding, and original text for each phrase to Pinecone.

<Warning>
  High-cardinality metadata values (like the unique text values used here) can reduce the number of vectors that fit on a single pod. For more information, see [Known limitations](/reference/api/known-limitations).
</Warning>

```Python Python theme={null}
from tqdm.auto import tqdm

count = 0  # we'll use the count to create unique IDs
batch_size = 32  # process everything in batches of 32
for i in tqdm(range(0, len(trec['text']), batch_size)):
    # set end position of batch
    i_end = min(i+batch_size, len(trec['text']))
    # get batch of lines and IDs
    lines_batch = trec['text'][i: i+batch_size]
    ids_batch = [str(n) for n in range(i, i_end)]
    # create embeddings
    res = client.embeddings.create(input=lines_batch, model=MODEL)
    embeds = [record.embedding for record in res.data]
    # prep metadata and upsert batch
    meta = [{'text': line} for line in lines_batch]
    to_upsert = zip(ids_batch, embeds, meta)
    # upsert to Pinecone
    index.upsert(vectors=list(to_upsert))
```

### Run a semantic search

With your data indexed, you're ready to perform searches. This follows a similar process to indexing. Start with a text `query` that you want to use to find similar sentences. As before, encode it with OpenAI's text similarity Babbage model to create a query vector, `xq`. Then use `xq` to query the Pinecone index.

```Python Python theme={null}
query = "What caused the 1929 Great Depression?"

xq = client.embeddings.create(input=query, model=MODEL).data[0].embedding
```

Now query the index.

```Python Python theme={null}
res = index.query(vector=xq, top_k=5, include_metadata=True)
```

The response from Pinecone includes your original text in the `metadata` field. Print the `top_k` most similar questions and their similarity scores.

```Python Python theme={null}
for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]: theme={null}
0.75: Why did the world enter a global depression in 1929 ?
0.60: When was `` the Great Depression '' ?
0.37: What crop failure caused the Irish Famine ?
0.32: What were popular songs and types of songs in the 1920s ?
0.32: When did World War I start ?
```

The top results are relevant. To make the search harder, replace "depression" with the incorrect term "recession."

```Python Python theme={null}
query = "What was the cause of the major recession in the early 20th century?"

# create the query embedding
xq = client.embeddings.create(input=query, model=MODEL).data[0].embedding

# query, returning the top 5 most similar results
res = index.query(vector=xq, top_k=5, include_metadata=True)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]: theme={null}
0.63: Why did the world enter a global depression in 1929 ?
0.55: When was `` the Great Depression '' ?
0.34: What were popular songs and types of songs in the 1920s ?
0.33: What crop failure caused the Irish Famine ?
0.29: What is considered the costliest disaster the insurance industry has ever faced ?
```

Finally, search using the definition of depression rather than the word or related words.

```Python Python theme={null}
query = "Why was there a long-term economic downturn in the early 20th century?"

# create the query embedding
xq = client.embeddings.create(input=query, model=MODEL).data[0].embedding

# query, returning the top 5 most similar results
res = index.query(vector=xq, top_k=5, include_metadata=True)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]: theme={null}
0.62: Why did the world enter a global depression in 1929 ?
0.54: When was `` the Great Depression '' ?
0.34: What were popular songs and types of songs in the 1920s ?
0.33: What crop failure caused the Irish Famine ?
0.32: What do economists do ?
```

This example shows that the semantic search pipeline can identify the meaning behind each of your queries. Using these embeddings with Pinecone lets you return the most semantically similar questions from the already indexed TREC dataset.

### Clean up

When you're finished with the index, delete it to save resources.

```Python Python theme={null}
pc.delete_index(name=index_name)
```

## Resources

* [Generative Question-Answering with Long-Term Memory](https://www.pinecone.io/learn/openai-gen-qa)
* [OpenAI's Text Embeddings v3](https://www.pinecone.io/learn/openai-embeddings-v3/)
