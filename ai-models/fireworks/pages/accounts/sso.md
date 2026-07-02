---
title: "Custom SSO"
source: https://docs.fireworks.ai/accounts/sso
path: accounts/sso
---

Set up custom Single Sign-On (SSO) authentication for Fireworks AI

Fireworks uses single sign-on (SSO) as the primary mechanism to authenticate with the platform.
By default, Fireworks supports Google SSO.

If you have an enterprise account, Fireworks supports bringing your own identity provider using:

* OpenID Connect (OIDC) provider
* SAML 2.0 provider

<Info>
  Coordinate with your Fireworks AI representative to enable the integration.
</Info>

## OpenID Connect (OIDC) provider

<Steps>
  <Step title="Create OIDC client application">
    Create an OIDC client application in your identity provider, e.g. Okta.
  </Step>

  <Step title="Configure client">
    Ensure the client is configured for "code authorization" of the "web" type (i.e. with a client\_secret).
  </Step>

  <Step title="Set redirect URL">
    Set the client's "allowed redirect URL" to the URL provided by Fireworks. It looks like:

    ```
    https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/oauth2/idpresponse
    ```
  </Step>

  <Step title="Note down client details">
    Note down the `issuer`, `client_id`, and `client_secret` for the newly created client. You will need to provide this to your Fireworks.ai representative to complete your account set up.
  </Step>
</Steps>

## SAML 2.0 provider

<Steps>
  <Step title="Create SAML 2.0 application">
    Create a SAML 2.0 application in your identity provider, e.g. [Okta](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm).
  </Step>

  <Step title="Set SSO URL">
    Set the SSO URL to the URL provided by Fireworks. It looks like:

    ```
    https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/saml2/idpresponse
    ```
  </Step>

  <Step title="Configure Audience URI">
    Configure the Audience URI (SP Entity ID) as provided by Fireworks. It looks like:

    ```
    urn:amazon:cognito:sp:<some-unique-identifier>
    ```
  </Step>

  <Step title="Create Attribute Statement">
    Create an Attribute Statement with the name:

    ```
    http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
    ```

    and the value `user.email`

    <Note>
      **Okta:** After saving the app, open **Sign On** → **Attribute Statements (SAML)** → expand **Show legacy configuration** → add the attribute statement there. Okta no longer configures this during app creation.
    </Note>
  </Step>

  <Step title="Keep default settings">
    Leave the rest of the settings as defaults.
  </Step>

  <Step title="Note down metadata URL">
    Note down the "metadata url" for your newly created application. You will need to provide this to your Fireworks AI representative to complete your account set up.
  </Step>
</Steps>

## Just-In-Time (JIT) user provisioning

JIT user provisioning automatically creates user accounts when they sign in through SSO for the first time. When enabled, users who authenticate through your identity provider are automatically added to your Fireworks account without requiring manual user creation.

To enable JIT user provisioning, use the [`--enable-jit-user-provisioning`](/tools-sdks/firectl/commands/identity-provider-create) flag when creating your identity provider with firectl.

## Enforce SSO

When SSO enforcement is enabled, account access is restricted to users with approved tenant domains only. Users with matching domains must authenticate via the identity provider, and users with other domains are blocked.

To enforce SSO, use the [`--enforce-sso`](/tools-sdks/firectl/commands/identity-provider-create) flag when creating your identity provider with firectl, or toggle "Enforce SSO for all users" in the Fireworks console.

## Troubleshooting

### Invalid samlResponse or relayState from identity provider

This error occurs if you are trying to use identity provider (IdP) initiated login. Fireworks currently only supports
service provider (SP) initiated login.

See [Understanding SAML](https://developer.okta.com/docs/concepts/saml/#understand-sp-initiated-sign-in-flow) for an
in-depth explanation.

### Required String parameter 'RelayState' is not present

See above.
