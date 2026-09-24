---
title: "Single Sign-On (SSO)"
source: https://elevenlabs.io/docs/overview/administration/workspaces/sso.md
path: docs/overview/administration/workspaces/sso
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Single Sign-On (SSO)

## Overview

> **Info**
>
> SSO is available for **Enterprise** customers only. Only Workspace admins can enable this feature.
> To upgrade, [get in touch with our sales team](https://elevenlabs.io/contact-sales).

Single Sign-On (SSO) allows your team to sign in to ElevenLabs using your existing identity
provider (IdP). ElevenLabs supports **SAML 2.0** and **OIDC** for enterprise SSO, and
Service Provider (SP) initiated sign-in.

Before enabling SSO, you must verify your email domain. Workspace members sign in with the same
email domain that is verified and associated with your SSO configuration.

## Set up SSO

#### Open Security & SSO settings

Go to **Workspace settings** > **Security & SSO**.

#### Restrict sign-in methods (optional)

Under **Allowed Identity Providers**, you can restrict which sign-in methods workspace members
may use — for example, limiting sign-in to your enterprise SSO provider only and disabling
social providers such as Google, Apple, and GitHub.

By default, all providers are enabled. Changes take effect immediately.

#### Verify your email domain

Under **User Auto Provisioning**, verify the email domain your users will sign in with. This
proves ownership of the domain and is required before you can associate it with an SSO
provider.

Add a DNS TXT record to your domain's DNS settings with the verification code shown, then click
**Verify**. You can also enable auto-provisioning so users with a matching email domain are
automatically added to your workspace when they sign up.

#### Configure your SSO provider

Under **SSO Provider**, select your protocol:

* **SAML** — use with Okta, Microsoft Entra, OneLogin, and other SAML 2.0 identity providers.
* **OIDC** (OpenID Connect) — use with providers that support OIDC.

> **Warning**
>
> Microsoft Entra (formerly Azure AD) is only supported through SAML. Do not use OIDC with
> Entra — it can cause sign-in failures.

> **Info**
>
> Only SP-initiated SSO is supported for SAML. To simplify sign-in, create a bookmark app in
> your IdP that links to `https://elevenlabs.io/app/sign-in?use_sso=true`. You can include the
> user email as a query parameter to pre-fill it:
> `https://elevenlabs.io/app/sign-in?use_sso=true&email=user@company.com`

Fill in the required fields for your provider (entity ID, sign-in URL, certificate), then
click **Update SSO**.

> **Warning**
>
> Saving a new SSO provider configuration will immediately log out all workspace members
> currently signed in with SSO.

#### Add your verified domain

After saving the SSO provider configuration, click **Add Domain** and select the verified
domain that matches your users' email addresses. Only verified domains appear in this list.

For provider-specific field mappings and screenshots, see the guides below.

#### [Microsoft Entra SAML](/docs/overview/administration/workspaces/sso/microsoft-entra-saml)

Step-by-step setup for Microsoft Entra ID (formerly Azure AD).

#### [Okta SAML](/docs/overview/administration/workspaces/sso/okta-saml)

Step-by-step setup for Okta SAML 2.0.

## SCIM

> **Info**
>
> SCIM is available for Enterprise workspaces, configurable by Workspace admins.

#### [SCIM](/docs/overview/administration/workspaces/sso/scim)

SCIM (System for Cross-domain Identity Management) allows your Identity Provider (IdP) to
automatically provision, update, and deprovision users and groups in your ElevenLabs workspace.

## FAQ

#### Microsoft Entra / Azure AD - SAML

For Microsoft Entra-specific setup steps, field mappings, and troubleshooting notes, see
[Microsoft Entra SAML SSO](/docs/overview/administration/workspaces/sso/microsoft-entra-saml).

#### Okta - SAML

For Okta-specific setup steps, field mappings, and troubleshooting notes, see
[Okta SAML SSO](/docs/overview/administration/workspaces/sso/okta-saml).

#### OneLogin - SAML

In your OneLogin app configuration, set **Recipient** to:

* `https://elevenlabs.io/__/auth/handler` for standard environments
* `https://<region>.residency.elevenlabs.io/__/auth/handler` for [data residency](/docs/overview/administration/data-residency) environments, replacing `<region>` with your region code.

Set **ACS (Consumer) URL Validator** to the same value. Set **ACS (Consumer) URL** to the
ElevenLabs **Redirect URL** shown in your SSO provider settings. Set the **SAML Initiator** to
**Service Provider** (SP-initiated only).

#### OIDC - Common Errors

Ensure that `email` and `email_verified` are included in the OIDC response claims. Without
these, the following errors may occur:

* *No email address was received* — add `email` to the response.
* *Account exists with different credentials* — add `email_verified` to the response.

#### I am getting the error 'Unable to login with saml.workspace...'

Inside the `<saml:Subject>` field of the SAML response, confirm that `<saml:NameID>` is set to
the user's email address. See the field mapping guide for your IdP for the correct attribute to
use.

#### Does ElevenLabs support IdP-initiated SSO?

No. Only Service Provider (SP) initiated SSO is supported. Users must start sign-in from the
ElevenLabs sign-in page (`https://elevenlabs.io/app/sign-in?use_sso=true`). You can create a
bookmark app in your IdP that links there for a smoother experience.
