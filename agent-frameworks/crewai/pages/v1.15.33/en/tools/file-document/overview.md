---
title: "Overview"
source: https://docs.crewai.com/v1.15.33/en/tools/file-document/overview
path: v1.15.33/en/tools/file-document/overview
---

Read, write, and search through various file formats with CrewAI's document processing tools

These tools enable your agents to work with various file formats and document types. From reading PDFs to processing JSON data, these tools handle all your document processing needs.

## **Available Tools**

> **[File Read Tool](/en/tools/file-document/filereadtool)**
>
> Read content from any file type including text, markdown, and more.

> **[File Write Tool](/en/tools/file-document/filewritetool)**
>
> Write content to files, create new documents, and save processed data.

> **[PDF Search Tool](/en/tools/file-document/pdfsearchtool)**
>
> Search and extract text content from PDF documents efficiently.

> **[DOCX Search Tool](/en/tools/file-document/docxsearchtool)**
>
> Search through Microsoft Word documents and extract relevant content.

> **[JSON Search Tool](/en/tools/file-document/jsonsearchtool)**
>
> Parse and search through JSON files with advanced query capabilities.

> **[CSV Search Tool](/en/tools/file-document/csvsearchtool)**
>
> Process and search through CSV files, extract specific rows and columns.

> **[XML Search Tool](/en/tools/file-document/xmlsearchtool)**
>
> Parse XML files and search for specific elements and attributes.

> **[MDX Search Tool](/en/tools/file-document/mdxsearchtool)**
>
> Search through MDX files and extract content from documentation.

> **[TXT Search Tool](/en/tools/file-document/txtsearchtool)**
>
> Search through plain text files with pattern matching capabilities.

> **[Directory Search Tool](/en/tools/file-document/directorysearchtool)**
>
> Search for files and folders within directory structures.

> **[Directory Read Tool](/en/tools/file-document/directoryreadtool)**
>
> Read and list directory contents, file structures, and metadata.

> **[OCR Tool](/en/tools/file-document/ocrtool)**
>
> Extract text from images (local files or URLs) using a vision‑capable LLM.

> **[PDF Text Writing Tool](/en/tools/file-document/pdf-text-writing-tool)**
>
> Write text at specific coordinates in PDFs, with optional custom fonts.

## **Common Use Cases**

* **Document Processing**: Extract and analyze content from various file formats
* **Data Import**: Read structured data from CSV, JSON, and XML files
* **Content Search**: Find specific information within large document collections
* **File Management**: Organize and manipulate files and directories
* **Data Export**: Save processed results to various file formats

## **Quick Start Example**

```python theme={null}
from crewai_tools import FileReadTool, PDFSearchTool, JSONSearchTool

# Create tools
file_reader = FileReadTool()
pdf_searcher = PDFSearchTool()
json_processor = JSONSearchTool()

# Add to your agent
agent = Agent(
    role="Document Analyst",
    tools=[file_reader, pdf_searcher, json_processor],
    goal="Process and analyze various document types"
)
```

## **Tips for Document Processing**

* **File Permissions**: Ensure your agent has proper read/write permissions
* **Large Files**: Consider chunking for very large documents
* **Format Support**: Check tool documentation for supported file formats
* **Error Handling**: Implement proper error handling for corrupted or inaccessible files
