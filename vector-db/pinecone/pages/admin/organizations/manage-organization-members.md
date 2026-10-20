---
title: "Manage organization members"
source: https://docs.pinecone.io/admin/organizations/manage-organization-members
path: admin/organizations/manage-organization-members
---

Add, invite, and manage members in your Pinecone organization, including assigning organization roles, changing permissions, and removing users.

This page shows how [organization owners](/admin/organizations/understanding-organizations#organization-roles) can add and manage organization members.

To assign and manage roles programmatically with the Admin API, or to manage roles for service accounts and API keys, see [Manage roles and access](/admin/security/manage-rbac).

> [!TIP]
>
> For information about managing members at the project level, see [Manage project members](/admin/projects/manage-project-members).

## Add a member to an organization

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the **Invite by email** field, enter the member's email address.
3. Choose an [**Organization role**](/admin/organizations/understanding-organizations#organization-roles) for the member. The role determines the member's permissions within Pinecone.
4. Click **Invite**.

When you invite a member, Pinecone emails them an invite link, whether or not they already have a Pinecone account. They join the organization when they accept the invite. Until then, the invite appears in the **Invites** list on the **Members** page.

## Change a member's role

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member whose role you want to change, click **ellipsis (...) menu > Edit role**.
3. Select an [**Organization role**](/admin/organizations/understanding-organizations#organization-roles) for the member.
4. Click **Save**.

## Remove a member

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member you want to remove, click **ellipsis (...) menu > Remove member**.
3. Click **Remove member**.

> [!NOTE]
>
> To remove yourself from an organization, in your user's row, click **ellipsis (...) menu > Leave organization** and confirm. If you're the only owner, you can't leave.
