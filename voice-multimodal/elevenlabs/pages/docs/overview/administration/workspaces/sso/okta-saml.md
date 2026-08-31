---
title: "Okta SAML SSO"
source: https://elevenlabs.io/docs/overview/administration/workspaces/sso/okta-saml.md
path: docs/overview/administration/workspaces/sso/okta-saml
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Okta SAML SSO

Okta SAML SSO lets workspace members sign in to ElevenLabs through an Okta SAML 2.0 app integration.

SSO is available for Enterprise workspaces. Only Workspace admins can configure SSO settings.

ElevenLabs supports Service Provider (SP) initiated SAML SSO. To start sign-in, use
`https://elevenlabs.io/app/sign-in?use_sso=true`. You can add `email=user@example.com` as a query
parameter to prefill the email field.

## Prerequisites

* An Enterprise ElevenLabs workspace.
* Workspace admin access in ElevenLabs.
* Admin access in Okta.
* A verified email domain in ElevenLabs for the users who will sign in through Okta.

## Set up Okta SAML SSO

#### Open SSO settings in ElevenLabs

Go to **Workspace settings** > **Security & SSO**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3bc083c160206a93cce639948b66d9aefdacfc7ed238d60548d1bde2ae365479/assets/images/okta-saml-workspace-security-sso.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=b02109c7c0829f2250e674ce5096f952e3c77ee70c53b3523bbe85a321edddd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Workspace settings Security and SSO tab" />

#### Select SAML as the SSO provider

In **SSO Provider**, select **SAML**. Copy the **Service Provider Entity Id** and **Redirect
URL** values. You will use these values in Okta.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/299948b19e628c531333c21ced70086b975d926f834b0f8a55e13edbd5898303/assets/images/okta-saml-elevenlabs-provider-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=88f6e24229c3035b908c16d40284d45fd7e2c329269df79cbeccff382c5df82e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs SAML provider settings" />

#### Create an Okta app integration

In the Okta Admin Console, go to **Applications** > **Applications**, then click **Create App
Integration**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ed1e7575d777d053d3749efc7f0a31ebfdf19a5f37de5f266ea147b26e4a2487/assets/images/okta-saml-okta-applications.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=d0cd961ecc1d1708f2088e0871d5cdf1bbc323c6a27be69e47af332dc109154f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta Applications page with Create App Integration" />

Select **SAML 2.0**, then click **Next**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/89e194f26b79f20c6e34af660802266901dd96464987be2f38ea41c7d338704b/assets/images/okta-saml-create-app-integration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=66c1443ce7eb3176b7b0553d2daac472d002e4a3add351139e0bd5a2cd154e22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta Create a new app integration dialog with SAML 2.0 selected" />

#### Add the app name

In **General Settings**, set **App name** to `ElevenLabs`, then click **Next**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/56ed422543674b8b81608e27e585faf71fdca05d28ceb1493aef5d5d3c256722/assets/images/okta-saml-general-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=6316b578606249ab295b2c9932da1698e5ba337ea7a05969cd1a460dc7dd0d4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta Create SAML Integration general settings" />

#### Configure SAML settings in Okta

In **SAML Settings**, configure the app with the values from ElevenLabs:

* Set **Single sign-on URL** to the ElevenLabs **Redirect URL**.
* Select **Use this for Recipient URL and Destination URL**.
* Set **Audience URI (SP Entity ID)** to the ElevenLabs **Service Provider Entity Id**.
* Set **Name ID format** to **EmailAddress**.
* Set **Application username** to **Email**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/45c4621749048612f9dcaa96123b07b60e661f3a84c03c654a0e229dce385ad6/assets/images/okta-saml-configure-saml.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=4e9316a5a94c903d000bd877c748f7ce42f6f163dd2f3f647dd4b6841231e108&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta SAML settings for ElevenLabs" />

#### Assign users or groups

Open the Okta app's **Assignments** tab and assign the users or groups that should be able to
sign in to ElevenLabs.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3cf08aff22d992d143bfb1c655f3a807c5b2b6b5cafba4ee2aff6e18bd997676/assets/images/okta-saml-assignments.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=754dfbba6271ae2dc566995b950fa31442abcb56b8e3a811f4cbb93fe1e04462&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta app Assignments tab" />

#### Add the Okta certificate to ElevenLabs

In Okta, open **SAML Signing Certificates** and use **Actions** > **Download certificate** for
the active certificate.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/334a3a8fb4355a170254e0dd132b141fd9f6a86dd58374d054ae1a708a8778f9/assets/images/okta-saml-download-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=6bbe22429dbd99fed7847b88a001b9f5d27ba35360440c8c2d804a13bfb18047&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta SAML Signing Certificates download certificate action" />

