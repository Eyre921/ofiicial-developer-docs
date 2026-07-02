---
title: "Aryn"
source: https://docs.pinecone.io/integrations/aryn
path: integrations/aryn
---

Connect Pinecone and Aryn to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

Aryn is an AI-powered ETL system for complex, unstructured documents like PDFs, HTML, presentations, and more. It's purpose-built for building RAG and GenAI applications, providing up to 6x better accuracy in chunking and extracting information from documents. This can lead to 30% better recall and 2x improvement in answer accuracy for real-world use cases.

Aryn's ETL system has two components: Sycamore and the Aryn Partitioning Service. Sycamore is Aryn's open source document processing engine, available as a Python library. It contains a set of transforms for information extraction, LLM-powered enrichment, data cleaning, creating vector embeddings, and loading Pinecone indexes.

The Aryn Partitioning Service is used as a first step in a Sycamore data processing pipeline, and it identifies and extracts parts of documents, like text, tables, images, and more. It uses a state-of-the-art vision segmentation AI model, trained on hundreds of thousands of human-annotated documents.

The Pinecone integration with Aryn enables developers to easily chunk documents, create vector embeddings, and load Pinecone with high-quality data.

<PrimarySecondaryCTA />
