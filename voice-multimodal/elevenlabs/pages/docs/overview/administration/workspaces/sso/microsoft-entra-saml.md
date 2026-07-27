---
title: "Microsoft Entra SAML SSO"
source: https://elevenlabs.io/docs/overview/administration/workspaces/sso/microsoft-entra-saml.md
path: docs/overview/administration/workspaces/sso/microsoft-entra-saml
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Microsoft Entra SAML SSO

Microsoft Entra SAML SSO lets workspace members sign in to ElevenLabs through a Microsoft Entra ID
(formerly Azure AD) enterprise application.

SSO is available for Enterprise workspaces. Only Workspace admins can configure SSO settings.

ElevenLabs supports Service Provider (SP) initiated SAML SSO. To start sign-in, use
`https://elevenlabs.io/app/sign-in?use_sso=true`. You can add `email=user@example.com` as a query
parameter to prefill the email field.

Microsoft Entra is only supported through SAML. OIDC with Microsoft Entra is not recommended and
can cause sign-in issues.

## Prerequisites

* An Enterprise ElevenLabs workspace.
* Workspace admin access in ElevenLabs.
* Admin access in the Microsoft Entra admin center.
* A verified email domain in ElevenLabs for the users who will sign in through Microsoft Entra.

## Set up Microsoft Entra SAML SSO

#### Open SSO settings in ElevenLabs

Go to **Workspace settings** > **Security & SSO**.

#### Verify your email domain

Under **User Auto Provisioning**, verify the email domain your Microsoft Entra users will sign in
with. Enter the domain (subdomains are allowed), then follow the prompts to confirm ownership.
Optionally enable auto-provisioning so users with a matching email domain automatically join your
workspace.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9b471a5441feffcb2f57e3e1ee85bafdccf687bfbe61e6cfb89234f38bc5821d/assets/images/entra-saml-verify-domain.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=2ff73ddb348cc78344397993a55eea8d6388949cb9b080e25ff5d5a227d3484f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs bulk domain verification dialog" />

{" "}

#### Select SAML as the SSO provider

In **SSO Provider**, select **SAML**. Copy the **Service Provider Entity Id** and **Redirect URL**
values. You will use these values in Microsoft Entra.

#### Create a Microsoft Entra enterprise application

In the Microsoft Entra admin center, open your directory **Overview**, then click **Add** >
**Enterprise application**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3d80c303777e59820fc3e9240368ffaf6fd5af53279f5ce574b21d57f4433cff/assets/images/entra-saml-new-application.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=e1f89c9622e435922ca2769c66a769c8fbb64b2f01f0d9d2e7c5427bcb60a101&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra Overview Add menu with Enterprise application selected" />

On **Browse Microsoft Entra App Gallery**, click **Create your own application**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e78db7434ea9a3b210ef75544126423d1a55fb04aa6e08408dc0abaed1aa2fb2/assets/images/entra-saml-create-application.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=806c64c4edccd0461618b0101742003a5d4cc8a96bff708f35261af3968ee954&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra App Gallery with Create your own application" />

#### Name the application

Enter a name (for example, `ElevenLabs`), select **Integrate any other application you don't find
in the gallery (Non-gallery)**, then click **Create**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4ab66649e94c88812f19c55412be1370aa3d8d7a9249f55576dfd62c3cb33558/assets/images/entra-saml-name-application.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=4f71c52afe862eeef33591420f1370ea7a0049554f6cce5f1055ec6f0375b1ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra Create your own application panel with a non-gallery app" />

#### Start single sign-on setup

On the application **Overview**, under **Getting Started**, select **Set up single sign on** >
**Get started**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1fcee15188b6ebc3c5773af4fd1ffb0dd9ff986821a57702b9b4ae876b8e26cf/assets/images/entra-saml-set-up-sso.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=f4ef45a46fd8ce7227b931a06ddd77527619e5b64cf45aa144fd8ceeabe6db85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra enterprise application Getting Started with Set up single sign on" />