Open the certificate file and copy the full PEM certificate, including
`-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d62e28cf4ff1d3240d190cc9405345e193177e533b185acd64b19ab7f77596c5/assets/images/okta-saml-copy-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=5f61f0cbc837df9e9be4148dc55fa3c90351ca056dcc0180fcb05f6d2ad07a68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta certificate file in PEM format" />

In ElevenLabs, click **Add Certificate**, paste the Okta certificate, then click **Add**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/910152284bd98c1ebdae064a7424d7d1ac185fe716abdda751607bad9b4cc147/assets/images/okta-saml-add-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=de605585ab8566985f3f0029594f802dc069ef294566eca1b749507d770649de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Add X509 Certificate dialog" />

#### Copy Okta metadata values into ElevenLabs

In Okta, open the IdP metadata XML. Copy the metadata values into ElevenLabs:

* Use `entityID` for **Identity Provider Entity Id**.
* Use the `SingleSignOnService Location` URL that ends in `/sso/saml` for **Identity Provider
  Sign-In URL**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/96f8ad35da0fbeafc265310e0ca761c69163cb53c76baf8d35c97e9a992d4ee8/assets/images/okta-saml-idp-metadata.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=d1f956bdc0815922eca2ffefdde1ee0c2b192a82386c7955381af897588ef477&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta IdP metadata XML showing entityID and SingleSignOnService Location" />

#### Add your allowed email domain

In ElevenLabs, click **Add Domain** and select the verified domain that matches the email
domain of your Okta users.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bd532d18051c43e9db7c3b33e54b5910a2050ec16e04e85c9b7541fda20f7b6f/assets/images/okta-saml-add-domain.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260831T100015Z&X-Amz-Expires=604800&X-Amz-Signature=a3dbe4a977ecc8059daced2523c620a16ff60d37527606cccc1ab8ecc9aa5c6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Add allowed email domains dialog" />

#### Save the SSO provider

Review the configuration, select **I acknowledge this change will log out users currently using
SSO**, then click **Update SSO**.

## Field mappings

Use this table to map Okta SAML settings to ElevenLabs SSO fields.

| Okta field or location                                     | ElevenLabs field                  | Value to use                                                                  |
| ---------------------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------- |
| **Sign-in method**                                         | **SSO Provider**                  | `SAML`                                                                        |
| **Audience URI (SP Entity ID)**                            | **Service Provider Entity Id**    | Use the ElevenLabs value, for example `https://elevenlabs.io`                 |
| **Single sign-on URL**                                     | **Redirect URL**                  | Use the ElevenLabs value, for example `https://elevenlabs.io/__/auth/handler` |
| **Recipient URL**                                          | **Redirect URL**                  | Same as **Single sign-on URL**                                                |
| **Destination URL**                                        | **Redirect URL**                  | Same as **Single sign-on URL**                                                |
| **SAML Issuer ID** or metadata `entityID`                  | **Identity Provider Entity Id**   | Okta issuer, for example `http://www.okta.com/exk...`                         |
| **Sign On URL** or metadata `SingleSignOnService Location` | **Identity Provider Sign-In URL** | Okta SAML URL ending in `/sso/saml`                                           |
| **X.509 Certificate** or metadata `ds:X509Certificate`     | **Certificate**                   | Okta signing certificate in valid PEM format                                  |
| **Application username**                                   | No manual config required         | Set to **Email**                                                              |
| **Name ID format**                                         | No manual config required         | Set to **EmailAddress**                                                       |
| User or app email domain in Okta                           | **Domain**                        | Must match a verified ElevenLabs domain, for example `company.com`            |

## Troubleshooting

#### Okta shows a successful sign-in, but ElevenLabs says unable to sign in

Check the browser Network response for `accounts:signInWithIdp`. Okta System Log entries such as
`User single sign on to app SUCCESS` only confirm that Okta authenticated the user. ElevenLabs
can still reject the SAML response if the assertion values do not match the SSO configuration.

#### INVALID\_IDP\_RESPONSE: Error when parsing certificate

The browser Network response may show `INVALID_IDP_RESPONSE: Error when parsing certificate`.
Remove the certificate from ElevenLabs, then re-add the Okta X.509 certificate in valid PEM
format. Do not use an LLM to format the certificate. Copy the certificate exactly, including
`-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.

#### User or authentication mismatch errors

Make sure Okta sends the user's email address as `NameID`. In Okta, set **Name ID format** to
**EmailAddress** and **Application username** to **Email**.

#### Which Okta metadata values should I use?

Use metadata `entityID` for **Identity Provider Entity Id**, `SingleSignOnService Location` for
**Identity Provider Sign-In URL**, and `ds:X509Certificate` for **Certificate**.
