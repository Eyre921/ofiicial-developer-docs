---
title: "BigCommerce"
source: https://elevenlabs.io/docs/reception-ai/integrations/bigcommerce.md
path: docs/reception-ai/integrations/bigcommerce
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# BigCommerce

Your receptionist can look up a caller's order in your BigCommerce store and tell them its status. A [webhook tool](/docs/reception-ai/integrations/webhooks) finds orders by the customer's email address through the BigCommerce Orders API.

> **Warning**
>
> Orders contain customers' names, addresses, phone numbers, and purchases. Your receptionist must
> confirm the caller is the customer before sharing anything. The tool description below makes it
> ask for both the order number and the email address on the order, and only discuss an order when
> both match.

## Before you start

### Create a read-only API account

In your BigCommerce control panel, open **Settings** → **Store-level API accounts** and create an API account. Give it a name, such as "Reception", and set the **Orders** scope to **read-only**, with every other scope set to **None**. You can't change scopes later.

### Copy the credentials

Save the account and copy the **Access token** and the **API path**. The API path looks like `https://api.bigcommerce.com/stores/STORE_HASH/v3/`; the part after `/stores/` is your store hash. Treat the access token as a secret.

## Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_bigcommerce_order`                                                                                                                                                                                                                                                                            |
| **Description**      | "Look up an order when a caller asks about it. First ask for the order number and the email address on the order, and have them spell the email. Only share details of an order whose id and billing email both match what the caller said. Otherwise, say you can't find it and offer a callback." |
| **Method**           | GET                                                                                                                                                                                                                                                                                                 |
| **URL**              | `https://api.bigcommerce.com/stores/STORE_HASH/v2/orders`                                                                                                                                                                                                                                           |
| **Request Headers**  | `X-Auth-Token`: your access token  `Accept`: `application/json`                                                                                                                                                                                                                                     |
| **Query Parameters** | `email` (string, required): "The email address the caller gave."  `sort` (string, required): "Always the exact value `date_created:desc`."  `limit` (number, required): "Always the exact value `5`."                                                                                               |
| **Assign to agents** | **Receptionist**                                                                                                                                                                                                                                                                                    |

The `sort` and `limit` values return the customer's most recent orders first, instead of their oldest.

Select **Enable**, then [test your receptionist](/docs/reception-ai/receptionist/testing) with a test order: ask about it with the right order number and email, then with a wrong email, and check that the second call gets no details.

> **Tip**
>
> The response includes the billing address and payment details of each order. Add a [rule or procedure](/docs/reception-ai/receptionist/rules-and-procedures) for what your receptionist may
> share on the phone, for example only the status and the order date.

## Troubleshooting

| Problem                 | What to check                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| BigCommerce returns 401 | The header must be named `X-Auth-Token` and hold the access token, not the client ID or client secret. |
| BigCommerce returns 403 | The API account lacks the **Orders** read-only scope. Create a new account with it.                    |
| BigCommerce returns 404 | Check the store hash in the URL, and that the URL uses `/v2/orders`.                                   |
| The response is empty   | No order has that email. Check that the caller gave the email used at checkout.                        |
