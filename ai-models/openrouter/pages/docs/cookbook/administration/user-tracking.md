---
title: "User Tracking"
source: https://openrouter.ai/docs/cookbook/administration/user-tracking.md
path: docs/cookbook/administration/user-tracking
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Tracking

The OpenRouter API supports **User Tracking** through the optional `user` parameter. Supplying a stable per-end-user identifier helps isolate abuse blocks and improves your application's reporting.

## What is User Tracking?

User tracking enables you to specify an arbitrary string identifier for your end users in API requests. This optional metadata helps OpenRouter understand your sub-users.

## How It Works

Include a `user` parameter in chat-completions or image-generation requests with a stable identifier for your end user. This can be a user ID, client-side hash, pseudonym, or another stable identifier. OpenRouter folds it into the hashed identity sent upstream and never forwards it raw.

```json lines theme={null}
{
  "model": "~openai/gpt-sol-latest",
  "messages": [
    {"role": "user", "content": "Hello, how are you?"}
  ],
  "user": "user_12345"
}
```

## Register External Users with the Management API

Organizations can explicitly register the same caller-supplied tracking identifiers through the Management API. Registration requires an organization [management key](https://openrouter.ai/docs/guides/overview/auth/management-api-keys.md) and does not create a login, organization member, credential, or generated OpenRouter end-user ID.

```bash theme={null}
curl https://openrouter.ai/api/v1/external-users \
  -H "Authorization: Bearer $OPENROUTER_MANAGEMENT_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "user": "employee_123"
  }'
```

The `user` value is the source of truth and must exactly match the value sent on inference requests. It is case-sensitive, immutable, and unique within the organization.

Use the collection and resource routes to manage registrations:

* `POST /api/v1/external-users` registers a tracking identifier. The request body accepts only `user`.
* `GET /api/v1/external-users` lists active registrations; set `include_inactive=true` to include deactivated registrations.
* `GET /api/v1/external-users/{user}` retrieves one registration, including a deactivated one; check `is_active` for its lifecycle state. URL-encode the exact `user` value.
* `PATCH /api/v1/external-users/{user}` updates the registration with the required `is_active` boolean.
* `DELETE /api/v1/external-users/{user}` soft-deactivates a registration. Repeating the request succeeds, and the identifier remains reserved.

Registration alone does not attribute requests. Continue sending the same identifier as `user` on chat completions, image generation, and the Responses API; `safety_identifier` sets only the upstream abuse-isolation identity and does not attribute requests to a registered external user. Deactivation is a management lifecycle state and does not block inference.

## Implementation Example

## Per-User Abuse Isolation

Send a stable per-end-user identifier with every request: `user` on chat completions and image generation, or `safety_identifier` on the Responses API. A client-side hash or pseudonym works — when a provider requires a user identity, OpenRouter folds it into the hashed identity sent upstream and never forwards the raw value. Requests that include neither field share a single account-level identity upstream, so a provider policy block triggered by one end user can affect your whole account.

## Best Practices

### Choose Stable Identifiers

Use consistent, stable identifiers for the same user across requests:

* **Good**: `user_12345`, `customer_abc123`, `account_xyz789`
* **Avoid**: Random strings that change between requests

### Consider Privacy

When using user identifiers, consider privacy implications:

* Use internal user IDs rather than exposing personal information
* Avoid including personally identifiable information in user identifiers
* Consider using anonymized identifiers for better privacy protection

### Be Consistent

Use the same user identifier format throughout your application:

```python lines theme={null}
# Consistent format
user_id = f"app_{internal_user_id}"
```

