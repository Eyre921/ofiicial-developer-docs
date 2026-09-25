---
title: "Zendesk"
source: https://elevenlabs.io/docs/eleven-agents/customization/integrations/zendesk.md
path: docs/eleven-agents/customization/integrations/zendesk
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Zendesk

## Overview

Connect your ElevenLabs AI agents with [Zendesk](https://www.zendesk.com/) to manage support tickets, users, and organizations. This integration enables your agents to create and update tickets, search for existing records, manage users, and respond to incoming ticket comments.

## Capabilities

| Capability                | Support                                                                                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zero retention mode (ZRM) | Not supported                                                                                                                                                                                  |
| Attachments in triggers   | Images (PNG, JPEG, GIF, WebP) and PDF files on incoming ticket comments, when **Allow file attachments** is enabled in the agent settings and the agent's LLM supports image or document input |
| Attachments in tools      | Not supported — tools such as `zendesk_show_ticket` and `zendesk_list_ticket_comments` return text fields and do not download attachments                                                      |

## Setup

This integration supports three authentication methods: the ElevenLabs OAuth app, your own OAuth client, and an API token.

> **Note**
>
> Zendesk is [deprecating API tokens](https://support.zendesk.com/hc/en-us/articles/10851263566234)
> as an authentication method and moving to OAuth-only access. Existing API token-based Zendesk
> integrations will continue to work until April 30, 2027. ElevenLabs is working to support this
> migration and will proactively reach out to affected customers to help transition to OAuth before
> then. You can switch to the **Custom OAuth client** method below at any time.

#### OAuth

#### Find your subdomain

Your Zendesk subdomain is the first part of your Zendesk URL (e.g., `mycompany` from `mycompany.zendesk.com`).

#### Connect in ElevenLabs

In the ElevenLabs integration setup, select the **OAuth2** credential, enter your **subdomain**, and click **Connect**.

#### Authorize the connection

Zendesk shows an authorization page listing the access the ElevenLabs app requests: read access across your account, plus write access to tickets, users, webhooks, and triggers. Sign in as a user who holds the permissions your agent needs and click **Allow**. Zendesk redirects you back to ElevenLabs and the connection is created.

Authorize as an administrator if you plan to use Zendesk triggers — creating webhooks and editing triggers is restricted to Zendesk admins.

#### API token

#### Enable API token access

In [Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554-Using-Admin-Center), go to **Apps and integrations > APIs > Zendesk API** and enable **Token Access**.

#### Generate an API token

Go to **Apps and integrations > APIs > API tokens** and click **Add API token**. Copy the token immediately — it is not shown again after closing the dialog.

#### Find your subdomain

Your Zendesk subdomain is the first part of your Zendesk URL (e.g., `mycompany` from `mycompany.zendesk.com`).

#### Connect in ElevenLabs

In the ElevenLabs integration setup, enter your **email**, **API token**, and **subdomain**.

#### Custom OAuth client

#### Copy the redirect URL

In the ElevenLabs Zendesk integration setup, copy the **redirect URL**.

#### Create an OAuth client in Zendesk

In [Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554-Using-Admin-Center), go to **Apps and integrations > APIs > OAuth clients** and click **Add Client**. Enter a **name** and a unique **identifier**.

#### Add the redirect URL

Paste the **redirect URL** copied from ElevenLabs into the OAuth client configuration.

#### Save the secret

Save the OAuth client. Zendesk displays a **secret** — copy and store it securely. It is not shown again after closing the dialog.

#### Connect in ElevenLabs

In the ElevenLabs integration setup, enter the **identifier** as the client ID and provide the **secret**. Zendesk redirects you to authorize the connection.

## OAuth scopes

Connecting with the **OAuth2** credential grants ElevenLabs the following [Zendesk OAuth scopes](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/). Read access is granted account-wide, while write access is requested per resource so the token cannot modify resources the integration does not use.

| Scope            | Purpose                                                                                                                                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `read`           | Read access to GET endpoints. Used to fetch tickets, ticket comments and their attachments, users, organizations, problem tickets, and search results, and — when a trigger is connected — to look up the Zendesk trigger and read the signing secret of the webhook ElevenLabs creates. |
| `tickets:write`  | Create, update, delete, and merge tickets, post public and internal comments, and add or remove tags. Used by the ticket tools and to post the agent's reply when a Zendesk trigger fires.                                                                                               |
| `users:write`    | Create, update, and delete users, including bulk create-or-update. Used by the user management tools.                                                                                                                                                                                    |
| `webhooks:write` | Create the webhook that delivers ticket events to your agent when you activate a Zendesk trigger, and delete that webhook when you deactivate the trigger.                                                                                                                               |
| `triggers:write` | Add the ElevenLabs webhook action to the Zendesk trigger you name, and remove that action when you deactivate the trigger.                                                                                                                                                               |

A token never exceeds the permissions of the user who authorized it — the effective access is the intersection of these scopes and that user's Zendesk role.

These scopes do not apply to the other two authentication methods: a custom OAuth client requests `read` and `write` (full read and write access), and an API token carries all permissions of the Zendesk user it belongs to.

## Data disclosure

The table below lists every field the integration accesses in your Zendesk account, whether ElevenLabs stores it, and when and why it is accessed. **Read** means the value is used during processing but not persisted. **Read & stored** means it is persisted on the ElevenLabs conversation record. **Written** means the integration sends it to Zendesk.

| Data                                                 | Access        | Reason                                                                                                                                                                                                                            |
| ---------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ticket ID                                            | Read & stored | Arrives in the trigger webhook payload — the only ticket data Zendesk pushes to ElevenLabs. Stored as the conversation's external ID, as the `integration__zendesk_ticket_id` dynamic variable, and as a link back to the ticket. |
| Ticket subject                                       | Read & stored | Read from the ticket when a trigger fires. Stored as the `integration__zendesk_ticket_subject` dynamic variable so the system prompt and tools can reference what the ticket is about.                                            |
| Ticket creation timestamp                            | Read & stored | Read with the ticket. Stored as the `integration__zendesk_ticket_created_at` dynamic variable for use in the prompt, for example to reason about ticket age.                                                                      |
| Requester ID                                         | Read & stored | Read with the ticket. Stored as the `integration__zendesk_ticket_requester_id` dynamic variable, and used to attribute comments — a requester who is also a staff member is still treated as the customer.                        |
| Ticket tags                                          | Read          | Read on each trigger run to detect an `agent-rating-<score>` tag and a `force-agent` tag. Only the resulting rating is stored on the conversation; the tag list itself is not persisted.                                          |
| Comment bodies, public and internal                  | Read & stored | Read from the ticket's comments on every trigger run. Stored as the conversation transcript and sent to the agent's LLM — this is the conversation the agent replies to.                                                          |
| Comment IDs                                          | Read & stored | Read with the comments. The most recent ID is stored as the last-processed marker so the next trigger run skips comments the agent has already answered.                                                                          |
| Comment author ID                                    | Read & stored | Read with the comments and used to look up the author. Stored as the transcript message's user identifier when the author has no email address.                                                                                   |
| Comment author role                                  | Read          | Read per comment author to decide whether a comment becomes a customer message or a staff message in the transcript. The role itself is not persisted, only the resulting attribution on each message.                            |
| Comment author email address                         | Read & stored | Read per comment author. Stored as the user identifier on transcript messages attributed to the customer, so conversations can be tied to a person across tickets.                                                                |
| Requester email address                              | Read & stored | Read with the requester's user record. Stored as the `integration__zendesk_ticket_requester_email` dynamic variable so the prompt and tools can address or look up the customer.                                                  |
| Attachment metadata: filename, MIME type, size       | Read & stored | Read with the comments to check that an attachment is a supported type and within size limits. Stored on the transcript message the attachment belongs to.                                                                        |
| Attachment file contents                             | Read & stored | Downloaded only when **Allow file attachments** is enabled on the agent and its LLM supports the file type. Stored as conversation files so the agent can read what the customer sent.                                            |
| Zendesk subdomain                                    | Read & stored | Provided by you when connecting. Stored in the integration's connection settings because it forms the API base URL.                                                                                                               |
| Zendesk account email, API token authentication only | Read & stored | Provided by you when connecting. Stored in the connection settings because API token authentication sends the account email alongside the token.                                                                                  |
| API token, OAuth access and refresh tokens           | Read & stored | Stored encrypted at rest and used only to authenticate API calls. Never exposed to the agent, the prompt, or the API.                                                                                                             |
| Webhook signing secret                               | Read & stored | Read once when you activate a trigger. Stored encrypted and used to verify that inbound webhooks genuinely come from your Zendesk account.                                                                                        |
| Trigger title, conditions, and actions               | Read          | Read when you activate a trigger, to find the trigger by name and to preserve its existing actions when the ElevenLabs webhook action is added. Not persisted.                                                                    |
| Agent reply                                          | Written       | Posted as a public comment on the ticket, or as an internal comment when shadow mode is on. This is the integration's purpose.                                                                                                    |
| Conversation link                                    | Written       | Posted once per ticket as an internal comment so staff can open the conversation in ElevenLabs.                                                                                                                                   |
| Attachment error notice                              | Written       | Posted as an internal comment when an attachment was skipped because it is an unsupported type, too large, or failed to download, so staff know the agent did not see it.                                                         |
| ElevenLabs webhook registration                      | Written       | Created when you activate a Zendesk trigger and deleted when you deactivate it. This is the endpoint Zendesk calls on ticket events.                                                                                              |
| Webhook action on your trigger                       | Written       | Added to the trigger you name when you activate it and removed when you deactivate it. Existing actions on the trigger are preserved.                                                                                             |
| Tickets, comments, tags, users, and organizations    | Written       | Written only by the Zendesk tools you enable on the agent, with the parameters the agent supplies during a conversation. No writes occur outside a tool call or a trigger reply.                                                  |

The integration calls the Zendesk API only when a connected trigger fires or when an agent invokes a Zendesk tool. It does not poll your Zendesk account and does not export data in bulk.

Records returned by Zendesk tools are stored in the conversation transcript as part of the tool call result, so a tool that reads a record also stores it. Retention of stored data follows the privacy settings of the agent that handled the ticket, including transcript and PII deletion.

## Zendesk tools

Add Zendesk tools to your agent to manage tickets, users, and organizations during conversations. Once the integration is connected, you can enable individual tools on your agent's configuration page.

### Available tools

The integration provides over 30 tools organized into the following categories:

* **Tickets** — create, update, delete, list, and search tickets. Bulk operations (create many, update many, delete many) are also available.
* **Comments & tags** — add public or internal comments to tickets, and add or remove tags.
* **Users** — look up, create, update, and delete users. Bulk create-or-update is supported for syncing user data.
* **Organizations** — retrieve organization details and list an organization's tickets.
* **Search** — run Zendesk search queries across tickets, users, and organizations (e.g., `type:ticket status:open`).

### Example tools

#### zendesk\_create\_ticket

Creates a new support ticket. The agent collects details from the caller and opens a ticket on their behalf.

| Parameter                | Type    | Description                                             |
| ------------------------ | ------- | ------------------------------------------------------- |
| `ticket.subject`         | string  | Short subject line for the ticket                       |
| `ticket.comment.body`    | string  | Detailed description of the issue                       |
| `ticket.requester.email` | string  | Requester's email address                               |
| `ticket.requester.name`  | string  | Requester's full name                                   |
| `ticket.priority`        | string  | `urgent`, `high`, `normal`, or `low`                    |
| `ticket.status`          | string  | `new`, `open`, `pending`, `hold`, `solved`, or `closed` |
| `ticket.assignee_id`     | integer | Agent ID to assign the ticket to                        |
| `ticket.group_id`        | integer | Group ID to route the ticket to                         |
| `ticket.custom_fields`   | array   | Array of `{id, value}` objects for custom fields        |

#### zendesk\_search

Searches Zendesk for tickets, users, or organizations using the Zendesk search query syntax.

| Parameter | Type   | Description                                                                          |
| --------- | ------ | ------------------------------------------------------------------------------------ |
| `query`   | string | Search query (e.g., `type:ticket status:open` or `type:user email:user@example.com`) |

#### zendesk\_add\_comment

Adds a public or internal comment to an existing ticket — useful for posting call summaries or follow-up notes.

| Parameter                  | Type    | Description                                     |
| -------------------------- | ------- | ----------------------------------------------- |
| `ticket_id`                | integer | The ticket to comment on                        |
| `ticket.comment.body`      | string  | Comment text in plain text                      |
| `ticket.comment.html_body` | string  | HTML version of the comment (optional)          |
| `ticket.comment.public`    | boolean | Whether the comment is visible to the requester |

#### zendesk\_get\_user

Retrieves a user's profile so the agent can greet callers by name or verify their identity.

| Parameter | Type    | Description                    |
| --------- | ------- | ------------------------------ |
| `user_id` | integer | The Zendesk user ID to look up |

### Configuring tools

#### Add an integration tool

On your agent's configuration page, click **Add tool** and select **Add integration tool**.

![Add integration tool](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ef3a82e0747f1b1da18fb6b4755812abe161d436582312e47836e621a44d83c7/agents-platform/pages/customization/integrations/zendesk/zendesk_add_tool_step_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233131Z&X-Amz-Expires=604800&X-Amz-Signature=169785b85274c7daf9d1101bda80cfb2a7f9d4fa0faa191b066dae240d143014&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Select Zendesk tools

Choose your Zendesk connection and toggle the tools you want the agent to use. You can enable as many or as few as needed — for example, a read-only triage agent might only need search and list tools, while a full-service agent might also create and update tickets.

![Select Zendesk tools](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9161ae75a4c514d477174622bd4857d6faf62a11825bc7d4d191176e52a72f91/agents-platform/pages/customization/integrations/zendesk/zendesk_add_tool_step_2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260925T233131Z&X-Amz-Expires=604800&X-Amz-Signature=8b4da2f356403b670ea53d235760e08a582e50ba5f76ad656865b7caaa5cef40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### (Optional) Provide parameters

Each tool's parameters are filled by the agent during the conversation based on what the caller says. You do not need to hard-code parameter values. However, you can optionally pre-fill or constrain specific parameters — for example, setting a default `priority` or `group_id` — to guide the agent's behavior.

#### Legacy webhook setup

> **Note**
>
> If you use the native Zendesk integration, tools are configured automatically. The steps below
> apply only to manual webhook setup.

The legacy integration uses three webhook tools to create the support agent. Review each tool's configuration in the tabs below.

#### zendesk\_get\_ticket\_comments

**Name:** zendesk\_get\_ticket\_comments
**Description:** Retrieves the comments of a ticket.
**Method:** GET
**URL:** `https://acmecorp.zendesk.com/api/v2/tickets/{ticket_id}/comments.json`

**Headers:**

* **Content-Type:** `application/json`
* **Authorization:** *(Secret: `zendesk_key`)*

**Path Parameters:**

* **ticket\_id:** Extract the value from the `id` field in the get\_resolved\_tickets results.

**Tool JSON:**

```json
{
  "type": "webhook",
  "name": "zendesk_get_ticket_comments",
  "description": "Retrieves the comments of a ticket.",
  "api_schema": {
    "url": "https://acmecorp.zendesk.com/api/v2/tickets/{ticket_id}/comments.json",
    "method": "GET",
    "path_params_schema": [
      {
        "id": "ticket_id",
        "type": "string",
        "description": "Extract the value from the id field in the get_resolved_tickets results.",
        "dynamic_variable": "",
        "constant_value": "",
        "required": false,
        "value_type": "llm_prompt"
      }
    ],
    "query_params_schema": [],
    "request_body_schema": null,
    "request_headers": [
      {
        "type": "secret",
        "name": "Authorization",
        "secret_id": "zendesk_api_token"
      },
      {
        "type": "value",
        "name": "Content-Type",
        "value": "application/json"
      }
    ]
  },
  "response_timeout_secs": 20,
  "dynamic_variables": {
    "dynamic_variable_placeholders": {}
  }
}
```

#### zendesk\_get\_resolved\_tickets

**Name:** zendesk\_get\_resolved\_tickets
**Description:** Retrieves all resolved support tickets from Zendesk.
**Method:** GET
**URL:** `https://acmecorp.zendesk.com/api/v2/search.json?query=type:ticket+status:solved`

**Headers:**

* **Content-Type:** `application/json`
* **Authorization:** *(Secret: `zendesk_key`)*

**Tool JSON:**

```json
{
  "type": "webhook",
  "name": "zendesk_get_resolved_tickets",
  "description": "Retrieves all resolved support tickets from Zendesk.",
  "api_schema": {
    "url": "https://acmecorp.zendesk.com/api/v2/search.json?query=type:ticket+status:solved",
    "method": "GET",
    "path_params_schema": [],
    "query_params_schema": [],
    "request_body_schema": null,
    "request_headers": [
      {
        "type": "secret",
        "name": "Authorization",
        "secret_id": "zendesk_api_token"
      },
      {
        "type": "value",
        "name": "Content-Type",
        "value": "application/json"
      }
    ]
  },
  "response_timeout_secs": 20,
  "dynamic_variables": {
    "dynamic_variable_placeholders": {}
  }
}
```

#### zendesk\_open\_ticket

**Name:** zendesk\_open\_ticket
**Description:** Opens a new support ticket.
**Method:** POST
**URL:** `https://acmecorp.zendesk.com/api/v2/tickets.json`

**Headers:**

* **Content-Type:** `application/json`
* **Authorization:** *(Secret: `zendesk_key`)*

**Body Parameters:**

* **ticket:** An object containing:
  * **comment:**
    * **body:** Detailed description of the support issue.
  * **subject:** A short subject line.
  * **requester:**
    * **name:** The full name of the requester.
    * **email:** A valid email address.

**Tool JSON:**

```json
{
  "type": "webhook",
  "name": "zendesk_open_ticket",
  "description": "API endpoint to open a customer support ticket\nMake sure the authorization header is formated as \"Authorization: Basic <auth>\".",
  "api_schema": {
    "url": "https://acmecorp.zendesk.com/api/v2/tickets.json",
    "method": "POST",
    "path_params_schema": [],
    "query_params_schema": [],
    "request_body_schema": {
      "id": "body",
      "type": "object",
      "description": "Details for the support ticket",
      "required": false,
      "properties": [
        {
          "id": "ticket",
          "type": "object",
          "description": "This is the main ticket body which contains all of the information needed to open a ticket.",
          "required": true,
          "properties": [
            {
              "id": "comment",
              "type": "object",
              "description": "This is the comment with information about the issue.",
              "required": true,
              "properties": [
                {
                  "id": "body",
                  "type": "string",
                  "description": "Body of the issue. Include all relevant details for the issue. ",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                }
              ]
            },
            {
              "id": "subject",
              "type": "string",
              "description": "Create a short subject line for the support issue. Add \"DEMO: \" before the subject.",
              "dynamic_variable": "",
              "constant_value": "",
              "required": true,
              "value_type": "llm_prompt"
            },
            {
              "id": "requester",
              "type": "object",
              "description": "The details of the support requester",
              "required": true,
              "properties": [
                {
                  "id": "email",
                  "type": "string",
                  "description": "The email address of the requester. This should look like \njohnsmith@hotmail.com\nYou MUST use the @ symbol and remove any spaces.",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                },
                {
                  "id": "name",
                  "type": "string",
                  "description": "The full name of the requester. ",
                  "dynamic_variable": "",
                  "constant_value": "",
                  "required": true,
                  "value_type": "llm_prompt"
                }
              ]
            }
          ]
        }
      ]
    },
    "request_headers": [
      {
        "type": "secret",
        "name": "Authorization",
        "secret_id": "zendesk_api_token"
      },
      {
        "type": "value",
        "name": "Content-Type",
        "value": "application/json"
      }
    ]
  },
  "response_timeout_secs": 20,
  "dynamic_variables": {
    "dynamic_variable_placeholders": {}
  }
}
```

> **Warning**
>
> Ensure that you add your workspace's Zendesk secret to the agent's secrets.

## Zendesk triggers

Configure Zendesk triggers to have your agent monitor and react to incoming ticket comments, providing first-line support.

### Setup

#### Create a trigger in Zendesk

In Zendesk Admin Center, go to **Objects and rules > Business rules > Triggers** and click **Add trigger**. Configure the conditions that determine which ticket events the agent should respond to (e.g., new tickets in a specific group, ticket comments with a certain tag). Note the trigger name — you will need it in the next step.

If you cannot save the trigger because an action is missing, add a simple action like adding an "agent is processing" tag to the ticket.

#### Connect the trigger in ElevenLabs

On your agent's configuration page, add a new trigger and select **Zendesk Trigger**. Configure the fields:

* **Agent**: the agent that handles incoming conversations.
* **Trigger Rule Name**: the name of the Zendesk trigger you created in the previous step.
* **Daily Ticket Limit** (optional): maximum number of tickets the agent handles per day. Leave empty for unlimited.

When you activate the trigger, ElevenLabs creates a webhook in your Zendesk account and adds it as an action to the trigger you specified. Deactivating the trigger removes the webhook and action.

#### (Optional) Check your trigger in Zendesk

In Zendesk Admin Center, go to **Objects and rules > Business rules > Triggers** and view your previously created trigger. You should see a new action added to it.

If you created another action previously, you can now remove it again.

### Shadow mode

Enable shadow mode on a Zendesk trigger to let the agent observe and draft responses without replying to customers directly. When shadow mode is active, the agent writes its responses as **internal comments** on the ticket instead of public replies. Only Zendesk agents and admins can see internal comments — the end user is not notified.

> **Warning**
>
> Shadow mode only affects how the agent posts its responses. If the agent uses tools that modify
> the ticket (e.g., changing status, adding tags, or assigning the ticket), those changes still
> apply. To prevent unintended modifications, use a separate branch of the agent with modifying tool
> calls removed.

Shadow mode is useful for evaluating agent quality before going live. Review the internal comments alongside the actual support responses to compare accuracy and tone, then promote the agent to active mode once you are confident in its output.

### Avoiding loops

When the agent responds to a ticket comment via the Zendesk API, that response is itself a new comment — which can re-trigger the agent and create an infinite loop. Add either of the following conditions to your Zendesk trigger to prevent this.

**Exclude the service account from the trigger.** Create a separate Zendesk user for the integration (e.g., `ai-agent@yourcompany.com`) and use this account's credentials when connecting in ElevenLabs. Then add this condition to your Zendesk trigger:

* **Current User**, **Is Not**, **\<your service account>**

**Exclude API updates from the trigger.** This filters out all updates made through the Zendesk API, regardless of which user made them:

* **Ticket > Update Via**, **Is Not**, **Web Service (API)**

## Useful links

* [Zendesk API documentation](https://developer.zendesk.com/api-reference/)
* [Managing API tokens](https://support.zendesk.com/hc/en-us/articles/4408889192858-Managing-API-token-access-to-the-Zendesk-API)
* [Zendesk triggers guide](https://support.zendesk.com/hc/en-us/articles/203662246-About-triggers-and-how-they-work)
