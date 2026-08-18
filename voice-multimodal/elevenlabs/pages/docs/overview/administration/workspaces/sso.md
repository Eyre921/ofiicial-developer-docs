---
title: "Single Sign-On (SSO)"
source: https://elevenlabs.io/docs/overview/administration/workspaces/sso.md
path: docs/overview/administration/workspaces/sso
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Single Sign-On (SSO)

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e1575b62be17ed4dbd459539161c7853f9f3e000c8d2eeba01f40e1335d7dad0/assets/images/product-guides/workspaces/workspace-sso.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260818%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260818T113155Z&X-Amz-Expires=604800&X-Amz-Signature=7315f27e80db1ba949dcea607ef7c33b85134cfd2d203423abea87a71f62e170&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="SSO" />

## Overview

SSO is currently only available for Enterprise customers, and only Workspace admins can enable
this feature. To upgrade, [get in touch with our sales team](https://elevenlabs.io/contact-sales).

Single Sign-On (SSO) allows your team to log in to ElevenLabs by using your existing identity provider. This allows your team to use the same credentials they use for other services to log in to ElevenLabs.

## Guide

#### Access your SSO settings

Click on your profile icon located in the top right corner of the dashboard, select **Workspace settings**, and then navigate to the **Security & SSO** tab.

#### Choose identity providers

You can choose from a variety of pre-configured identity providers, including Google, Apple, GitHub, etc. Custom organization SSO providers will only appear in this list after they have been configured, as shown in the "SSO Provider" section.

#### Verify your email domain

Next, you need to verify your email domain for authentication. This lets ElevenLabs know that you own the domain you are configuring for SSO. This is a security measure to prevent unauthorized access to your Workspace.

Click the **Verify domain** button and enter the domain name you want to verify. After completing this step, click on the domain pending verification. You will be prompted to add a DNS TXT record to your domain's DNS settings. Once the DNS record has been added, click on the **Verify** button.

#### Configure SSO

If you want to configure your own SSO provider, select the SSO provider dropdown to select between OIDC (OpenID Connect) and SAML (Security Assertion Markup Language).

**Important:** We do <b>not</b> recommend using Microsoft Entra (formerly Azure AD) with OIDC for SSO. For best compatibility and support, use SAML when integrating with Entra/Azure.

Only Service Provider (SP) initiated SSO is supported for SAML. To ease the sign in process, you can create a bookmark app in your SSO provider linking to [https://elevenlabs.io/app/sign-in?use\_sso=true](https://elevenlabs.io/app/sign-in?use_sso=true). You can include the user's email as an additional query parameter to pre-fill the field. For example [https://elevenlabs.io/app/sign-in?use\_sso=true\&email=test@test.com](https://elevenlabs.io/app/sign-in?use_sso=true\&email=test@test.com)

Once you've filled out the required fields, click the **Update SSO** button to save your changes.

Configuring a new SSO provider will log out all Workspace members currently logged in with SSO.

## SCIM

SCIM is available for Enterprise workspaces, configurable by Workspace admins.

#### [SCIM](/docs/overview/administration/workspaces/sso/scim)

SCIM (System for Cross-domain Identity Management) allows your Identity Provider (IdP) to
automatically manage users and groups in your ElevenLabs workspace.

## FAQ

#### Microsoft Entra / Azure AD - SAML

For Microsoft Entra-specific setup steps, field mappings, and troubleshooting notes, see
[Microsoft Entra SAML SSO](/docs/overview/administration/workspaces/sso/microsoft-entra-saml).

#### Okta - SAML

For Okta-specific setup steps, field mappings, and troubleshooting notes, see
[Okta SAML SSO](/docs/overview/administration/workspaces/sso/okta-saml).

#### OneLogin - SAML

**What to fill in on the OneLogin side**:

* **Recipient**: Use `https://elevenlabs.io/__/auth/handler`
  * For [data residency](/docs/overview/administration/data-residency) environments, use `https://<region>.residency.elevenlabs.io/__/auth/handler`, replacing `<region>` with your region code.

#### OIDC - Common Errors

Please ensure that `email` and `email_verified` are included in the custom attributes returned in the OIDC response. Without these, the following errors may be hit:

* *No email address was received*: Fixed by adding **email** to the response.
* *Account exists with different credentials*: Fixed by adding **email\_verified** to the response

#### I am getting the error 'Unable to login with saml.workspace...'

* One known error: Inside the `<saml:Subject>` field of the SAML response, make sure `<saml:NameID>` is set to the email address of the user.
