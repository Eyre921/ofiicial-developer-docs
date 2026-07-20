---
title: "Monitor usage and cost"
source: https://docs.pinecone.io/guides/assistant/admin/monitor-spend-and-usage
path: guides/assistant/admin/monitor-spend-and-usage
---

Set monthly spend alerts and monitor usage across your organization.

## Set monthly spend alerts

You can set up email alerts to monitor your organization's monthly spending. These alerts notify designated recipients when spending reaches specified thresholds. The alerts automatically reset at the start of each monthly billing cycle.

<Note>
  Spend alerts are available on the [Standard and Enterprise plans](https://www.pinecone.io/pricing/). They are not needed on the Starter or Builder plans, where usage is capped by plan quotas rather than billed per unit.
</Note>

To set a spend alert:

1. Go to [Settings > Spend alerts](https://app.pinecone.io/organizations/-/settings/spend-alerts) in the Pinecone console
2. Click **+ Add Alert**.
3. Enter the dollar amount for the spend alert.
4. Enter the email addresses to send the alert to. [Organization owners](/guides/organizations/understanding-organizations#organization-roles) are listed by default.
5. Click **Create**.

To edit a spend alert:

1. In the row of the spend alert you want to edit, click **ellipsis (...) menu > Edit**.
2. Change the dollar amount and/or email addresses for the spend alert.
3. Click **Update**.

<Note>
  **Auto-spend spike alert**: To protect from unexpected cost increases, Pinecone sends an alert when spending exceeds double your previous month's invoice amount. While the alert threshold is fixed and the alert cannot be deleted, you can modify which email addresses receive the alert and enable or disable the alert notifications.
</Note>

## Monitor organization-level usage

<Note>
  You must be an [organization owner or billing admin](/guides/assistant/admin/organizations-overview#organization-roles) to view usage across your Pinecone organization. Also, this feature is available only to organizations on the Standard or Enterprise plans.
</Note>

To view and download a report of your usage and costs for your Pinecone organization, go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.

All dates are given in UTC to match billing invoices.

## Monitor token usage

Requests to the [chat](/reference/api/latest/assistant/chat_assistant), [context retrieval](/reference/api/latest/assistant/context_assistant), and [evaluation](/reference/api/latest/assistant/metrics_alignment) API endpoints return a `usage` parameter with `prompt_tokens`, `completion_tokens`, and `total_tokens` generated.

<Tabs>
  <Tab title="Chat">
    For [chat](/guides/assistant/chat-with-assistant), tokens are defined as follows:

    * `prompt_tokens` are based on the messages sent to the assistant and the context snippets retrieved from the assistant and sent to a model. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

      `prompt_tokens` appear as **Assistants Input Tokens** on invoices.
    * `completion_tokens` are based on the answer from the model.

      `completion_tokens` appear as **Assistants Output Tokens** on invoices.
    * `total_tokens` is the sum of `prompt_tokens` and `completion_tokens`.

    ```json Example chat response {9-13} theme={null}
    {
        "finish_reason": "stop",
        "message": {
            "role": "assistant",
            "content": "The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
        },
        "id": "000000000000000030513193ccc52814",
        "model": "gpt-4o-2024-11-20",
        "usage": {
            "prompt_tokens": 23626,
            "completion_tokens": 21,
            "total_tokens": 23647
        },
        "citations": [
            {
                "position": 63,
                "references": [
                    {
                        "file": {
                            "status": "Available",
                            "id": "99305805-3844-41b5-af56-ee693ab80527",
                            "name": "Netflix-10-K-01262024.pdf",
                            "size": 1073470,
                            "metadata": null,
                            "updated_on": "2025-07-29T20:07:53.171752661Z",
                            "created_on": "2025-07-29T20:07:36.361322699Z",
                            "signed_url": "https://storage.googleapis.com/..."
                        },
                        "pages": [
                            78,
                            79,
                            80
                        ],
                        "highlight": null
                    },
                    {
                        "file": {
                            "status": "Available",
                            "id": "99305805-3844-41b5-af56-ee693ab80527",
                            "name": "Netflix-10-K-01262024.pdf",
                            "size": 1073470,
                            "metadata": null,
                            "updated_on": "2025-07-29T20:07:53.171752661Z",
                            "created_on": "2025-07-29T20:07:36.361322699Z",
                            "signed_url": "https://storage.googleapis.com/..."
                        },
                        "pages": [
                            77,
                            78
                        ],
                        "highlight": null
                    }
                ]
            }
        ]
    }
    ```
  </Tab>

  <Tab title="Context retrieval">
    For [context retrieval](/guides/assistant/context-snippets-overview), tokens are defined as follows:

    * `prompt_tokens` are based on the messages sent to the assistant and the context snippets retrieved from the assistant. Messages sent to the assistant can include messages from the chat history in addition to the newest message.

      `prompt_tokens` appear as **Assistants Context Tokens Processed** on invoices.

    * `completion_tokens` do not apply for context retrieval because, unlike for chat, there is no answer from a model. `completion_tokens` will always be 0.

    * `total_tokens` is the sum of `prompt_tokens` and `completion_tokens`.

    ```json Example context response {30-34} theme={null}
    {
        "snippets": [
            {
                "type": "text",
                "content": "edures, or caused such disclosure controls and procedures to be designed under our supervision, to\r\nensure that material information relating to the registrant, including its consolidated subsidiaries, ...",
                "score": 0.86632514,
                "reference": {
                    "type": "pdf",
                    "file": {
                        "status": "Available",
                        "id": "99305805-3844-41b5-af56-ee693ab80527",
                        "name": "Netflix-10-K-01262024.pdf",
                        "size": 1073470,
                        "metadata": null,
                        "updated_on": "2025-07-29T20:07:53.171752661Z",
                        "created_on": "2025-07-29T20:07:36.361322699Z",
                        "signed_url": "https://storage.googleapis.com/..."
                    },
                    "pages": [
                        78,
                        79,
                        80
                    ]
                }
            },
            ...
        ],
        "usage": {
            "prompt_tokens": 22914,
            "completion_tokens": 0,
            "total_tokens": 22914
        },
        "id": "00000000000000007b6ad859184a31b3"
    }
    ```
  </Tab>

  <Tab title="Response evaluation">
    For [response evaluation](/guides/assistant/evaluation-overview), tokens are defined as follows:

    * `prompt_tokens` are based on two requests to a model: The first request contains a question, answer, and ground truth answer, and the second request contains the same details plus generated facts returned by the model for the first request.

      `prompt_tokens` appear as **Assistants Evaluation Tokens Processed** on invoices.
    * `completion_tokens` are based on two responses from a model: The first response contains generated facts, and the second response contains evaluation metrics.

      `completion_tokens` appear as **Assistants Evaluation Tokens Out** on invoices.
    * `total_tokens` is the sum of `prompt_tokens` and `completion_tokens`.

    ```json Response evaluation response {17-21} theme={null}
    {
      "metrics": {
        "correctness": 123,
        "completeness": 123,
        "alignment": 123
      },
      "reasoning": {
        "evaluated_facts": [
          {
            "fact": {
              "content": "<string>"
            },
            "entailment": "entailed"
          }
        ]
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 123,
        "total_tokens": 123
      }
    }
    ```
  </Tab>
</Tabs>
