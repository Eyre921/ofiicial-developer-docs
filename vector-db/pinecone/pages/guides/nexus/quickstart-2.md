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
* A [Pinecone API key](/reference/api/nexus/authentication#get-an-api-key) for the target project.
* Documents to build your context from, such as files to upload or a Hugging Face, GitHub, Box, or Google Drive source.

## 1. Deploy Nexus

Nexus runs in your own cloud, so deploying it comes first.

<Steps>
  <Step title="Install Nexus">
    Follow [Deploy Nexus BYOC](/guides/nexus/byoc/deploy) to install Nexus in your own cloud account with the Pulumi installer.
  </Step>

  <Step title="Get your console URL and API host">
    When the install finishes, it prints your workspace console URL and API host. Open the console to work in the UI, or use the host as your data-plane base URL for the API. See [Authentication](/reference/api/nexus/authentication) to set `NEXUS_BASE_URL` and get a token.
  </Step>
</Steps>

## 2. Add a context

Build a context from your own documents. A company knowledge base might include a refund policy, an expense policy, and a vendor-approval matrix. Nexus ingests dense documents like PDFs directly, alongside Markdown and plain text. For example, two PDFs and a Markdown file could read:

* `policies/refunds.md`: Refund requests must be submitted within 30 days of purchase. After that window, customers receive store credit, not a direct refund.
* `policies/expenses.pdf`: Standard expenses over \$1,000 require manager approval before reimbursement.
* `policies/vendors.pdf`: Vendor invoices over \$10,000 require finance approval. Invoices over \$25,000 also require VP sign-off.

The queries later in this quickstart draw on these files. You can build the context through the API or the console.

<Tabs>
  <Tab title="API">
    <Steps>
      <Step title="Set your base URL and token">
        Point at your workspace host and exchange your Pinecone API key for a session token. See [Authentication](/reference/api/nexus/authentication) for details.

        ```bash theme={null}
        export NEXUS_BASE_URL="https://YOUR_WORKSPACE_HOST/api"
        export NEXUS_TOKEN="$(
          curl -fsS "$NEXUS_BASE_URL/auth/login" \
            -H 'Content-Type: application/json' \
            -H 'X-Pinecone-Api-Version: 2026-07' \
            -d "{\"api_key\":\"$PINECONE_API_KEY\"}" | jq -r '.token'
        )"
        ```
      </Step>

      <Step title="Create the context">
        Create the context with a slug and a name:

        ```bash curl theme={null}
        curl -fsS -X POST "$NEXUS_BASE_URL/contexts" \
          -H "Authorization: Bearer $NEXUS_TOKEN" \
          -H 'Content-Type: application/json' \
          -H 'X-Pinecone-Api-Version: 2026-07' \
          -d '{"slug": "company-knowledge-base", "name": "Company knowledge base"}'
        ```

        A new context curates under the default manifest. To define your own artifact and edge types, see [Design your own manifest](/guides/nexus/design-your-own-manifest).
      </Step>

      <Step title="Add sources">
        Upload each of your files, one request per file (archives are expanded automatically), or import from a connector with `POST /contexts/{slug}/import`:

        ```bash curl theme={null}
        for f in policies/refunds.md policies/expenses.pdf policies/vendors.pdf; do
          curl -fsS -X POST "$NEXUS_BASE_URL/contexts/company-knowledge-base/import/upload" \
            -H "Authorization: Bearer $NEXUS_TOKEN" \
            -H 'X-Pinecone-Api-Version: 2026-07' \
            -F "file=@$f"
        done
        ```
      </Step>

      <Step title="Curate">
        Curate the context to build its knowledge from the sources:

        ```bash curl theme={null}
        curl -fsS -X POST "$NEXUS_BASE_URL/contexts/company-knowledge-base/curate" \
          -H "Authorization: Bearer $NEXUS_TOKEN" \
          -H 'Content-Type: application/json' \
          -H 'X-Pinecone-Api-Version: 2026-07' \
          -d '{}'
        ```

        Curation chunks your sources, distills them into typed artifacts, and indexes everything. It runs as a background task, so query the context once it finishes. See [How curation works](/guides/nexus/how-curation-works).
      </Step>
    </Steps>
  </Tab>

  <Tab title="Console">
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

        Pick a template that fits, such as **General knowledge base**. If none fit, [design your own manifest](/guides/nexus/design-your-own-manifest) through the API.

        Click **Review**.
      </Step>

      <Step title="Curate">
        On the **Review and curate** step, check the artifact types, edge types, model, and estimated cost, then click **Save and curate**. The curation task opens.

        Nexus [curates](/guides/nexus/how-curation-works) your sources. It chunks them, distills them into the typed artifacts the manifest defines, then indexes everything.

        Curation runs in the background, so you can leave the task and return to the context while it works.
      </Step>
    </Steps>

    <Tip>
      Have a `.context.zip` pack? In the **New context** dialog, open the **Restore** tab, drop the pack (or click **choose a file**), then click **Restore context**. Packs come from a context's **Packs** tab.
    </Tip>
  </Tab>
</Tabs>

## 3. Query your context

Once curation finishes, ask your context a question and get back a grounded answer with citations.

<Tabs>
  <Tab title="API">
    Send a [KnowQL](/guides/nexus/concepts#knowql) query over HTTP, passing the context slug as `scope`:

    ```bash curl theme={null}
    curl -fsS -X POST "$NEXUS_BASE_URL/query" \
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

    The full response also carries `citations` and `usage`. See the [Nexus API](/reference/api/nexus/introduction) for the full surface, or connect an [MCP server](/guides/nexus/mcp-server) for Claude Desktop and other MCP clients.
  </Tab>

  <Tab title="Console">
    <Steps>
      <Step title="Open the context">
        Use **Query this context** on the curation task, or open the context anytime from the console sidebar. The context opens on the **Query** tab.
      </Step>

      <Step title="Ask a question">
        In the **Query this context** box on the **Query** tab, type your question and run it. You can also pick the answering **model**.
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Tip>
  To query several contexts at once, pass multiple slugs in the query's `scope` array. In the console, start a session from **Sessions** with **+ New session** and select each context to query across.
</Tip>

### A grounded, cited answer

Nexus plans its own retrieval across the context's curated knowledge, gathers the relevant evidence, and composes a single grounded answer with inline citations. Asking the company knowledge base "What is the refund policy?" returns something like:

> Refund requests must be submitted within 30 days of purchase. After that window, customers can still get store credit, but not a direct refund. **\[1]**
>
> **\[1]** `policies/refunds.md`

The answer is grounded in your sources, and every claim cites the document it came from, so you can check it. To see how Nexus produced it, open the query's [trace](/guides/nexus/query-tracing). In the console, Nexus also suggests follow-up topics and saves the query as a session you can reopen from **Sessions**.

### A multi-document answer

Questions that span multiple documents work the same way. Asking "Which purchases need approval, and what's the threshold for each?" returns something like:

> * Standard expenses over \$1,000 need manager approval. **\[1]**
> * Vendor invoices over \$10,000 need finance approval. **\[2]**
> * Vendor invoices over \$25,000 need VP and finance approval. **\[2]**
>
> **\[1]** `policies/expenses.pdf`  **\[2]** `policies/vendors.pdf`

To answer this, Nexus draws on the artifacts it compiled from your policies during curation, gathering the matching rules from across your documents, each with its own citation. A plain RAG search returns only the passages closest to your question, so it can miss rules in other documents. Reaching across your whole corpus is a core reason to use Nexus over RAG. For exact counts and enumerations over structured data, define a SQLite artifact, covered in [artifact formats](/guides/nexus/configure-artifact-formats). See [how queries work](/guides/nexus/how-queries-work) for what the runtime does on each turn, or the [overview](/guides/nexus/overview#what-nexus-is-not) for how Nexus compares to RAG.