Select **SAML** as the single sign-on method.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e0a67bdc3f893e3d00fefc2531db05e2ae5db569821ab59479f629bf9619d6e9/assets/images/entra-saml-select-saml.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=b9c2df0acbc4b74b438cc98fcca49032956a2361db1fa9d277eac5f8183a27ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra Select a single sign-on method with SAML" />

#### Configure basic SAML settings

In **Basic SAML Configuration**, configure the app with the values from ElevenLabs:

* Set **Identifier (Entity ID)** to the ElevenLabs **Service Provider Entity Id**.
* Set **Reply URL (Assertion Consumer Service URL)** to the ElevenLabs **Redirect URL**.
* Leave **Sign on URL** blank. ElevenLabs uses SP-initiated SSO.

Click **Save**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9961d266eb4ccb0bd4b6aa6f2d9a3322b059322fa7b933fe2741ca2c2ac2edb9/assets/images/entra-saml-basic-configuration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=048945305e3b64456607e0da093d082fdc70fc882cfe9358f1aa75a006a75616&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra Basic SAML Configuration with Identifier and Reply URL" />

For [data residency](/docs/overview/administration/data-residency) environments, use
`https://<region>.residency.elevenlabs.io/__/auth/handler` as the Reply URL, replacing
`<region>` with your region code.

#### Configure the Name ID claim

In **Attributes & Claims**, edit the **Unique User Identifier (Name ID)** claim:

* Set **Name identifier format** to **Email address**.
* Set **Source** to **Attribute**.
* Set **Source attribute** to the field that contains the email address for all users. This is
  usually `user.mail`, but may be `user.userprincipalname`.

Click **Save**.

Choose the attribute that holds an email address for every user. If `user.mail` is not populated
for all of your users, use `user.userprincipalname` instead.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1d94d0fecd19d9ca30ff5cce93294fda6a8c84ed98837ea89549f79b97ae153d/assets/images/entra-saml-attributes-claims.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=bc16ba8954fefb1e89ab37bbf16cea8a67def595eccce29a46963e43719a5a76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra Manage claim with Email address format and user.mail source attribute" />

#### Download the signing certificate

In **SAML Certificates**, next to **Certificate (Base64)**, click **Download**. Open the
downloaded file in a text editor.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/684fac9e520103b4c6978ef8dd3e95ea30d04a34e31b6ec7d13d97128492af07/assets/images/entra-saml-download-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=1c26244d2e1090e04f59e3e0a2b1edf1b2e4c59cf64d57d110bd67bbb20573c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra SAML Certificates with Certificate Base64 download" />

#### Assign users or groups

Open the app's **Users and groups**, then assign the users or groups that should be able to sign
in to ElevenLabs.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c07ddb7a33eb511ada81ce437cdf468aecbfb83ef11a5c3a25f3fa6c87f5afcc/assets/images/entra-saml-assign-users.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=4aa143d69904d7626bac44c7918b76edbe90d09d231d326350a421f2bad07908&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra Add Assignment users list" />

#### Add the Entra certificate to ElevenLabs

In ElevenLabs, click **Add Certificate**. Paste the full PEM certificate from the Base64 file,
including `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`, then click **Add**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bd8d3e047624b0c8f5b119d77e79ef4b721ef2917ad9049a2a44b36b6016201b/assets/images/entra-saml-add-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=f033acf931206fb40f7bd302de0ffd955cb82900a8cd0cf11742b8a085540b86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Add X509 Certificate dialog" />

#### Copy Entra identity provider values into ElevenLabs

In the Microsoft Entra **Set up** section, copy the identity provider values into ElevenLabs:

