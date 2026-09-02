---
title: "Manage documents"
source: https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base/manage-documents.md
path: docs/eleven-agents/customization/knowledge-base/manage-documents
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Manage documents

Manage your knowledge base from the [knowledge base dashboard](https://elevenlabs.io/app/agents/knowledge-base), the CLI, or the API. For what a knowledge base is and how agents use it, see [Knowledge base](/docs/eleven-agents/customization/knowledge-base).

![Knowledge base main interface showing a list of
documents](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0887213c4d8099240b7e5a8fec86fc75f4763e8fd80a6f7a6de33545c45f37a2/assets/images/conversational-ai/kb-content.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=dc825e2dbdac3d850e63e30f6f2c3d26c4d4a314a2308ccb19662e9d0e293629&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Add documents

Documents can be created from files, webpages, or plain text. Once created, attach them to an agent to make their contents available in conversations.

#### Dashboard

From the [knowledge base dashboard](https://elevenlabs.io/app/agents/knowledge-base), or directly from an agent's configuration, click **Add document** and choose a source.

#### File

Upload a document in PDF, TXT, DOCX, HTML, EPUB, or Markdown format, up to 20MB per file.

![File upload interface showing supported formats and the 20MB size limit](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b428874877d6aa2b24167c0293709e6a52a096a13b02244c0a5463139d3988e4/assets/images/conversational-ai/knowledge-file.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=57c14517d5c9100763aa20c884fe3d0e86a1ee97e01cad13bb7501013e6e8e75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### URL

Import a webpage by pasting its URL. To ingest an entire site, use the crawl option — either
crawl the whole website by following links from the starting URL, or import pages from the
site's sitemap.

![URL import interface where users can paste a documentation link](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8523ea5c5ae0418007eb7042d4af3e792a111ca41b74a090357df34cd5b4a369/assets/images/conversational-ai/knowledge-url.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=78e85c2b7d775826ee3065067b395ea9f707f10ff7b72e98554423899e9bb4bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Ensure you have permission to use the content from the URLs you provide.

#### Text

Enter text manually and give it a name.

![Text input interface where users can name and add custom content](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4e44e310335dcea24b4832d38813992f1bdc55ef85b4e54353963dc47e9baa0a/assets/images/conversational-ai/knowledge-text.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=ff4a5c95c0ee27e9d95bf7f420ec5b44a7951d8eabc670ef310c45db5fac7dd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### CLI

The CLI does not upload knowledge base documents directly. Create them via the dashboard or API, then attach the resulting document IDs to your agent configuration.

#### Pull the agent configuration

```bash
elevenlabs agents pull --agent "<agent-name>"
```

#### Edit \`agent\_configs/\<agent-name>.json\`

Set `conversation_config.agent.prompt.knowledge_base`:

```json
{
  "conversation_config": {
    "agent": {
      "prompt": {
        "knowledge_base": [
          {
            "type": "file",
            "name": "Unladen Swallow Facts",
            "id": "i2YYI6huwBmcgYydAXARmQJc3pmX",
            "usage_mode": "auto"
          }
        ]
      }
    }
  }
}
```

#### Push your changes

```bash
elevenlabs agents push --agent "<agent-name>"
```

#### API

Create each document, then attach the returned IDs to the agent's configuration.

```python
import os

from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Create a document from text
text_doc = elevenlabs.conversational_ai.knowledge_base.documents.create_from_text(
    text="The airspeed velocity of an unladen swallow (European) is 24 miles per hour, or roughly 11 meters per second.",
    name="Unladen Swallow facts",
)

# Create a document from a URL
url_doc = elevenlabs.conversational_ai.knowledge_base.documents.create_from_url(
    url="https://en.wikipedia.org/wiki/Unladen_swallow",
    name="Unladen Swallow Wikipedia page",
)

# Create a document from a file
file_doc = elevenlabs.conversational_ai.knowledge_base.documents.create_from_file(
    file=open("/path/to/unladen-swallow-facts.txt", "rb"),
    name="Unladen Swallow Facts",
)

# Attach the documents to an agent
elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "agent": {
            "prompt": {
                "knowledge_base": [
                    {"type": "text", "name": text_doc.name, "id": text_doc.id},
                    {"type": "url", "name": url_doc.name, "id": url_doc.id},
                    {"type": "file", "name": file_doc.name, "id": file_doc.id},
                ]
            }
        }
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import fs from "node:fs";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

// Create a document from text
const textDoc = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromText({
  name: "Unladen Swallow Facts",
  text: "The airspeed velocity of an unladen swallow (European) is 24 miles per hour, or roughly 11 meters per second.",
});

// Create a document from a URL
const urlDoc = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromUrl({
  name: "Unladen Swallow Wikipedia page",
  url: "https://en.wikipedia.org/wiki/Unladen_swallow",
});

// Create a document from a file
const fileBuffer = fs.readFileSync("/path/to/unladen-swallow-facts.txt");
const file = new File([fileBuffer], "unladen-swallow-facts.txt", { type: "text/plain" });
const fileDoc = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromFile({
  name: "Unladen Swallow Facts",
  file,
});

// Attach the documents to an agent
await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    agent: {
      prompt: {
        knowledgeBase: [
          { type: "text", name: textDoc.name, id: textDoc.id },
          { type: "url", name: urlDoc.name, id: urlDoc.id },
          { type: "file", name: fileDoc.name, id: fileDoc.id },
        ],
      },
    },
  },
});
```

To crawl an entire website into a folder of documents instead of adding a single page, start a crawl job. Crawling runs asynchronously — use the returned job ID to check its status or cancel it.

```python
crawl = elevenlabs.conversational_ai.knowledge_base.crawl_jobs.create(
    url="https://elevenlabs.io/docs",
    max_depth=3,
    max_pages=1000,
)
```

```typescript
const crawl = await elevenlabs.conversationalAi.knowledgeBase.crawlJobs.create({
  url: "https://elevenlabs.io/docs",
  maxDepth: 3,
  maxPages: 1000,
});
```

## Add existing documents to an agent

Documents can be reused across agents, so shared knowledge only needs to be maintained once.

1. Navigate to the agent's [configuration](https://elevenlabs.io/app/agents/agents).
2. Find the knowledge base section and click **Add document**.
3. Select an existing document from your knowledge base, or upload a new one.

![Interface for adding documents to an
agent](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8e8a6a2df244ed20d1ab889c8ae5dda76aefed0d15f3dd2fe09c35b281c63673/assets/images/conversational-ai/kb-add-doc-items.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=c50f2436e13c33aadd349f792b2e1bb8bd5583352ee967c20506605f91aff9e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Reusing documents across agents keeps knowledge consistent and avoids duplicating uploads.

## Edit documents

You can edit a document's content directly instead of deleting and re-uploading it. Editing a document automatically regenerates its content-search chunks and RAG embeddings, so search and agent retrieval stay in sync.

* **Text and file documents**: Edit the content inline and save.
* **File documents**: Alternatively, replace the underlying file with a new version.
* **URL documents**: Edit the content when auto-sync is off. When auto-sync is on, the sync cycle manages the document and manual edits are blocked.

![Editing a document's content inline in the knowledge
base](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4ea01bb2c13162f31f7610b049ae0db542e279a26da38f4c79f17fb89a8524f5/assets/images/conversational-ai/kb-edit-content.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=287b476c672d8aa5f601288973a28e59aea80b5e685208a025bc40cf2382ff72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
# Update a document's name or content
elevenlabs.conversational_ai.knowledge_base.documents.update(
    documentation_id="i2YYI6huwBmcgYydAXARmQJc3pmX",
    name="Unladen Swallow Facts",
    content="The airspeed velocity of an unladen swallow (European) is 24 miles per hour.",
)

# Replace the underlying file of a file document

elevenlabs.conversational_ai.knowledge_base.document.update_file(
documentation_id="i2YYI6huwBmcgYydAXARmQJc3pmX",
file=open("/path/to/unladen-swallow-facts-v2.txt", "rb"),
)

```

```typescript
// Update a document's name or content
await elevenlabs.conversationalAi.knowledgeBase.documents.update("i2YYI6huwBmcgYydAXARmQJc3pmX", {
  name: "Unladen Swallow Facts",
  content: "The airspeed velocity of an unladen swallow (European) is 24 miles per hour.",
});

// Replace the underlying file of a file document
const fileBuffer = fs.readFileSync("/path/to/unladen-swallow-facts-v2.txt");
const updatedFile = new File([fileBuffer], "unladen-swallow-facts-v2.txt", { type: "text/plain" });
await elevenlabs.conversationalAi.knowledgeBase.document.updateFile("i2YYI6huwBmcgYydAXARmQJc3pmX", {
  file: updatedFile,
});
```

## Keep URL content up to date

Documents created from a URL can be refreshed to re-fetch the latest content from their source. Refreshing re-indexes the document so RAG-enabled agents use the updated content.

```python
elevenlabs.conversational_ai.knowledge_base.document.refresh(
    documentation_id="i2YYI6huwBmcgYydAXARmQJc3pmX",
)
```

```typescript
await elevenlabs.conversationalAi.knowledgeBase.document.refresh("i2YYI6huwBmcgYydAXARmQJc3pmX");
```

In the dashboard, you can also enable auto-sync to refresh URL documents automatically on a schedule, so their content stays current without manual updates.

## Organize with folders

Folders group related documents so they are easier to manage and attach in bulk. Create a folder, then move documents into it from the dashboard or the API.

A folder attached to an agent makes all of its documents available through RAG, so the agent must have RAG enabled to use folders.

![Creating a folder and moving documents into
it](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8267c0d4a36282c1fcaaacf0a665e5caf8c4cf6f2908451fc5a3b1cf6a8dd2e0/assets/images/conversational-ai/knowledge-folder.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=3e092e19d18d4f299c1f11c663692a09db11f94c9d88170cab5940cce76dec8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
# Create a folder
folder = elevenlabs.conversational_ai.knowledge_base.documents.create_folder(
    name="Product documentation",
)

# Move a document into the folder

elevenlabs.conversational_ai.knowledge_base.documents.move(
document_id="i2YYI6huwBmcgYydAXARmQJc3pmX",
move_to=folder.id,
)

```

```typescript
// Create a folder
const folder = await elevenlabs.conversationalAi.knowledgeBase.documents.createFolder({
  name: "Product documentation",
});

// Move a document into the folder
await elevenlabs.conversationalAi.knowledgeBase.documents.move("i2YYI6huwBmcgYydAXARmQJc3pmX", {
  moveTo: folder.id,
});
```

## Dependencies and deletion

Each document has a **Dependent agents** tab that lists the agents currently depending on it.

![Document detail view showing the Dependent agents
tab](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/20ecce9f1db77d27bdf760b4a90c9bd2baacb612b48cf660e0f395c82aa3a725/assets/images/conversational-ai/kb-dependent-agents.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T211202Z&X-Amz-Expires=604800&X-Amz-Signature=d91933f3c14976ebd9a2941d3d8cbf3557e89bde0f7edb877a1fb27f25123bfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

A document cannot be deleted while an agent depends on it. Remove the document from those agents first, or use force deletion to detach it from all dependents at once.
