---
title: "Amazon Bedrock"
source: https://docs.pinecone.io/integrations/amazon-bedrock
path: integrations/amazon-bedrock
---

Use Pinecone as the vector store for a Knowledge Base for Amazon Bedrock, then create a Bedrock agent that retrieves your data for RAG on AWS.

You can select Pinecone as a Knowledge Base for [Amazon Bedrock](https://aws.amazon.com/bedrock/), a fully managed service from Amazon Web Services (AWS) for building GenAI applications.

Pinecone Database helps companies reduce hallucinations, one of the biggest challenges in deploying GenAI solutions. With Pinecone, companies can store and search their own data, find the most relevant, up-to-date information, and send that context to large language models (LLMs) with every query. This workflow is called retrieval-augmented generation (RAG). With Pinecone, RAG helps search and GenAI applications return relevant, accurate, and fast responses to end users.

With Knowledge Bases for Amazon Bedrock, you can integrate your enterprise data into Amazon Bedrock and use Pinecone as the vector store for your GenAI applications. Pinecone helps those applications in the following ways:

* Pinecone searches through data in milliseconds. Metadata filters and support for sparse-dense vectors in a single index improve relevance, so results are quick, accurate, and grounded across diverse search tasks.
* You can start for free on the Starter plan and scale usage with transparent usage-based pricing. Add or remove resources to meet your desired capacity and performance, upwards of billions of embeddings.
* You can launch, use, and scale your AI solution without maintaining infrastructure, monitoring services, or troubleshooting algorithms. Pinecone meets the security and operational requirements of enterprises.

<PrimarySecondaryCTA />

## Agents for Amazon Bedrock

In Bedrock, users interact with agents, which combine the natural language interface of the supported LLMs with that of a knowledge base. Bedrock's Knowledge Base feature uses the supported LLMs to generate embeddings from the original data source. These embeddings are stored in Pinecone, and Bedrock uses the Pinecone index to retrieve semantically relevant content when a user queries the agent.

<Note>
  The LLM used for embeddings can be different from the one used for natural language generation. For example, you can use Amazon Titan to generate embeddings and Anthropic's Claude to generate natural language responses.
</Note>

You can also configure Agents for Amazon Bedrock to execute various actions while responding to a user's query. This guide doesn't cover that functionality.

## Knowledge Bases for Amazon Bedrock

A Bedrock knowledge base ingests raw text data or documents found in Amazon S3, embeds the content, and upserts the embeddings into Pinecone. Then, a Bedrock agent can interact with the knowledge base to retrieve the most semantically relevant content for a user's query.

The Knowledge Base feature helps you improve your AI models' performance. With Bedrock's LLMs and Pinecone, you can integrate your data from AWS storage solutions and improve the accuracy and relevance of your AI models.

This guide walks through creating a Knowledge Base for Amazon Bedrock and an agent that retrieves information from it.

<img alt="" />

## Setup guide

Using a Bedrock knowledge base with Pinecone involves the following steps:

<Steps>
  <Step title="Create a Pinecone index.">
    Create an empty Pinecone index with an embedding model in mind. The index must be empty for Bedrock integration.
  </Step>

  <Step title="Set up a data source.">
    Upload sample data to Amazon S3.
  </Step>

  <Step title="Create a Bedrock knowledge base.">
    Sync data with Bedrock to create embeddings saved in Pinecone.
  </Step>

  <Step title="Connect Pinecone to Bedrock.">
    Use the knowledge base to reference the data saved in Pinecone.
  </Step>

  <Step title="Create and link agents to Bedrock.">
    Agents can interact directly with the Bedrock knowledge base, which will retrieve the semantically relevant content.
  </Step>
</Steps>

### Create a Pinecone index

The knowledge base stores data in a Pinecone index. Decide which [supported embedding model](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) to use with Bedrock before you create the index, because your index's dimensions must match the model's. For example, the AWS Titan Text Embeddings V2 model can use dimension sizes 1024, 384, and 256.

After you sign up for Pinecone, follow the [quickstart guide](/guides/get-started/quickstart) to create your Pinecone index and retrieve your `apiKey` and index host from the [Pinecone console](https://app.pinecone.io).

<Note>
  Your index must have the same dimensions as the model you'll later select for creating your embeddings. Also, your index must be empty. All data must be ingested through Bedrock's sync process.
</Note>

### Set up your data source

#### Set up secrets

After you set up your Pinecone index, create a secret in [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/newsecret):

1. In the **Secret type** section, select **Other type of secret**.
2. In the **Key/value pairs** section, enter a key-value pair for the Pinecone API key name and its respective value. For example, use `apiKey` and the API key value.
   <img alt="" />
3. Click **Next**.
4. Enter a **Secret name** and **Description**.
5. Click **Next** to save your key.
6. On the **Configure rotation** page, select all the default options in the next screen, and click **Next**.
7. Click **Store**.
8. Click the new secret you created and save the secret ARN for a later step.

#### Set up S3

The knowledge base draws on data saved in S3. This example uses a [sample of research papers](https://huggingface.co/datasets/jamescalam/ai-arxiv2-semantic-chunks) obtained from a dataset. Bedrock embeds this data and then saves it in Pinecone. Follow these steps to set up S3:

1. Create a new general purpose bucket in [Amazon S3](https://console.aws.amazon.com/s3/home).

2. After the bucket is created, upload a CSV file.

   <Note>
     The CSV file must have a field for text that will be embedded, and a field for metadata to upload with each embedded text.
   </Note>

3. Save your bucket's address (`s3://…`) for the following configuration steps.

### Create a Bedrock knowledge base

To [create a Bedrock knowledge base](https://console.aws.amazon.com/bedrock/home?#/knowledge-bases/create-knowledge-base), use the following steps:

1. Enter a **Knowledge Base name**.
2. In the **Choose data source** section, select **Amazon S3**.
3. Click **Next**.
4. On the **Configure data source** page, enter the **S3 URI** for the bucket you created.
5. If you don't want to use the default chunking strategy, select a chunking strategy.
6. Click **Next**.

### Connect Pinecone to the knowledge base

Next, select an embedding model to configure with Bedrock, and configure the data sources:

1. Select the embedding model you decided on earlier.
2. For the **Vector database**, select **Choose a vector store you have created** and select **Pinecone**.
3. Select the checkbox that authorizes AWS to access your Pinecone index.

   <Note>
     Ensure your Pinecone index is empty before proceeding. Bedrock can't work with indexes that contain existing data. All data must be ingested through Bedrock's sync process.
   </Note>
4. For the **Endpoint URL**, enter the Pinecone index host retrieved from the Pinecone console.
5. For the **Credentials secret ARN**, enter the secret ARN you created earlier.
6. In the **Metadata field mapping** section, enter the **Text field name** you want to embed and the **Bedrock-managed metadata field name** that Bedrock uses for metadata it manages (e.g., `metadata`).
7. Click **Next**.
8. Review your selections and complete the creation of the knowledge base.
9. On the [Knowledge Bases](https://console.aws.amazon.com/bedrock/home?#/knowledge-bases) page, select the knowledge base you just created to view its details.
10. Click **Sync** for the newly created data source.
    <Note>
      Whenever you add new data, sync the data source to start the ingestion workflow, which converts your Amazon S3 data into vector embeddings and upserts them into your Pinecone index. Depending on the amount of data, this can take some time.
    </Note>

### Create and link an agent to Bedrock

Lastly, [create an agent](https://console.aws.amazon.com/bedrock/home?#/agents) that will use the knowledge base for retrieval:

1. Click **Create Agent**.
2. Enter a **Name** and **Description**.
3. Click **Create**.
4. Select the LLM provider and model you'd like to use.
5. Provide instructions for the agent. These define what the agent is trying to accomplish.
6. In the **Knowledge Bases** section, select the knowledge base you created.
7. Prepare the agent by clicking **Prepare** near the top of the builder page.
8. Test the agent after preparing it to verify it's using the knowledge base.
9. Click **Save and exit**.

Your agent is now set up. The following sections show how to deploy and interact with it.

#### Create an alias for your agent

To deploy the agent, create an alias for it that points to a specific version of the agent. After you create the alias, it appears in the agent view.

1. On the [Agents](https://console.aws.amazon.com/bedrock/home?#/agents) page, select the agent you created.
2. Click **Create Alias**.
3. Enter an **Alias name** and **Description**.
4. Click **Create alias**.

#### Test the Bedrock agent

To test the newly created agent, open it and use the playground on the right of the screen.

This example uses a dataset of research papers as its source data. You can ask a question about those papers and get a detailed response, this time from the deployed version.

<img alt="" />

Inspect the trace to see which chunks the agent used and to diagnose issues with responses.

<img alt="" />

## Resources

* [Pinecone as a Knowledge Base for Amazon Bedrock](https://www.pinecone.io/blog/amazon-bedrock-integration/)
