---
title: "Organizations"
source: https://docs.together.ai/docs/organizations
path: docs/organizations
---

Create and manage your Together Organization, invite Members, and configure billing

An Organization is your company's account on Together. It's the top-level container for everything: Projects, Members, resources, and billing. Every Together account belongs to one Organization.

Manage your Organization from [**Organization Settings**](https://api.together.ai/settings/organization/~current) in the Together dashboard.

## Organization Membership

Members join your Organization using either Single Sign-On (SSO) or Invitation-Based (OAuth) authentication. These methods are mutually exclusive -- you must choose one or the other.

### Single Sign-On (SSO)

If your company uses an Identity Provider (Okta, Google Workspace, Microsoft Entra, JumpCloud) with SSO configured, Members authenticate through your IdP and are automatically provisioned into your Organization.

See [Single Sign-On (SSO)](/docs/sso) for setup instructions.

### Invitation-Based (OAuth)

Admins in paid tier Organizations can invite Members by email. Here is how:

1. Go to [**Organization > Member Settings**](https://api.together.ai/settings/organization/~current/members)
2. Select **Invite Member**
3. Enter the user's email address
4. Select **Send Invitation**

Invitations expire after **7 days**. The recipient will receive an email with a link to accept. A Together account will be created when they accept. If the user already has an existing Together account, [contact support](https://portal.usepylon.com/together-ai/forms/support-request) for assistance migrating it to your Organization.

### Removing Members

Admins can remove Members at any time:

1. Go to [**Organization > Member Settings**](https://api.together.ai/settings/organization/~current/members)
2. Find the Member you want to remove
3. Click the three-dot menu next to their name
4. Select **Remove Member**

<Warning>
  Removing a Member revokes their access to all Projects and resources in the Organization. Resources they created (models, endpoints, files) remain in the Project.
</Warning>

<Info>
  If your Organization uses SSO, a removed Member may be re-provisioned automatically the next time they authenticate through your IdP. To fully revoke access, remove or deactivate the user in your Identity Provider.
</Info>

## Roles

Organizations support two roles: **Admin** and **Developer**. For a full breakdown of what each role can do across the platform, see [Roles & Permissions](/docs/roles-permissions).

<Note>
  Roles and permissions are being progressively rolled out across products and services. Today, the primary distinction is that Admins can manage infrastructure and team membership, while Developers can use resources but not modify them. See [Roles & Permissions](/docs/roles-permissions) for details.
</Note>

## Projects

Projects are isolated workspaces within your Organization. They scope resources, API keys, and membership so teams can work independently.

Every Organization starts with a [**Default Project**](/docs/projects#default-project). All Members are automatically added to it when they join.

For Organizations that need to separate resources by team, environment, or workload, multi-Project support is available in early access. [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) to enable it.

For full details on creating and managing Projects, see [Projects](/docs/projects).

## Privacy

Privacy toggles for prompt history, training opt-in, and passthrough models are on the main [Organization Settings](https://api.together.ai/settings/organization/~current) page. Only organization admins can change them. See [Privacy and security](/docs/privacy-and-security) for what each toggle controls.

## Billing

[Billing](https://api.together.ai/settings/organization/~current/billing) is consolidated at the Organization level. All usage across all Projects and Members rolls up to a single bill. Individual Members are not billed separately.

Members can jointly purchase and spend credits. For details, see [Credits & Billing](/docs/billing-credits).
