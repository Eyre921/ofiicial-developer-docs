---
title: "Credential Protection"
source: https://upstash.com/docs/redis/features/credential-protection
path: docs/redis/features/credential-protection
---

Enabling Credential Protection ensures your database credentials are never stored within Upstash infrastructure. This enhances security by making credentials accessible only once—at the moment they are generated.

<Note>
  Credential Protection is a [Production
  Pack](/docs/redis/overall/enterprise#prod-pack-features)
  feature.
</Note>

## How It Works

When enabled:

* Redis database credentials are no longer stored in Upstash infrastructure
* Credentials are displayed only once during enablement - save them immediately
* Console features requiring database access are disabled (CLI, Data Browser, Monitor, ACL)

## Managing Credential Protection

1. Go to database details page → Configuration section
2. Toggle **Protect Credentials** switch:

  <img />

3. Save the credentials shown in the modal:

  <img />

<Warning>
  Disabling this feature will permanently revoke current credentials and
  generate new ones, potentially breaking applications using those credentials.
</Warning>

## What If You Lose Your Credentials

**Reset Credentials**: This function remains available and, when credential protection is enabled, will generate new protected credentials.

  <img />
