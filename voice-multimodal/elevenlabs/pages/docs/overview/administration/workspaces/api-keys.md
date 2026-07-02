---
title: "API Keys"
source: https://elevenlabs.io/docs/overview/administration/workspaces/api-keys.md
path: docs/overview/administration/workspaces/api-keys
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# API Keys

## Overview

API keys authenticate your requests to the ElevenLabs API and track usage against your workspace's quota. There are two types:

* **User API keys** belong to an individual user and inherit that user's access to workspace resources. They are well suited to personal development and scripts. Because they are tied to a person, a user API key is affected if that user's access changes or they leave the workspace. Creating personal API keys requires a [Full Seat](/docs/overview/administration/workspaces/members#full-seats).
* **Service account API keys** belong to a [service account](/docs/overview/administration/workspaces/service-accounts) rather than an individual, so they keep working regardless of changes to individual membership. They are recommended for backend systems, automation, and production workloads. Service accounts are available to multi-seat customers and are managed by workspace admins.

**Your API key is a secret.** Do not share it with others or expose it in client-side code (browsers, apps). For details on how to send your key with a request, see the [API Authentication](/docs/api-reference/authentication) reference.

Both types of key can be restricted in several ways:

1. **Scope restriction:** limit which API endpoints the key can access.
2. **Credit quota:** set a custom credit limit to control usage.
3. **IP allowlisting:** restrict the key to specific IP addresses or CIDR ranges. See [IP allowlisting](#ip-allowlisting).

## Rotating API keys

When creating a new API key to replace one that you are rotating out, copy the permissions from
the old key to the new one so that no access is lost. For service account keys, make sure to
create the new key for the same service account.

Rotation follows the same pattern in both cases: create a new key, switch your applications over to it, then delete the old key.

**User API keys** are rotated from the dashboard. Open your [personal API keys settings](https://elevenlabs.io/app/settings/api-keys), create a new key, and delete the old one once you have switched over.

**Service account API keys** can be rotated from the dashboard or via the API:

* In the dashboard, click your profile icon in the top right corner, select **Workspace settings**, and open the **Service Accounts** tab. Create a new key for the same service account, then delete the old one once you have switched over.
* Via the API, [create a new key](/docs/api-reference/service-accounts/api-keys/create) for the same service account, then [delete the old one](/docs/api-reference/service-accounts/api-keys/delete).

## IP allowlisting

You can restrict an API key so that it only works from specific IP addresses or CIDR ranges. Requests made from any other IP will be rejected with a [`403` error](/docs/eleven-api/resources/errors).

### Supported formats

* Individual IPv4 addresses (e.g. `203.0.113.10`)
* Individual IPv6 addresses (e.g. `2001:db8::1`)
* CIDR ranges (e.g. `203.0.113.0/24`)

You can add between 1 and 100 entries per API key. Bare IP addresses are automatically normalized to `/32` (IPv4) or `/128` (IPv6).

Private IP ranges (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) are not accepted. Only
public IP addresses can be allowlisted.

## Detecting leaked keys

ElevenLabs participates in [GitHub's secret scanning partner program](https://docs.github.com/en/code-security/secret-scanning/secret-scanning-partner-program). If an ElevenLabs API key is committed to a public GitHub repository, GitHub notifies ElevenLabs and the key is automatically disabled to prevent unauthorized use.

A key disabled this way reports a `disable_reason` of `exposed_publicly`. To restore access, [rotate the key](#rotating-api-keys) and update your applications to use the new one.

Automatic disabling of leaked keys only applies when third-party disabling is allowed for the key.
See [Controlling who can disable keys](#controlling-who-can-disable-keys).

## Self-disabling a key

If you believe a key has been compromised, the holder of the key can disable it directly using the [Disable API key](/docs/api-reference/api-keys/disable) endpoint. Call it with the query parameter `api_key_name=self`, which is required as an explicit confirmation that you intend to disable the key used to authenticate the request.

## Controlling who can disable keys

The `third_party_disable_allowed` setting controls whether a key can be disabled by its holder, either through the self-disable endpoint or automatically when it leaks publicly. By default, this is enabled for non-Enterprise plans and disabled for Enterprise plans.

A notification email is sent to the workspace owner and the key's owner when a key is disabled by
a third party, either automatically through GitHub secret scanning or through the self-disable
endpoint. Disabling a key yourself in the web UI does not send a notification.

**Per key:** set `third_party_disable_allowed` when you [create](/docs/api-reference/service-accounts/api-keys/create) or [update](/docs/api-reference/service-accounts/api-keys/update) a service account API key. Omit it to use the workspace default, or pass `clear` on update to reset an individual key to the workspace default.

**Workspace-wide:** workspace admins can override every key's setting at once using the [Set workspace third-party disabling policy](/docs/api-reference/api-keys/set-third-party-disabling-policy) endpoint:

* `true` allows every key in the workspace to be disabled by its holder.
* `false` forbids it for every key.
* `null` removes the workspace-wide override, so each key's own value and the plan default apply again.
