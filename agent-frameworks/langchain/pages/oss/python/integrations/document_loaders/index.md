---
title: "Document loader integrations"
source: https://docs.langchain.com/oss/python/integrations/document_loaders/index
path: oss/python/integrations/document_loaders/index
---

Integrate with document loaders using LangChain Python.

Document loaders provide a **standard interface** for reading data from different sources (such as Slack, Notion, or Google Drive) into LangChain’s [Document](https://reference.langchain.com/python/langchain-core/documents/base/Document) format.
This ensures that data can be handled consistently regardless of the source.

All document loaders implement the [`BaseLoader`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader) interface.

<Warning>
  Community document loaders are user-contributed and unverified. LangChain does not review or endorse these integrations; use them at your own risk.
</Warning>

## Interface

Each document loader may define its own parameters, but they share a common API:

* `load()` – Loads all documents at once.
* `lazy_load()` – Streams documents lazily, useful for large datasets.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_docling.loader import DoclingLoader

FILE_PATH = "https://arxiv.org/pdf/2408.09869"

loader = DoclingLoader(file_path=FILE_PATH)

# Load all documents
documents = loader.load()

# For large datasets, lazily load documents
for document in loader.lazy_load():
    print(document)
```

## By category

### Productivity tools

The below document loaders allow you to load data from commonly used productivity tools.

| Document Loader                                                  | API reference                                                            |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [AgentMail](/oss/python/integrations/document_loaders/agentmail) | [`AgentMailLoader`](https://github.com/agentmail-to/langchain-agentmail) |

### Webpages

The below document loaders allow you to load webpages.

| Document Loader                                                             | Description                                                                                                          | Package/API |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Unstructured](/oss/python/integrations/document_loaders/unstructured_file) | Uses Unstructured to load and parse web pages                                                                        | Package     |
| [Apify Dataset](/oss/python/integrations/document_loaders/apify_dataset)    | Load documents from Apify datasets                                                                                   | API         |
| [Docling](/oss/python/integrations/document_loaders/docling)                | Uses Docling to load and parse web pages                                                                             | Package     |
| [Hyperbrowser](/oss/python/integrations/document_loaders/hyperbrowser)      | Platform for running and scaling headless browsers, can be used to scrape/crawl any site                             | API         |
| [AgentQL](/oss/python/integrations/document_loaders/agentql)                | Web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt | API         |
| [Browserbase](/oss/python/integrations/document_loaders/browserbase)        | Load webpages using managed headless browsers with stealth mode                                                      | API         |

### PDFs

The below document loaders allow you to load PDF documents.

| Document Loader                                                                    | Description                                          | Package/API |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------- |
| [Unstructured](/oss/python/integrations/document_loaders/unstructured_file)        | Uses Unstructured's open source library to load PDFs | Package     |
| [Upstage Document Parse Loader](/oss/python/integrations/document_loaders/upstage) | Load PDF files using UpstageDocumentParseLoader      | Package     |
| [Docling](/oss/python/integrations/document_loaders/docling)                       | Load PDF files using Docling                         | Package     |
| [UnDatasIO](/oss/python/integrations/document_loaders/undatasio)                   | Load PDF files using UnDatasIO                       | Package     |
| [OpenDataLoader PDF](/oss/python/integrations/document_loaders/opendataloader_pdf) | Load PDF files using OpenDataLoader PDF              | Package     |

### Cloud providers

The below document loaders allow you to load documents from your favorite cloud providers.

| Document Loader                                                                                            | Description                                         | Partner Package | API reference                                                                                                              |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Google Cloud Storage Directory](/oss/python/integrations/document_loaders/google_cloud_storage_directory) | Load documents from GCS bucket                      | ✅               | [`GCSDirectoryLoader`](https://reference.langchain.com/python/langchain-google-community/gcs_directory/GCSDirectoryLoader) |
| [Google Cloud Storage File](/oss/python/integrations/document_loaders/google_cloud_storage_file)           | Load documents from GCS file object                 | ✅               | [`GCSFileLoader`](https://reference.langchain.com/python/langchain-google-community/gcs_file/GCSFileLoader)                |
| [Google Drive](/oss/python/integrations/document_loaders/google_drive)                                     | Load documents from Google Drive (Google Docs only) | ✅               | [`GoogleDriveLoader`](https://reference.langchain.com/python/langchain-google-community/drive/GoogleDriveLoader)           |

### Common file types

The below document loaders allow you to load data from common data formats.

| Document Loader                                                                                  | Data Type                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Unstructured`](/oss/python/integrations/document_loaders/unstructured_file)                    | Many file types (see [https://docs.unstructured.io/platform/supported-file-types](https://docs.unstructured.io/platform/supported-file-types))                               |
| [`DoclingLoader`](/oss/python/integrations/document_loaders/docling)                             | Various file types (see [https://ds4sd.github.io/docling/](https://ds4sd.github.io/docling/))                                                                                |
| [`PolarisAIDataInsightLoader`](/oss/python/integrations/document_loaders/polaris_ai_datainsight) | Various file types (see [https://datainsight.polarisoffice.com/documentation?docType=doc\_extract](https://datainsight.polarisoffice.com/documentation?docType=doc_extract)) |

## All document loaders

<Columns>
  <Card title="AgentMail" icon="link" href="/oss/python/integrations/document_loaders/agentmail" />

  <Card title="AgentQLLoader" icon="link" href="/oss/python/integrations/document_loaders/agentql" />

  <Card title="AirbyteLoader" icon="link" href="/oss/python/integrations/document_loaders/airbyte" />

  <Card title="Apify Dataset" icon="link" href="/oss/python/integrations/document_loaders/apify_dataset" />

  <Card title="AstraDB" icon="link" href="/oss/python/integrations/document_loaders/astradb" />

  <Card title="Azure Blob Storage" icon="link" href="/oss/python/integrations/document_loaders/azure_blob_storage" />

  <Card title="Box" icon="link" href="/oss/python/integrations/document_loaders/box" />

  <Card title="Browserbase" icon="link" href="/oss/python/integrations/document_loaders/browserbase" />

  <Card title="Copy Paste" icon="link" href="/oss/python/integrations/document_loaders/copypaste" />

  <Card title="Docling" icon="link" href="/oss/python/integrations/document_loaders/docling" />

  <Card title="Docugami" icon="link" href="/oss/python/integrations/document_loaders/docugami" />

  <Card title="Google AlloyDB for PostgreSQL" icon="link" href="/oss/python/integrations/document_loaders/google_alloydb" />

  <Card title="Google BigQuery" icon="link" href="/oss/python/integrations/document_loaders/google_bigquery" />

  <Card title="Google Bigtable" icon="link" href="/oss/python/integrations/document_loaders/google_bigtable" />

  <Card title="Google Cloud SQL for SQL Server" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_sql_mssql" />

  <Card title="Google Cloud SQL for MySQL" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_sql_mysql" />

  <Card title="Google Cloud SQL for PostgreSQL" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_sql_pg" />

  <Card title="Google Cloud Storage Directory" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_storage_directory" />

  <Card title="Google Cloud Storage File" icon="link" href="/oss/python/integrations/document_loaders/google_cloud_storage_file" />

  <Card title="Google Firestore in Datastore Mode" icon="link" href="/oss/python/integrations/document_loaders/google_datastore" />

  <Card title="Google Drive" icon="link" href="/oss/python/integrations/document_loaders/google_drive" />

  <Card title="Google El Carro for Oracle Workloads" icon="link" href="/oss/python/integrations/document_loaders/google_el_carro" />

  <Card title="Google Firestore (Native Mode)" icon="link" href="/oss/python/integrations/document_loaders/google_firestore" />

  <Card title="Google Memorystore for Redis" icon="link" href="/oss/python/integrations/document_loaders/google_memorystore_redis" />

  <Card title="Google Spanner" icon="link" href="/oss/python/integrations/document_loaders/google_spanner" />

  <Card title="Google Speech-to-Text" icon="link" href="/oss/python/integrations/document_loaders/google_speech_to_text" />

  <Card title="HyperbrowserLoader" icon="link" href="/oss/python/integrations/document_loaders/hyperbrowser" />

  <Card title="Kinetica" icon="link" href="/oss/python/integrations/document_loaders/kinetica" />

  <Card title="LangSmith" icon="link" href="/oss/python/integrations/document_loaders/langsmith" />

  <Card title="Near Blockchain" icon="link" href="/oss/python/integrations/document_loaders/mintbase" />

  <Card title="OpenDataLoader PDF" icon="link" href="/oss/python/integrations/document_loaders/opendataloader_pdf" />

  <Card title="Oracle Autonomous Database" icon="link" href="/oss/python/integrations/document_loaders/oracleadb_loader" />

  <Card title="Oracle AI Database" icon="link" href="/oss/python/integrations/document_loaders/oracleai" />

  <Card title="Outline Document Loader" icon="link" href="/oss/python/integrations/document_loaders/outline" />

  <Card title="PaddleOCR-VL" icon="link" href="/oss/python/integrations/document_loaders/paddleocr_vl" />

  <Card title="Polaris AI DataInsight" icon="link" href="/oss/python/integrations/document_loaders/polaris_ai_datainsight" />

  <Card title="Dell PowerScale" icon="link" href="/oss/python/integrations/document_loaders/powerscale" />

  <Card title="PyMuPDF4LLM" icon="link" href="/oss/python/integrations/document_loaders/pymupdf4llm" />

  <Card title="SingleStore" icon="link" href="/oss/python/integrations/document_loaders/singlestore" />

  <Card title="Soniox" icon="link" href="/oss/python/integrations/document_loaders/soniox" />

  <Card title="UnDatasIO" icon="link" href="/oss/python/integrations/document_loaders/undatasio" />

  <Card title="Unstructured" icon="link" href="/oss/python/integrations/document_loaders/unstructured_file" />

  <Card title="Upstage" icon="link" href="/oss/python/integrations/document_loaders/upstage" />

  <Card title="YoutubeLoaderDL" icon="link" href="/oss/python/integrations/document_loaders/yt_dlp" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
