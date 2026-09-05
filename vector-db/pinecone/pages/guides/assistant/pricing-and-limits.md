---
title: "Pricing and limits"
source: https://docs.pinecone.io/guides/assistant/pricing-and-limits
path: guides/assistant/pricing-and-limits
---

Understand Pinecone Assistant pricing for ingestion units, chat tokens, and storage, plus plan-based service limits for file uploads and knowledge size.

Pricing and limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

## Pricing

Pinecone Assistant usage is billed monthly. Costs can include:

* [Minimum usage](#minimum-usage) (Builder, Standard, and Enterprise plans)
* [Ingestion](#ingestion) (file uploads)
* [Tokens](#tokens) (chat, context retrieval, and evaluation)
* [Storage](#storage)

### Minimum usage

The Builder, Standard, and Enterprise [pricing plans](https://www.pinecone.io/pricing/) include a monthly minimum usage commitment:

| Plan       | Minimum usage     |
| ---------- | ----------------- |
| Starter    | \$0/month         |
| Builder    | \$20/month (flat) |
| Standard   | \$50/month        |
| Enterprise | \$500/month       |

On the Builder plan, the monthly minimum is a flat fee that covers included usage; additional usage beyond [Builder limits](/reference/api/database-limits/rate-limits#monthly-usage-limits) is blocked rather than billed. On the Standard and Enterprise plans, customers are charged for what they use each month beyond the monthly minimum.

The minimum is a commitment you grow into rather than an extra charge. Once your usage exceeds the minimum, you pay only for what you use.

**Examples**

<AccordionGroup>
  <Accordion title="Usage below monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$20.
    * Your usage is below the \$50 monthly minimum, so your total for the month is \$50.

    In this case, the August invoice would include line items for each service you used (totaling \$20), plus a single line item covering the rest of the minimum usage commitment (\$30).
  </Accordion>

  <Accordion title="Usage exceeds monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$100.
    * Your usage exceeds the \$50 monthly minimum, so your total for the month is \$100.

    In this case, the August invoice would only show line items for each service you used (totaling \$100). Since your usage exceeds the minimum usage commitment, you are only charged for your actual usage and no additional minimum usage line item appears on your invoice.
  </Accordion>
</AccordionGroup>

### Ingestion

When you upload or replace files for an assistant, usage is measured in **ingestion units**. One ingestion unit is approximately **400 tokens** (\~300 words); exact counts can vary by document.

| Processing path         | Rate (per ingestion unit) |
| ----------------------- | ------------------------- |
| Standard file ingestion | \$0.0005                  |

*Multimodal PDF processing uses the same ingestion unit; it is billed at about **twice** the standard per-unit rate. For current rates, see [Pricing](https://www.pinecone.io/pricing/).*

| Plan       | File uploads (ingestion units) |
| ---------- | ------------------------------ |
| Starter    | **1,000 / month** included     |
| Builder    | **10,000 / month** included    |
| Standard   | Pay per unit at the rate above |
| Enterprise | Pay per unit at the rate above |

Multimodal ingestion applies to content processed through the [multimodal PDF](/guides/assistant/multimodal) path. Standard ingestion applies to other supported file types.

Usage and invoices reflect a single ingestion usage line item. With [API version](/reference/api/versioning) `2026-04` or later, a completed file-ingestion operation may include **`ingestion_units`**. Use [Describe an operation](/reference/api/2026-04/assistant/describe_operation) or [Track file operations](/guides/assistant/manage-files#track-file-operations) for details.

### Tokens

For paid plans, you are charged for the number of tokens used by each assistant. [Ingestion](#ingestion) is billed separately from chat and context retrieval tokens.

#### Chat tokens

[Chatting with an assistant](/guides/assistant/chat-with-assistant) involves both input and output tokens:

* **Input tokens** are based on the messages sent to the assistant and the context snippets retrieved from the assistant and sent to a model. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

* **Output tokens** are based on the answer from the model.

| Plan       | Input token rate                 | Output token rate                |
| ---------- | -------------------------------- | -------------------------------- |
| Starter    | Included (**500,000 / month**)   | Included (**300,000 / month**)   |
| Builder    | Included (**2,000,000 / month**) | Included (**1,000,000 / month**) |
| Standard   | \$8/million tokens               | \$15/million tokens              |
| Enterprise | \$8/million tokens               | \$15/million tokens              |

<Note>
  Chat input tokens appear as "Assistants Input Tokens" on invoices and `prompt_tokens` in API responses. Chat output tokens appear as "Assistants Output Tokens" on invoices and `completion_tokens` in API responses.
</Note>

#### Context tokens

When you [retrieve context snippets](/guides/assistant/context-snippets-overview), tokens are based on the messages sent to the assistant and the context snippets retrieved from the assistant. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

| Plan       | Token rate                       |
| ---------- | -------------------------------- |
| Starter    | Included (**500,000 / month**)   |
| Builder    | Included (**2,000,000 / month**) |
| Standard   | \$5/million tokens               |
| Enterprise | \$5/million tokens               |

<Note>
  Context retrieval tokens appear as **Assistants Context Tokens Processed** on invoices and `prompt_tokens` in API responses. In API responses, `completion_tokens` will always be 0 because, unlike for chat, there is no answer from a model.
</Note>

#### Evaluation tokens

[Evaluating responses](/guides/assistant/evaluation-overview) involves both input and output tokens:

* **Input tokens** are based on two requests to a model: The first request contains a question, answer, and ground truth answer, and the second request contains the same details plus generated facts returned by the model for the first request.
* **Output tokens** are based on two responses from a model: The first response contains generated facts, and the second response contains evaluation metrics.

| Plan       | Input token rate   | Output token rate   |
| ---------- | ------------------ | ------------------- |
| Starter    | Not available      | Not available       |
| Builder    | Not available      | Not available       |
| Standard   | \$8/million tokens | \$15/million tokens |
| Enterprise | \$8/million tokens | \$15/million tokens |

<Note>
  Evaluation input tokens appear as **Assistants Evaluation Tokens Processed** on invoices and `prompt_tokens` in API responses. Evaluation output tokens appear as **Assistants Evaluation Tokens Out** on invoices and `completion_tokens` in API responses.
</Note>

### Storage

For paid plans, you are charged for the size of each assistant.

| Plan       | Storage rate            |
| ---------- | ----------------------- |
| Starter    | Free (1 GB max per org) |
| Builder    | Free up to 3 GB per org |
| Standard   | \$3/GB per month        |
| Enterprise | \$3/GB per month        |

## Limits

Pinecone Assistant limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

### Object limits

Object limits are restrictions on the number or size of assistant-related objects. Limits below are scoped **per organization** except for **Assistants per project**, which is scoped per project.

| Metric                              | Starter plan    | Builder plan      | Standard plan | Enterprise plan |
| :---------------------------------- | :-------------- | :---------------- | :------------ | :-------------- |
| Assistants per project              | 5               | 200               | Unlimited     | Unlimited       |
| File storage per org                | 1 GB            | 3 GB              | Unlimited     | Unlimited       |
| Chat input tokens per org           | 500,000 / month | 2,000,000 / month | Unlimited     | Unlimited       |
| Chat output tokens per org          | 300,000 / month | 1,000,000 / month | Unlimited     | Unlimited       |
| Context retrieval tokens per org    | 500,000 / month | 2,000,000 / month | Unlimited     | Unlimited       |
| Ingestion units per org             | 1,000 / month   | 10,000 / month    | Unlimited     | Unlimited       |
| File size (.docx, .json, .md, .txt) | 10 MB           | 10 MB             | 10 MB         | 10 MB           |
| File size (.pdf)                    | 10 MB           | 50 MB             | 100 MB        | 100 MB          |
| Metadata size per file              | 16 KB           | 16 KB             | 16 KB         | 16 KB           |

Additionally, the following limits apply to [multimodal PDFs](/guides/assistant/multimodal) (currently in [public preview](/release-notes/feature-availability)):

Multimodal PDF processing uses the same [ingestion unit](/guides/assistant/pricing-and-limits#ingestion) as standard uploads; it is billed at about **twice** the standard per-unit rate (see [Pricing and limits](/guides/assistant/pricing-and-limits)). Object and rate limits for assistants also apply—see [#limits](/guides/assistant/pricing-and-limits#limits) and [#rate-limits](/guides/assistant/pricing-and-limits#rate-limits).

| Metric        | Starter plan | Builder plan | Standard plan | Enterprise plan |
| :------------ | :----------- | :----------- | :------------ | :-------------- |
| Max file size | 10 MB        | 10 MB        | 50 MB         | 50 MB           |
| Page limit    | 100          | 100          | 100           | 100             |

### Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

Requests that exceed a rate limit fail and return a `429 - TOO_MANY_REQUESTS` status.

<Tip>To handle rate limits, implement [retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).</Tip>

| Metric                                      | Starter plan  | Builder plan  | Standard plan | Enterprise plan |
| :------------------------------------------ | :------------ | :------------ | :------------ | :-------------- |
| Assistant list/get requests per minute      | 40            | 50            | 100           | 500             |
| Assistant create/update requests per minute | 20            | 25            | 50            | 100             |
| Assistant delete requests per minute        | 20            | 25            | 50            | 100             |
| File get requests per minute                | 100           | 150           | 300           | 6,000           |
| File list requests per minute               | 50            | 75            | 150           | 3,000           |
| File upload requests per minute             | 5             | 15            | 20            | 300             |
| Multimodal PDF upload requests per minute   | 5             | 10            | 20            | 40              |
| File delete requests per minute             | 5             | 15            | 20            | 300             |
| Chat input tokens per minute                | 100,000       | 200,000       | 300,000       | 1,000,000       |
| Chat history tokens per query               | 64,000        | 64,000        | 64,000        | 64,000          |
| Evaluation input tokens per minute          | Not available | Not available | 150,000       | 500,000         |
