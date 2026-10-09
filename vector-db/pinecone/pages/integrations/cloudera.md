---
title: "Cloudera AI"
source: https://docs.pinecone.io/integrations/cloudera
path: integrations/cloudera
---

Integrate Cloudera AI with Pinecone to run distributed Spark and Python embedding pipelines and power scalable RAG and vector search on enterprise data.

[Cloudera AI](https://www.cloudera.com/) is an enterprise data cloud service for scalable, secure machine learning and AI workflows. It uses Python, Apache Spark, R, and other runtimes for distributed data processing, so you can create, ingest, and update vector embeddings at scale.

Integrating Pinecone with Cloudera AI adds vector search to retrieval-augmented generation (RAG) applications built on Cloudera AI. Pinecone retrieves relevant context from large datasets to ground model output in relevant, real-time data, with low query latency, dynamic index updates, and scale to billions of vector embeddings.

Cloudera AI integrates with the rest of the Cloudera ecosystem, so data flows across the stages of machine learning and AI pipelines. It offers interactive sessions, collaborative projects, model hosting, and application hosting in a Python-centric development environment. You can use its project and session management features to prototype, develop, and deploy RAG applications that combine Cloudera AI's hosted models with retrieval from Pinecone.

Cloudera's Accelerators for Machine Learning Projects (AMPs) are prebuilt projects that do the development work of deploying RAG architectures for you. This AMP is a prototype that fully integrates Pinecone into a RAG use case and shows semantic search with RAG at scale.

<PrimarySecondaryCTA />

## Resources

* [Python script](https://github.com/cloudera/CML_llm-hol/blob/main/2_populate_vector_db/pinecone_vectordb_insert.py) - Example of creating vectors in Pinecone
* [Jupyter notebook](https://github.com/cloudera/CML_llm-hol/blob/main/3_query_vector_db/pinecone_vectordb_query.ipynb) - Example of querying a Pinecone index
