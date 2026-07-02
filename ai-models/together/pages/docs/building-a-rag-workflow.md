---
title: "Build a RAG workflow"
source: https://docs.together.ai/docs/building-a-rag-workflow
path: docs/building-a-rag-workflow
---

Learn how to build a RAG workflow with Together AI embedding and chat endpoints!

## Introduction

For AI models to be effective in specialized tasks, they often require domain-specific knowledge. For instance, a financial advisory chatbot needs to understand market trends and products offered by a specific bank, while an AI legal assistant must be equipped with knowledge of statutes, regulations, and past case law.

A common solution is Retrieval-Augmented Generation (RAG), which retrieves relevant data from a knowledge base and combines it with the user’s prompt, thereby improving and customizing the model's output to the provided data.

<Frame>
  <img alt="" />
</Frame>

## RAG Explanation

RAG operates by preprocessing a large knowledge base and dynamically retrieving relevant information at runtime.

Here's a breakdown of the process:

1. Indexing the Knowledge Base: The corpus (collection of documents) is divided into smaller, manageable chunks of text. Each chunk is converted into a vector embedding using an embedding model. These embeddings are stored in a vector database optimized for similarity searches.
2. Query Processing and Retrieval: When a user submits a prompt that would initially go directly to an LLM we process that and extract a query, the system searches the vector database for chunks semantically similar to the query. The most relevant chunks are retrieved and injected into the prompt sent to the generative AI model.
3. Response Generation: The AI model then uses the retrieved information along with its pre-trained knowledge to generate a response. Not only does this reduce the likelihood of hallucination since relevant context is provided directly in the prompt but it also allows us to cite to source material as well.

<Frame>
  <img alt="" />
</Frame>

## Download and View the Dataset

```bash Shell theme={null}
wget https://raw.githubusercontent.com/togethercomputer/together-cookbook/refs/heads/main/datasets/movies.json
mkdir datasets
mv movies.json datasets/movies.json
```

```py Python theme={null}
import together, os
from together import Together

# Paste in your Together AI API Key or load it
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

import json

with open("./datasets/movies.json", "r") as file:
    movies_data = json.load(file)

movies_data[:1]
```

This dataset consists of movie information as below:

```py Python theme={null}
[
    {
        "title": "Minions",
        "overview": "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.",
        "director": "Kyle Balda",
        "genres": "Family Animation Adventure Comedy",
        "tagline": "Before Gru, they had a history of bad bosses",
    },
    {
        "title": "Interstellar",
        "overview": "Interstellar chronicles the adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
        "director": "Christopher Nolan",
        "genres": "Adventure Drama Science Fiction",
        "tagline": "Mankind was born on Earth. It was never meant to die here.",
    },
    {
        "title": "Deadpool",
        "overview": "Deadpool tells the origin story of former Special Forces operative turned mercenary Wade Wilson, who after being subjected to a rogue experiment that leaves him with accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life.",
        "director": "Tim Miller",
        "genres": "Action Adventure Comedy",
        "tagline": "Witness the beginning of a happy ending",
    },
]
```

## Implement Retrieval Pipeline - "R" part of RAG

Below we implement a simple retrieval pipeline:

1. Embed movie documents and query
2. Obtain top k movies ranked based on cosine similarities between the query and movie vectors.

```py Python theme={null}
# This function will be used to access the Together API to generate embeddings for the movie plots

from typing import List
import numpy as np


def generate_embeddings(
    input_texts: List[str],
    model_api_string: str,
) -> List[List[float]]:
    """Generate embeddings from Together python library.

    Args:
        input_texts: a list of string input texts.
        model_api_string: str. An API string for a specific embedding model of your choice.

    Returns:
        embeddings_list: a list of embeddings. Each element corresponds to the each input text.
    """
    together_client = together.Together(api_key=TOGETHER_API_KEY)
    outputs = together_client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    )
    return np.array([x.embedding for x in outputs.data])


# We will concatenate fields in the dataset in prep for embedding

to_embed = []

for movie in movies_data:
    text = ""
    for field in ["title", "overview", "tagline"]:
        value = movie.get(field, "")
        text += str(value) + " "
    to_embed.append(text.strip())

# Use multilingual-e5-large-instruct model to generate embeddings
embeddings = generate_embeddings(
    to_embed, "intfloat/multilingual-e5-large-instruct"
)
```

This will generate embeddings of the movies which we can use later to retrieve similar movies.

When a user makes a query we can embed the query using the same model and perform a vector similarity search as shown below:

```py Python theme={null}
from sklearn.metrics.pairwise import cosine_similarity

# Generate the vector embeddings for the query
query = "super hero action movie with a timeline twist"

query_embedding = generate_embeddings(
    [query], "intfloat/multilingual-e5-large-instruct"
)[0]

# Calculate cosine similarity between the query embedding and each movie embedding
similarity_scores = cosine_similarity([query_embedding], embeddings)
```

