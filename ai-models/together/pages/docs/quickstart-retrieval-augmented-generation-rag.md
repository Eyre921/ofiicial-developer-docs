---
title: "Retrieval-augmented generation (RAG) quickstart"
source: https://docs.together.ai/docs/quickstart-retrieval-augmented-generation-rag
path: docs/quickstart-retrieval-augmented-generation-rag
---

Build a RAG workflow in under five minutes.

In this Quickstart you'll learn how to build a RAG workflow using Together AI in 6 quick steps that can be run in under 5 minutes!

You'll leverage the embedding, reranking, and inference endpoints.

## 1. Register for an account

First, [register for an account](https://api.together.ai/settings/projects/~first/api-keys) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```bash Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

## 2. Install your preferred library

Together provides an official library for Python:

```sh Shell theme={null}
pip install together --upgrade
```

```py Python theme={null}
from together import Together

client = Together(api_key=TOGETHER_API_KEY)
```

## 3. Data processing and chunking

You'll RAG over Paul Graham's latest essay titled [Founder Mode](https://paulgraham.com/foundermode.html). The code below will scrape and load the essay into memory.

```py Python theme={null}
import requests
from bs4 import BeautifulSoup


def scrape_pg_essay():
    url = "https://paulgraham.com/foundermode.html"

    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Paul Graham's essays typically have the main content in a font tag
        # You might need to adjust this selector based on the actual HTML structure
        content = soup.find("font")

        if content:
            # Extract and clean the text
            text = content.get_text()
            # Remove extra whitespace and normalize line breaks
            text = " ".join(text.split())
            return text
        else:
            return "Could not find the main content of the essay."

    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"


# Scrape the essay
pg_essay = scrape_pg_essay()
```

Chunk the essay:

```py Python theme={null}
# Naive fixed sized chunking with overlaps
def create_chunks(document, chunk_size=300, overlap=50):
    return [
        document[i : i + chunk_size]
        for i in range(0, len(document), chunk_size - overlap)
    ]


chunks = create_chunks(pg_essay, chunk_size=250, overlap=30)
```

## 4. Generate vector index and perform retrieval

You'll now use `multilingual-e5-large-instruct` to embed the augmented chunks above into a vector index.

```py Python theme={null}
from typing import List
import numpy as np


def generate_embeddings(
    input_texts: List[str],
    model_api_string: str,
) -> np.ndarray:
    """Generate embeddings from Together python library.

    Args:
        input_texts: a list of string input texts.
        model_api_string: str. An API string for a specific embedding model of your choice.

    Returns:
        embeddings_list: a list of embeddings. Each element corresponds to the each input text.
    """
    outputs = client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    )
    return np.array([x.embedding for x in outputs.data])


embeddings = generate_embeddings(
    chunks, "intfloat/multilingual-e5-large-instruct"
)
```

The function below will help us perform vector search:

```py Python theme={null}
def vector_retrieval(
    query: str,
    top_k: int = 5,
    vector_index: np.ndarray = None,
) -> List[int]:
    """
    Retrieve the top-k most similar items from an index based on a query.
    Args:
        query (str): The query string to search for.
        top_k (int, optional): The number of top similar items to retrieve. Defaults to 5.
        index (np.ndarray, optional): The index array containing embeddings to search against. Defaults to None.
    Returns:
        List[int]: A list of indices corresponding to the top-k most similar items in the index.
    """

    query_embedding = np.array(
        generate_embeddings(
            [query], "intfloat/multilingual-e5-large-instruct"
        )[0]
    )

    similarity_scores = np.dot(query_embedding, vector_index.T)

    return list(np.argsort(-similarity_scores)[:top_k])


top_k_indices = vector_retrieval(
    query="What are 'skip-level' meetings?",
    top_k=5,
    vector_index=embeddings,
)
top_k_chunks = [chunks[i] for i in top_k_indices]
```

You now have a way to retrieve from the vector index given a query.

## 5. Rerank to improve quality

You'll use a reranker model to improve retrieved chunk relevance quality:

<Tip>
  Rerank models like `Mxbai-Rerank-Large-V2` are only available with [dedicated model inference](https://api.together.ai/endpoints/configure). You can bring up a dedicated endpoint to use reranking in your applications.
</Tip>

```py Python theme={null}
def rerank(query: str, chunks: List[str], top_k=3) -> List[int]:

    response = client.rerank.create(
        model="mixedbread-ai/Mxbai-Rerank-Large-V2",
        query=query,
        documents=chunks,
        top_n=top_k,
    )

    return [result.index for result in response.results]


rerank_indices = rerank(
    "What are 'skip-level' meetings?",
    chunks=top_k_chunks,
    top_k=3,
)

reranked_chunks = ""

for index in rerank_indices:
    reranked_chunks += top_k_chunks[index] + "\n\n"

print(reranked_chunks)
```

## 6. Call generative model

You'll pass the final 3 concatenated chunks into an LLM to get the final answer.

```py Python theme={null}
query = "What are 'skip-level' meetings?"

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a helpful chatbot."},
        {
            "role": "user",
            "content": f"Answer the question: {query}. Use only information provided here: {reranked_chunks}",
        },
    ],
)

response.choices[0].message.content
```

If you want to learn more about how to best use open models refer to the [docs](/docs) here!
