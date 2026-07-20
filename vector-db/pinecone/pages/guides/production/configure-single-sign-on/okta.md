---
title: "Configure SSO with Okta"
source: https://docs.pinecone.io/guides/production/configure-single-sign-on/okta
path: guides/production/configure-single-sign-on/okta
---

Configure SAML SSO with Okta for enterprise.

This page describes how to set up Pinecone with Okta as the single sign-on (SSO) provider. These instructions can be adapted for any provider with SAML 2.0 support.

<Note>SSO is available on Standard and Enterprise plans.</Note>

## Before you begin

This page assumes you have the following:

* Access to your organization's [Pinecone console](https://login.pinecone.io) as an [organization owner](/guides/organizations/understanding-organizations#organization-roles).
* Access to your organization's [Okta Admin console](https://login.okta.com/).

## 1. Start SSO setup in Pinecone

First, start setting up SSO in Pinecone. In this step, you'll capture a couple values necessary for configuring Okta in [Step 2](#2-create-an-app-integration-in-okta).

1. In the Pinecone console, go to [**Settings > Access > Identity provider**](https://app.pinecone.io/organizations/-/settings/access/identity-provider).
2. In the **Single sign-on** section, click **Enable SSO**.
3. In the **Setup SSO** dialog, copy the **Entity ID** and the **Assertion Consumer Service (ACS) URL**. You'll need these values in [Step 2](#2-create-an-app-integration-in-okta).
4. Click **Next**.

Keep this window or browser tab open. You'll come back to it in [Step 4](#4-complete-sso-setup-in-pinecone).

## 2. Create an app integration in Okta

In [Okta](https://login.okta.com/), follow these steps to create and configure a Pinecone app integration:

1. If you're not already on the Okta Admin console, navigate there by clicking the **Admin** button.

2. Navigate to **Applications > Applications**.

3. Click **Create App Integration**.

4. Select **SAML 2.0**.

5. Click **Next**.

6. Enter the **General Settings**:

   * **App name**: `Pinecone`
   * **App logo**: (optional)
   * **App visibility**: Set according to your organization's needs.

7. Click **Next**.

8. For **SAML Settings**, enter values you copied in [Step 1](#1-start-sso-setup-in-pinecone):

   * **Single sign-on URL**: Your **Assertion Consumer Service (ACS) URL**
   * **Audience URI (SP Entity ID)**: Your **Entity ID**
   * **Name ID format**: `EmailAddress`
   * **Application username**: `Okta username`
   * **Update application username on**: `Create and update`

9. In the **Attribute Statements (SAML)** section, create the following attribute:

   * **Name**: `email`
   * **Value**: `user.email`

   <Note>
     In newer versions of Okta, attribute statements are configured on the app's **Sign On** tab after the app is created, rather than in the app creation wizard. If you don't see the **Attribute Statements (SAML)** section here, finish creating the app, then add the attribute from **Applications > Pinecone > Sign On**, expanding **Show legacy configuration** if needed.
   </Note>

10. Click **Next**.

11. Click **Finish**.

## 3. Get the sign on URL and certificate from Okta

Next, in Okta, get the URL and certificate for the Pinecone application you just created. You'll use these in [Step 4](#4-complete-sso-setup-in-pinecone).

1. In the Okta Admin console, navigate to **Applications > Pinecone > Sign On**. If you're continuing from the previous step, you should already be on the right page.
2. In the **SAML 2.0** section, expand **More details**.
3. Copy the **Sign on URL**.
4. Download the **Signing Certificate**.

   <Warning>
     Download the certificate, don't copy it. The downloaded version contains necessary `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
   </Warning>

## 4. Complete SSO setup in Pinecone

In the browser tab or window you kept open in [Step 1](#1-start-sso-setup-in-pinecone), complete the SSO setup in Pinecone:

1. In the **SSO Setup** window, enter the following values:

   * **Login URL**: The URL copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).
   * **Email domain**: Your company's email domain. To target multiple domains, enter each domain separated by a comma.
   * **Certificate**: The contents of the certificate file you copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).

     <Warning>
       When pasting the certificate, be sure to include the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
     </Warning>

2. Choose whether or not to **Enforce SSO for all users**.

   * If enabled, all members of your organization must use SSO to log in to Pinecone.
   * If disabled, members can choose to log in with SSO or with their Pinecone credentials.

3. Click **Next**.

4. Select a **Default role** for all users who log in with SSO. You can change user roles later.

   <Note>
     The **Default role** does not apply if you enable [SAML role management](/guides/production/configure-single-sign-on/okta-role-management). In that mode, every user's organization and project roles come entirely from your identity provider's SAML attributes.
   </Note>

   <Warning>
     When users first log in via SSO, they receive the default SSO role regardless of their previous role. Subsequent SSO logins do not change the role. If the default is **Member** or **Manager**, existing owners will lose owner access on their first SSO login.

     To prevent losing access to organization management features:

     * **Sole owner**: Temporarily set the default to **Owner**, log in via SSO to retain owner access, then change the default back to **Member**. After changing it back, check your organization's user list to verify no one else logged in via SSO while the default was **Owner**—if they did, adjust their roles accordingly.
     * **Multiple owners**: Keep at least one owner signed in via email while others log in via SSO. That owner can restore roles as needed, then log in via SSO last.

     If all owners lose access, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).
   </Warning>

Okta is now ready to be used for single sign-on. Follow the [Okta docs](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-main.htm) to learn how to add users and groups.

## Manage roles automatically

Optionally, you can have Pinecone assign organization and project roles automatically from your identity provider on each login, instead of managing them manually. For more information, see [Manage roles with Okta](/guides/production/configure-single-sign-on/okta-role-management).
