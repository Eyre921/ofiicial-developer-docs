---
title: "Pinecone Assistant: n8n quickstart"
source: https://docs.pinecone.io/guides/assistant/quickstart/n8n-quickstart
path: guides/assistant/quickstart/n8n-quickstart
---

Build an n8n workflow with Pinecone Assistant and OpenAI that downloads files over HTTP, uploads them to an assistant, and lets you chat with them.

In this quickstart, you import an [n8n](https://docs.n8n.io/choose-n8n/) workflow that downloads files over HTTP and uploads them to Pinecone Assistant. You then chat with the files through an n8n AI agent, which uses an OpenAI model to answer questions with context retrieved from your assistant.

To follow along, you need a Pinecone account, an n8n account, and an OpenAI API key.

<Steps>
  <Step title="Create an assistant">
    In the Pinecone console, [create an assistant](https://app.pinecone.io/organizations/-/projects/-/assistant) named `n8n-assistant`. The workflow template looks for an assistant with this name.
  </Step>

  <Step title="Install the Pinecone Assistant node">
    In your n8n account, open the nodes panel, search for **Pinecone Assistant**, and install the node.

    <Note>
      If the Pinecone Assistant node doesn't appear in the nodes panel, restart your n8n workspace.
    </Note>
  </Step>

  <Step title="Import the workflow">
    Copy the workflow template URL:

    ```text theme={null}
    https://raw.githubusercontent.com/pinecone-io/n8n-templates/refs/heads/main/assistant-quickstart/assistant-quickstart.json
    ```

    In your n8n account, [create a new workflow](https://docs.n8n.io/workflows/create/) and paste the URL anywhere in the workflow editor. Then click **Import** to add the workflow.
  </Step>

  <Step title="Connect the nodes to your accounts">
    The workflow has two Pinecone Assistant nodes, **Upload file to Assistant** and **Get context from Assistant**. In each one, do the following:

    1. Click **Connect to Pinecone** and sign in to your Pinecone account. If the button doesn't appear, as on self-hosted n8n, create a Pinecone credential with your [Pinecone API key](https://app.pinecone.io/organizations/-/keys) instead.
    2. For **Assistant Name**, select `n8n-assistant`.

    Then open the **OpenAI Chat Model** node, select **Credential to connect with > Create new credential**, and paste in your OpenAI API key.
  </Step>

  <Step title="Upload files">
    Click **Execute workflow**. By default, the workflow downloads Pinecone's release notes and uploads them to your assistant.

    <Tip>
      To upload your own files, change the URLs in the **Set file urls** node.
    </Tip>
  </Step>

  <Step title="Chat with your files">
    After the files finish uploading, click **Open chat** at the bottom of the workflow editor and ask a question about them:

    ```text theme={null}
    What support does Pinecone have for MCP?
    ```

    The AI agent retrieves relevant context from your assistant and uses it to answer.
  </Step>

  <Step title="Clean up">
    When you no longer need `n8n-assistant`, delete it in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Deleting an assistant also deletes all files uploaded to it. You can also delete the imported workflow in n8n, so it doesn't run by accident later.
  </Step>
</Steps>

## Next steps

You can customize the workflow for your own use case:

* Change the URLs in the **Set file urls** node to use your own files.
* Edit the system message in the **AI Agent** node to describe what kind of knowledge your assistant holds.
* Add the **Top K** or **Snippet Size** parameters to the **Get context from Assistant** node to manage token usage.
* Add a **Metadata Filter** to the **Get context from Assistant** node to narrow the context it retrieves.

To go further:

* [Chat with your Google Drive documents](https://n8n.io/workflows/9942-rag-powered-document-chat-with-google-drive-openai-and-pinecone-assistant/) using n8n, Pinecone Assistant, and OpenAI.
* Learn more about [Pinecone Assistant](/guides/assistant/overview).
* Get help in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH).
