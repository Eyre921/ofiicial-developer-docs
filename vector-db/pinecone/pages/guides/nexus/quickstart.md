---
title: "Nexus quickstart"
source: https://docs.pinecone.io/guides/nexus/quickstart
path: guides/nexus/quickstart
---

Deploy Nexus in your own cloud, then create a context and query it.

Pinecone Nexus runs in your own cloud account. This quickstart deploys Nexus with bring-your-own-cloud (BYOC), then builds a context from your own documents and queries it from your deployment's console.

## Prerequisites

* A Pinecone **Enterprise** plan (required for BYOC).
* A dedicated cloud account (AWS, GCP, or Azure) with admin access, plus the install tooling. See the [deploy prerequisites](/guides/nexus/byoc/deploy#prerequisites) for the full list.

## 1. Deploy Nexus

Nexus runs in your own cloud, so deploying it comes first.

<Steps>
  <Step title="Install Nexus">
    Follow [Deploy Nexus BYOC](/guides/nexus/byoc/deploy) to install Nexus in your own cloud account with the Pulumi installer.
  </Step>

  <Step title="Open your deployment's console">
    When the install finishes, it prints your workspace console URL. Open it to reach your deployment's console, where the rest of this quickstart happens.
  </Step>
</Steps>

## 2. Add a context

Build a context from your own documents.

<Steps>
  <Step title="Create a context">
    In your deployment's console sidebar, next to **Contexts**, click **+ New**. On the **New context** tab, enter a **Name** (the URL slug is generated from it) and a **Description**, then click **Create context**.
  </Step>

  <Step title="Import sources">
    On the **Sources** tab, click **+ Import**, then bring in your documents one of these ways:

    * **Upload** files or an archive.
    * Pull from a public **Hugging Face** or **GitHub** repository URL.
    * Connect a **Box** or **Google Drive** account and import from it.
  </Step>

  <Step title="Design the manifest">
    On the **Design** tab, pick a **[manifest](/guides/nexus/context-design) template** that fits your sources (for example, **General knowledge base**). The template describes the artifacts and edges it will build and shows an estimated cost and time.
  </Step>

  <Step title="Curate">
    Apply the template to [curate](/guides/nexus/how-curation-works). Nexus chunks your sources and distills them into the artifacts the manifest defines, then indexes everything. Follow progress on the **Sources** and **Knowledge** tabs, and under **Activity**.
  </Step>
</Steps>

<Tip>
  Have a `.context.zip` pack? In the **New context** dialog, open the **Restore** tab, drop the pack (or click **choose a file**), then click **Restore context**. Packs come from a context's **Packs** tab.
</Tip>

## 3. Query your context

Once curation finishes, ask your context a question and get a grounded, cited answer.

<Steps>
  <Step title="Open the Query tab">
    Open your context's **Query** tab, and optionally pick the answering **model**.
  </Step>

  <Step title="Ask a question">
    Type your question in the **Search this context** box and run it. Nexus returns a grounded, cited answer with suggested follow-up topics, and saves it as a session you can reopen from **Sessions**.
  </Step>
</Steps>

<Tip>
  To query several contexts at once, start a session from **Sessions** with **+ New session**, click each context in the **Query across** row, and ask.
</Tip>

You can also query from your own code, using the [KnowQL query endpoint](/reference/api/nexus/query) or an [MCP server](/guides/nexus/mcp-server).
