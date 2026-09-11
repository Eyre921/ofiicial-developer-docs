---
title: "Databricks"
source: https://docs.pinecone.io/integrations/databricks
path: integrations/databricks
---

Use Databricks and the Pinecone Spark connector to distribute embedding jobs across a cluster and upsert vectors at scale for semantic search and RAG.

Databricks is a Unified Analytics Platform on top of Apache Spark. The primary advantage of using Spark is its ability to distribute workloads across a cluster of machines. By adding more machines or increasing the number of cores on each machine, it is easy to horizontally scale a cluster to handle computationally intensive tasks like vector embedding, where parallelization can save many hours of precious computation time and resources. Leveraging GPUs with Spark can produce even better results — enjoying the benefits of the fast computation of a GPU combined with parallelization will ensure optimal performance.

Efficiently create, ingest, and update vector embeddings at scale with Databricks and Pinecone.

<PrimarySecondaryCTA />

## Setup guide

In this guide, you'll create embeddings based on the [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model from [Hugging Face](https://huggingface.co/), but the approach demonstrated here should work with any other model and dataset.

### Before you begin

Ensure you have the following:

* A [Databricks cluster](https://docs.databricks.com/en/compute/configure.html)
* A [Pinecone account](https://app.pinecone.io/)
* A [Pinecone API key](/guides/projects/understanding-projects#api-keys)

### 1. Install the Spark-Pinecone connector

<Tabs>
  <Tab title="Databricks platform">
    1. [Install the Spark-Pinecone connector as a library](https://docs.databricks.com/en/libraries/cluster-libraries.html#install-a-library-on-a-cluster).
    2. Configure the library as follows:
       1. Select **File path/S3** as the **Library Source**.

       2. Enter the S3 URI for the Pinecone assembly JAR file:

          ```
          s3://pinecone-jars/1.1.0/spark-pinecone-uberjar.jar  
          ```

          <Note>
            Databricks platform users must use the Pinecone assembly jar listed above to ensure that the proper dependecies are installed.
          </Note>

       3. Click **Install**.
  </Tab>

  <Tab title="Databricks on AWS">
    1. [Install the Spark-Pinecone connector as a library](https://docs.databricks.com/en/libraries/cluster-libraries.html#install-a-library-on-a-cluster).
    2. Configure the library as follows:
       1. Select **File path/S3** as the **Library Source**.

       2. Enter the S3 URI for the Pinecone assembly JAR file:

          ```
          s3://pinecone-jars/1.1.0/spark-pinecone-uberjar.jar  
          ```

       3. Click **Install**.
  </Tab>

  <Tab title="Databricks on GCP / Azure">
    1. [Install the Spark-Pinecone connector as a library](https://docs.databricks.com/en/libraries/cluster-libraries.html#install-a-library-on-a-cluster).
    2. Configure the library as follows:
       1. [Download the Pinecone assembly JAR file](https://repo1.maven.org/maven2/io/pinecone/spark-pinecone_2.12/1.1.0/).
       2. Select **Workspace** as the **Library Source**.
       3. Upload the JAR file.
       4. Click **Install**.
  </Tab>
</Tabs>

### 2. Load the dataset into partitions

As your example dataset, use a collection of news articles from Hugging Face's datasets library:

1. [Create a new notebook](https://docs.databricks.com/en/notebooks/notebooks-manage.html#create-a-notebook) attached to your cluster.

2. Install dependencies:

   ```
   pip install datasets transformers pinecone torch  
   ```

3. Load the dataset:

   ```Python Python theme={null}
   from datasets import list_datasets, load_dataset  
   dataset_name = "allenai/multinews_sparse_max"  
   dataset = load_dataset(dataset_name, split="train")  
   ```

4. Convert the dataset from the Hugging Face format and repartition it:

   ```Python Python theme={null}
   dataset.to_parquet("/dbfs/tmp/dataset_parquet.pq")  
   num_workers = 10  
   dataset_df = spark.read.parquet("/tmp/dataset_parquet.pq").repartition(num_workers)  
   ```

   Once the repartition is complete, you get back a DataFrame, which is a distributed collection of the data organized into named columns. It is conceptually equivalent to a table in a relational database or a dataframe in R/Python, but with richer optimizations under the hood. As mentioned above, each partition in the dataframe has an equal amount of the original data.

5. The dataset doesn't have identifiers associated with each document, so add them:

   ```Python Python theme={null}
   from pyspark.sql.types import StringType  
   from pyspark.sql.functions import monotonically_increasing_id  
   dataset_df = dataset_df.withColumn("id", monotonically_increasing_id().cast(StringType()))  
   ```

   As its name suggests, `withColumn` adds a column to the dataframe, containing a simple increasing identifier that you cast to a string.

### 3. Create the vector embeddings

1. Create a UDF (User-Defined Function) to create the embeddings, using the AutoTokenizer and AutoModel classes from the Hugging Face transformers library:

   ```Python Python theme={null}
   from transformers import AutoTokenizer, AutoModel  
   def create_embeddings(partitionData):  
       tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")  
       model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")  
       for row in partitionData:  
           document = str(row.document)  
           inputs = tokenizer(document, padding=True, truncation=True, return_tensors="pt", max_length=512)  
           result = model(**inputs)  
           embeddings = result.last_hidden_state[:, 0, :].cpu().detach().numpy()  
       lst = embeddings.flatten().tolist()  
       yield [row.id, lst, "", "{}", None]  
   ```

2. Apply the UDF to the data:

   ```Python Python theme={null}
   embeddings = dataset_df.rdd.mapPartitions(create_embeddings)  
   ```

   A dataframe in Spark is a higher-level abstraction built on top of a more fundamental building block called a resilient distributed dataset (RDD). Here, you use the `mapPartitions` function, which provides finer control over the execution of the UDF by explicitly applying it to each partition of the RDD.

3. Convert the resulting RDD back into a dataframe with the schema required by Pinecone:

   ```Python Python theme={null}
   from pyspark.sql.types import StructType, StructField, StringType, ArrayType, FloatType, IntegerType  
   schema = StructType([  
       StructField("id",StringType(),True),  
       StructField("values",ArrayType(FloatType()),True),  
       StructField("namespace",StringType(),True),  
       StructField("metadata", StringType(), True),  
       StructField("sparse_values", StructType([  
           StructField("indices", ArrayType(LongType(), False), False),  
           StructField("values", ArrayType(FloatType(), False), False)  
       ]), True)  
   ])  
   embeddings_df = spark.createDataFrame(data=embeddings,schema=schema)  
   ```

### 4. Save the embeddings in Pinecone

1. Initialize the connection to Pinecone:

   ```Python Python theme={null}
   from pinecone.grpc import PineconeGRPC as Pinecone
   from pinecone import ServerlessSpec

   pc = Pinecone(api_key="YOUR_API_KEY")
   ```

2. Create an index for your embeddings:

   ```Python Python theme={null}
   pc.create_index(
   name="news",
   dimension=1536,
   metric="cosine",
   spec=ServerlessSpec(
       cloud="aws",
       region="us-east-1"
   )
   )
   ```

3. Use the Spark-Pinecone connector to save the embeddings to your index:

   ```Python Python theme={null}
   (  
       embeddings_df.write  
       .option("pinecone.apiKey", api_key) 
       .option("pinecone.indexName", index_name)  
       .format("io.pinecone.spark.pinecone.Pinecone")  
       .mode("append")  
       .save()  
   )  
   ```

   The process of writing the embeddings to Pinecone should take approximately 15 seconds. When it completes, you'll see the following:

   ```
   spark: org.apache.spark.sql.SparkSession = org.apache.spark.sql.SparkSession@41638051  
   pineconeOptions: scala.collection.immutable.Map[String,String] = Map(pinecone.apiKey -><YOUR API KEY>, pinecone.indexName -> "news")  
   ```

   This means the process was completed successfully and the embeddings have been stored in Pinecone.

4. Perform a similarity search using the embeddings you loaded into Pinecone by providing a set of vector values or a vector ID. The [query endpoint](/reference/api/2025-10/data-plane/query) will return the IDs of the most similar records in the index, along with their similarity scores:
   ```Python Python theme={null}
       index.query(
           namespace="example-namespace",
           vector=[0.3, 0.3, 0.3, 0.3, 0.3],
           top_k=3,
           include_values=True
       )
   ```
   <Note>
     If you want to make a query with a text string (e.g., `"Summarize this article"`), use the [`search` endpoint via integrated inference](/reference/api/2025-10/data-plane/search_records).
   </Note>
