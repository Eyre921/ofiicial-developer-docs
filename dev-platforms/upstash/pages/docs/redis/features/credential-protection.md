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
* In the **Connect** section of the **Details** tab, commands and connection strings use `YOUR_PASSWORD` and `YOUR_TOKEN` placeholders, and SDK examples read the credentials from environment variables. Replace the placeholders with the credentials you saved.

## Managing Credential Protection

1. Go to the database's **Settings** tab → Configuration section
2. Toggle **Protect Credentials** switch:

  <img alt="Enable Redis credential protection" />

3. Save the credentials shown in the modal:

  <img alt="Save protected Redis credentials" />

<Note>
  When protection is enabled, the database details card shows a **Protected**
  field in place of the password and token. This field links to
  **Settings** → **Protect Credentials**.
</Note>

<Warning>
  Disabling this feature will permanently revoke current credentials and
  generate new ones, potentially breaking applications using those credentials.
</Warning>

## What If You Lose Your Credentials

**Reset Credentials**: This function remains available and, when credential protection is enabled, will generate new protected credentials.
Navigate to the settings tab of your database and click **Reset Credentials**. You will be prompted to save the new credentials.

  <img alt="Reset protected Redis credentials" />
