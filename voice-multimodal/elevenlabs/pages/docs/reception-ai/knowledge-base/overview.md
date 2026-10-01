---
title: "Knowledge base"
source: https://elevenlabs.io/docs/reception-ai/knowledge-base/overview.md
path: docs/reception-ai/knowledge-base/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Knowledge base

The knowledge base contains everything your receptionist knows about your business beyond structured data such as services, hours, and staff.

## What the knowledge base contains

* **Website content**: pages read from your website.
* **Uploaded files**: PDFs, documents, and other files you provide.
* **FAQ answers**: your answers to questions the receptionist could not answer. See [FAQ](/docs/reception-ai/knowledge-base/faq).
* **Business configuration**: your services, hours, locations, and staff, added automatically.

## How your receptionist uses it

When a caller asks a question, the receptionist:

1. Searches the knowledge base for relevant information.
2. Answers based on what it finds.
3. If nothing relevant is found, adds the question to your FAQ for you to answer.

If your knowledge base is under 2,000,000 characters and 2,000 documents, you can turn on **Skip retrieval (RAG)** in [Advanced settings](/docs/reception-ai/receptionist/advanced-settings) to include the whole knowledge base in every response instead of searching. This lowers response time.

## Managing knowledge sources

Open your business page from the sidebar (labeled with your business name) and go to **Knowledge Sources**. Select **Add new** and choose **Upload file**, **Entire website**, or **Single page**. Filter the list by files, websites, or pages, or search by name.

### Importing business details

When a website or file finishes processing, Reception.ai extracts business details such as contact information, locations, services, products, assets, and staff. Open the source to review them, then select **Import all** or **Import selection** to add them to your business. Each source can be imported once.

#### [Website scraping](/docs/reception-ai/knowledge-base/website-scraping)

Import content from your website.

#### [File uploads](/docs/reception-ai/knowledge-base/file-uploads)

Upload documents and files.

#### [FAQ](/docs/reception-ai/knowledge-base/faq)

Answer questions your receptionist couldn't.

## Limits

| Plan    | Knowledge sources |
| ------- | ----------------- |
| Trial   | 5                 |
| Basic   | 5                 |
| Plus    | 10                |
| Premium | 20                |

You can add up to 20 files, 20 website sources, and 20 reprocessing runs per hour.

## Best practices

* **Keep it current**: update your knowledge base when policies, pricing, or services change.
* **Be specific**: detailed answers produce better responses.
* **Answer FAQ questions regularly**: each answer improves accuracy for future callers.
* **Avoid duplication**: services, hours, and staff are already available to the receptionist.
