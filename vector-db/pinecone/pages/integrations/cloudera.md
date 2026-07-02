---
title: "Cloudera AI"
source: https://docs.pinecone.io/integrations/cloudera
path: integrations/cloudera
---

Connect Pinecone and Cloudera AI to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

[Cloudera AI](https://www.cloudera.com/) is an enterprise data cloud experience that provides scalable, secure, and agile machine learning and AI workflows. It leverages the power of Python, Apache Spark, R, and a host of other runtimes for distributed data processing, enabling the efficient creation, ingestion, and updating of vector embeddings at scale.

The primary advantage of Cloudera AI lies in its integration with the Cloudera ecosystem, which facilitates seamless data flow and processing across various stages of machine learning and AI pipelines. Cloudera AI offers interactive sessions, collaborative projects, model hosting capabilities, and application hosting features, all within a Python-centric development environment. This multifaceted approach enables users to efficiently develop, train, and deploy machine learning and AI models at scale.

Integrating Pinecone with Cloudera AI elevates the potential of Retrieval-Augmented Generation (RAG) models by providing a robust, scalable vector search platform. Pinecone's strength in handling vector embeddings — characterized by its ultra-low query latency, dynamic index updates, and scalability to billions of vector embeddings — make it the perfect match for the nuanced needs of RAG applications built on Cloudera AI.

Within the Cloudera AI ecosystem, Pinecone acts as a first-class citizen for RAG by efficiently retrieving relevant context from massive datasets, enhancing the generation capabilities of models with relevant, real-time data. This integration enables the development of sophisticated machine learning and AI applications that combine the predictive power of Cloudera AI's hosted models with the dynamic retrieval capabilities of Pinecone, offering unparalleled accuracy and relevance for generated outputs. By leveraging Cloudera AI's project and session management features, developers can prototype, develop, and deploy these complex systems more effectively, making advanced machine learning and AI applications more accessible and practical for enterprise use.

Cloudera's Accelerators for Machine Learning Projects (AMPs) drive efficient deployment of RAG architectures by doing the development work for you. This AMP serves as a prototype for fully integrating Pinecone into a RAG use case and illustrates semantic search with RAG at scale.

<PrimarySecondaryCTA />

## Additional resources

* [Python script](https://github.com/cloudera/CML_llm-hol/blob/main/2_populate_vector_db/pinecone_vectordb_insert.py) - Example of creating vectors in Pinecone
* [Jupyter notebook](https://github.com/cloudera/CML_llm-hol/blob/main/3_query_vector_db/pinecone_vectordb_query.ipynb) - Example of querying Pinecone collections
