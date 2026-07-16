---
title: "Improve search with rerankers"
source: https://docs.together.ai/docs/how-to-improve-search-with-rerankers
path: docs/how-to-improve-search-with-rerankers
---

Improve semantic search quality with reranker models.

In this guide we will use a reranker model to improve the results produced from a simple semantic search workflow. To get a better understanding of how semantic search works please refer to the [Cookbook here](https://github.com/togethercomputer/together-cookbook/blob/main/Semantic_Search.ipynb).

A reranker model operates by looking at the query and the retrieved results from the semantic search pipeline one by one and assesses how relevant the returned result is to the query. Because the reranker model can spend compute assessing the query with the returned result at the same time it can better judge how relevant the words and meanings in the query are to individual documents. This also means that rerankers are computationally expensive and slower - thus they cannot be used to rank every document in our database.

We run a semantic search process to obtain a list of 15-25 candidate objects that are similar "enough" to the query and then use the reranker as a fine-toothed comb to pick the top 5-10 objects that are actually closest to our query.

We will be using the [Mxbai Rerank](/docs/inference/embeddings/rerank) reranker model.

<Tip>
  Rerank models like `Mxbai-Rerank-Large-V2` are only available with [dedicated model inference](https://api.together.ai/endpoints/configure). You can bring up a dedicated endpoint to use reranking in your applications.
</Tip>

<Frame>
  <img alt="How to improve search with rerankers" />
</Frame>

## Download and View the Dataset

```bash Shell theme={null}
wget https://raw.githubusercontent.com/togethercomputer/together-cookbook/refs/heads/main/datasets/movies.json
mkdir datasets
mv movies.json datasets/movies.json
```

```py Python theme={null}
import json
import together, os
from together import Together

# Paste in your Together AI API Key or load it
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

with open("./datasets/movies.json", "r") as file:
    movies_data = json.load(file)

movies_data[10:13]
```

Our dataset contains information about popular movies:

```
[{'title': 'Terminator Genisys',
  'overview': "The year is 2029. John Connor, leader of the resistance continues the war against the machines. At the Los Angeles offensive, John's fears of the unknown future begin to emerge when TECOM spies reveal a new plot by SkyNet that will attack him from both fronts; past and future, and will ultimately change warfare forever.",
  'director': 'Alan Taylor',
  'genres': 'Science Fiction Action Thriller Adventure',
  'tagline': 'Reset the future'},
 {'title': 'Captain America: Civil War',
  'overview': 'Following the events of Age of Ultron, the collective governments of the world pass an act designed to regulate all superhuman activity. This polarizes opinion amongst the Avengers, causing two factions to side with Iron Man or Captain America, which causes an epic battle between former allies.',
  'director': 'Anthony Russo',
  'genres': 'Adventure Action Science Fiction',
  'tagline': 'Divided We Fall'},
 {'title': 'Whiplash',
  'overview': 'Under the direction of a ruthless instructor, a talented young drummer begins to pursue perfection at any cost, even his humanity.',
  'director': 'Damien Chazelle',
  'genres': 'Drama',
  'tagline': 'The road to greatness can take you to the edge.'}]
```

## Implement Semantic Search Pipeline

Below we implement a simple semantic search pipeline:

1. Embed movie documents + query
2. Obtain a list of movies ranked based on cosine similarities between the query and movie vectors.

```py Python theme={null}
# This function will be used to access the Together API to generate embeddings for the movie plots

from typing import List


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
    return [x.embedding for x in outputs.data]


to_embed = []
for movie in movies_data[:1000]:
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

Next we implement a function that when given the above embeddings and a test query will return indices of most semantically similar data objects:

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

We will use the above function to retrieve 25 movies most similar to our query:

```py Python theme={null}
indices = retrieve(
    query="super hero mystery action movie about bats",
    top_k=25,
    index=embeddings,
)
```

This will give us the following movie indices and movie titles:

```
array([ 13, 265, 451,  33,  56,  17, 140, 450,  58, 828, 227,  62, 337,
       172, 724, 424, 585, 696, 933, 996, 932, 433, 883, 420, 744])
```

```py Python theme={null}
# Get the top 25 movie titles that are most similar to the query - these will be passed to the reranker
top_25_sorted_titles = [movies_data[index]["title"] for index in indices[0]][
    :25
]
```

```
['The Dark Knight',
 'Watchmen',
 'Predator',
 'Despicable Me 2',
 'Night at the Museum: Secret of the Tomb',
 'Batman v Superman: Dawn of Justice',
 'Penguins of Madagascar',
 'Batman & Robin',
 'Batman Begins',
 'Super 8',
 'Megamind',
 'The Dark Knight Rises',
 'Batman Returns',
 'The Incredibles',
 'The Raid',
 'Die Hard: With a Vengeance',
 'Kick-Ass',
 'Fantastic Mr. Fox',
 'Commando',
 'Tremors',
 'The Peanuts Movie',
 'Kung Fu Panda 2',
 'Crank: High Voltage',
 'Men in Black 3',
 'ParaNorman']
```

Notice here that not all movies in our top 25 have to do with our query - super hero mystery action movie about bats. This is because semantic search captures the "approximate" meaning of the query and movies.

The reranker can more closely determine the similarity between these 25 candidates and rerank which ones deserve to be atop our list.

## Use Llama Rank to Rerank Top 25 Movies

Treating the top 25 matching movies as good candidate matches, potentially with irrelevant false positives, that might have snuck in we want to have the reranker model look and rerank each based on similarity to the query.

```py Python theme={null}
query = "super hero mystery action movie about bats"  # we keep the same query - can change if we want

response = client.rerank.create(
    model="mixedbread-ai/Mxbai-Rerank-Large-V2",
    query=query,
    documents=top_25_sorted_titles,
    top_n=5,  # we only want the top 5 results
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {top_25_sorted_titles[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```

This will give us a reranked list of movies as shown below:

```
Document Index: 12
Document: Batman Returns
Relevance Score: 0.35380946383813044

Document Index: 8
Document: Batman Begins
Relevance Score: 0.339339115127178

Document Index: 7
Document: Batman & Robin
Relevance Score: 0.33013392395016167

Document Index: 5
Document: Batman v Superman: Dawn of Justice
Relevance Score: 0.3289763252445171

Document Index: 9
Document: Super 8
Relevance Score: 0.258483721657576
```

Here we can see that the reranker was able to improve the list by demoting irrelevant movies like Watchmen, Predator, Despicable Me 2, Night at the Museum: Secret of the Tomb, Penguins of Madagascar, further down the list and promoting Batman Returns, Batman Begins, Batman & Robin, Batman v Superman: Dawn of Justice to the top of the list!

The `multilingual-e5-large-instruct` embedding model gives us a fuzzy match to concepts mentioned in the query, the Llama-Rank-V1 reranker then improves the quality of our list further by spending more compute to resort the list of movies.

Learn more about how to use reranker models in the [docs here](/docs/inference/embeddings/rerank)!

***
