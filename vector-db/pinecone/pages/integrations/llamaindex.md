---
title: "LlamaIndex"
source: https://docs.pinecone.io/integrations/llamaindex
path: integrations/llamaindex
---

Use Pinecone with LlamaIndex to build RAG pipelines that ingest documents, structure private data, and run semantic search and question answering.

LlamaIndex is a framework for connecting data sources to LLMs, with its chief use case being the end-to-end development of retrieval-augmented generation (RAG) applications. LlamaIndex provides abstractions to ingest, structure, and access private or domain-specific data so you can inject it safely and reliably into LLMs for more accurate text generation. It's available in Python and TypeScript.

Integrate Pinecone Database with LlamaIndex to build semantic search and RAG applications.

## Setup guide

This guide shows you how to use LlamaIndex and Pinecone to both perform traditional semantic search and build a RAG pipeline. Specifically, you'll do the following:

* Load, transform, and vectorize sample data with LlamaIndex
* Index and store the vectorized data in Pinecone
* Search the data in Pinecone and use the results to augment an LLM call
* Evaluate the answer you get back from the LLM

To run this guide in your browser, see the [LlamaIndex notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/main/learn/generation/llama-index/using-llamaindex-with-pinecone.ipynb).

<Note>
  This guide shows one of many ways to use LlamaIndex as part of a RAG pipeline. See LlamaIndex's section on [Advanced RAG](https://developers.llamaindex.ai/python/framework/optimizing/advanced_retrieval/advanced_retrieval/) to learn more about what's possible.
</Note>

