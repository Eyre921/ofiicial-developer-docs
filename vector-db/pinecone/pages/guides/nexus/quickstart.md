---
title: "Nexus quickstart"
source: https://docs.pinecone.io/guides/nexus/quickstart
path: guides/nexus/quickstart
---

Deploy Pinecone Nexus with BYOC, curate a context from your own documents, and run KnowQL queries that return grounded, cited multi-document answers.

Pinecone Nexus runs in your own cloud account. This quickstart deploys Nexus with Bring Your Own Cloud (BYOC), turns a set of your documents into a context, and queries it for grounded, cited answers. See the [overview](/guides/nexus/overview) for what you can do with Nexus.

Nexus organizes knowledge in a hierarchy:

* A **workspace** holds one or more contexts.
* A **context** is built from the documents you ingest into it.
* A **query** can read one or more contexts, so several contexts together can give an agent its knowledge.

See [key concepts](/guides/nexus/concepts) for the full model.

<Note>
  The examples in this quickstart use a company knowledge base of internal policies for illustration. You bring your own documents, and any set works.
</Note>

## Prerequisites

* A Pinecone **Enterprise** plan (required for BYOC).
* A dedicated cloud account (AWS, GCP, or Azure) with admin access, plus the install tooling. See the [deploy prerequisites](/guides/nexus/byoc/deploy#prerequisites) for the full list.
* Documents to build your context from, such as files to upload or a Hugging Face, GitHub, Box, or Google Drive source.

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

Build a context from your own documents. A company knowledge base might include a refund policy, an expense policy, and a vendor-approval matrix. Nexus ingests dense documents like PDFs directly, alongside Markdown and plain text. For example, two PDFs and a Markdown file could read:

* `policies/refunds.md`: Refund requests must be submitted within 30 days of purchase. After that window, customers receive store credit, not a direct refund.
* `policies/expenses.pdf`: Standard expenses over \$1,000 require manager approval before reimbursement.
* `policies/vendors.pdf`: Vendor invoices over \$10,000 require finance approval. Invoices over \$25,000 also require VP sign-off.

The queries later in this quickstart draw on these files.

<Steps>
  <Step title="Create the context">
    In the console sidebar, next to **Contexts**, click **+ New**. The **New context** dialog opens on the **New context** tab.

    Enter a **Name** (for example, `Company knowledge base`) and a **Description**, then click **Create context**. The URL slug is generated from the name.

    Creating the context opens a guided setup with three steps: **Add sources**, **Design your context**, and **Review and curate**.
  </Step>

  <Step title="Add sources">
    On the **Add sources** step, bring in your documents in one of these ways:

    * **Upload** files from your computer, individually or as an archive (`.zip`, `.tar`, `.tar.gz`, or `.tgz`).
    * Pull from a public **Hugging Face** or **GitHub** repository URL.
    * Connect a **Box** or **Google Drive** account.

    After you add at least one source, click **Design your context**.
  </Step>

  <Step title="Design your context">
    On the **Design your context** step, Nexus scans your sources and suggests [manifest](/guides/nexus/context-design) templates that match. Each template describes the artifacts and edges it'll build.

    Pick a template that fits, such as **General knowledge base**. If none fit, you can [design your own manifest](/guides/nexus/design-your-own-manifest) or import one under **Or start from scratch**.

    Click **Review**.
  </Step>

  <Step title="Review and curate">
    On the **Review and curate** step, check the artifact types, edge types, model, and estimated cost, then click **Save and curate**. The curation task opens.

    Nexus [curates](/guides/nexus/how-curation-works) your sources. It chunks them, distills them into the typed artifacts the manifest defines, then indexes everything.

    Curation runs in the background, so you can leave the task and return to the context while it works.
  </Step>
</Steps>

<Tip>
  Have a `.context.zip` pack? In the **New context** dialog, open the **Restore** tab, drop the pack (or click **choose a file**), then click **Restore context**. Packs come from a context's **Packs** tab.
</Tip>

## 3. Query your context

Once curation finishes, ask your context a question and get back a grounded answer with citations.

<Steps>
  <Step title="Open the context">
    Use **Query this context** on the curation task, or open the context anytime from the console sidebar. The context opens on the **Query** tab.
  </Step>

  <Step title="Ask a question">
    In the **Query this context** box on the **Query** tab, type your question and run it. You can also pick the answering **model**.
  </Step>
</Steps>

### A grounded, cited answer

Nexus plans its own retrieval across the context's curated knowledge, gathers the relevant evidence, and composes a single grounded answer with inline citations. Asking the company knowledge base "What is the refund policy?" returns something like:

> Refund requests must be submitted within 30 days of purchase. After that window, customers can still get store credit, but not a direct refund. **\[1]**
>
> **\[1]** `policies/refunds.md`

The answer is grounded in your sources, and every claim cites the document it came from, so you can check it. To see how Nexus produced it, open the query's [trace](/guides/nexus/query-tracing). Nexus also suggests follow-up topics and saves the query as a session you can reopen from **Sessions**.

### A multi-document answer

Questions that span multiple documents work the same way. Asking "Which purchases need approval, and what is the threshold for each?" returns something like:

> * Standard expenses over \$1,000 need manager approval. **\[1]**
> * Vendor invoices over \$10,000 need finance approval. **\[2]**
> * Vendor invoices over \$25,000 need VP and finance approval. **\[2]**
>
> **\[1]** `policies/expenses.pdf`  **\[2]** `policies/vendors.pdf`

To answer this, Nexus queried the structured tables it compiled from your policies during curation, so it enumerates every matching rule across documents, each with its own citation. A plain RAG search returns only the passages closest to your question, so it can miss rules in other documents. Answering completely across your whole corpus is a core reason to reach for Nexus over RAG. See [how queries work](/guides/nexus/how-queries-work) for what the runtime does on each turn, or the [overview](/guides/nexus/overview#what-nexus-is-not) for how Nexus compares to RAG.

<Tip>
  To query several contexts at once, start a session from **Sessions** with **+ New session**, click each context in the **Query across** row, and ask.
</Tip>

## Query from your own code

Agents send a [KnowQL](/guides/nexus/concepts#knowql) query over HTTP, passing the context slug as `scope`, and get back the same answer plus citations to act on:

```bash curl theme={null}
curl -fsS "$NEXUS_BASE_URL/query" \
  -H "Authorization: Bearer $NEXUS_TOKEN" \
  -H 'X-Pinecone-Api-Version: 2026-07' \
  -H 'Content-Type: application/json' \
  -d '{"scope": ["company-knowledge-base"], "ask": "What is the refund policy?"}' \
| jq -r '.output[].content[].text'
```

```console Output theme={null}
Refund requests must be submitted within 30 days of purchase. After that
window, customers can still get store credit, but not a direct refund.
```

The full response also carries `citations` and `usage`. See [Authentication](/reference/api/nexus/authentication) to set `NEXUS_BASE_URL` and `NEXUS_TOKEN`, or the [Nexus API](/reference/api/nexus/introduction) for the full surface. You can also connect an [MCP server](/guides/nexus/mcp-server) for Claude Desktop and other MCP clients.
