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

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3bc083c160206a93cce639948b66d9aefdacfc7ed238d60548d1bde2ae365479/assets/images/okta-saml-workspace-security-sso.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=69ec6f5f6bbc3ce0c060d1928bce2c712de91d2b1a89a284520fb28203a2b810&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Workspace settings Security and SSO tab" />

#### Select SAML as the SSO provider

In **SSO Provider**, select **SAML**. Copy the **Service Provider Entity Id** and **Redirect
URL** values. You will use these values in Okta.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/299948b19e628c531333c21ced70086b975d926f834b0f8a55e13edbd5898303/assets/images/okta-saml-elevenlabs-provider-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=996fa98582f38501673dd5ab823d24d7b015ff1db32a91ef6e2acb1cce223612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs SAML provider settings" />

#### Create an Okta app integration

In the Okta Admin Console, go to **Applications** > **Applications**, then click **Create App
Integration**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ed1e7575d777d053d3749efc7f0a31ebfdf19a5f37de5f266ea147b26e4a2487/assets/images/okta-saml-okta-applications.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=5f4d07b169d49ab195322d83fa9d6d0bfb5bef243d93e24a8eaf02af1c32a0be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta Applications page with Create App Integration" />

Select **SAML 2.0**, then click **Next**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/89e194f26b79f20c6e34af660802266901dd96464987be2f38ea41c7d338704b/assets/images/okta-saml-create-app-integration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=7f3ad4e53b4329023c397d9caf2767f2d43fe3d92dd312d89951eccb07d6a259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta Create a new app integration dialog with SAML 2.0 selected" />

#### Add the app name

In **General Settings**, set **App name** to `ElevenLabs`, then click **Next**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/56ed422543674b8b81608e27e585faf71fdca05d28ceb1493aef5d5d3c256722/assets/images/okta-saml-general-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=8b6920c68714b8f667db2b5b2dd431c31b22619dd10b024b154ddd05b3d1dce3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta Create SAML Integration general settings" />

#### Configure SAML settings in Okta

In **SAML Settings**, configure the app with the values from ElevenLabs:

* Set **Single sign-on URL** to the ElevenLabs **Redirect URL**.
* Select **Use this for Recipient URL and Destination URL**.
* Set **Audience URI (SP Entity ID)** to the ElevenLabs **Service Provider Entity Id**.
* Set **Name ID format** to **EmailAddress**.
* Set **Application username** to **Email**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/45c4621749048612f9dcaa96123b07b60e661f3a84c03c654a0e229dce385ad6/assets/images/okta-saml-configure-saml.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=2b3bfa9aab8ee5a167820ab589b750e70389b3857904755b159f3624fed7a848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta SAML settings for ElevenLabs" />

#### Assign users or groups

Open the Okta app's **Assignments** tab and assign the users or groups that should be able to
sign in to ElevenLabs.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3cf08aff22d992d143bfb1c655f3a807c5b2b6b5cafba4ee2aff6e18bd997676/assets/images/okta-saml-assignments.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=c0fa0d52c5126ddb3937a3f93b3faa9f7ddbb6ae0994befe5bf89bc683df9b6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta app Assignments tab" />

#### Add the Okta certificate to ElevenLabs

In Okta, open **SAML Signing Certificates** and use **Actions** > **Download certificate** for
the active certificate.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/334a3a8fb4355a170254e0dd132b141fd9f6a86dd58374d054ae1a708a8778f9/assets/images/okta-saml-download-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=98f345d3540c02302bd286ed4066b81794e690ca6567a5fb93277f9158716eb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta SAML Signing Certificates download certificate action" />

Open the certificate file and copy the full PEM certificate, including
`-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d62e28cf4ff1d3240d190cc9405345e193177e533b185acd64b19ab7f77596c5/assets/images/okta-saml-copy-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=20c350a88b714ee4f265a4ba8275fb49b7f40dd707a80251e1a9d87dfed52e3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta certificate file in PEM format" />

In ElevenLabs, click **Add Certificate**, paste the Okta certificate, then click **Add**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/910152284bd98c1ebdae064a7424d7d1ac185fe716abdda751607bad9b4cc147/assets/images/okta-saml-add-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=2cd94dd62f6e7ebfeb35e1127c6763b1b72217d8c79555109fdb2176df86b429&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Add X509 Certificate dialog" />

#### Copy Okta metadata values into ElevenLabs

In Okta, open the IdP metadata XML. Copy the metadata values into ElevenLabs:

* Use `entityID` for **Identity Provider Entity Id**.
* Use the `SingleSignOnService Location` URL that ends in `/sso/saml` for **Identity Provider
  Sign-In URL**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/96f8ad35da0fbeafc265310e0ca761c69163cb53c76baf8d35c97e9a992d4ee8/assets/images/okta-saml-idp-metadata.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=65bdfc01d34905a6143c92883da04d83d0bc7d8e251e12161427c136754c581e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Okta IdP metadata XML showing entityID and SingleSignOnService Location" />

#### Add your allowed email domain

In ElevenLabs, click **Add Domain** and select the verified domain that matches the email
domain of your Okta users.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bd532d18051c43e9db7c3b33e54b5910a2050ec16e04e85c9b7541fda20f7b6f/assets/images/okta-saml-add-domain.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260828T113112Z&X-Amz-Expires=604800&X-Amz-Signature=3c8d0c6fb07e5c641b52629f1af68c0ecfcf79645a7e46c42db680bd254cc4a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Add allowed email domains dialog" />

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
