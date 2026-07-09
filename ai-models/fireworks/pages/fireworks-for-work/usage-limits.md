---
title: "Per-User Usage Limits"
source: https://docs.fireworks.ai/fireworks-for-work/usage-limits
path: fireworks-for-work/usage-limits
---

Set per-user spending limits on serverless inference — account defaults and per-user overrides

Set spending limits for individual users in your account on serverless (per-token) inference. You can apply an account-wide default cap and override it for specific users. When a user reaches their limit, their further serverless requests are blocked until the billing period resets.

<Note>
  Per-user usage limits are available on request. Reach out to your Fireworks
  contact to enable them for your account.
</Note>

## Concepts

* **Account default cap** — the per-user spending limit applied to every user who doesn't have their own override.
* **Per-user override** — a specific user's own cap. Takes precedence over the account default.
* **Effective limit** — the limit actually applied to a user: their override if set, otherwise the account default. If neither is set, the user is **uncapped**.
* **Current-period usage** — how much a user (and the account overall) has spent in the current billing period.

All amounts are in USD, and usage resets at the start of each billing period.

## Supported models

Per-user metering currently applies to a subset of serverless models. Usage on models **not** listed here does not count toward a user's limit and won't trigger blocking. Coverage is expanding as more models are updated.

Currently supported:

* GLM 5.2
* GLM 5.2 (Fast)
* GPT OSS 120B
* Kimi K2.6 Fast
* Kimi K2.7 Fast
* DeepSeek V4 Flash
* MiniMax M2.7

Coming soon:

* DeepSeek V4 Pro

## Who can do what

* **Account admins** — view and manage everything: set the default cap, set/clear per-user overrides, and view every user's usage.
* **Members (non-admin)** — view the account-level limits and **their own** usage and limit. Members cannot view other users' limits, list all users, or change any limits.

Each command below is annotated with who can run it.

## Using `firectl`

### Account-level

```bash theme={null}
# View the account default cap and account-wide usage — any member
firectl usage-limits get

# Set a $100 default per-user cap — admin only
firectl usage-limits update --default-user-limit=100
```

The default cap applies to every user who doesn't have their own override.

### Per-user

```bash theme={null}
# List every user with their usage, effective limit, and override — admin only
firectl usage-limits user list

# View a single user — admin, or that user viewing their own
firectl usage-limits user get <USER_ID>

# Give a user their own cap, overriding the account default — admin only
firectl usage-limits user set <USER_ID> --limit=500

# Remove a user's override, reverting them to the account default — admin only
firectl usage-limits user unset <USER_ID>
```

A user record shows:

* **used** — current-period spend
* **effective\_limit** — the limit applied to them (override, else account default)
* **override** — their per-user override, if any
* **exceeded\_until** — set only when the user is currently blocked; shows when the block lifts (the end of the current billing period)

### Cap a single user (no account default)

You don't need an account-wide default to cap individuals. Set an override for just the users you want to limit and leave the account default unset — only those users are capped, and everyone else stays **uncapped**.

```bash theme={null}
# Cap only this user; everyone else remains uncapped — admin only
firectl usage-limits user set <USER_ID> --limit=50
```

A configured cap enforces by default, so the capped user is blocked at their limit while uncapped users are unaffected.

## Using the REST API

### Read

```bash theme={null}
# Account-level usage limits — any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/usageLimits

# A single user's usage limits — admin, or that user
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/users/<USER_ID>/usageLimits

# All users in the account — admin only
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/userUsageLimits
```

### Update (admin only)

Updates use `PATCH` with a field mask indicating which fields to change:

* `PATCH /v1/accounts/<ACCOUNT_ID>/usageLimits` — set `default_user_limit`
* `PATCH /v1/accounts/<ACCOUNT_ID>/users/<USER_ID>/usageLimits` — set `limit_override` (an unset value removes the override)

`firectl` (above) is the simplest way to make changes; the same operations are available through the API and SDKs.

## How enforcement works

* **A user who reaches their effective limit is blocked** from further serverless requests until the billing period resets. Blocked requests receive **HTTP 402**.
* **Limits are per billing period.** Usage and any blocks reset when the period rolls over.
* **Enforcement is near-real-time, not instantaneous.** After a user crosses their limit there is a short delay (typically a few minutes) before requests start being blocked, and a similar delay before a user is unblocked after you raise their limit. Plan around this lag rather than expecting an immediate cutoff.
* **A `$0` cap** means the user is allowed no serverless spend — they are blocked immediately.
* **Removing the account default** leaves users uncapped unless they have their own override.
* Only **serverless (per-token) inference on [supported models](#supported-models)** counts toward these limits. Usage on other serverless models — and dedicated deployment (GPU-hour) usage — is not metered per user here.

## FAQ

<AccordionGroup>
  <Accordion title="What counts toward a user's limit?">
    Serverless per-token inference spend in the current billing period.
  </Accordion>

  <Accordion title="What does a blocked user see?">
    Their serverless requests return HTTP `402` until the billing period resets or their limit is raised.
  </Accordion>

  <Accordion title="Can a user check their own usage?">
    Yes — a user can read their own usage and limit; they just can't see other users' limits or change any limits.
  </Accordion>

  <Accordion title="Do limits carry over between periods?">
    No. Usage and blocks reset each billing period.
  </Accordion>
</AccordionGroup>
