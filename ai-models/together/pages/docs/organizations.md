---
title: "Organizations"
source: https://docs.together.ai/docs/organizations
path: docs/organizations
---

Create and manage your Together organization, invite members, and configure billing

An organization is your company's account on Together. It's the top-level container for everything: projects, members, resources, and billing. Every Together account belongs to one organization.

Manage your organization from [**Organization Settings**](https://api.together.ai/settings/organization/~current) in the Together dashboard.

## Organization membership

Members join your organization using either single sign-on (SSO) or invitation-based (OAuth) authentication. These methods are mutually exclusive -- you must choose one or the other.

### Single sign-on (SSO)

If your company uses an Identity Provider (Okta, Google Workspace, Microsoft Entra, JumpCloud) with SSO configured, members authenticate through your IdP and are automatically provisioned into your organization.

See [Single Sign-On (SSO)](/docs/sso) for setup instructions.

### Invitation-based (OAuth)

Admins in paid tier organizations can invite members by email. Here is how:

1. Go to [**Organization > Member Settings**](https://api.together.ai/settings/organization/~current/members).
2. Select **Invite Member**.
3. Enter the user's email address.
4. Select **Send Invitation**.

Invitations expire after **7 days**. The recipient will receive an email with a link to accept. A Together account will be created when they accept. If the user already has an existing Together account, [contact support](https://portal.usepylon.com/together-ai/forms/support-request) for assistance migrating it to your organization.

### Removing members

Admins can remove members at any time:

1. Go to [**Organization > Member Settings**](https://api.together.ai/settings/organization/~current/members).
2. Find the member you want to remove.
3. Select the three-dot menu next to their name.
4. Select **Remove Member**.

<Warning>
  Removing a member revokes their access to all projects and resources in the organization. Resources they created (models, endpoints, files) remain in the project.
</Warning>

<Info>
  If your organization uses SSO, a removed member may be re-provisioned automatically the next time they authenticate through your IdP. To fully revoke access, remove or deactivate the user in your Identity Provider.
</Info>

## Roles

Organizations support two roles: **admin** and **developer**. For a full breakdown of what each role can do across the platform, see [Roles & Permissions](/docs/roles-permissions).

<Note>
  Roles and permissions are being progressively rolled out across products and services. Today, the primary distinction is that admins can manage infrastructure and team membership, while developers can use resources but not modify them. See [Roles & Permissions](/docs/roles-permissions) for details.
</Note>

## Projects

Projects are isolated workspaces within your organization. They scope resources, API keys, and membership so teams can work independently.

Every organization starts with a [default project](/docs/projects#default-project). All members are automatically added to it when they join. Create additional projects to separate resources by team, environment, or workload.

For full details on creating and managing projects, see [Projects](/docs/projects).

## Privacy

Privacy toggles for prompt history, training opt-in, and passthrough models are on the main [Organization Settings](https://api.together.ai/settings/organization/~current) page. Only organization admins can change them. See [Privacy and security](/docs/privacy-and-security) for what each toggle controls.

## Billing

[Billing](https://api.together.ai/settings/organization/~current/billing) is consolidated at the organization level. All usage across all projects and members rolls up to a single bill. Individual members are not billed separately.

Members can jointly purchase and spend credits. For details, see [Credits & Billing](/docs/billing-credits).
