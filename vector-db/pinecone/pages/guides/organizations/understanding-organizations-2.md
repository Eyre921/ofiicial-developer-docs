---
title: "Understanding organizations"
source: https://docs.pinecone.io/guides/organizations/understanding-organizations
path: guides/organizations/understanding-organizations
---

Learn how Pinecone organizations group projects, share billing, and use organization roles to control member permissions and access to resources.

A Pinecone organization is a set of [projects](/guides/projects/understanding-projects) that use the same billing. Organizations allow one or more users to control billing and project permissions for all of the projects belonging to the organization. Each project belongs to an organization.

<Note>
  While an email address can be associated with multiple organizations, it cannot be used to create more than one organization. For information about managing organization members, see [Manage organization members](/guides/organizations/manage-organization-members).
</Note>

## Projects in an organization

Each organization contains one or more projects that share the same organization owners and billing settings. Each project belongs to exactly one organization. If you need to move a project from one organization to another, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

## Billing settings

All of the projects in an organization share the same billing method and settings. The billing settings for the organization are controlled by the organization owners.

Organization owners can update the billing contact information, update the payment method, and view and download invoices using the [Pinecone console](https://app.pinecone.io/organizations/-/settings/billing).

## Organization roles

Organization owners can manage access to their organizations and projects by assigning roles to organization members and service accounts. A role determines the permissions that a [principal](/guides/production/security-overview#role-based-access-controls-rbac) (a user, service account, or API key) has within Pinecone. The organization roles are as follows:

* **Organization owner** (`OrgOwner`): Full control over the organization, including billing, members, service accounts, security, and every project. Inherits [owner access](/guides/projects/understanding-projects#project-roles) to all projects in the organization.

* **Organization manager** (`OrgManager`): Can view organization details and create projects. Organization managers cannot manage billing, members, service accounts, or organization settings.

* **Organization member** (`OrgMember`): Can view organization details and access the projects they are added to. Organization members cannot create projects or manage organization settings. To grant project access, add the member to one or more projects and assign a [project role](/guides/projects/understanding-projects#project-roles); see [Manage project members](/guides/projects/manage-project-members).

* **Billing admin** (`OrgBillingAdmin`): Can view organization details and manage billing, subscriptions, and usage. Billing admins cannot manage members or organization settings, and they cannot manage projects unless they are also [project owners](/guides/projects/understanding-projects#project-roles).

The following table summarizes the permissions for each organization role:

| Permission                             | Owner | Manager | Member | Billing admin |
| -------------------------------------- | :---: | :-----: | :----: | :-----------: |
| View account details                   |   ✓   |    ✓    |    ✓   |       ✓       |
| Create projects                        |   ✓   |    ✓    |        |               |
| View billing and usage details         |   ✓   |         |        |       ✓       |
| Manage billing details                 |   ✓   |         |        |       ✓       |
| Invite and remove organization members |   ✓   |         |        |               |
| Update organization member roles       |   ✓   |         |        |               |
| Manage service accounts                |   ✓   |         |        |               |
| Configure single sign-on (SSO)         |   ✓   |         |        |               |
| Configure audit logs                   |   ✓   |         |        |               |
| Update organization name               |   ✓   |         |        |               |
| Delete the organization                |   ✓   |         |        |               |

## Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can specify a default role for teammates when they sign up.

<Note>For organizations that use SSO for authentication, console sessions are re-authenticated at least every 24 hours.</Note>

For more information, see [Configure single sign-on](/guides/production/configure-single-sign-on/okta).

<Note>SSO is available on Standard and Enterprise plans.</Note>

## Service accounts

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

[Service accounts](/guides/organizations/manage-service-accounts) enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.

Use service accounts to automate infrastructure management and integrate Pinecone into your deployment workflows, rather than through manual actions in the Pinecone console. Service accounts use the [organization roles](/guides/organizations/understanding-organizations#organization-roles) and [project role](/guides/projects/understanding-projects#project-roles) for permissioning, and provide a secure and auditable way to handle programmatic access.

## See also

* [Manage organization members](/guides/organizations/manage-organization-members)
* [Manage project members](/guides/projects/manage-project-members)
