---
title: "Single sign-on (SSO)"
source: https://docs.together.ai/docs/sso
path: docs/sso
---

Connect your Identity Provider for secure, automated team access to Together

Single Sign-On enables your company to authenticate to your Together Organization through your company's existing Identity Provider (IdP) when configured for SSO. Instead of managing separate credentials, Members sign in with the same account they use for everything else at your company.

<Info>
  SSO is available for **Scale and Enterprise** accounts. [Contact sales](https://www.together.ai/contact-sales) to upgrade.
</Info>

## Supported providers

Together supports SSO via **SAML** and **OIDC** protocols with these Identity Providers:

* Google Workspace
* Okta
* Microsoft Entra (Azure AD)
* JumpCloud

For detailed setup instructions per provider, see the guides below:

| Provider         | Protocol | Setup Guide                                                                                                      |
| ---------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| Most IdPs        | SAML     | [SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#saml-\(most-idps\))                     |
| Most IdPs        | OIDC     | [OIDC setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#oidc-\(most-idps\))                     |
| Okta             | SAML     | [Okta SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#okta-saml)                         |
| Okta             | OIDC     | [Okta OIDC setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#okta-oidc)                         |
| Google Workspace | SAML     | [Google Workspace SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#google-workspace-saml) |
| Microsoft Entra  | SAML     | [Microsoft Entra SAML setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#microsoft-entra-saml)   |
| Microsoft Entra  | OIDC     | [Microsoft Entra OIDC setup guide](https://stytch.com/docs/b2b/guides/sso/provider-setup#microsoft-entra-oidc)   |

## What SSO enables

* **Automated provisioning.** Members are added to your [organization](https://api.together.ai/settings/organization/~current/members) automatically when they authenticate through your IdP.
* **Centralized offboarding.** Deactivate a user in your IdP and their Together access is revoked.
* **Shared resources.** SSO members can collaborate on fine-tuned models, inference analytics, clusters, and billing within their [projects](/docs/projects).
* **Audit trail.** Individual authentication means you can track who did what.

## Setting up SSO

Contact [support](https://portal.usepylon.com/together-ai/forms/support-request) or your Account Executive with:

1. Your company's legal name
2. The email domain(s) to associate (e.g., `@yourcompany.com`)
3. Which Identity Provider you use
4. The email address of the initial account owner

Setup typically takes **24 to 48 working hours** from when Together receives your request. Complex configurations (multiple domains, custom attribute mapping) may take longer.

## Migrating from legacy enterprise sign-on

If your team currently uses a shared username/password enterprise account, migrate to SSO. Shared credential accounts will be deprecated in the coming months.

Benefits of migrating:

* Individual accountability (each person has their own login)
* Automated onboarding/offboarding through your IdP
* Stronger security (no shared passwords)
* Access to [role-based permissions](/docs/roles-permissions) and [multi-project support](/docs/projects)

## Session management

Together manages its own session timeouts independently from your IdP's default settings. Session duration and re-authentication requirements are configured on the Together side.

## FAQs

<AccordionGroup>
  <Accordion title="Can I use SSO and email invitations together?">
    No. Organizations use either SSO or invitation-based membership, not both. If SSO is enabled, all members authenticate through your IdP.
  </Accordion>

  <Accordion title="What happens to existing members when I enable SSO?">
    Existing members will need to re-authenticate through your IdP on their next login. Their resources and project membership are preserved.
  </Accordion>

  <Accordion title="Can I configure SSO myself?">
    Not yet. Self-service SSO configuration is on our roadmap. For now, our team handles setup.
  </Accordion>
</AccordionGroup>

## What's coming

* Spend controls per member or project
* Self-service SSO configuration
* SCIM provisioning for automated group and role sync

## Related

<CardGroup>
  <Card title="Together's IAM Model" icon="diagram-project" href="/docs/identity-access-management">
    How users, credentials, and resources fit together
  </Card>

  <Card title="Organizations" icon="building" href="/docs/organizations">
    Manage your org and membership
  </Card>

  <Card title="Roles & Permissions" icon="shield" href="/docs/roles-permissions">
    What Admins, Developers, and Editors can do
  </Card>
</CardGroup>
