---
title: "Custom SSO"
source: https://docs.fireworks.ai/accounts/sso
path: accounts/sso
---

Set up custom Single Sign-On (SSO) authentication and SCIM user provisioning for Fireworks accounts, including SAML setup, group mapping, and lifecycle sync.

Fireworks uses single sign-on (SSO) as the primary mechanism to authenticate with the platform.
By default, Fireworks supports Google SSO.

If you have an enterprise account, Fireworks supports bringing your own identity provider using:

* OpenID Connect (OIDC) provider
* SAML 2.0 provider
* Optionally, the work-email domain your users sign in with, so they can start SSO by entering their email instead of your account ID

> [!NOTE]
>
> Coordinate with your Fireworks AI representative to enable the integration.

## OpenID Connect (OIDC) provider

**1. Create OIDC client application**

Create an OIDC client application in your identity provider, e.g. Okta.

**2. Configure client**

Ensure the client is configured for "code authorization" of the "web" type (i.e. with a client_secret).

**3. Set redirect URL**

Set the client's "allowed redirect URL" to the URL provided by Fireworks. It looks like:

```
https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/oauth2/idpresponse
```

**4. Note down client details**

Note down the `issuer`, `client_id`, and `client_secret` for the newly created client. You will need to provide this to your Fireworks.ai representative to complete your account set up.

## SAML 2.0 provider

**1. Create SAML 2.0 application**

Create a SAML 2.0 application in your identity provider, e.g. [Okta](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm).

**2. Set SSO URL**

Set the SSO URL to the URL provided by Fireworks. It looks like:

```
https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/saml2/idpresponse
```

**3. Configure Audience URI**

Configure the Audience URI (SP Entity ID) as provided by Fireworks. It looks like:

```
urn:amazon:cognito:sp:<some-unique-identifier>
```

**4. Create Attribute Statement**

Create an Attribute Statement with the name:

```
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
```

and the value `user.email`

> [!NOTE]
>
> **Okta:** After saving the app, open **Sign On** → **Attribute Statements (SAML)** → expand **Show legacy configuration** → add the attribute statement there. Okta no longer configures this during app creation.

**5. Keep default settings**

Leave the rest of the settings as defaults.

**6. Note down metadata URL**

Note down the "metadata url" for your newly created application. You will need to provide this to your Fireworks AI representative to complete your account set up. If the metadata URL is not publicly reachable, provide the metadata XML file instead.

## SAML sign-in flow

