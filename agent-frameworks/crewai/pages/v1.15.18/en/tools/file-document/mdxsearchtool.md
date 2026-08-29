---
title: "MDX RAG Search"
source: https://docs.crewai.com/v1.15.18/en/tools/file-document/mdxsearchtool
path: v1.15.18/en/tools/file-document/mdxsearchtool
---

The `MDXSearchTool` is designed to search MDX files and return the most relevant results.

# `MDXSearchTool`

<Note>
  The MDXSearchTool is in continuous development. Features may be added or removed, and functionality could change unpredictably as we refine the tool.
</Note>

## Description

The MDX Search Tool is a component of the `crewai_tools` package aimed at facilitating advanced markdown language extraction. It enables users to effectively search and extract relevant information from MD files using query-based searches. This tool is invaluable for data analysis, information management, and research tasks, streamlining the process of finding specific information within large document collections.

## Installation

Before using the MDX Search Tool, ensure the `crewai_tools` package is installed. If it is not, you can install it with the following command:

```shell theme={null}
pip install 'crewai[tools]'
```

## Usage Example

To use the MDX Search Tool, you must first set up the necessary environment variables. Then, integrate the tool into your crewAI project to begin your market research. Below is a basic example of how to do this:

```python Code theme={null}
from crewai_tools import MDXSearchTool

# Initialize the tool to search any MDX content it learns about during execution
tool = MDXSearchTool()

# OR

# Initialize the tool with a specific MDX file path for an exclusive search within that document
tool = MDXSearchTool(mdx='path/to/your/document.mdx')
```

## Parameters

* mdx: **Optional**. Specifies the MDX file path for the search. It can be provided during initialization.

## Customization of Model and Embeddings

The tool defaults to using OpenAI for embeddings and summarization. For customization, utilize a configuration dictionary as shown below:

```python Code theme={null}
from chromadb.config import Settings

tool = MDXSearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
            }
        },
    }
)
```
