---
title: "Stripe"
source: https://elevenlabs.io/docs/reception-ai/integrations/stripe.md
path: docs/reception-ai/integrations/stripe
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Stripe

Connect Stripe's hosted [MCP server](/docs/reception-ai/integrations/mcp-server) to answer billing questions, such as whether an invoice has been paid. Stripe's API doesn't accept the JSON bodies webhook tools send, so MCP is the way to connect it.

> **Warning**
>
> Never let your receptionist collect card numbers. Callers should pay through a Stripe payment link
> or invoice, not by reading card details out on a call.

## Setup

### Create a restricted key

In the Stripe Dashboard, open **Developers** → **API keys** and select **Create restricted key**. Give it **Read** access to **Customers**, **Invoices**, and **PaymentIntents**, and nothing else unless you need it. Start with a test mode key, which begins with `rk_test_`.

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field            | Value                    |
| ---------------- | ------------------------ |
| **Name**         | Stripe                   |
| **Server type**  | Streamable HTTP          |
| **Server URL**   | `https://mcp.stripe.com` |
| **Secret Token** | Your restricted key      |

Select **Enable**. Reception.ai sends the key as a bearer token and lists Stripe's tools.

### Assign tools

Open the **Tools** tab. Assign the read tools, such as `list_customers`, `list_invoices`, and `list_payment_intents`, to the **Client** (receptionist).

Tools that create or change objects, such as `create_refund` or `create_payment_link`, fail unless the key has write access. If you grant it, assign them only to the **Assistant**, so only your team can use them from the dashboard.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking whether a test customer's invoice is paid. When it works, replace the key with a live mode restricted key.

## Troubleshooting

| Problem                                   | What to check                                                                                                   |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| No tools are listed                       | Check the server type is **Streamable HTTP** and the key is a restricted key, not a publishable key.            |
| A tool returns a permission error         | The restricted key lacks access to that resource. Edit the key in Stripe.                                       |
| The receptionist finds the wrong customer | Ask for the email on the account. Stripe looks customers up by email more reliably than by name.                |
| You changed the key                       | The secret token can only be set when you create the integration. Disconnect and reconnect it with the new key. |
