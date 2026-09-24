---
title: "Spend Limits Reference"
source: https://docs.fireworks.ai/nexus/usage-limits-reference
path: nexus/usage-limits-reference
---

Group precedence, supported models, firectl, and REST API details for per-user spend limits.

Use [Spend Limits](/nexus/usage-limits) to set caps in the User Limits page. This reference covers precedence, group rules, supported models, `firectl`, and the REST API.

<Note>
  Per-user usage limits are available on request. Reach out to your Fireworks
  contact to enable them. Group limits additionally require [SCIM group
  sync](/accounts/sso#group-provisioning). Limit changes are admin-only.
</Note>

## Limit types

| Term                     | Meaning                                                                                                                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Account default cap**  | The per-user limit for anyone with no user override or group cap. Productivity-only accounts receive a **\$100** default when Fireworks enables usage limits unless an admin changes it. Other accounts have no default until an admin sets one |
| **Group limit**          | A reusable cap assigned to one or more [groups](#group-limits). The User Limits page calls these **limit options**                                                                                                                              |
| **Per-user override**    | A cap set for one user                                                                                                                                                                                                                          |
| **Effective limit**      | The cap applied after resolving [precedence](#limit-precedence)                                                                                                                                                                                 |
| **Current-period usage** | The amount a user, or the account overall, has spent during the current billing period                                                                                                                                                          |

All amounts are in USD. Usage resets at the start of each billing period.

### Limit precedence

A user's effective limit is resolved in this order:

1. Their **per-user override**, if they have one.
2. Otherwise, the **highest** cap among the group limits assigned to their groups. A group limit *below* the account default still wins: a group cap replaces the default rather than competing with it.
3. Otherwise, the **account default cap**.

A user with no override, no group limit, and no account default has no cap. Use a per-user override when someone needs a cap their group membership won't produce.

## Group limits

A group limit is a reusable per-user cap. It does not create a shared group budget.

<Note>
  On a $500 group limit, each member can spend up to $500. The members do not share \$500.
</Note>

`firectl` and the REST API call this resource a *group usage limit tier*.

### Where groups come from

Groups come from your identity provider through the group provisioning described in [Custom SSO](/accounts/sso#group-provisioning); that is the only way to create one. Groups and their membership are read-only in Fireworks; add, rename, delete, and populate them in your directory. The limit assignment is the one part you set in Fireworks.

### Group-limit constraints

| Constraint            | Behavior                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Maximum**           | An account can define at most **9 group limits**. The User Limits page shows 10 slots because the account default occupies one              |
| **Distinct amounts**  | Each group limit must use a different amount. A group limit may equal the account default                                                   |
| **Valid amounts**     | Amounts must be non-negative USD values. A **\$0** limit blocks serverless spend after enforcement refreshes                                |
| **Scope**             | A group limit stores an amount only. Each user still resolves to one effective limit                                                        |
| **Unassigned groups** | An unassigned group contributes no cap. Its members fall back to another assigned group or the account default                              |
| **Deletion**          | `firectl` and the REST API reject deletion while groups remain assigned. The User Limits page reassigns those groups to the account default |

## Supported models

Per-user metering applies to serverless models included in the account's metering configuration. Dedicated deployments are not included.

## Permissions

| Action                                                   | Account admin | Member |
| -------------------------------------------------------- | ------------: | -----: |
| View account-level limits and group assignments          |           Yes |    Yes |
| View own usage and effective limit                       |           Yes |    Yes |
| View every user's usage and limits                       |           Yes |     No |
| List all users                                           |           Yes |     No |
| Change defaults, group limits, assignments, or overrides |           Yes |     No |

The commands below identify any narrower permissions for individual records.

## Using `firectl`

### Account-level

```bash wrap theme={null}
# View the account default cap and account-wide usage: any member
firectl usage-limits get

# Update the default per-user cap: admin only
firectl usage-limits update --default-user-limit=200
```

### Defining group limits

```bash wrap theme={null}
# List the account's group limits: any member
firectl usage-limits group-tier list

# Define a group limit: admin only
firectl usage-limits group-tier create contractors --limit=100 --display-name="Contractors"

# View one group limit: any member
firectl usage-limits group-tier get contractors

# Update this limit for every assigned group: admin only
firectl usage-limits group-tier update contractors --limit=250

# Rename it: admin only
firectl usage-limits group-tier update contractors --display-name="Contractors (2026)"

# Delete it: admin only, and only once no group is assigned
firectl usage-limits group-tier delete contractors
```

### Group assignments

```bash wrap theme={null}
# List every group's limit assignment, unassigned groups included: any member
firectl usage-limits group list

# View a single group's assignment: any member
firectl usage-limits group get platform-team

# Assign a group limit to a group: admin only
firectl usage-limits group set platform-team --group-usage-limit-tier=contractors

# Clear the assignment, so the group contributes no cap: admin only
firectl usage-limits group unset platform-team
```

<Note>
  Every command accepts either a bare ID or a full resource name. For example:

  ```bash wrap theme={null}
  firectl usage-limits group set accounts/my-account/groups/platform-team \
    --group-usage-limit-tier=accounts/my-account/groupUsageLimitTiers/contractors
  ```

  This is equivalent to the short form above.
</Note>

### Per-user

```bash wrap theme={null}
# List every user with their usage, effective limit, and override: admin only
firectl usage-limits user list

# View a single user: admin, or that user viewing their own
firectl usage-limits user get <USER_ID>

# Give a user their own cap, overriding groups and the account default: admin only
firectl usage-limits user set <USER_ID> --limit=500

# Remove a user's override, reverting them to their group cap or the account default: admin only
firectl usage-limits user unset <USER_ID>
```

A user record contains:

| Field             | Meaning                                                             |
| ----------------- | ------------------------------------------------------------------- |
| `used`            | Current-period spend                                                |
| `effective_limit` | The cap selected by the [precedence rules](#limit-precedence)       |
| `limit_source`    | `USER_OVERRIDE`, `GROUP_ASSIGNMENT`, or `ACCOUNT_DEFAULT`           |
| `limit_groups`    | For a group-derived cap, the groups assigned at the winning amount  |
| `override`        | The user's per-user override, if set                                |
| `exceeded_until`  | When the current block ends. Present only while the user is blocked |

An override wins outright, so it is also how you lower a single user below their group's limit. Unsetting it resolves the limit again: the highest assigned group cap, then the account default, or no cap if neither exists. Account admins cannot clear the account default.

## Using the REST API

Create requests use `POST`, updates use `PATCH`, and deletions use `DELETE`. The update examples below pass `updateMask` explicitly using field names from the API schema. If you omit it, the mask is derived from the fields in your request body.

### Read limits

```bash wrap theme={null}
# Account-level usage limits: any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/usageLimits

# A single user's usage limits: admin, or that user
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/users/<USER_ID>/usageLimits

# All users in the account: admin only
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/userUsageLimits

# The account's group limits: any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers

# Every group's limit assignment: any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimits

# One group's limit assignment: any member
curl -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/usageLimits
```

### Manage group limits (admin only)

Group-limit create and update requests use [`google.type.Money`](https://github.com/googleapis/googleapis/blob/master/google/type/money.proto). Set `currencyCode` to `USD`; `units` contains whole dollars.

```bash wrap theme={null}
curl -X POST \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers?groupUsageLimitTierId=contractors" \
  -d '{
    "displayName": "Contractors",
    "limit": {"currencyCode": "USD", "units": "100"}
  }'
```

```bash wrap theme={null}
# Update the limit: changes the cap for every assigned group
curl -X PATCH \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers/contractors?updateMask=limit" \
  -d '{"limit": {"currencyCode": "USD", "units": "250"}}'
```

```bash wrap theme={null}
# Delete the group limit: rejected while any group is still assigned to it
curl -X DELETE -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groupUsageLimitTiers/contractors
```

### Assign a group limit to a group (admin only)

Assigning and clearing are both updates of the group's usage-limits resource; there is no create or delete.

```bash wrap theme={null}
# Assign
curl -X PATCH \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/usageLimits?updateMask=group_usage_limit_tier" \
  -d '{"groupUsageLimitTier": "accounts/<ACCOUNT_ID>/groupUsageLimitTiers/contractors"}'

# Clear: an empty value removes the group's cap
curl -X PATCH \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  "https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/groups/<GROUP_ID>/usageLimits?updateMask=group_usage_limit_tier" \
  -d '{"groupUsageLimitTier": ""}'
```

### Update account and user limits (admin only)

* `PATCH /v1/accounts/<ACCOUNT_ID>/usageLimits` to update `default_user_limit` (account admins cannot clear it)
* `PATCH /v1/accounts/<ACCOUNT_ID>/users/<USER_ID>/usageLimits` to set `limit_override` (an unset value removes the override)

## Enforcement behavior

| Condition                                                                 | Result                                                                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **A user reaches their effective limit**                                  | Further requests to supported serverless models return HTTP `402` until the limit is raised or the billing period resets |
| **The billing period resets**                                             | Current-period usage and blocks reset                                                                                    |
| **A cap is set to `$0`**                                                  | The user can make no supported serverless spend after enforcement refreshes                                              |
| **A limit or group membership changes**                                   | The change takes effect during the next enforcement refresh                                                              |
| **A productivity-only account is still being created and has no default** | Serverless requests return HTTP `412` until provisioning creates the \$100 default                                       |

Enforcement refreshes about once per minute. Blocking, unblocking, cap changes, group assignments, and directory membership changes can therefore take 1–2 minutes.

Limits count a user's supported serverless usage across the account. Dedicated deployment usage is not included.

## Approved increase requests

If an admin approves an amount above the user's current effective limit, Fireworks creates a per-user override at that amount. Approval never lowers the user's effective limit.
