---
title: "Webhooks"
source: https://elevenlabs.io/docs/reception-ai/integrations/webhooks.md
path: docs/reception-ai/integrations/webhooks
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Webhooks

The **Webhook Tool** integration exposes your HTTP endpoints as tools that your receptionist or business assistant can call during conversations. The AI decides when to call the endpoint based on the conversation.

## How webhook tools work

When you create a webhook tool, you define:

1. An HTTP endpoint to call.
2. A description of what it does, so the AI knows when to use it.
3. Parameters the AI should collect from the conversation.

During a call, when the conversation matches the tool's purpose, your receptionist collects the parameters, calls the endpoint, and uses the response to continue the conversation.

## Creating a webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**. Configure the fields below and select **Enable**. You can add multiple webhook tools.

| Field                          | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Name**                       | Tool name the AI sees, for example `check_order_status`      |
| **Description**                | When and why to use this tool                                |
| **Method**                     | GET, POST, PUT, PATCH, or DELETE                             |
| **URL**                        | Your HTTP endpoint                                           |
| **Response timeout (seconds)** | How long to wait for your server: 5–120 seconds, default 20  |
| **Assign to agents**           | **Receptionist**, **Assistant agent**, or both               |
| **Disable interruptions**      | Prevent the caller from interrupting while the tool runs     |
| **Request Headers**            | Optional headers sent with every request, such as an API key |
| **Body Parameters**            | Parameters sent in the request body                          |
| **Query Parameters**           | Parameters sent as URL query strings                         |

### Parameters

Each parameter has:

* **Key**: the field name.
* **Type**: `string`, `number`, or `boolean`.
* **Description**: what value the AI should extract from the conversation.
* **Required**: whether the AI must collect it before calling.

## Use cases

| Scenario        | Description                                           | Method |
| --------------- | ----------------------------------------------------- | ------ |
| CRM lookup      | Look up customer info in your system                  | GET    |
| Inventory check | Check product availability in real time               | GET    |
| Lead capture    | Send caller details to your marketing system          | POST   |
| Ticket creation | Create a support ticket during the call               | POST   |
| Price quote     | Calculate a custom quote based on caller requirements | POST   |

## Example

A plumbing business creates a webhook tool:

* **Name:** `check_service_area`
* **Description:** "Check if we service the caller's zip code and what the next available slot is."
* **URL:** `https://api.mybusiness.com/check-area`
* **Method:** POST
* **Request Headers:** `Authorization` set to the business's API key
* **Body Parameters:** `zip_code` (string, required), `service_type` (string, required)

When a caller asks about service in their area, the receptionist collects their zip code, calls the webhook, and tells them the result.

Webhook tools are available on every plan.
