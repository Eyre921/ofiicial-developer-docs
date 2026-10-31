---
title: "Shopify"
source: https://elevenlabs.io/docs/reception-ai/integrations/shopify.md
path: docs/reception-ai/integrations/shopify
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Shopify

Every Shopify store has a Storefront [MCP server](/docs/reception-ai/integrations/mcp-server) that exposes its catalog and policies. Connect it so your receptionist can answer questions about products, prices, availability, shipping, and returns from your live store.

## Setup

### Add the MCP server

In Reception.ai, go to **Integrations**, select **Add integration**, and choose **MCP Server**.

| Field           | Value                                      |
| --------------- | ------------------------------------------ |
| **Name**        | Shopify                                    |
| **Server type** | Streamable HTTP                            |
| **Server URL**  | `https://YOUR-STORE.myshopify.com/api/mcp` |

Leave **Secret Token** empty. The Storefront MCP server only exposes what your online store already shows publicly. Select **Enable**.

### Assign tools

Open the **Tools** tab and assign these to the **Client** (receptionist):

* `search_shop_catalog`: finds products and their prices and availability.
* `get_product_details`: gives the options and variants of one product.
* `search_shop_policies_and_faqs`: answers shipping, return, and store policy questions.

Leave the cart tools unassigned. A phone caller can't use a cart your receptionist builds.

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking whether a product is in stock and what your return policy is.

## Limitations

Your receptionist can't look up orders. Shopify only shares order details after a customer signs in to their account, which a caller can't do on a call. To answer order status questions, connect an order lookup through a [webhook](/docs/reception-ai/integrations/webhooks) to your own system or [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                  | What to check                                                                     |
| ------------------------ | --------------------------------------------------------------------------------- |
| No tools are listed      | Use your `myshopify.com` address and the **Streamable HTTP** server type.         |
| Products are missing     | The server only sees products published to your online store sales channel.       |
| Policy answers are empty | Fill in your store's policies in Shopify admin under **Settings** → **Policies**. |
