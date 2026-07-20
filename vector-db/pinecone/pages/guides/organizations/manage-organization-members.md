---
title: "Manage organization members"
source: https://docs.pinecone.io/guides/organizations/manage-organization-members
path: guides/organizations/manage-organization-members
---

Add and manage organization members and roles.

This page shows how [organization owners](/guides/organizations/understanding-organizations#organization-roles) can add and manage organization members.

To assign and manage roles programmatically with the Admin API, or to manage roles for service accounts and API keys, see [Manage roles and access](/guides/production/manage-rbac).

<Tip>
  For information about managing members at the **project-level**, see [Manage project members](/guides/projects/manage-project-members).
</Tip>

## Add a member to an organization

You can add members to your organization in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the **Invite by email** field, enter the member's email address.
3. Choose an [**Organization role**](/guides/organizations/understanding-organizations#organization-roles) for the member. The role determines the member's permissions within Pinecone.
4. Click **Invite**.

When you invite a member to join your organization, Pinecone sends them an email containing a link that enables them to gain access to the organization or project. If they already have a Pinecone account, they still receive an email, but they can also immediately view the project.

## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member whose role you want to change, click **ellipsis (...) menu > Edit role**.
3. Select an [**Organization role**](/guides/organizations/understanding-organizations#organization-roles) for the member.
4. Click **Edit role**.

## Remove a member

You can remove a member from your organization in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member you want to remove, click **ellipsis (...) menu > Remove member**.
3. Click **Remove Member**.

<Note>
  To remove yourself from an organization, click the **Leave organization** button in your user's row and confirm.
</Note>
