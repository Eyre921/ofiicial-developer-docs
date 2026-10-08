---
title: "Aryn"
source: https://docs.pinecone.io/integrations/aryn
path: integrations/aryn
---

Use Aryn Sycamore and the Partitioning Service with Pinecone to extract, chunk, and embed complex PDFs and documents for higher-accuracy RAG pipelines.

Aryn is an AI-powered ETL system for complex, unstructured documents like PDFs, HTML, and presentations. It's built for RAG and generative AI applications, and Aryn reports up to 6x better accuracy in chunking and extracting information from documents. This can lead to 30% better recall and 2x improvement in answer accuracy for real-world use cases. The Pinecone integration with Aryn lets you chunk documents, create vector embeddings, and load the results into Pinecone.

Aryn's ETL system has two components: Sycamore and the Aryn Partitioning Service. Sycamore is Aryn's open-source document processing engine, available as a Python library. It contains a set of transforms for information extraction, LLM-powered enrichment, data cleaning, creating vector embeddings, and loading Pinecone indexes.

The Aryn Partitioning Service is the first step in a Sycamore data processing pipeline. It identifies and extracts parts of documents, like text, tables, and images, using a vision segmentation AI model trained on hundreds of thousands of human-annotated documents.

<PrimarySecondaryCTA />
