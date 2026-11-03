---
title: "Spend Limits"
source: https://docs.fireworks.ai/nexus/usage-limits
path: nexus/usage-limits
---

Set account, group, and user-specific spend limits to cap per-user spend on supported Fireworks serverless models.

Set limits on the [User Limits](#manage-limits-and-monitor-spend) page under **Settings**.

* Spend limits are part of [Nexus Enterprise](/nexus/plans).
* Only admins can change limits.
* Group limits also require [SCIM group sync](/accounts/sso#group-provisioning).

- Fireworks counts a user's spend on supported models toward that user's effective limit across the account.

## Set defaults, group limits, and exceptions

| Control | Use it for |
| - | - |
| **Account default** | The per-user ceiling for anyone without a group limit or user override |
| **Group limit** | A reusable per-user ceiling for SCIM-synced teams |
| **User override** | An exception for one person |

![Setting a custom usage limit for one user](https://mintcdn.com/fireworksai/3Wytiu2ff7ypB2uB/images/usage-limits/override-user-limit.gif?s=2a632a07599097895d6746764c74f198)

* Nexus accounts receive a \$100 account default when limits are provisioned. Other accounts have no default until an admin sets one.

### Limit precedence

When a user has more than one limit, the first match wins:

1. Their **user override**.
2. The **highest** of their groups' limits. A group limit below the account default still wins.
3. The **account default**.

* A group cap replaces the account default, which is why a lower group limit still wins.
* A user with no override, no group limit, and no account default has no cap.
* Use a per-user override when someone needs a cap their groups don't give them. An override wins outright, so it is also how you lower one user below their group's limit.
* Unsetting an override resolves the limit again: the highest assigned group cap, then the account default, or no cap if neither exists.

## Group limits

A group limit caps each member, not the group. On a $500 group limit, each member can spend up to $500.

Groups come from your identity provider through [group provisioning](/accounts/sso#group-provisioning). Manage groups and members in your directory. In Fireworks, you only assign each group a limit.

* A group limit does not create a shared group budget. The User Limits page calls these **limit options**. `firectl` and the REST API call the resource a *group usage limit tier*.
* You cannot create a group any other way. Groups and their members are read-only in Fireworks, so add, rename, delete, and populate them in your directory.

| Constraint | Behavior |
| - | - |
| **Maximum** | An account can define at most **9 group limits**. The User Limits page shows 10 slots because the account default occupies one |
| **Distinct amounts** | Each group limit must use a different amount. A group limit may equal the account default |
| **Valid amounts** | Amounts must be non-negative USD values. A **\$0** limit blocks serverless spend after enforcement refreshes |
| **Scope** | A group limit stores an amount only. Each user still resolves to one effective limit |
| **Unassigned groups** | An unassigned group contributes no cap. Its members fall back to another assigned group or the account default |
| **Deletion** | `firectl` and the REST API reject deletion while groups remain assigned. The User Limits page reassigns those groups to the account default |

## Supported models

Limits apply to serverless models in the account's metering configuration. Dedicated deployments aren't included.

* All amounts are in USD.
* Usage resets at the start of each billing period.

## Manage limits and monitor spend

The User Limits page shows each user's current-period spend, effective limit, and where that limit comes from. Admins set the account default, group limits, and user overrides there.

If an admin approves an increase request above a user's current limit, Fireworks creates a user override at that amount. Approval never lowers a limit.

## What happens when a user reaches the limit

Requests to supported serverless models return HTTP `402` until an admin raises the limit or the billing period resets. Changes take effect within 1–2 minutes.

Enforcement refreshes about once per minute. Blocking, unblocking, cap changes, group assignments, and directory membership changes can take 1–2 minutes.

| Condition | Result |
| - | - |
| **A user reaches their effective limit** | Further requests to supported serverless models return HTTP `402` |
| **The billing period resets** | Current-period usage and blocks reset |
| **A cap is set to `$0`** | The user can make no supported serverless spend after enforcement refreshes |
| **A limit or group membership changes** | The change takes effect during the next enforcement refresh |
| **A productivity-only account is still being created and has no default** | Serverless requests return HTTP `412` until provisioning creates the \$100 default |

### Permissions

| Action | Account admin | Member |
| - | -: | -: |
| View account-level limits and group assignments | Yes | Yes |
| View own usage and effective limit | Yes | Yes |
| View every user's usage and limits | Yes | No |
| List all users | Yes | No |
| Change defaults, group limits, assignments, or overrides | Yes | No |

The commands below identify any narrower permissions for individual records.

## Using `firectl`

`firectl` is the older interface for spend limits and remains supported for existing scripts. For new setups, use the User Limits page in Nexus settings.

| Task | Command |
| - | - |
| Set the account default | `firectl usage-limits update --default-user-limit=200` |
| Define a group limit | `firectl usage-limits group-tier create contractors --limit=100` |
| Assign it to a group | `firectl usage-limits group set platform-team --group-usage-limit-tier=contractors` |
| Override one user | `firectl usage-limits user set <USER_ID> --limit=500` |
| List users and spend | `firectl usage-limits user list` |

Every command accepts either a bare ID or a full resource name. For example, this is equivalent to the short form:

```bash wrap theme={null}
firectl usage-limits group set accounts/my-account/groups/platform-team \
  --group-usage-limit-tier=accounts/my-account/groupUsageLimitTiers/contractors
```

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

| Field | Meaning |
| - | - |
| `used` | Current-period spend |
| `effective_limit` | The cap selected by the [precedence rules](#limit-precedence) |
| `limit_source` | `USER_OVERRIDE`, `GROUP_ASSIGNMENT`, or `ACCOUNT_DEFAULT` |
| `limit_groups` | For a group-derived cap, the groups assigned at the winning amount |
| `override` | The user's per-user override, if set |
| `exceeded_until` | When the current block ends. Present only while the user is blocked |

Account admins cannot clear the account default.

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