<Steps>
  <Step title="Set up the environment">
    Install the libraries:

    ```shell Shell theme={null}
    pip install -qU \
        "pinecone[grpc]==9.1.0" \
        llama-index==0.14.25 \
        llama-index-vector-stores-pinecone==0.9.0 \
        llama-index-readers-file==0.7.0 \
        arxiv==4.0.1 \
        setuptools  # (Optional)
    ```

    Set your Pinecone and OpenAI API keys as environment variables:

    ```shell Shell theme={null}
    export PINECONE_API_KEY="your-pinecone-api-key"  # Get from app.pinecone.io
    export OPENAI_API_KEY="your-openai-api-key"  # Get from platform.openai.com/api-keys
    ```

    All code on this page runs on Python 3.12.
  </Step>

  <Step title="Load the data">
    This guide uses the [canonical HNSW paper](https://arxiv.org/pdf/1603.09320.pdf) by Yuri Malkov (PDF) as the sample dataset. First, download the PDF from arXiv.org and load it into a LlamaIndex loader called [PDF Loader](https://llamahub.ai/l/file-pdf?from=all). This loader is available (along with many more) on [LlamaHub](https://llamahub.ai/), a directory of data loaders.

    ```Python Python theme={null}
    import arxiv
    from pathlib import Path
    from urllib.request import urlretrieve
    from llama_index.readers.file import PDFReader

    # Download paper to local file system (LFS)
    # `id_list` contains 1 item that matches our PDF's arXiv ID
    paper = next(arxiv.Client().results(arxiv.Search(id_list=["1603.09320"])))
    urlretrieve(paper.pdf_url, "hnsw.pdf")

    # Instantiate `PDFReader` from LlamaHub
    loader = PDFReader()

    # Load HNSW PDF from LFS
    documents = loader.load_data(file=Path('./hnsw.pdf'))

    # Preview one of our documents
    documents[0]
    ```

    ```text Response theme={null}
    Document(id_='b0e25022-b6ef-4a39-9705-fdde26f7b1ae', embedding=None, metadata={'page_label': '1', 'file_name': 'hnsw.pdf'}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, metadata_template='{key}: {value}', metadata_separator='\n', text_resource=MediaResource(embeddings=None, data=None, text="IEEE TRANSACTIONS ON JOURNAL NAME,  MANUSCRIPT ID 1 \n \nEfficient and robust approximate nearest \nneighbor search using Hierarchical Navigable \nSmall World graphs  \nYu. A. Malkov, D. A. Yashunin \nAbstract — We present a new approach for the approximate K -nearest neighbor search based on navigable small world \ngraphs with controllable hierarchy (Hierarchical NSW, ...
    ```

    Each `Document` has a lot of useful information, but depending on which loader you choose, you may have to clean your data. In this case, you need to remove things like remaining `\n` characters and broken, hyphenated words (e.g., `alg o-\nrithms` → `algorithms`).

    ```Python Python theme={null}
    # Clean up our Documents' content
    import re

    def clean_up_text(content: str) -> str:
        """
        Remove unwanted characters and patterns in text input.

        :param content: Text input.
        
        :return: Cleaned version of original text input.
        """

        # Fix hyphenated words broken by newline
        content = re.sub(r'(\w+)-\n(\w+)', r'\1\2', content)

        # Remove specific unwanted patterns and characters
        unwanted_patterns = [
            "\\n", "  —", "——————————", "—————————", "—————",
            r'\\u[\dA-Fa-f]{4}', r'\uf075', r'\uf0b7'
        ]
        for pattern in unwanted_patterns:
            content = re.sub(pattern, "", content)

        # Fix improperly spaced hyphenated words and normalize whitespace
        content = re.sub(r'(\w)\s*-\s*(\w)', r'\1-\2', content)
        content = re.sub(r'\s+', ' ', content)

        return content

    # Call function
    cleaned_docs = []
    for d in documents: 
        cleaned_text = clean_up_text(d.text)
        d.set_content(cleaned_text)
        cleaned_docs.append(d)

    # Inspect output
    cleaned_docs[0].get_content()
    ```

    ```text Response theme={null}
    "IEEE TRANSACTIONS ON JOURNAL NAME, MANUSCRIPT ID 1 Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs Yu. A. Malkov, D. A. Yashunin Abstract — We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW, HNSW). The proposed solution is fully graph-based, ..."
    ```

    A file loader from LlamaHub breaks your PDF down into LlamaIndex [Documents](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/#documents-nodes). Each Document object comes with a [customizable](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_documents/#metadata) metadata dictionary and a hash ID, among other useful artifacts.
  </Step>

  <Step title="Transform the data">
    #### Metadata

    If you look at one of your cleaned Document objects, you'll see that the default values in your metadata dictionary aren't particularly useful.

    ```Python Python theme={null}
    cleaned_docs[0].metadata
    ```

    ```text Response theme={null}
    {'page_label': '1', 'file_name': 'hnsw.pdf'}
    ```

    To make the metadata more helpful, add the authors' names and the paper's title. Whatever metadata you add to the metadata dictionary applies to all [Nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/#nodes), so keep your additions high-level.

    <Note>
      LlamaIndex also provides [advanced customizations](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_documents/#advanced-metadata-customization) for what metadata the LLM can see vs. the embedding, etc.
    </Note>

    ```Python Python theme={null}
    # Iterate through `documents` and add our new key:value pairs
    metadata_additions = {"authors": ["Yu. A. Malkov", "D. A. Yashunin"],
      "title": "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"}

    # Update dict in place
    for cd in cleaned_docs:
        cd.metadata.update(metadata_additions)

    # Let's confirm everything worked:
    cleaned_docs[0].metadata
    ```

    ```text Response theme={null}
    {'page_label': '1',
     'file_name': 'hnsw.pdf',
     'authors': ['Yu. A. Malkov', 'D. A. Yashunin'],
     'title': 'Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs'}
    ```

    #### Ingestion pipeline

    To turn your data into indexable vectors and put them into Pinecone, create what's called an [Ingestion Pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/). An Ingestion Pipeline takes your list of Documents, parses them into Nodes (or "[chunks](https://www.pinecone.io/learn/chunking-strategies/)" in non-LlamaIndex contexts), vectorizes each Node's content, and upserts them into Pinecone.

    In the following pipeline, you'll use LlamaIndex's [SemanticSplitterNodeParser](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/modules/#semanticsplitternodeparser), which uses OpenAI's [text-embedding-3-small model](https://platform.openai.com/docs/models/text-embedding-3-small) to split Documents into semantically coherent Nodes.

    This step uses the OpenAI API key you set as an environment variable [earlier](#set-up-the-environment).

    ```Python Python theme={null}
    import os

    from llama_index.core.node_parser import SemanticSplitterNodeParser
    from llama_index.embeddings.openai import OpenAIEmbedding
    from llama_index.core.ingestion import IngestionPipeline

    # This will be the model we use both for Node parsing and for vectorization
    embed_model = OpenAIEmbedding(
        model="text-embedding-3-small",
        api_key=os.environ["OPENAI_API_KEY"],
    )

    # Define the initial pipeline
    pipeline = IngestionPipeline(
        transformations=[
            SemanticSplitterNodeParser(
                buffer_size=1,
                breakpoint_percentile_threshold=95, 
                embed_model=embed_model,
                ),
            embed_model,
            ],
        )
    ```

    Don't run this pipeline yet. You'll modify it in the next section.
  </Step>

  <Step title="Upsert the data">
    The Ingestion Pipeline you defined still needs a vector store to upsert your transformed data into.

    LlamaIndex lets you declare a [VectorStore](https://developers.llamaindex.ai/python/examples/vector_stores/pineconeindexdemo/) and add it directly to the pipeline for ingestion. The following code does this with Pinecone.

    This step uses the Pinecone API key you set as an environment variable [earlier](#set-up-the-environment).

    ```Python Python theme={null}
    from pinecone.grpc import PineconeGRPC
    from pinecone import ServerlessSpec

    from llama_index.vector_stores.pinecone import PineconeVectorStore

    # Initialize connection to Pinecone
    pc = PineconeGRPC(api_key=os.environ["PINECONE_API_KEY"])
    index_name = "llama-integration-example"

    # Create your index if it doesn't exist
    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    # Initialize your index 
    pinecone_index = pc.Index(index_name)

    # Initialize VectorStore
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    ```

    Now that your `PineconeVectorStore` is initialized, add it to your `pipeline` and run it.

    ```Python Python theme={null}
    # Our pipeline with the addition of our PineconeVectorStore
    pipeline = IngestionPipeline(
        transformations=[
            SemanticSplitterNodeParser(
                buffer_size=1,
                breakpoint_percentile_threshold=95, 
                embed_model=embed_model,
                ),
            embed_model,
            ],
        vector_store=vector_store,  # Our new addition
        )

    # Now we run our pipeline!
    pipeline.run(documents=cleaned_docs)
    ```

    Confirm that your index is up and running with a Pinecone-native method like `.describe_index_stats()`:

    ```Python Python theme={null}
    pinecone_index.describe_index_stats()
    ```

    ```text Response theme={null}
    DescribeIndexStatsResponse(dimension=1536, total_vector_count=46, metric='cosine', namespaces=1)
    ```

    Your index now has vectors in it. Because it has 46 vectors, you can infer that your `SemanticSplitterNodeParser` split your list of Documents into 46 Nodes.
  </Step>

  <Step title="Query the data">
    To fetch search results from Pinecone itself, you need to create a [VectorStoreIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/) object and a [VectorIndexRetriever](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/indices/vector_store/retrievers/retriever.py) object. You can then pass natural language queries to your Pinecone index and receive results.

    ```Python Python theme={null}
    from llama_index.core import VectorStoreIndex
    from llama_index.core.retrievers import VectorIndexRetriever

    # Instantiate VectorStoreIndex object from your vector_store object
    vector_index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=embed_model,
    )

    # Grab 5 search results
    retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=5)

    # Query vector DB
    answer = retriever.retrieve('How does logarithmic complexity affect graph construction?')

    # Inspect results
    print([i.get_content() for i in answer])
    ```

    ```text Response theme={null}
    ['AUTHOR ET AL.: TITLE 7 be auto-configured by using sample data. The construction process can be easily and efficiently parallelized ...',
     'AUTHOR ET AL.: TITLE 3 from a low degree node and traverses the graph simultaneously increasing the node’s degree ...',
     'the number of distance calculations). Links to the closest neighbors in a k-NN graph serve as a simple approximation of the Delaunay graph ...',
     'Simulations show that at least for low dimensional data (Fig. 11, d=4) the dependence of the required ef parameter ...',
     '4 IEEE TRANSACTIONS ON JOURNAL NAME, MANUSCRIPT ID NSW approach thus can utilize the same methods for making the distributed approximate search/overlay structures ...']
    ```

    These search results can now be plugged into any downstream task you want.

    One of the most common ways to use these search results is as additional context to augment a query sent to an LLM. This workflow is commonly called a [RAG application](https://www.pinecone.io/learn/retrieval-augmented-generation/).
  </Step>

  <Step title="Build a RAG app with the data">
    You could create a [Query Engine](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/usage_pattern/#usage-pattern) out of your `vector_index` object by calling `vector_index.as_query_engine().query('some query')`, but then you wouldn't be able to specify the number of Pinecone search results you'd like to use as context.

    To control how many search results your RAG app uses from your Pinecone index, create your Query Engine with the [RetrieverQueryEngine](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/query_engine/retriever_query_engine.py) class instead. This class lets you pass in the `retriever` you created earlier, which you configured to retrieve the top 5 search results.

    ```Python Python theme={null}
    from llama_index.core import Settings
    from llama_index.core.query_engine import RetrieverQueryEngine
    from llama_index.llms.openai import OpenAI

    # Set the LLM that generates answers (and evaluates them later)
    Settings.llm = OpenAI(model="gpt-4o-mini")

    # Pass in your retriever from above, which is configured to return the top 5 results
    query_engine = RetrieverQueryEngine(retriever=retriever)

    # Now you query:
    llm_query = query_engine.query('How does logarithmic complexity affect graph construction?')

    llm_query.response
    ```

    ```text Response theme={null}
    'Logarithmic complexity in graph construction allows for efficient scaling as the dataset size increases. Specifically, it ensures that the time required to construct the graph grows at a manageable rate, proportional to the logarithm of the number of elements rather than linearly. This means that even as the dataset expands, the construction process remains feasible and does not become prohibitively time-consuming. The construction complexity is influenced by parameters that control the number of connections and layers, allowing for a balance between speed and the quality of the resulting graph. Consequently, this logarithmic scaling facilitates the handling of large datasets while maintaining performance.'
    ```

    You can also inspect the context (Nodes) that informed your LLM's answer with the `.source_nodes` attribute. The following example inspects the first Node:

    ```Python Python theme={null}
    llm_query.source_nodes[0].get_content()
    ```

    ```text Response theme={null}
    'AUTHOR ET AL.: TITLE 7 be auto-configured by using sample data. The construction process can be easily and efficiently parallelized with only few synchronization points (as demonstrated in Fig. 9) and no measurable effect on index quality. Construction speed/index quality tradeoff is controlled via ...'
    ```
  </Step>

  <Step title="Evaluate the data">
    Now that you've made a RAG app and queried your LLM, evaluate its response.

    With LlamaIndex, there are [many ways](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/usage_pattern/) to evaluate the results your RAG app generates. A good first step is to confirm (or deny) that your LLM's responses are relevant, given the context retrieved from your Pinecone index. To do this, you can use LlamaIndex's [RelevancyEvaluator](https://developers.llamaindex.ai/python/examples/evaluation/relevancy_eval/#relevancy-evaluator) class.

    This type of evaluation doesn't need [ground truth data](https://dtunkelang.medium.com/evaluating-search-using-human-judgement-fbb2eeba37d9) (i.e., labeled datasets to compare answers with).

    ```Python Python theme={null}
    from llama_index.core.evaluation import RelevancyEvaluator

    # (Need to avoid peripheral asyncio issues)
    import nest_asyncio
    nest_asyncio.apply()

    # Define evaluator
    evaluator = RelevancyEvaluator()

    # Issue query
    llm_response = query_engine.query(
        "How does logarithmic complexity affect graph construction?"
    )

    # Grab context used in answer query & make it pretty
    llm_response_source_nodes = [i.get_content() for i in llm_response.source_nodes]

    # Take your previous question and pass in the response you got above
    eval_result = evaluator.evaluate_response(query="How does logarithmic complexity affect graph construction?", response=llm_response)

    # Print response
    print(f'\nGiven the {len(llm_response_source_nodes)} chunks of content (below), is your '
          f'LLM\'s response relevant? {eval_result.passing}\n'
          f'\n ----Contexts----- \n'
          f'\n{llm_response_source_nodes}')
    ```

    ```text Response theme={null}
    Given the 5 chunks of content (below), is your LLM's response relevant? True
             
     ----Contexts----- 
             
    ['AUTHOR ET AL.: TITLE 7 be auto-configured by using sample data. The construction process can be easily and efficiently parallelized with only few synchronization points (as demonstrated in Fig...']
    ```

    Your evaluator's result has various attributes you can inspect to see what's going on behind the scenes. To get a quick binary True/False signal as to whether your LLM is producing relevant results given your context, inspect the `.passing` attribute.

    Next, send an out-of-scope query through your RAG app. Issue a random query you know your RAG app can't answer, given what's in your index:

    ```Python Python theme={null}
    query = "Why did the chicken cross the road?"
    response = query_engine.query(query)

    print(response.response)
    ```

    ```text Response theme={null}
    To get to the other side.
    ```

    Then evaluate the response. The evaluator returns `False`, because the answer doesn't come from the retrieved context:

    ```Python Python theme={null}
    eval_result = evaluator.evaluate_response(query=query, response=response)

    print(str(eval_result.passing))
    ```

    ```text Response theme={null}
    False
    ```

    As expected, when you send an out-of-scope question through your RAG pipeline, your evaluator says the LLM's answer isn't relevant to the retrieved context.
  </Step>

  <Step title="Clean up">
    When you're finished with the index, delete it.

    ```Python Python theme={null}
    pc.delete_index(name=index_name)
    ```
  </Step>
</Steps>

### Summary

This guide covered how to build semantic search and RAG applications with LlamaIndex and Pinecone, and LlamaIndex has many more features. [Explore more](https://developers.llamaindex.ai/python/framework/) on your own and [let us know how it goes](https://discord.gg/tJ8V62S3sH).