We get a similarity score for each of our 1000 movies - the higher the score, the more similar the movie is to the query.

We can sort this similarity score to get the movies most similar to our query = `super hero action movie with a timeline twist`

```py Python theme={null}
# Get the indices of the highest to lowest values
indices = np.argsort(-similarity_scores)

top_10_sorted_titles = [movies_data[index]["title"] for index in indices[0]][
    :10
]

top_10_sorted_titles
```

This produces the top ten most similar movie titles below:

```
['The Incredibles',
 'Watchmen',
 'Mr. Peabody & Sherman',
 'Due Date',
 'The Next Three Days',
 'Super 8',
 'Iron Man',
 'After Earth',
 'Men in Black 3',
 'Despicable Me 2']
```

## We can encapsulate the above in a function

```py Python theme={null}
def retrieve(
    query: str,
    top_k: int = 5,
    index: np.ndarray = None,
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

    query_embedding = generate_embeddings(
        [query], "intfloat/multilingual-e5-large-instruct"
    )[0]
    similarity_scores = cosine_similarity([query_embedding], index)

    return np.argsort(-similarity_scores)[0][:top_k]
```

Which can be used as follows:

```py Python theme={null}
retrieve(
    "super hero action movie with a timeline twist",
    top_k=5,
    index=embeddings,
)
```

Which returns an array of indices for movies that best match the query.

```
array([172, 265, 768, 621, 929])
```

## Generation Step - "G" part of RAG

Below we will inject/augment the information the retrieval pipeline extracts into the prompt to the Llama3 8b Model.

This will help guide the generation by grounding it from facts in our knowledge base!

```py Python theme={null}
# Extract out the titles and overviews of the top 10 most similar movies
titles = [movies_data[index]["title"] for index in indices[0]][:10]
overviews = [movies_data[index]["overview"] for index in indices[0]][:10]

client = Together(api_key=TOGETHER_API_KEY)

# Generate a story based on the top 10 most similar movies

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a pulitzer award winning craftful story teller. Given only the overview of different plots you can weave together an interesting storyline.",
        },
        {
            "role": "user",
            "content": f"Tell me a story about {titles}. Here is some information about them {overviews}",
        },
    ],
)

print(response.choices[0].message.content)
```

Which produces the grounded output below:

```txt Text theme={null}
What a delightful mix of plots! Here's a story that weaves them together:

In a world where superheroes are a thing of the past, Bob Parr, aka Mr. Incredible, has given up his life of saving the world to become an insurance adjuster in the suburbs. His wife, Helen, aka Elastigirl, has also hung up her superhero suit to raise their three children. However, when Bob receives a mysterious assignment from a secret organization, he's forced to don his old costume once again.

As Bob delves deeper into the assignment, he discovers that it's connected to a sinister plot to destroy the world. The plot is masterminded by a group of rogue superheroes, who were once part of the Watchmen, a group of vigilantes that were disbanded by the government in the 1980s.

The Watchmen, led by the enigmatic Rorschach, have been secretly rebuilding their team and are now determined to take revenge on the world that wronged them. Bob must team up with his old friends, including the brilliant scientist, Dr. Manhattan, to stop the Watchmen and prevent their destruction.

Meanwhile, in a different part of the world, a young boy named Sherman, who has a genius-level IQ, has built a time-travel machine with his dog, Penny. When the machine is stolen, Sherman and Penny must travel through time to prevent a series of catastrophic events from occurring.

As they travel through time, they encounter a group of friends who are making a zombie movie with a Super-8 camera. The friends, including a young boy named Charles, witness a train derailment and soon discover that it was no accident. They team up with Sherman and Penny to uncover the truth behind the crash and prevent a series of unexplained events and disappearances.

As the story unfolds, Bob and his friends must navigate a complex web of time travel and alternate realities to stop the Watchmen and prevent the destruction of the world. Along the way, they encounter a group of agents from the Men in Black, who are trying to prevent a catastrophic event from occurring.

The agents, led by Agents J and K, are on a mission to stop a powerful new super criminal, who is threatening to destroy the world. They team up with Bob and his friends to prevent the destruction and save the world.

In the end, Bob and his friends succeed in stopping the Watchmen and preventing the destruction of the world. However, the journey is not without its challenges, and Bob must confront his own demons and learn to balance his life as a superhero with his life as a husband and father.

The story concludes with Bob and his family returning to their normal lives, but with a newfound appreciation for the importance of family and the power of teamwork. The movie ends with a shot of the Parr family, including their three children, who are all wearing superhero costumes, ready to take on the next adventure that comes their way.
```

Here we can see a simple RAG pipeline where we use semantic search to perform retrieval and pass relevant information into the prompt of an LLM to condition its generation.

To learn more about the Together AI API please refer to the [docs here](/intro)!
