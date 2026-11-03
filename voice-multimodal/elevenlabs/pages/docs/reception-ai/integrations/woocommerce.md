---
title: "WooCommerce"
source: https://elevenlabs.io/docs/reception-ai/integrations/woocommerce.md
path: docs/reception-ai/integrations/woocommerce
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# WooCommerce

Your receptionist can look up a caller's order in your WooCommerce store and tell them its status. A [webhook tool](/docs/reception-ai/integrations/webhooks) searches your store's orders through the WooCommerce REST API.

> **Warning**
>
> Orders contain customers' names, addresses, phone numbers, and purchases. Your receptionist must
> confirm the caller is the customer before sharing anything. The tool description below makes it
> ask for both the order number and the email address on the order, and only discuss an order when
> both match.

## Before you start

### Check your store's settings

Your store must use HTTPS, and pretty permalinks must be on: in WordPress, open **Settings** → **Permalinks** and choose any option other than **Plain**.

### Create a read-only API key

In WordPress, open **WooCommerce** → **Settings** → **Advanced** → **REST API** and select **Add key**. Enter a description, such as "Reception", pick a user, set **Permissions** to **Read**, and select **Generate API key**. Copy the **Consumer key** and **Consumer secret**; the secret is only shown once.

### Build the header value

WooCommerce authenticates keys with HTTP basic auth. Build the header value on your computer:

```bash
printf 'CONSUMER_KEY:CONSUMER_SECRET' | base64
```

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_woocommerce_order`                                                                                                                                                                                                                                                                                |
| **Description**      | "Look up an order when a caller asks about it. First ask for the order number and the email address on the order, and have them spell the email. Only share details of an order whose number and billing email both match what the caller said. Otherwise, say you can't find it and offer a callback." |
| **Method**           | GET                                                                                                                                                                                                                                                                                                     |
| **URL**              | `https://YOUR-STORE.com/wp-json/wc/v3/orders`                                                                                                                                                                                                                                                           |
| **Request Headers**  | `Authorization` set to `Basic ` followed by the encoded value                                                                                                                                                                                                                                           |
| **Query Parameters** | `search` (string, required): "The email address the caller gave."  `per_page` (number, required): "Always the exact value `5`."                                                                                                                                                                         |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                        |

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) with a test order: ask about it with the right order number and email, then with a wrong email, and check that the second call gets no details.

> **Tip**
>
> The response includes every field of each order, including addresses. Add a [rule or procedure](/docs/reception-ai/receptionist/rules-and-procedures) for what your receptionist may
> share on the phone, for example only the status, the order date, and the tracking number.

## Troubleshooting

| Problem                                 | What to check                                                                                                                       |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| WooCommerce returns 401                 | Re-encode the header value. Some hosts strip the `Authorization` header before WordPress sees it; ask your host to pass it through. |
| 404 `rest_no_route`                     | Check the store address in the URL and that permalinks aren't set to **Plain**.                                                     |
| Known orders aren't found               | The search matches the billing details stored on the order. Check that the caller gave the email used at checkout.                  |
| A firewall or security plugin blocks it | Allow requests to `/wp-json/wc/` in the plugin or your host's firewall.                                                             |
