---
title: "Configure SSO with Okta"
source: https://docs.pinecone.io/admin/security/configure-single-sign-on/okta
path: admin/security/configure-single-sign-on/okta
---

Set up SAML single sign-on between Pinecone and Okta so your organization members can log in with corporate credentials.

This page describes how to set up Pinecone with Okta as the single sign-on (SSO) provider. You can adapt these instructions for any provider with SAML 2.0 support.

> [!NOTE]
>
> SSO is available on Standard and Enterprise plans.

## Before you begin

This page assumes you have the following:

* Access to your organization's [Pinecone console](https://login.pinecone.io) as an [organization owner](/admin/organizations/understanding-organizations#organization-roles).
* Access to your organization's [Okta Admin console](https://login.okta.com/).

## 1. Start SSO setup in Pinecone

In this step, you'll copy two values you need to configure Okta in [Step 2](#2-create-an-app-integration-in-okta).

1. In the Pinecone console, go to [**Settings > Access > Identity provider**](https://app.pinecone.io/organizations/-/settings/access/identity-provider).
2. In the **Single sign-on** section, click **Enable SSO**.
3. In the **Setup SSO** dialog, copy the **Entity ID** and the **Assertion Consumer Service (ACS) URL**. You'll need these values in [Step 2](#2-create-an-app-integration-in-okta).
4. Click **Next**.

Keep this window or browser tab open. You'll come back to it in [Step 4](#4-complete-sso-setup-in-pinecone).

## 2. Create an app integration in Okta

1. In [Okta](https://login.okta.com/), if you're not already on the Okta Admin console, click **Admin**.

2. Go to **Applications > Applications**.

3. Click **Create App Integration**.

4. Select **SAML 2.0**.

5. Click **Next**.

6. Enter the **General Settings**:

   * **App name**: `Pinecone`
   * **App logo**: (optional)
   * **App visibility**: Set according to your organization's needs.

7. Click **Next**.

8. For **SAML Settings**, enter the values you copied in [Step 1](#1-start-sso-setup-in-pinecone):

   * **Single sign-on URL**: Your **Assertion Consumer Service (ACS) URL**
   * **Audience URI (SP Entity ID)**: Your **Entity ID**
   * **Name ID format**: `EmailAddress`
   * **Application username**: `Okta username`
   * **Update application username on**: `Create and update`

9. In the **Attribute Statements (SAML)** section, create the following attribute:

   * **Name**: `email`
   * **Value**: `user.email`

   > [!NOTE]
   >
   > In newer versions of Okta, attribute statements are configured on the app's **Sign On** tab after the app is created, rather than in the app creation wizard. If you don't see the **Attribute Statements (SAML)** section here, finish creating the app, then add the attribute from **Applications > Pinecone > Sign On**, expanding **Show legacy configuration** if needed.

10. Click **Next**.

11. Click **Finish**.

## 3. Get the sign on URL and certificate from Okta

Next, in Okta, get the URL and certificate for the Pinecone application you just created. You'll use these in [Step 4](#4-complete-sso-setup-in-pinecone).

1. In the Okta Admin console, go to **Applications > Pinecone > Sign On**. If you're continuing from the previous step, you should already be on the right page.
2. In the **SAML 2.0** section, expand **More details**.
3. Copy the **Sign on URL**.
4. Download the **Signing Certificate**.

   > [!WARNING]
   >
   > Download the certificate, don't copy it. The downloaded version contains necessary `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.

## 4. Complete SSO setup in Pinecone

Return to the browser tab or window you kept open in [Step 1](#1-start-sso-setup-in-pinecone).

1. In the **Setup SSO** dialog, enter the following values:

   * **Login URL**: The URL copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).
   * **Email domain**: Your company's email domain. To target multiple domains, enter each domain separated by a comma.
   * **Certificate**: The contents of the certificate file you copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).

     > [!WARNING]
     >
     > When pasting the certificate, include the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.

2. Choose whether to **Enforce SSO for all users**.

   * If enabled, all members of your organization must use SSO to log in to Pinecone.
   * If disabled, members can choose to log in with SSO or with their Pinecone credentials.

3. Click **Next**.

4. Select a **Default role** for all users who log in with SSO. You can change user roles later.

   > [!NOTE]
   >
   > The **Default role** doesn't apply if you enable [SAML role management](/admin/security/configure-single-sign-on/okta-role-management). In that mode, every user's organization and project roles come entirely from your identity provider's SAML attributes.

   > [!WARNING]
   >
   > When users first log in through SSO, they receive the default SSO role regardless of their previous role. Subsequent SSO logins do not change the role. If the default is **Member** or **Manager**, existing owners lose owner access on their first SSO login.
   >
   > To prevent losing access to organization management features:
   >
   > * **Sole owner**: Temporarily set the default to **Owner**, log in through SSO to retain owner access, then change the default back to **Member**. After changing it back, check your organization's user list to verify no one else logged in through SSO while the default was **Owner**. If they did, adjust their roles.
   > * **Multiple owners**: Keep at least one owner signed in with email while others log in through SSO. That owner can restore roles as needed, then log in through SSO last.
   >
   > If all owners lose access, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

Okta is now ready for single sign-on. To add users and groups, see the [Okta docs](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-main.htm).

## Manage roles automatically

You can also have Pinecone assign organization and project roles automatically from your identity provider on each login, instead of managing them manually. For more information, see [Manage roles with Okta](/admin/security/configure-single-sign-on/okta-role-management).
