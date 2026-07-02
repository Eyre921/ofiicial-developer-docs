---
title: "Verify webhooks"
source: https://replicate.com/docs/topics/webhooks/verify-webhook.md
path: docs/topics/webhooks/verify-webhook
---

To prevent unauthorized requests, Replicate signs every webhook and its metadata with a unique key for each user or organization. You can use this signature to verify the webhook indeed comes from Replicate before you process it.

[](#why-verify-webhooks)Why verify webhooks?
--------------------------------------------

A webhook is an HTTP POST from an unknown source. Attackers can impersonate services by simply sending a fake webhook to an endpoint.

Another potential security hole is a [replay attack](https://en.wikipedia.org/wiki/Replay_attack), wherein an attacker intercepts a valid webhook payload (including the signature) and re-transmits it to your endpoint. This payload will pass signature validation, and will therefore be acted upon. To mitigate replay attacks, Replicate includes a timestamp indicating when the webhook attempt occurred.

[](#manually-validating-webhook-data)Manually validating webhook data
---------------------------------------------------------------------

Each webhook delivery includes three HTTP headers with additional information that you can use to verify the authenticity of the request:

*   `webhook-id`: The unique message identifier for the webhook messages. This identifier is unique across all messages but will be the same when a webhook is being resent (e.g. retried).
*   `webhook-timestamp`: timestamp in [seconds since epoch](https://en.wikipedia.org/wiki/Unix_time).
*   `webhook-signature`: the [Base64](https://en.wikipedia.org/wiki/Base64) encoded list of signatures (space delimited).

[](#constructing-the-signed-content)Constructing the signed content
-------------------------------------------------------------------

As a webhook receiver, you are responsible for constructing this signed content and performing the validation steps. To validate a webhook, the signed data must be constructed into a well-defined structure from the payload data (body), `webhook-id`, and `webhook-timestamp` headers.

The content to sign is composed by concatenating the `id`, `timestamp`, and `data`, separated by the full-stop character (`.`).

In code it will look something like:

```js
const signedContent = `${webhook_id}.${webhook_timestamp}.${body}`
```

In the example above, `body` is the raw body of the request. The signature is sensitive to any changes, so even a small change in the body will cause the signature to be completely different. This means that you should not change the body in any way before verifying.

[](#retrieving-the-webhook-signing-key)Retrieving the webhook signing key
-------------------------------------------------------------------------

Replicate provides an [API endpoint you can use to retrieve the signing key](https://replicate.com/docs/reference/http#get-the-signing-secret-for-the-default-webhook). The signing key is unique to your user or organization. The endpoint will return only the signing key associated with the API token and its corresponding user or organization.

For optimal performance of the webhook receiver, it is advised to locally cache the signing key. By doing so, you eliminate the need for the receiver to make a request to the Replicate API for validation every time a webhook is received.

```plaintext
GET https://api.replicate.com/v1/webhooks/default/secret
```

Example cURL request:

```bash
curl -s -X GET -H "Authorization: Bearer <paste-your-token-here>" \
https://api.replicate.com/v1/webhooks/default/secret
```

The response will be a JSON object with a single `key` field:

```json
{
    "key": "whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD"
}
```

[](#determining-the-expected-signature)Determining the expected signature
-------------------------------------------------------------------------

Replicate uses an [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code) with [SHA-256](https://en.wikipedia.org/wiki/SHA-2) to sign its webhooks.

To calculate the expected signature, you should HMAC the `signed_content` from above using the base64 portion of the signing secret (this is the part after the `whsec_` prefix) as the key. For example, given a secret `whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD`, you will want to use `C2FVsBQIhrscChlQIMV+b5sSYspob7oD`.

Here’s an example of how you can calculate the signature:

This generated signature should match one of the ones sent in the `webhook-signature` header.

The `webhook-signature` header is composed of a list of space-delimited signatures and their corresponding version identifiers. The signature list is most commonly of length one, though there could be any number of signatures. For example:

```plaintext
v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE= v1,bm9ldHUjKzFob2VudXRob2VodWUzMjRvdWVvdW9ldQo= v2,MzJsNDk4MzI0K2VvdSMjMTEjQEBAQDEyMzMzMzEyMwo=
```

Make sure to remove the version prefix and delimiter (e.g. `v1,`) before verifying the signature.

Please note that to compute the signatures it’s recommended to use a constant-time string comparison method in order to prevent timing attacks.

An example of how to do the signature verification:

[](#verify-timestamp)Verify timestamp
-------------------------------------

As mentioned above, Replicate also sends the timestamp of the attempt in the `webhook-timestamp` header. You should compare the timestamp against your system timestamp and make sure it’s within your tolerance in order to prevent replay attacks.

[](#complete-verification-example)Complete verification example
---------------------------------------------------------------
