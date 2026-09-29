---
title: "Microsoft Entra SAML SSO"
source: https://elevenlabs.io/docs/overview/administration/workspaces/sso/microsoft-entra-saml.md
path: docs/overview/administration/workspaces/sso/microsoft-entra-saml
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Microsoft Entra SAML SSO

Microsoft Entra SAML SSO lets workspace members sign in to ElevenLabs through a Microsoft Entra ID
(formerly Azure AD) enterprise application.

> **Info**
>
> SSO is available for Enterprise workspaces. Only Workspace admins can configure SSO settings.

> **Warning**
>
> ElevenLabs supports Service Provider (SP) initiated SAML SSO. To start sign-in, use
> `https://elevenlabs.io/app/sign-in?use_sso=true`. You can add `email=user@example.com` as a query
> parameter to prefill the email field.

> **Note**
>
> Microsoft Entra is only supported through SAML. OIDC with Microsoft Entra is not recommended and
> can cause sign-in issues.

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

![ElevenLabs bulk domain verification dialog](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9b471a5441feffcb2f57e3e1ee85bafdccf687bfbe61e6cfb89234f38bc5821d/assets/images/entra-saml-verify-domain.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=ef3b51149998a40b7e078339b4672b1f9bd7d632170d3addfab45618fa8c9169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Select SAML as the SSO provider

In **SSO Provider**, select **SAML**. Copy the **Service Provider Entity Id** and **Redirect URL**
values. You will use these values in Microsoft Entra.

#### Create a Microsoft Entra enterprise application

In the Microsoft Entra admin center, open your directory **Overview**, then click **Add** >
**Enterprise application**.

![Microsoft Entra Overview Add menu with Enterprise application selected](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3d80c303777e59820fc3e9240368ffaf6fd5af53279f5ce574b21d57f4433cff/assets/images/entra-saml-new-application.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=42d8a385b48d89f786ce4a6c52ba31968d65971a124dec6ca65d16265dad3a29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

On **Browse Microsoft Entra App Gallery**, click **Create your own application**.

![Microsoft Entra App Gallery with Create your own application](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e78db7434ea9a3b210ef75544126423d1a55fb04aa6e08408dc0abaed1aa2fb2/assets/images/entra-saml-create-application.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=0b36c66f6ef5386c861b82fa413d6f2ef47c11dcc7e6f332aac748252201e110&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Name the application

Enter a name (for example, `ElevenLabs`), select **Integrate any other application you don't find
in the gallery (Non-gallery)**, then click **Create**.

![Microsoft Entra Create your own application panel with a non-gallery app](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4ab66649e94c88812f19c55412be1370aa3d8d7a9249f55576dfd62c3cb33558/assets/images/entra-saml-name-application.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=4ee94088b98408e007441d3d3883140b012b15dc052096cbcd68e3ea05e257dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Start single sign-on setup

On the application **Overview**, under **Getting Started**, select **Set up single sign on** >
**Get started**.

![Microsoft Entra enterprise application Getting Started with Set up single sign on](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1fcee15188b6ebc3c5773af4fd1ffb0dd9ff986821a57702b9b4ae876b8e26cf/assets/images/entra-saml-set-up-sso.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=17efe00b7f5003249c0d0adf3906c839fa4dfb7e93088a1f130e61b3d91dab7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Select **SAML** as the single sign-on method.

![Microsoft Entra Select a single sign-on method with SAML](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e0a67bdc3f893e3d00fefc2531db05e2ae5db569821ab59479f629bf9619d6e9/assets/images/entra-saml-select-saml.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=a9e072e2d233d1ad2a3176a226da30efd32a59cdc14d58ddfc961ebd355268df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Configure basic SAML settings

In **Basic SAML Configuration**, configure the app with the values from ElevenLabs:

* Set **Identifier (Entity ID)** to the ElevenLabs **Service Provider Entity Id**.
* Set **Reply URL (Assertion Consumer Service URL)** to the ElevenLabs **Redirect URL**.
* Leave **Sign on URL** blank. ElevenLabs uses SP-initiated SSO.

Click **Save**.

![Microsoft Entra Basic SAML Configuration with Identifier and Reply URL](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9961d266eb4ccb0bd4b6aa6f2d9a3322b059322fa7b933fe2741ca2c2ac2edb9/assets/images/entra-saml-basic-configuration.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=8e1d7b91b927248b0f57f15dee6620c1f92b351ce0a423e1460b3dbc004c0dce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Note**
>
> For [data residency](/docs/overview/administration/data-residency) environments, use
> `https://<region>.residency.elevenlabs.io/__/auth/handler` as the Reply URL, replacing
> `<region>` with your region code.

#### Configure the Name ID claim

In **Attributes & Claims**, edit the **Unique User Identifier (Name ID)** claim:

* Set **Name identifier format** to **Email address**.
* Set **Source** to **Attribute**.
* Set **Source attribute** to the field that contains the email address for all users. This is
  usually `user.mail`, but may be `user.userprincipalname`.

Click **Save**.

> **Note**
>
> Choose the attribute that holds an email address for every user. If `user.mail` is not populated
> for all of your users, use `user.userprincipalname` instead.

![Microsoft Entra Manage claim with Email address format and user.mail source attribute](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/1d94d0fecd19d9ca30ff5cce93294fda6a8c84ed98837ea89549f79b97ae153d/assets/images/entra-saml-attributes-claims.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=484e9457a8f05b1e6a53b0023122fc92b41a61f2f6d861d3da5aa44db2d1bcde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Download the signing certificate

In **SAML Certificates**, next to **Certificate (Base64)**, click **Download**. Open the
downloaded file in a text editor.

![Microsoft Entra SAML Certificates with Certificate Base64 download](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/684fac9e520103b4c6978ef8dd3e95ea30d04a34e31b6ec7d13d97128492af07/assets/images/entra-saml-download-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=cf9da114cbaae0a4bd5556d7ab54b0b09da06872f556f081e1c95832f8fe8846&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Assign users or groups

Open the app's **Users and groups**, then assign the users or groups that should be able to sign
in to ElevenLabs.

![Microsoft Entra Add Assignment users list](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c07ddb7a33eb511ada81ce437cdf468aecbfb83ef11a5c3a25f3fa6c87f5afcc/assets/images/entra-saml-assign-users.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=c690676847368aa8106d327fc3309f2619175af020f1771acb6732bf5c1766fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add the Entra certificate to ElevenLabs

In ElevenLabs, click **Add Certificate**. Paste the full PEM certificate from the Base64 file,
including `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`, then click **Add**.

![ElevenLabs Add X509 Certificate dialog](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/bd8d3e047624b0c8f5b119d77e79ef4b721ef2917ad9049a2a44b36b6016201b/assets/images/entra-saml-add-certificate.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=dc678d47f8baff3d45bec05a35beab842bab9e242365a11b546dcc0084f33202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Copy Entra identity provider values into ElevenLabs

In the Microsoft Entra **Set up** section, copy the identity provider values into ElevenLabs:

* Use the **Microsoft Entra Identifier** for **Identity Provider Entity Id**.
* Use the **Login URL** for **Identity Provider Sign-In URL**.

![Microsoft Entra set up values showing Login URL and Microsoft Entra Identifier](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/abddc7178305f0c220d6b9ad92d21320859824c024a84506933fd67a9045144e/assets/images/entra-saml-idp-values.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=447b4ce76dcd0641307bcdefe6d0693b2f59e2a0e51258523fe0d94a31992704&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add your allowed email domain

In ElevenLabs, click **Add Domain** and select the verified domain that matches the email domain
of your Microsoft Entra users.

![ElevenLabs Add allowed email domains dialog](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3039fce378edac35eaeab847e55a99ec82a241d7fc3bc46be24b23ec52e4a2bf/assets/images/entra-saml-add-domain.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260929T233054Z&X-Amz-Expires=604800&X-Amz-Signature=5ceddfdbb221944ed72b4ce405aea40a99a57aeca1256e79f93e458952e835f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