By default, Fireworks uses **service provider (SP) initiated** SAML: users start at [app.fireworks.ai](https://app.fireworks.ai) or with `firectl signin` and are redirected to your identity provider.

**IdP-initiated** SAML is supported as an opt-in for SAML identity providers. When enabled, users can also start from your identity provider's portal (for example, the Okta app tile). Enable it with [`--enable-idp-initiated-sso`](/tools-sdks/firectl/commands/identity-provider-create) when creating or updating the identity provider. This option is SAML-only; OIDC providers cannot use it.

## Just-in-time (JIT) user provisioning

JIT user provisioning automatically creates user accounts when they sign in through SSO for the first time. When enabled, users who authenticate through your identity provider are automatically added to your Fireworks account without requiring manual user creation.

To enable JIT user provisioning, use the [`--enable-jit-user-provisioning`](/tools-sdks/firectl/commands/identity-provider-create) flag when creating your identity provider with firectl.

## SCIM provisioning

System for Cross-domain Identity Management (SCIM) provisioning synchronizes the user and group lifecycle between your identity provider and Fireworks. Users assigned to Fireworks in your directory are added to your Fireworks account, and users are removed when they are deactivated or unassigned in the directory.

SCIM provisioning is available for enterprise accounts and works with supported directory providers, including Okta, Microsoft Entra ID, and Google Workspace. Fireworks uses [WorkOS Directory Sync](https://workos.com/docs/directory-sync) to connect to your directory.

> [!NOTE]
>
> SCIM manages provisioning only. Users continue to authenticate through your
> existing OIDC or SAML SSO integration.

### Set up SCIM provisioning

**1. Configure custom SSO**

Complete the OIDC or SAML setup above. Custom SSO must be configured before
you can enable SCIM provisioning.

**2. Request SCIM enablement**

Contact your Fireworks AI representative. Fireworks will enable Directory
Sync for your account and provide a secure setup link.

**3. Connect your directory**

Open the setup link, select your directory provider, and follow the
provider-specific instructions to authorize the connection.

**4. Assign users and groups**

In your identity provider, assign the users who should have access to
Fireworks, plus any groups you want mirrored into Fireworks. Confirm that
they appear on the **Users** and **Groups** tabs of the [Users
page](https://app.fireworks.ai/account/users).

### Group provisioning

Directory groups assigned to Fireworks are synced alongside your users. Creating, renaming, or deleting a group in your directory creates, updates, or deletes the matching Fireworks group, and adding or removing someone from a directory group changes their Fireworks group membership. Deleting a group removes its memberships; the users themselves are unaffected.

Synced groups appear on the **Groups** tab of the [Users page](https://app.fireworks.ai/account/users), marked `SCIM-synced`, with their member count and the time of the last sync. Directory sync is the only way to create a Fireworks group, and groups are read-only in Fireworks — your directory is the source of truth for both the group and its membership.

Synced groups have one use in Fireworks today: assigning them a [group limit](/nexus/usage-limits#group-limits), which caps serverless spend for each of the group's members. That is a **Fireworks Nexus** feature and is enabled separately — syncing groups does not by itself give your account spend limits.

> [!WARNING]
>
> Group-to-role mappings are not currently supported: a group's members do not
> inherit a role from the group, and provisioned users receive the `User` role
> by default. Set roles per user as described in [Managing
> users](/accounts/users#updating-a-users-role).

We recommend disabling JIT provisioning when SCIM is enabled so that your directory remains the source of truth for account membership. SSO enforcement is also recommended to prevent access outside your configured identity provider.

## Enforce SSO

When SSO enforcement is enabled, account access is restricted to users with approved tenant domains only. Users with matching domains must authenticate via the identity provider, and users with other domains are blocked. API keys and service accounts are not blocked by SSO enforcement.

To enforce SSO, use the [`--enforce-sso`](/tools-sdks/firectl/commands/identity-provider-create) flag when creating your identity provider with firectl, or toggle "Enforce SSO for all users" in the Fireworks console.

## Rotate your OIDC client secret

You can replace the client secret of an OIDC identity provider without changing your sign-in URL, redirect URL, or users. Fireworks updates the secret in place, so existing sessions stay signed in and users don't need to do anything.

You need the `admin` role on your Fireworks account. If your account's SSO was set up by your Fireworks AI representative and the identity provider doesn't appear on the [SSO page](https://app.fireworks.ai/account/sso) or in `firectl identity-provider list`, contact your representative to rotate the secret instead.

> [!WARNING]
>
> If **Enforce SSO** is on, a wrong secret blocks sign-in for every user on your tenant domains, including admins. API keys keep working. Keep the old secret active until you've confirmed sign-in works with the new one, and keep an API key with the `admin` role on hand so you can roll back with firectl.

**1. Create a new secret in your identity provider**

Generate a new client secret for the Fireworks OIDC application in your identity provider. Keep the old secret active. Most providers, including Okta and Microsoft Entra ID, allow two active secrets at once.

**2. Update the secret in Fireworks**

**Console:** Open the [SSO page](https://app.fireworks.ai/account/sso), edit your identity provider, replace the contents of **Client Secret** with the new secret, and select **Update**. Don't leave the field blank.

**firectl:** Pass only the new secret. The issuer and client ID stay as they are.

```bash theme={null}
firectl identity-provider list
firectl identity-provider update <provider-id> --oidc-client-secret="<new-client-secret>"
```

> [!NOTE]
>
> If you set a custom email claim on your identity provider with firectl, update the secret with firectl rather than the console.

**3. Confirm the provider is ready**

The provider shows `UPDATING` while the change is applied, then `READY`, usually within a minute.

```bash theme={null}
firectl identity-provider get <provider-id>
```

Check that `State` is `READY` and `Status` shows no error. If it stays `UPDATING` or shows an error, check the secret and run the update again. While the provider is `UPDATING`, SSO enforcement is paused, and new users can't be added through JIT provisioning.

**4. Test sign-in**

Open an incognito or private window, sign in to [app.fireworks.ai](https://app.fireworks.ai) through your identity provider, and confirm you reach your account. Fireworks doesn't check the secret when you save it, so a mistyped secret only shows up here, as a failed sign-in.

**5. Revoke the old secret**

After sign-in works with the new secret, delete the old one in your identity provider.

## Troubleshooting

### Invalid samlResponse or relayState from identity provider

This error usually means the login started from the identity provider (IdP-initiated) but IdP-initiated SAML is not enabled for your identity provider.

* For SP-initiated login, start from [app.fireworks.ai](https://app.fireworks.ai) instead of your IdP's app tile.
* For IdP-initiated login, enable [`--enable-idp-initiated-sso`](/tools-sdks/firectl/commands/identity-provider-create) on a SAML identity provider (or ask your Fireworks representative to enable it).

See [Understanding SAML](https://developer.okta.com/docs/concepts/saml/#understand-sp-initiated-sign-in-flow) for SP-initiated versus IdP-initiated flows.

### Required String parameter 'RelayState' is not present

Same cause as above: an IdP-initiated login without IdP-initiated SSO enabled.
