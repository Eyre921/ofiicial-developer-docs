---
title: "Zero Data Retention policy"
source: https://docs.fireworks.ai/accounts/zero-data-retention
path: accounts/zero-data-retention
---

Ensure no user actions on your account can persist or log customer content

[Most of Fireworks](/guides/security_compliance/data_handling) never stores prompts or generations. A few features do store customer content, such as stored responses, batch jobs, and training. The Zero Data Retention policy blocks those features for everyone on the account by rejecting every request and job that would persist or log customer content.

<Info>
  **Enterprise feature.** The Zero Data Retention policy is available on Enterprise accounts. Contact your Fireworks representative if you need this enabled.
</Info>

<Info>
  Only account **Admins** can change the Zero Data Retention policy. Other roles can view the current setting but cannot change it.
</Info>

The policy applies **account-wide**: every user and API key on the account follows it.

The policy doesn't affect prompt caching, which holds KV caches only in memory, or the request metadata used to operate and bill the service. Fireworks may still retain data where required by law or to prevent abuse.

## Settings

| Setting | Effect |
| :- | :- |
| **Default Policy** | Applies to Inference and Training. Off by default. |
| **Inference** | Follows Default Policy unless set to enforced or not enforced. |
| **Training** | Follows Default Policy unless set to enforced or not enforced. |

## What it controls

| Operation | Scope | When enforced |
| :- | :- | :- |
| Chat completions and completions | Inference | Allowed |
| Chat completions and completions with `store: true` | Inference | **Rejected** |
| Anthropic Messages API | Inference | Allowed |
| Embeddings and reranking | Inference | Allowed |
| Responses API with `store: false` | Inference | Allowed |
| Responses API with `store: true` (default) | Inference | **Rejected** |
| Responses API with `background: true` | Inference | **Rejected** |
| FireRouter virtual models | Inference | **Rejected** |
| Batch inference jobs | Inference | **Rejected** |
| Supervised fine-tuning, DPO, and reinforcement fine-tuning jobs | Training | **Rejected** |
| Training API: forward and backward passes, optimizer steps, sampling, and checkpoints | Training | **Rejected** |
| Evaluators and evaluation jobs | Training | **Rejected** |
| Dataset uploads | Training | **Rejected** |
| Custom model uploads and imports | Inference or Training | **Rejected** |
| Model quantization with `firectl model prepare` | Inference or Training | **Rejected** |

Data sent to third parties, such as MCP servers you connect or the search providers and websites behind web search, is handled under their own policies.

## Existing data

Turning on the policy doesn't delete anything already stored on the account, such as stored responses, datasets, and uploaded models. You can delete any of it whenever you like.

## Configure in the console

Account admins can set the Zero Data Retention policy in the Fireworks console at **Settings → Governances → Zero Data Retention** ([open in console](https://app.fireworks.ai/settings/governances/zero-data-retention)).

Turn on Default Policy, or set Inference and Training individually, and save.

## Configure with firectl

Enforce for Inference and Training:

```bash theme={null}
firectl policy zdr set --default on
```

Set Inference and Training individually:

```bash theme={null}
firectl policy zdr set --inference on --training off
```

Inspect the current setting:

```bash theme={null}
firectl policy zdr get
```

Make Inference and Training follow Default Policy again:

```bash theme={null}
firectl policy zdr reset
```

Turn the policy off:

```bash theme={null}
firectl policy zdr set --default off --inference inherit --training inherit
```

## Configure with the API

Use [Update Policy Settings](/api-reference/update-policy-settings) with `updateMask=zero_data_retention` and an API key that belongs to an account Admin. Each request replaces the whole Zero Data Retention section, so always send `defaultEnforced`. A scope you leave out follows Default Policy.

Enforce for Inference and Training:

```bash theme={null}
curl -X PATCH \
  "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/policySettings?updateMask=zero_data_retention" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"zeroDataRetention": {"defaultEnforced": true}}'
```

Set Inference and Training individually:

```bash theme={null}
curl -X PATCH \
  "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/policySettings?updateMask=zero_data_retention" \
  -H "Authorization: Bearer ${FIREWORKS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "zeroDataRetention": {
      "defaultEnforced": false,
      "inference": {"enforcement": "ENFORCED"},
      "training": {"enforcement": "NOT_ENFORCED"}
    }
  }'
```

To turn the policy off, send `{"zeroDataRetention": {"defaultEnforced": false}}`.

[Get Policy Settings](/api-reference/get-policy-settings) returns the current setting. An absent `zeroDataRetention` means the policy is off.

## Related

* [Zero Data Retention](/guides/security_compliance/data_handling) — baseline Fireworks retention behavior
* [Data Security & Privacy](/guides/security_compliance/data_security) — encryption and data controls
* [Data residency](/accounts/data-residency) — restrict processing geography
* [Model access policy](/accounts/model-access-policy) — restrict model capabilities
