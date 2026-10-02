---
title: "Pinecone Assistant: n8n quickstart"
source: https://docs.pinecone.io/guides/assistant/quickstart/n8n-quickstart
path: guides/assistant/quickstart/n8n-quickstart
---

Build an n8n workflow with Pinecone Assistant and OpenAI to download files via HTTP, upload documents, and chat with them from an automation.

Create an [n8n](https://docs.n8n.io/choose-n8n/) workflow that that downloads files via HTTP, uploads them to Pinecone Assistant, and enables you to chat with documents using OpenAI.

## 1. Create an assistant

[Create an assistant](https://app.pinecone.io/organizations/-/projects/-/assistant) in the Pinecone console:

* Name your assistant `n8n-assistant`.

## 2. Install the Pinecone Assistant node

In your n8n account, install the Pinecone Assistant node using the nodes panel:

<img />

<img />

<Note>
  Restart your n8n workspace if the Pinecone Assistant node doesn't appear in the nodes panel.
</Note>

## 3. Create a new workflow

Copy this workflow template URL:

```shell theme={null}
https://raw.githubusercontent.com/pinecone-io/n8n-templates/refs/heads/main/assistant-quickstart/assistant-quickstart.json
```

In your n8n account, [create a new workflow](https://docs.n8n.io/workflows/create/) and paste the URL anywhere in the workflow editor. Click **Import** to add the workflow.

## 4. Add credentials

<Steps>
  <Step title="Authenticate with Pinecone">
    * Use the **Connect to Pinecone** button in the node to connect to a new or existing Pinecone account:

    <img />

    <img />

    * If you self-host n8n, add your [Pinecone API key](https://app.pinecone.io/organizations/-/keys) directly.
  </Step>

  <Step title="Add your OpenAI credentials">
    * In the **OpenAI Chat Model** node, select **Credential to connect with > Create new credential** and paste in your OpenAI API key.
  </Step>
</Steps>

## 5. Execute the workflow

By default, the workflow downloads recent Pinecone release notes and uploads them to your assistant. Click **Execute workflow** to start uploading documents.

<Tip>
  You can add your own files to the workflow by changing the URLs in the **Set file urls** node.
</Tip>

## 4. Chat with your docs

Once the documents are uploaded, you can chat with your assistant. In the n8n workflow, use the **Chat input** node to ask questions like:

```
What support does Pinecone have for MCP?
```

## Next steps

* Customize the workflow for your own use case:
  * Change the urls in the **Set file urls** node to use your own files.
  * Customize the system message on the **AI Agent** node to indicate what kind of knowledge is stored in Pinecone Assistant.
  * To help manage token consumption, add the Top K and/or Snippet Size parameters to the **Get context from Assistant** node.
  * Filter the context snippets even further by adding metadata filters to the **Get context from Assistant** node.
* Use n8n, Pinecone Assistant, and OpenAI to [chat with your Google Drive documents](https://n8n.io/workflows/9942-rag-powered-document-chat-with-google-drive-openai-and-pinecone-assistant/).
* Learn more about [Pinecone Assistant](/guides/assistant/overview).
* Get help in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH).
