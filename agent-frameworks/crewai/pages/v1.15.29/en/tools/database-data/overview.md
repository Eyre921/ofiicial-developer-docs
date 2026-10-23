---
title: "Overview"
source: https://docs.crewai.com/v1.15.29/en/tools/database-data/overview
path: v1.15.29/en/tools/database-data/overview
---

Connect to databases, vector stores, and data warehouses for comprehensive data access

These tools enable your agents to interact with various database systems, from traditional SQL databases to modern vector stores and data warehouses.

## **Available Tools**

> **[MySQL Tool](/en/tools/database-data/mysqltool)**
>
> Connect to and query MySQL databases with SQL operations.

> **[PostgreSQL Search](/en/tools/database-data/pgsearchtool)**
>
> Search and query PostgreSQL databases efficiently.

> **[Snowflake Search](/en/tools/database-data/snowflakesearchtool)**
>
> Access Snowflake data warehouse for analytics and reporting.

> **[NL2SQL Tool](/en/tools/database-data/nl2sqltool)**
>
> Convert natural language queries to SQL statements automatically.

> **[Qdrant Vector Search](/en/tools/database-data/qdrantvectorsearchtool)**
>
> Search vector embeddings using Qdrant vector database.

> **[Weaviate Vector Search](/en/tools/database-data/weaviatevectorsearchtool)**
>
> Perform semantic search with Weaviate vector database.

> **[MongoDB Vector Search](/en/tools/database-data/mongodbvectorsearchtool)**
>
> Vector similarity search on MongoDB Atlas with indexing helpers.

> **[SingleStore Search](/en/tools/database-data/singlestoresearchtool)**
>
> Safe SELECT/SHOW queries on SingleStore with pooling and validation.

## **Common Use Cases**

* **Data Analysis**: Query databases for business intelligence and reporting
* **Vector Search**: Find similar content using semantic embeddings
* **ETL Operations**: Extract, transform, and load data between systems
* **Real-time Analytics**: Access live data for decision making

```python theme={null}
from crewai_tools import MySQLTool, MongoDBVectorSearchTool, QdrantVectorSearchTool, NL2SQLTool

# Create database tools
mysql_db = MySQLTool()
mongodb_vector_search = MongoDBVectorSearchTool(
    connection_string="<MONGODB_URI>",
    database_name="<database>",
    collection_name="<collection>",
)
qdrant_vector_search = QdrantVectorSearchTool()
nl_to_sql = NL2SQLTool()

# Add to your agent
agent = Agent(
    role="Data Analyst",
    tools=[mysql_db, mongodb_vector_search, qdrant_vector_search, nl_to_sql],
    goal="Extract insights from various data sources"
)
```
