---
title: "Overview"
source: https://docs.crewai.com/v1.15.28/en/tools/cloud-storage/overview
path: v1.15.28/en/tools/cloud-storage/overview
---

Interact with cloud services, storage systems, and cloud-based AI platforms

These tools enable your agents to interact with cloud services, access cloud storage, and leverage cloud-based AI platforms for scalable operations.

## **Available Tools**

> **[S3 Reader Tool](/en/tools/cloud-storage/s3readertool)**
>
> Read files and data from Amazon S3 buckets.

> **[S3 Writer Tool](/en/tools/cloud-storage/s3writertool)**
>
> Write and upload files to Amazon S3 storage.

> **[Bedrock Invoke Agent](/en/tools/integration/bedrockinvokeagenttool)**
>
> Invoke Amazon Bedrock agents for AI-powered tasks.

> **[Bedrock KB Retriever](/en/tools/cloud-storage/bedrockkbretriever)**
>
> Retrieve information from Amazon Bedrock knowledge bases.

## **Common Use Cases**

* **File Storage**: Store and retrieve files from cloud storage systems
* **Data Backup**: Backup important data to cloud storage
* **AI Services**: Access cloud-based AI models and services
* **Knowledge Retrieval**: Query cloud-hosted knowledge bases
* **Scalable Operations**: Leverage cloud infrastructure for processing

```python theme={null}
from crewai_tools import S3ReaderTool, S3WriterTool, BedrockInvokeAgentTool

# Create cloud tools
s3_reader = S3ReaderTool()
s3_writer = S3WriterTool()
bedrock_agent = BedrockInvokeAgentTool()

# Add to your agent
agent = Agent(
    role="Cloud Operations Specialist",
    tools=[s3_reader, s3_writer, bedrock_agent],
    goal="Manage cloud resources and AI services"
)
```
