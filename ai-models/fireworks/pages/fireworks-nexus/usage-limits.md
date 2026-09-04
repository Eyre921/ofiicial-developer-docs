---
title: "Per-User Usage Limits"
source: https://docs.fireworks.ai/fireworks-nexus/usage-limits
path: fireworks-nexus/usage-limits
---

Set per-user spending limits on serverless inference — account defaults, group limits, and per-user overrides

Set spending limits for individual users in your account on serverless (per-token) inference. Nexus accounts start with a **\$100 per-user default** limit. You can change the account-wide default cap, cap everyone in a group at a shared amount with a **group limit**, and override the limit for specific users. When a user reaches their limit, their further serverless requests are blocked until the billing period resets.

<Note>
  Per-user usage limits are available on request. Reach out to your Fireworks
  contact to enable them for your account. Group limits additionally require
  groups to be enabled and your directory connected through [SCIM group
  sync](/accounts/sso#group-provisioning).
</Note>

## Concepts

* **Account default cap** — the per-user spending limit applied to every user who has neither an override nor a group cap. Nexus accounts start with a **\$100** default.
* **Group limit** — a named, reusable cap you define once and assign to one or more [groups](#group-limits). Every member of an assigned group is capped at that amount.
* **Per-user override** — a specific user's own cap. Takes precedence over both group caps and the account default.
* **Effective limit** — the limit actually applied to a user, resolved by the precedence below.
* **Current-period usage** — how much a user (and the account overall) has spent in the current billing period.

All amounts are in USD, and usage resets at the start of each billing period.

### Limit precedence

A user's effective limit is resolved in this order:

1. Their **per-user override**, if they have one.
2. Otherwise, the **highest** cap among the group limits assigned to their groups. A group limit *below* the account default still wins: a group cap replaces the default rather than competing with it.
3. Otherwise, the **account default cap**.

A user with no override, no group limit, and no account default has no cap. Use a per-user override when someone needs a cap their group membership won't produce.

## Group limits

A group limit is just a named amount. You define a handful of them for the account, then point groups at them. Editing a group limit's amount moves the cap for every group assigned to it. (`firectl` and the REST API call this resource a *group usage limit tier*.)

A group limit caps **each member individually** — it is not a shared budget for the group. Ten members on a \$500 limit can spend up to \$500 each.

### Where groups come from

Groups come from your identity provider through [SCIM group sync](/accounts/sso#group-provisioning) — that is the only way to create one. Groups and their membership are read-only in Fireworks; add, rename, delete, and populate them in your directory. The limit assignment is the one part you set in Fireworks.

### Rules and limits

* An account may define **at most 9 group limits**.
* **Each group limit must hold a distinct amount.** Creating or updating one to an amount another already holds is rejected. A group limit *may* equal the account default.
* Amounts are **USD and non-negative**. A **`$0`** group limit is a real cap — its members are blocked from serverless spend immediately.
* A group limit sets an **amount only**. Reaching any cap blocks the user, so someone in several groups has one unambiguous outcome.
* An **unassigned group contributes no cap**; its members fall back to another of their groups or to the account default.
* **Deleting a group limit that groups are still assigned to is rejected** by `firectl` and the REST API — clear those assignments first. In the web app, deleting a limit option reassigns its groups to the org default for you.

## Supported models

Per-user metering applies to **all serverless models** except **[MiniMax M2.7](https://app.fireworks.ai/models/fireworks/minimax-m2p7)**. Usage on MiniMax M2.7 does not count toward a user's limit and won't trigger blocking.

## Who can do what

* **Account admins** — view and manage everything: update the default cap, define and assign group limits, set/clear per-user overrides, and view every user's usage.
* **Members (non-admin)** — view the account-level limits, every group's limit assignment and the group limits themselves, and **their own** usage and limit. Members cannot view other users' limits, list all users, or change any limits.

Each command below is annotated with who can run it.

## In the web app

Account admins manage limits on the [User Limits](https://app.fireworks.ai/settings/user-limits) page under **Settings** in the Fireworks web app. Members see their own usage and limit there, and can request an increase.

The page has three tabs — **Groups** appears once group limits are enabled for your account:

* **Usage** — every user's current-period spend against their effective limit, with the source of that limit and, for a group-derived cap, which group it came from.
* **Groups** — each group with its assigned limit and member count. The web app calls group limits **limit options**: pick one from the dropdown on a group's row to assign it, or choose **Org default** to clear the assignment and fall back to the account default. Create, edit, and delete limit options from the same tab.
* **Increase Request** — pending per-user increase requests to approve or reject.

Group rows show a **SCIM-synced** source and the time of the last directory sync. Membership changes belong in your identity provider; only the limit assignment is editable here.

## Using `firectl`

### Account-level

```bash theme={null}
# View the account default cap and account-wide usage — any member
firectl usage-limits get

# Update the default per-user cap — admin only
firectl usage-limits update --default-user-limit=200
```

### Defining group limits

```bash theme={null}
# List the account's group limits — any member
firectl usage-limits group-tier list

# Define a group limit — admin only
firectl usage-limits group-tier create contractors --limit=100 --display-name="Contractors"

# View one group limit — any member
firectl usage-limits group-tier get contractors

# Re-price every group using this limit — admin only
firectl usage-limits group-tier update contractors --limit=250

# Rename it — admin only
firectl usage-limits group-tier update contractors --display-name="Contractors (2026)"

# Delete it — admin only, and only once no group is assigned
firectl usage-limits group-tier delete contractors
```

### Group assignments

```bash theme={null}
# List every group's limit assignment, unassigned groups included — any member
firectl usage-limits group list

# View a single group's assignment — any member
firectl usage-limits group get platform-team

# Assign a group limit to a group — admin only
firectl usage-limits group set platform-team --group-usage-limit-tier=contractors

# Clear the assignment, so the group contributes no cap — admin only
firectl usage-limits group unset platform-team
```

Every command takes either a bare ID or a full resource name, so `firectl usage-limits group set accounts/my-account/groups/platform-team --group-usage-limit-tier=accounts/my-account/groupUsageLimitTiers/contractors` is equivalent to the short form above.

### Per-user

```bash theme={null}
# List every user with their usage, effective limit, and override — admin only
firectl usage-limits user list

# View a single user — admin, or that user viewing their own
firectl usage-limits user get <USER_ID>

# Give a user their own cap, overriding groups and the account default — admin only
firectl usage-limits user set <USER_ID> --limit=500

# Remove a user's override, reverting them to their group cap or the account default — admin only
firectl usage-limits user unset <USER_ID>
```

A user record shows:

* **used** — current-period spend
* **effective\_limit** — the limit applied to them, per the [precedence rules](#limit-precedence)
* **limit\_source** — which rule produced it: `USER_OVERRIDE`, `GROUP_ASSIGNMENT`, or `ACCOUNT_DEFAULT`
* **limit\_groups** — for a group-derived cap, the groups sitting at that amount (several groups can share one cap)
* **override** — their per-user override, if any
* **exceeded\_until** — set only when the user is currently blocked; shows when the block lifts (the end of the current billing period)

An override wins outright, so it is also how you lower a single user below their group's limit. Unsetting it resolves the user to their group cap if they have one and the account default otherwise; the account-wide default itself cannot be cleared.

## Using the REST API

Writes are `PATCH` (or `POST` to create a group limit). The examples below pass `updateMask` explicitly, using the proto field names; if you omit it, the mask is derived from the fields present in your request body.

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

# The account's group limits — any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers

# Every group's limit assignment — any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimits

# One group's limit assignment — any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/usageLimits
```

### Define a group limit (admin only)

Amounts use [`google.type.Money`](https://github.com/googleapis/googleapis/blob/master/google/type/money.proto): `currencyCode` must be `USD`, and `units` is whole dollars.

```bash theme={null}
curl -X POST \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers?groupUsageLimitTierId=contractors" \
  -d '{
    "displayName": "Contractors",
    "limit": {"currencyCode": "USD", "units": "100"}
  }'
```

```bash theme={null}
# Re-price the group limit — moves the cap for every group assigned to it
curl -X PATCH \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers/contractors?updateMask=limit" \
  -d '{"limit": {"currencyCode": "USD", "units": "250"}}'
```

```bash theme={null}
# Delete the group limit — rejected while any group is still assigned to it
curl -X DELETE -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers/contractors
```

### Assign a group limit to a group (admin only)

Assigning and clearing are both updates of the group's usage-limits singleton — there is no create or delete.

```bash theme={null}
# Assign
curl -X PATCH \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/usageLimits?updateMask=group_usage_limit_tier" \
  -d '{"groupUsageLimitTier": "accounts/<ACCOUNT_ID>/groupUsageLimitTiers/contractors"}'

# Clear — an empty value removes the group's cap
curl -X PATCH \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/usageLimits?updateMask=group_usage_limit_tier" \
  -d '{"groupUsageLimitTier": ""}'
```

### Other updates (admin only)

* `PATCH /v1/accounts/<ACCOUNT_ID>/usageLimits` — update `default_user_limit` (cannot be cleared)
* `PATCH /v1/accounts/<ACCOUNT_ID>/users/<USER_ID>/usageLimits` — set `limit_override` (an unset value removes the override)

## How enforcement works

* **A user who reaches their effective limit is blocked** from further serverless requests until the billing period resets. Blocked requests receive **HTTP 402**.
* **Limits are per billing period.** Usage and any blocks reset when the period rolls over.
* **Enforcement is near-real-time, not instantaneous.** After a user crosses their limit there is a short delay (typically a few minutes) before requests start being blocked, and a similar delay before a user is unblocked after you raise their limit. Plan around this lag rather than expecting an immediate cutoff.
* **The same lag applies to group changes.** Re-pricing a group limit, reassigning a group, or a directory sync that changes someone's membership takes effect on the next enforcement pass, not on the next request.
* **A `$0` cap** — whether from a group limit, an override, or the account default — means the user is allowed no serverless spend and is blocked immediately.
* **Enforcement is account-wide.** Reaching a cap blocks the user whether the cap came from a group limit, an override, or the account default.
* Only **serverless (per-token) inference on [supported models](#supported-models)** counts toward these limits. **[MiniMax M2.7](https://app.fireworks.ai/models/fireworks/minimax-m2p7)** is excluded. Dedicated deployment (GPU-hour) usage is not metered per user here.

## FAQ

<AccordionGroup>
  <Accordion title="What counts toward a user's limit?">
    Serverless per-token inference spend in the current billing period.
  </Accordion>

  <Accordion title="What does a blocked user see?">
    Their serverless requests return HTTP `402` until the billing period resets or their limit is raised.
  </Accordion>

  <Accordion title="A user is in two groups with different limits. Which applies?">
    The **higher** of the two caps. If that isn't what you want for a particular
    person, give them a per-user override — an override outranks every group cap.
  </Accordion>

  <Accordion title="Does a group limit below the account default still apply?">
    Yes. A group cap replaces the account default for that group's members, so a
    restrictive group limit lowers them rather than being ignored.
  </Accordion>

  <Accordion title="Can I use group limits without SCIM?">
    No. Groups are provisioned only through SCIM group sync, so a group limit has
    nothing to attach to until your directory is connected. Until then, use the
    account default cap and per-user overrides.
  </Accordion>

  <Accordion title="Why was my group limit rejected?">
    Most likely the amount duplicates an existing group limit — each must hold
    a distinct amount — or the account already has the maximum of 9. Reuse or
    delete one and retry.
  </Accordion>

  <Accordion title="What happens to a group's members when I remove its limit?">
    Clearing a group's assignment (or deleting a limit option in the web app,
    which clears the assignments for you) drops that group's contribution, and
    its members fall back to another of their groups or to the account default.
  </Accordion>

  <Accordion title="What does an approved increase request do to a group cap?">
    Approving a request writes a per-user override at the requested amount, so
    that user's cap no longer follows their groups.
  </Accordion>

  <Accordion title="Can a user check their own usage?">
    Yes — a user can read their own usage and limit; they just can't see other
    users' limits or change any limits.
  </Accordion>

  <Accordion title="Do limits carry over between periods?">
    No. Usage and blocks reset each billing period.
  </Accordion>
</AccordionGroup>
