---
title: "Introduction"
source: https://docs.fireworks.ai/api-reference/introduction
path: api-reference/introduction
---

Fireworks AI REST API enables you to interact with various language, image and embedding models using an API Key. It also lets you automate management of models, deployments, datasets, and more.

## Authentication

All requests made to the Fireworks AI REST API must include an `Authorization` header with a valid `Bearer` token using your API key, along with the `Content-Type: application/json` header.

### Getting your API key

You can obtain an API key by:

* Using the [`firectl api-key create`](/tools-sdks/firectl/commands/api-key-create) command
* Generating one through the [Fireworks AI dashboard](https://app.fireworks.ai/settings/users/api-keys)

### Request headers

Include the following headers in your REST API requests:

```json theme={null}
authorization: Bearer <API_KEY>
content-type: application/json
```

## Account management APIs

In addition to inference and deployment APIs, Fireworks exposes account-scoped
quota endpoints.

* [List Quotas](/api-reference/list-quotas)
* [Get Quota](/api-reference/get-quota)
* [Update Quota](/api-reference/update-quota)