* Use the **Microsoft Entra Identifier** for **Identity Provider Entity Id**.
* Use the **Login URL** for **Identity Provider Sign-In URL**.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/abddc7178305f0c220d6b9ad92d21320859824c024a84506933fd67a9045144e/assets/images/entra-saml-idp-values.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=39e9c8909f4c568747e1ab68a1a8ef32bbfb067c8e9174554f339cecc28bf7bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Microsoft Entra set up values showing Login URL and Microsoft Entra Identifier" />

#### Add your allowed email domain

In ElevenLabs, click **Add Domain** and select the verified domain that matches the email domain
of your Microsoft Entra users.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3039fce378edac35eaeab847e55a99ec82a241d7fc3bc46be24b23ec52e4a2bf/assets/images/entra-saml-add-domain.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T113130Z&X-Amz-Expires=604800&X-Amz-Signature=1b136170411da791126249dbc8ee4498093e38fbd08b11cbe9eab11c2fd8e14e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="ElevenLabs Add allowed email domains dialog" />

#### Save the SSO provider

Review the configuration, select **I acknowledge this change will log out users currently using
SSO**, then click **Update SSO**.

## Field mappings

Use this table to map Microsoft Entra SAML settings to ElevenLabs SSO fields.

| Microsoft Entra field or location              | ElevenLabs field                  | Value to use                                                                              |
| ---------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Sign-in method**                             | **SSO Provider**                  | `SAML`                                                                                    |
| **Identifier (Entity ID)**                     | **Service Provider Entity Id**    | Use the ElevenLabs value, for example `https://elevenlabs.io`                             |
| **Reply URL (Assertion Consumer Service URL)** | **Redirect URL**                  | Use the ElevenLabs value, for example `https://elevenlabs.io/__/auth/handler`             |
| **Microsoft Entra Identifier**                 | **Identity Provider Entity Id**   | Entra issuer, for example `https://sts.windows.net/{tenant-id}/`                          |
| **Login URL**                                  | **Identity Provider Sign-In URL** | Entra SAML sign-in URL, for example `https://login.microsoftonline.com/{tenant-id}/saml2` |
| **Certificate (Base64)**                       | **Certificate**                   | Entra token signing certificate in valid PEM format                                       |
| **Name ID format**                             | No manual config required         | Set to **Email address**                                                                  |
| **Name ID source attribute**                   | No manual config required         | Field containing the user's email, usually `user.mail` (or `user.userprincipalname`)      |
| User or app email domain in Microsoft Entra    | **Domain**                        | Must match a verified ElevenLabs domain, for example `company.com`                        |

## Troubleshooting

#### Microsoft Entra shows a successful sign-in, but ElevenLabs says unable to sign in

Check the browser Network response for `accounts:signInWithIdp`. Microsoft Entra sign-in logs only
confirm that Entra authenticated the user. ElevenLabs can still reject the SAML response if the
assertion values do not match the SSO configuration.

#### INVALID\_IDP\_RESPONSE: Error when parsing certificate

The browser Network response may show `INVALID_IDP_RESPONSE: Error when parsing certificate`.
Remove the certificate from ElevenLabs, then re-add the Entra **Certificate (Base64)** in valid
PEM format. Do not use an LLM to format the certificate. Open the Base64 certificate in a text
editor and copy it exactly, including `-----BEGIN CERTIFICATE-----` and
`-----END CERTIFICATE-----`.

#### Unable to login with saml.workspace... or user mismatch errors

Make sure Microsoft Entra sends the user's email address as the `NameID`. In **Attributes &
Claims**, set the **Unique User Identifier (Name ID)** claim **Name identifier format** to **Email
address** and **Source attribute** to the field that contains the email address for all users
(usually `user.mail`, or `user.userprincipalname` if `user.mail` is not populated). Inside the
`<saml:Subject>` field of the SAML response, `<saml:NameID>` must be the user's email address.

#### Which Microsoft Entra values should I use?

Use the **Microsoft Entra Identifier** for **Identity Provider Entity Id**, the **Login URL** for
**Identity Provider Sign-In URL**, and the **Certificate (Base64)** for **Certificate**.
