---
title: "Model access policy"
source: https://docs.fireworks.ai/accounts/model-access-policy
path: accounts/model-access-policy
---

Restrict which models users on your Enterprise account can access for inference, deployments, and training

Model access policy lets Enterprise account admins control which models users on the account can use. You can allowlist models (deny by default, then permit specific models) or deny specific models while leaving the rest of the catalog open.

<Info>
  **Enterprise feature.** Model access policy is available on Enterprise accounts. Contact your Fireworks representative if you need this enabled.
</Info>

Policy applies **account-wide**: every user on the account shares the same rules. There is no per-user or per-group model access control today.

## What it controls

Each model can be allowed or denied independently across four capabilities:

| Capability                | What it governs                                                   |
| :------------------------ | :---------------------------------------------------------------- |
| **Serverless inference**  | Chat, completions, embeddings, and other serverless API routes    |
| **Serverless Fast**       | The model's Fast serving mode (separate from standard serverless) |
| **Dedicated deployments** | Creating on-demand deployments on that base model                 |
| **Training**              | Supervised fine-tuning, DPO, and reinforcement fine-tuning jobs   |

Fast mode is evaluated separately from standard serverless. You can allow one without the other.

## Default behavior

Accounts that never configure a policy keep today's open default: **all models are allowed** for all users.

| State                                    | Effect                        |
| :--------------------------------------- | :---------------------------- |
| No policy configured                     | All models allowed            |
| After `policy clear`                     | All models allowed (restored) |
| Deny-all default + per-model allow rules | Only listed models allowed    |

## Configure in the console

Account admins can manage model access policy in the Fireworks console at **Settings → Governances → Model Access** ([open in console](https://app.fireworks.ai/settings/governances/model-access)).

Use the console to allowlist or block models and toggle capabilities (serverless, Fast, deployments, and training) without using the CLI or API.

You can also configure policy with [firectl](#allowlist-a-set-of-models) or the [REST API](#rest-api).

## Allowlist a set of models

The most common pattern is to deny everything by default and allow only the models your organization approves.

```bash theme={null}
firectl policy allowlist qwen3-235b-a22b kimi-k2-instruct
```

This sets a deny-all default and creates one allow rule per model ID. By default, all four capabilities are allowed for each listed model.

To allow only serverless inference (not training or deployments):

```bash theme={null}
firectl policy allowlist qwen3-235b-a22b \
  --deployments=false --training=false
```

Inspect the active policy:

```bash theme={null}
firectl policy get
```

Restore the open default:

```bash theme={null}
firectl policy clear
```

## Deny specific models (blocklist)

To block individual models while leaving the rest of the catalog open, add per-model deny rules without changing the default:

```bash theme={null}
firectl policy set <model-id> \
  --serverless=false --serverless-fast=false --deployments=false --training=false
```

Or set a partial deny, such as blocking Fast mode only:

```bash theme={null}
firectl policy set <model-id> --serverless-fast=false
```

## Step-by-step allowlist

If you prefer explicit steps instead of `policy allowlist`:

```bash theme={null}
# 1. Deny all models by default
firectl policy set-default --deny-all

# 2. Allow specific models (hosted models use the fireworks account)
firectl policy set qwen3-235b-a22b --model-account fireworks
firectl policy set kimi-k2-instruct --model-account fireworks
```

Remove a model from the allowlist:

```bash theme={null}
firectl policy remove <model-id>
```

## Authorization

| Action        | Who                |
| :------------ | :----------------- |
| View policy   | Any account member |
| Update policy | Account **Admin**  |

## REST API

Account admins can also manage policy through the API:

* `GET /v1/accounts/{account_id}/policySettings`
* `PATCH /v1/accounts/{account_id}/policySettings`

Example allowlist body:

```json theme={null}
{
  "name": "accounts/my-account/policySettings",
  "defaultPermissions": {
    "allowServerless": false,
    "allowServerlessFast": false,
    "allowDedicatedDeployments": false,
    "allowTraining": false
  },
  "rules": [
    {
      "model": "accounts/fireworks/models/qwen3-235b-a22b",
      "permissions": {
        "allowServerless": true,
        "allowServerlessFast": true,
        "allowDedicatedDeployments": true,
        "allowTraining": false
      }
    }
  ]
}
```

All four permission booleans are required whenever `defaultPermissions` or a rule's `permissions` object is sent.

## Important limitations

* **Account-wide only.** Policy cannot differentiate access between teams, divisions, or individual users on the same account.
* **Explicit model IDs.** Rules are keyed on model resource names (for example `accounts/fireworks/models/qwen3-235b-a22b`). You must list the models you want to control.
* **Hosted models in rules.** New per-model rules apply to Fireworks-hosted serverless models. If you use a deny-all default and need to permit training or deployments on your own uploaded base models, configure those capabilities in `defaultPermissions` instead of per-model rules.
* **Propagation delay.** Policy changes are not instant at the API edge. Allow up to several minutes (and up to an hour for idle API keys) before assuming a change has taken effect everywhere.
* **Rule limit.** An account can store roughly 85 per-model rules.

## Related

* [Enterprise features](/accounts/enterprise-features) — overview of Enterprise administration capabilities
* [Managing users](/accounts/users) — account roles and permissions
* [Audit & access logs](/guides/security_compliance/audit_logs) — monitor account activity
