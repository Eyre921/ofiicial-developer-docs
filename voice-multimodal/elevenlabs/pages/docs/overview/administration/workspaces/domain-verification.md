---
title: "Domain Verification"
source: https://elevenlabs.io/docs/overview/administration/workspaces/domain-verification.md
path: docs/overview/administration/workspaces/domain-verification
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Domain Verification

Domain verification is available for **Enterprise** workspaces. Only Workspace admins can manage
domain verifications.

## Overview

Domain verification proves to ElevenLabs that your organization owns an email domain (for example, `company.com`). A verified domain is required before you can:

* Enable [Single Sign-On (SSO)](/docs/overview/administration/workspaces/sso) for that domain.
* Turn on automatic user provisioning, which adds users to your workspace automatically when they sign up with a matching email address.

Verification uses a DNS TXT record. You add a unique code to your domain's DNS configuration, and ElevenLabs checks for that record to confirm ownership.

## Prerequisites

* An Enterprise ElevenLabs workspace.
* Workspace admin access in ElevenLabs.
* Access to your domain's DNS settings.

## Add and verify a domain

#### Open Security & SSO settings

Go to **Workspace settings** > **Security & SSO**.

#### Add your domain

Under **User Auto Provisioning**, click **Verify domain** and enter the domain you want to
verify (for example, `company.com`). Subdomains are supported.

Optionally enable **Auto Provisioning** to automatically add users to your workspace when they
sign in with an email address on this domain for the first time.

Click **Continue** to generate your verification code.

#### Add the DNS TXT record

Copy the verification code shown in the dialog. In your DNS provider, add a **TXT record** to
the domain you are verifying:

| Field           | Value                                        |
| --------------- | -------------------------------------------- |
| **Type**        | `TXT`                                        |
| **Host / Name** | `@` (or the root of your domain)             |
| **Value**       | The verification code provided by ElevenLabs |

DNS changes can take up to 48 hours to propagate, although they typically apply within minutes
to a few hours.

#### Verify the domain

Return to the **Security & SSO** page. Click **Verify** next to the domain you added.
ElevenLabs will check for the TXT record.

* **Passed** — verification succeeded. The domain is now verified and can be used for SSO and
  auto-provisioning.
* **Pending** — the TXT record has not propagated yet. Wait and try again.
* **Failed** — the TXT record was not found. Check that the record is saved correctly in your
  DNS provider and try again.

## Auto-provisioning

When auto-provisioning is enabled for a verified domain, any user who signs up for ElevenLabs with
an email address on that domain is automatically added to your workspace. This removes the need to
manually invite each team member.

Auto-provisioning can be enabled or disabled at any time from the domain verification settings.

Auto-provisioning applies to new sign-ups only. Existing ElevenLabs users with a matching email
domain are not automatically added to your workspace.

## Remove a domain

You can remove a domain verification from **Security & SSO** at any time. Removing a verified
domain:

* Disables SSO for users whose email addresses match that domain if no other SSO configuration
  covers them.
* Disables auto-provisioning for that domain.
* Does not remove users who were already provisioned.

If you remove a domain and need to re-verify it later, you will receive a new verification code and
must update your DNS TXT record.

## FAQ

#### Can I verify multiple domains?

Yes. You can add and verify multiple domains for a single workspace. Each domain requires its
own TXT record.

#### Can a domain be verified by more than one workspace?

No. Each domain can only be verified by one workspace at a time. If you need a domain verified
on multiple workspaces, please contact us.

#### How long does DNS propagation take?

DNS changes typically propagate within minutes to a few hours, but can take up to 48 hours in
rare cases. If verification keeps failing, confirm the TXT record is saved correctly and wait
before retrying.

#### Do I need a verified domain before setting up SSO?

Yes. You must verify the email domain your SSO users will sign in with before you can associate
it with an SSO provider configuration. See [Single Sign-On (SSO)](/docs/overview/administration/workspaces/sso).

#### What happens to existing users if I enable auto-provisioning?

Auto-provisioning only affects new sign-ups after it is enabled. Existing users with a matching
domain who are not already workspace members are not automatically added.
