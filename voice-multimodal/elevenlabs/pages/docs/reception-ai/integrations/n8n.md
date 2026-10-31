---
title: "n8n"
source: https://elevenlabs.io/docs/reception-ai/integrations/n8n.md
path: docs/reception-ai/integrations/n8n
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# n8n

Connect an n8n workflow to a [webhook tool](/docs/reception-ai/integrations/webhooks). When a conversation matches the tool's description, your receptionist collects the details, calls the workflow, and reads its response back to the caller. Through n8n, the receptionist can reach any app n8n connects to.

## Build the workflow

### Add a Webhook trigger

In n8n, create a workflow and add a **Webhook** node. Set **HTTP Method** to `POST`.

### Protect the webhook

Set **Authentication** to **Header Auth** and create a credential with a header name, such as `X-Reception-Key`, and a long random value. Reception.ai sends this header with every call.

### Return a response

Set **Respond** to **Using 'Respond to Webhook' Node**. Add your workflow steps, then end with a **Respond to Webhook** node that returns JSON, for example `{"available": true, "next_slot": "Tuesday 10am"}`. Your receptionist reads this response to decide what to say.

### Activate the workflow

Activate the workflow and copy the **Production URL** from the Webhook node. The test URL only works while the editor is listening.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | What the workflow does, for example `check_service_area`                                                                    |
| **Description**      | When to use it, for example "Check whether we serve the caller's zip code. Use it before booking an on-site visit."         |
| **Method**           | POST                                                                                                                        |
| **URL**              | The workflow's production URL                                                                                               |
| **Request Headers**  | The header name and value from the n8n credential                                                                           |
| **Body Parameters**  | One parameter per value the workflow needs, for example `zip_code` (string, required). n8n reads them from `body.zip_code`. |
| **Assign to agents** | **Receptionist**                                                                                                            |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) with a conversation that should trigger the workflow. Each run appears in n8n's **Executions** list.

> **Note**
>
> Body parameters are flat values that your receptionist fills in from the conversation. To send a
> fixed value, set it inside the workflow instead.

## Expose several workflows over MCP

To give your receptionist many n8n workflows at once, use n8n's **MCP Server Trigger** node instead. Connect the workflows or tool nodes you want to expose, set the trigger's authentication to bearer, and activate it. In Reception.ai, add an [MCP server](/docs/reception-ai/integrations/mcp-server) with the trigger's production URL and the bearer token as **Secret Token**, then assign the tools on the **Tools** tab.

## Troubleshooting

| Problem                               | What to check                                                                                                                                                  |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No execution appears in n8n           | The workflow must be active and the tool must use the production URL.                                                                                          |
| The workflow returns 403              | The header name and value in Reception.ai must match the n8n credential exactly.                                                                               |
| The receptionist says the tool failed | The workflow must finish within the tool's **Response timeout**. It defaults to 20 seconds and goes up to 120.                                                 |
| The receptionist never calls the tool | Make the tool's description name the situations where it should be used. You can also add a [procedure](/docs/reception-ai/receptionist/rules-and-procedures). |
