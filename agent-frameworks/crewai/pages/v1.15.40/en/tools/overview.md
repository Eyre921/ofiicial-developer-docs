---
title: "Tools Overview"
source: https://docs.crewai.com/v1.15.40/en/tools/overview
path: v1.15.40/en/tools/overview
---

Discover CrewAI's extensive library of 40+ tools to supercharge your AI agents

CrewAI provides an extensive library of pre-built tools to enhance your agents' capabilities. From file processing to web scraping, database queries to AI services - we've got you covered.

## **Tool Categories**

> [card] [File & Document](/en/tools/file-document/overview)
>
> Read, write, and search through various file formats including PDF, DOCX, JSON, CSV, and more. Perfect for document processing workflows.

> [card] [Web Scraping & Browsing](/en/tools/web-scraping/overview)
>
> Extract data from websites, automate browser interactions, and scrape content at scale with tools like Firecrawl, Selenium, and more.

> [card] [Search & Research](/en/tools/search-research/overview)
>
> Perform web searches, find code repositories, research YouTube content, and discover information across the internet.

> [card] [Database & Data](/en/tools/database-data/overview)
>
> Connect to databases, vector stores, and data warehouses. Query MySQL, PostgreSQL, MongoDB, Snowflake, Qdrant, and Weaviate.

> [card] [AI & Machine Learning](/en/tools/ai-ml/overview)
>
> Generate images with DALL-E, process vision tasks, integrate with LangChain, build RAG systems, and leverage code interpreters.

> [card] [Cloud & Storage](/en/tools/cloud-storage/overview)
>
> Interact with cloud services including AWS S3, Amazon Bedrock, and other cloud storage and AI services.

> [card] [Automation](/en/tools/automation/overview)
>
> Automate workflows with Apify, Composio, and other platforms to connect your agents with external services.

> [card] [Integrations](/en/tools/tool-integrations/overview)
>
> Integrate CrewAI with external systems like Amazon Bedrock and the CrewAI Automation toolkit.

## **Quick Access**

Need a specific tool? Here are some popular choices:

> [card] [RAG Tool](/en/tools/ai-ml/ragtool)
>
> Implement Retrieval-Augmented Generation

> [card] [Serper Dev](/en/tools/search-research/serperdevtool)
>
> Google search API

> [card] [File Read](/en/tools/file-document/filereadtool)
>
> Read any file type

> [card] [Directory Read](/en/tools/file-document/directoryreadtool)
>
> List and read directory contents

> [card] [Scrape Website](/en/tools/web-scraping/scrapewebsitetool)
>
> Extract web content

> [card] [Code Interpreter](/en/tools/ai-ml/codeinterpretertool)
>
> Execute Python code

> [card] [S3 Reader](/en/tools/cloud-storage/s3readertool)
>
> Access AWS S3 files

> [card] [MongoDB Vector Search](/en/tools/database-data/mongodbvectorsearchtool)
>
> Run vector similarity queries on MongoDB

## **Getting Started**

To use any tool in your CrewAI project:

1. **Import** the tool in your crew configuration
2. **Add** it to your agent's tools list
3. **Configure** any required API keys or settings

```python theme={null}
from crewai_tools import FileReadTool, SerperDevTool

# Add tools to your agent
agent = Agent(
    role="Research Analyst",
    tools=[FileReadTool(), SerperDevTool()],
    # ... other configuration
)
```

## **Max Usage Count**

You can set a maximum usage count for a tool to prevent it from being used more than a certain number of times.
By default, the max usage count is unlimited.

```python theme={null}
from crewai_tools import FileReadTool

tool = FileReadTool(max_usage_count=5, ...)
```

Ready to explore? Pick a category above to discover tools that fit your use case!
