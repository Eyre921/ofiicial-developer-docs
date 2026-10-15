---
title: "Organizations overview"
source: https://docs.pinecone.io/admin/organizations/understanding-organizations
path: admin/organizations/understanding-organizations
---

Learn how Pinecone organizations group projects, share billing, and use organization roles to control member permissions and access to resources.

A Pinecone organization is a set of [projects](/admin/projects/understanding-projects) that use the same billing. Organizations allow one or more users to control billing and project permissions for all of the projects belonging to the organization. Each project belongs to an organization.

<Note>
  An email address can be associated with multiple organizations, but each user can own at most 10 organizations. For information about managing organization members, see [Manage organization members](/admin/organizations/manage-organization-members).
</Note>

## Projects in an organization

Each organization contains one or more projects that share the same organization owners and billing settings. Each project belongs to exactly one organization. If you need to move a project from one organization to another, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

## Billing settings

All of the projects in an organization share the same billing method and settings. The billing settings for the organization are controlled by organization owners and billing admins.

Organization owners and billing admins can update the billing contact information, update the payment method, and view and download invoices using the [Pinecone console](https://app.pinecone.io/organizations/-/settings/billing).

## Organization roles

Organization owners can manage access to their organizations and projects by assigning roles to organization members and service accounts. A role determines the permissions that a [principal](/admin/security/security-overview#role-based-access-controls-rbac) (a user, service account, or API key) has within Pinecone.

* **Organization owner** (`OrgOwner`): Full control over the organization, including billing, members, service accounts, security, and every project. Inherits [owner access](/admin/projects/understanding-projects#project-roles) to all projects in the organization.

* **Organization manager** (`OrgManager`): Can view organization details and create projects. Organization managers can't manage billing, members, service accounts, or organization settings.

* **Organization member** (`OrgMember`): Can view organization details and access the projects they're added to. Organization members can't create projects or manage organization settings. To grant project access, add the member to one or more projects and assign a [project role](/admin/projects/understanding-projects#project-roles). For steps, see [Manage project members](/admin/projects/manage-project-members).

* **Billing admin** (`OrgBillingAdmin`): Can view organization details and manage billing, subscriptions, and usage. Billing admins can't manage members or organization settings, and they can't manage projects unless they're also [project owners](/admin/projects/understanding-projects#project-roles).

| Permission | Owner | Manager | Member | Billing admin |
| - | :-: | :-: | :-: | :-: |
| View account details | ✓ | ✓ | ✓ | ✓ |
| Create projects | ✓ | ✓ | | |
| View billing and usage details | ✓ | | | ✓ |
| Manage billing details | ✓ | | | ✓ |
| Invite and remove organization members | ✓ | | | |
| Update organization member roles | ✓ | | | |
| Manage service accounts | ✓ | | | |
| Configure single sign-on (SSO) | ✓ | | | |
| Configure audit logs | ✓ | | | |
| Update organization name | ✓ | | | |
| Delete the organization | ✓ | | | |

## Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can specify a default role for teammates when they sign up.

<Note>For organizations that use SSO for authentication, console sessions are re-authenticated at least every 24 hours.</Note>

For more information, see [Configure single sign-on](/admin/security/configure-single-sign-on/okta).

<Note>SSO is available on Standard and Enterprise plans.</Note>

## Service accounts

<Note>
  This feature is available on the [Enterprise plan](https://www.pinecone.io/pricing/).
</Note>

[Service accounts](/admin/organizations/manage-service-accounts) enable programmatic access to Pinecone's Admin API, which you can use to create and manage projects and API keys.

Use service accounts to automate infrastructure management and integrate Pinecone into your deployment workflows instead of working manually in the Pinecone console. Service accounts get their permissions from [organization roles](/admin/organizations/understanding-organizations#organization-roles) and [project roles](/admin/projects/understanding-projects#project-roles), and they give you a secure, auditable way to handle programmatic access.

## See also

* [Manage organization members](/admin/organizations/manage-organization-members)
* [Manage project members](/admin/projects/manage-project-members)
