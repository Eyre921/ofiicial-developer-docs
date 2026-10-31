---
title: "Make"
source: https://elevenlabs.io/docs/reception-ai/integrations/make.md
path: docs/reception-ai/integrations/make
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Make

Connect a Make scenario to a [webhook tool](/docs/reception-ai/integrations/webhooks). When a conversation matches the tool's description, your receptionist collects the details, runs the scenario, and reads its response back to the caller.

## Build the scenario

### Add a custom webhook

In Make, create a scenario and add **Webhooks** → **Custom webhook** as the trigger. Select **Add**, name the webhook, and copy its URL. Treat the URL as a secret: anyone who has it can run the scenario.

### Add your modules

Add the apps, routers, and filters the scenario needs.

### Return a response

End the scenario with **Webhooks** → **Webhook response**. Set **Status** to `200` and **Body** to JSON your receptionist can read, for example `{"order_status": "shipped", "eta": "Friday"}`. Without this module, Make replies `Accepted` and your receptionist gets no data.

### Turn on the scenario

Set the scenario to run **Immediately as data arrives** and turn it on.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Name**             | What the scenario does, for example `check_order_status`                                                       |
| **Description**      | When to use it, for example "Look up an order's shipping status. Use it when a caller asks about their order." |
| **Method**           | POST                                                                                                           |
| **URL**              | The custom webhook URL                                                                                         |
| **Body Parameters**  | One parameter per value the scenario needs, for example `order_number` (string, required)                      |
| **Assign to agents** | **Receptionist**                                                                                               |

Select **Enable**.

## Teach Make the data structure

Make learns the fields a webhook receives from its first request. Open the custom webhook, select **Redetermine data structure**, and [test your receptionist](/docs/reception-ai/receptionist/testing) with a conversation that triggers the tool. After Make shows **Successfully determined**, map the fields in your modules.

## Troubleshooting

| Problem                               | What to check                                                                                                   |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| The scenario doesn't run              | The scenario must be on and set to run immediately.                                                             |
| The receptionist gets no answer       | Add a **Webhook response** module and make sure every route reaches one.                                        |
| The receptionist says the tool failed | The scenario must respond within the tool's **Response timeout**. It defaults to 20 seconds and goes up to 120. |
| Fields are empty in later modules     | Redetermine the data structure after you add or rename body parameters.                                         |
