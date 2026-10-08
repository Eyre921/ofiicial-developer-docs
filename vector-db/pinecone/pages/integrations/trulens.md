---
title: "TruLens"
source: https://docs.pinecone.io/integrations/trulens
path: integrations/trulens
---

Use TruLens to evaluate and track RAG apps built on Pinecone by measuring groundedness, relevance, and hallucinations as you iterate.

TruLens is an open-source library for evaluating and tracking large language model-based applications. TruLens provides tools for developing and monitoring neural nets, including large language models (LLMs). These include TruLens-Eval, for evaluating LLMs and LLM-based applications, and TruLens-Explain, for deep learning explainability.

To build an effective RAG-style LLM application, experiment with different configuration choices as you set up your Pinecone index, and study their impact on performance metrics. Tracking and evaluation with TruLens help you iterate on your application.

<PrimarySecondaryCTA />

## Setup guide

[TruLens](https://github.com/truera/trulens) is an open-source library for evaluating and tracking large language model-based applications. In this guide, you'll learn how to use TruLens to evaluate applications built on Pinecone Database.

### TruLens for LLM evaluation

Reliable, non-hallucinatory LLM-based applications need systematic evaluation. TruLens contains instrumentation and evaluation tools for large language model (LLM)-based applications. For evaluation, TruLens provides a set of feedback functions, analogous to labeling functions, to programmatically score the input, output, and intermediate text of an LLM app. You can score each LLM application request on its question-answer relevance, context relevance, and groundedness. These feedback functions provide evidence that your LLM application is non-hallucinatory.

<img alt="diagram-1" />

Feedback functions also support the evaluation of ground truth agreement, sentiment, model agreement, language match, toxicity, and a full suite of moderation evaluations, including hate and violence. TruLens implements feedback functions as an extensible framework, so you can also write evaluations for your own needs.

During the development cycle, TruLens supports the iterative development of a wide range of LLM applications by wrapping your application to log cost, latency, key metadata, and evaluations of each application run. This lets you track and identify failure modes, find their root cause, and measure improvement across experiments.

<img alt="application-screenshot" />

### Pinecone for retrieval-augmented generation

Large language models alone have a hallucination problem. Several decades of machine learning research have optimized models, including modern LLMs, for generalization, while actively penalizing memorization. However, many of today's applications require factual, grounded answers. LLMs are also expensive to train and are provided by third-party APIs, so the knowledge of an LLM is fixed. Retrieval-augmented generation (RAG) is a way to reliably ensure models are grounded, with Pinecone as the curated source of real-world information, long-term memory, application domain knowledge, or allowlisted data.

In the RAG paradigm, the system first retrieves documents from the knowledge base that could help answer a user's question. It then passes those documents, along with the original question, to the language model to generate the final response. The most popular method for RAG involves chaining together LLMs with a retrieval system such as Pinecone Database.

In this process, the system calculates a numerical vector (an embedding) for each document and stores those vectors in a database optimized for storing and querying vectors. It vectorizes incoming queries as well, typically using an encoder LLM to convert the query into an embedding. It then matches the query embedding against the document embeddings in the vector database by embedding similarity to retrieve the documents that are relevant to the query.

<img alt="diagram-2" />

You can use Pinecone to build high-performance vector search applications, including retrieval-augmented question answering. Pinecone can handle hundreds of millions and even billions of vector embeddings. At that scale, Pinecone can hold long-term memory or a large corpus of external and domain-specific data, so the LLM component of a RAG application can focus on tasks like summarization, inference, and planning. This setup is well suited to developing a non-hallucinatory application.

Pinecone is also fully managed, so you can change configurations and components without managing infrastructure. Together with tracking and evaluation in TruLens, this lets you iterate on your application quickly.

### Use Pinecone and TruLens to improve LLM performance and reduce hallucination

To build an effective RAG-style LLM application, experiment with different configuration choices as you set up your Pinecone index, and study their impact on performance metrics.

This example explores how some of these configuration choices affect response quality, cost, and latency in a sample LLM application built on Pinecone Database. It uses the open-source [TruLens](https://www.trulens.org/) library for evaluation and experiment tracking. TruLens offers an extensible set of [feedback functions](https://truera.com/ai-quality-education/generative-ai-and-llms/whats-missing-to-evaluate-foundation-models-at-scale/) to evaluate LLM apps and lets you track your LLM app experiments.

Each component of this application has configuration choices that can affect downstream performance. Some of these choices include the following.

When you construct the index, you choose the following:

* Data preprocessing and selection
* Chunk size and chunk overlap
* Index distance metric
* Selection of embeddings

For retrieval, you choose the following:

* Amount of context retrieved (top k)
* Query planning

For the LLM, you choose the following:

* Prompting
* Model choice
* Model parameters (size, temperature, frequency penalty, model retries, etc.)

These configuration choices are useful to keep in mind when constructing your app. In general, there's no optimal choice for all use cases. Instead, we recommend that you experiment with and evaluate a variety of configurations to find the best selection as you build your application.

#### Create the index in Pinecone

First, download a pre-embedded dataset from the `pinecone-datasets` library, which lets you skip the embedding and preprocessing steps.

```Python Python theme={null}
import pinecone_datasets

dataset = pinecone_datasets.load_dataset('wikipedia-simple-text-embedding-ada-002-100K')
dataset.head()
```

After downloading the data, initialize your Pinecone environment and create your first index. This is your first potentially important choice, because you select the distance metric for the index.

```Python Python theme={null}
pinecone.create_index(
        name=index_name_v1,
        metric='cosine', # We'll try each distance metric here.
        dimension=1536  # 1536 dim of text-embedding-ada-002.
)
```

Then, upsert your documents into the index in batches.

```Python Python theme={null}
for batch in dataset.iter_documents(batch_size=100):
    index.upsert(batch)
```

#### Build the vector store

Now that you've built your index, use LangChain to initialize your vector store.

```Python Python theme={null}
embed = OpenAIEmbeddings(
    model='text-embedding-ada-002',
    openai_api_key=OPENAI_API_KEY
)

from langchain.vectorstores import Pinecone

text_field = "text"

# Switch back to a normal index for LangChain.
index = pinecone.Index(index_name_v1)

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)
```

In RAG, an LLM answers the query as a question, but it must base its answer on the information it receives from the `vectorstore`.

#### Initialize the RAG application

To do this, initialize a `RetrievalQA` as your app:

```Python Python theme={null}
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# completion llm
llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)
```

#### Evaluate and track LLM experiments with TruLens

Once you've set up your app, put together your [feedback functions](https://truera.com/ai-quality-education/generative-ai-and-llms/whats-missing-to-evaluate-foundation-models-at-scale/). As a reminder, feedback functions are an extensible method for evaluating LLMs. This example sets up two feedback functions, `qs_relevance` and `qa_relevance`, which are defined as follows:

*QS Relevance: query-statement relevance is the average of relevance (0 to 1) for each context chunk returned by the semantic search.*
*QA Relevance: question-answer relevance is the relevance (again, 0 to 1) of the final answer to the original question.*

```Python Python theme={null}
# Imports main tools for eval
from trulens_eval import TruChain, Feedback, Tru, feedback, Select
import numpy as np
tru = Tru()

# OpenAI as feedback provider
openai = feedback.OpenAI()

# Question/answer relevance between overall question and answer.
qa_relevance = Feedback(openai.relevance).on_input_output()

# Question/statement relevance between question and each context chunk.
qs_relevance = (
    Feedback(openai.qs_relevance)
    .on_input()
    # See explanation below 
    .on(Select.Record.app.combine_documents_chain._call.args.inputs.input_documents[:].page_content)
    .aggregate(np.mean)
)

```

The selectors in this code also need some explanation.

QA Relevance is the simpler of the two. It uses `.on_input_output()` to specify that the feedback function should be applied on both the input and output of the application.

QS Relevance uses TruLens selectors to locate the context chunks retrieved by the application. It breaks down into the following parts:

1. The `on_input` call, which appears first, is an argument specification. It's shorthand stating that the first argument to `qs_relevance` (the question) is the main input of the app.

2. The `on(Select...)` line is also an argument specification. It specifies where the statement argument to the implementation comes from. In this case, you want to evaluate the context chunks, which are an intermediate step of the LLM app. This form references the LangChain app object call chain, which you can view from `tru.run_dashboard()`. This lets you apply a feedback function to any intermediate step of your LLM app. The following example shows how TruLens displays the selector for each piece of the context.

   <img alt="subcomponents" />

3. The last line, `aggregate(np.mean)`, is the aggregation specification. It specifies how to aggregate feedback outputs, and it only applies when the argument specification names more than one value for an input or output.

As a result, you can run `qs_relevance` on apps and records, and it automatically selects the specified components of those apps and records.

To finish up, wrap your Retrieval QA app with TruLens along with a list of the feedback functions to use for evaluation.

```Python Python theme={null}
# wrap with TruLens
truchain = TruChain(qa,
    app_id='Chain1_WikipediaQA',
    feedbacks=[qa_relevance, qs_relevance])

truchain("Which state is Washington D.C. in?")
```

After submitting a number of queries to your application, track your experiment and evaluations with the TruLens dashboard.

```Python Python theme={null}
tru.run_dashboard()
```

The dashboard shows the results of the first experiment:

<img alt="trulens-dashboard-1" />

#### Experiment with distance metrics

You've now built a tracked RAG application using cosine as the distance metric. To run the next two experiments, rebuild the index with `euclidean` or `dotproduct` as the metric and follow the rest of the preceding steps as is.

Because this example uses OpenAI embeddings, which are normalized to length 1, dot product and cosine distance are equivalent, and Euclidean also yields the same ranking. See the OpenAI docs for more information. With the same document ranking, you shouldn't expect a difference in response quality, but computation latency may vary across the metrics. OpenAI advises that dot product computation may be a bit faster than cosine. You can confirm this expected latency difference with TruLens.

```Python Python theme={null}
index_name_v2 = 'langchain-rag-euclidean'
pinecone.create_index(
        name=index_name_v2,
        metric='euclidean', # metric='dotproduct',
        dimension=1536,  # 1536 dim of text-embedding-ada-002
    )
```

After doing so, you can view the evaluations for all three LLM apps running on the different indexes. All three apps are struggling with query-statement relevance. In other words, the context retrieved is only somewhat relevant to the original query.

Both the Euclidean and dot-product metrics also performed at a lower latency than cosine at roughly the same evaluation quality.

<img alt="trulens-dashboard-2" />

### Diagnose hallucination

Looking more closely at Query Statement Relevance shows one problem in particular, with a question about famous dental floss brands. The app responds correctly, but isn't backed up by the context retrieved, which doesn't mention any specific brands.

<img alt="trulens-dashboard-feedback-1" />

#### Evaluate app components with LangChain and TruLens

Using a less capable model is a common way to reduce hallucination for some applications. The next experiment evaluates ada-001 for this purpose.

<img alt="trulens-dashboard-3" />

With frameworks like LangChain, you can swap out components of your app. In this case, you call `text-ada-001` from the LangChain LLM store. Evaluating each change with TruLens lets you iterate through different components to find the best app configuration.

```Python Python theme={null}
# completion llm
from langchain.llms import OpenAI

llm = OpenAI(
    model_name='text-ada-001',
    temperature=0
)

from langchain.chains import RetrievalQAWithSourcesChain
qa_with_sources = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# wrap with TruLens
truchain = TruChain(qa_with_sources,
    app_id='Chain4_WikipediaQA',
    feedbacks=[qa_relevance, qs_relevance])
```

However, this configuration with a less capable model struggles to return a relevant answer given the context provided.

<img alt="trulens-dashboard-4" />

For example, when asked “Which year was Hawaii's state song written?”, the app retrieves context that contains the correct answer but responds with only the name of the song.

<img alt="trulens-dashboard-feedback-2" />

The relevance function doesn't do a great job here of differentiating which context chunks are relevant, but you can see manually that only one chunk (the fourth) mentions the year the song was written. Narrowing `top_k`, the number of context chunks retrieved by the semantic search, may help.

To narrow `top_k`, update the retriever:

```Python Python theme={null}
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(top_k = 1)
)
```

The way the `top_k` is implemented in LangChain's RetrievalQA is that the documents are still retrieved by semantic search and only the `top_k` are passed to the LLM. Therefore, TruLens also captures all of the context chunks that are retrieved. To calculate an accurate QS Relevance metric that matches what's passed to the LLM, calculate the relevance of only the top context chunk by slicing the `input_documents` passed into the TruLens Select function:

```Python Python theme={null}
qs_relevance = Feedback(openai.qs_relevance).on_input().on(
    Select.Record.app.combine_documents_chain._call.args.inputs.input_documents[:1].page_content
).aggregate(np.mean)
```

With this change, the final application has much improved `qs_relevance`, `qa_relevance`, and latency.

<img alt="trulens-dashboard-5" />

The application now retrieves the one piece of context it needs and forms an answer from that context.

<img alt="trulens-dashboard-feedback-3" />

The application also now recognizes when it doesn't know the answer:

<img alt="trulens-dashboard-feedback-4" />

### Summary

Exploring the downstream impact of Pinecone configuration choices on response quality, cost, and latency is an important part of the LLM app development process, because it helps you make the choices that lead to the best-performing app. You can use TruLens and Pinecone together to build reliable RAG-style applications. Pinecone stores and retrieves the context used by LLM apps, and TruLens tracks and evaluates each iteration of your application.
