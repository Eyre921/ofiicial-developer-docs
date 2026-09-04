---
title: "Manage project members"
source: https://docs.pinecone.io/guides/assistant/admin/manage-project-members
path: guides/assistant/admin/manage-project-members
---

Add users to a Pinecone project, assign project owner or user roles, edit permissions, and remove members to control access to indexes and API keys.

[Organization owners](/guides/assistant/admin/organizations-overview#organization-roles) or [project owners](/guides/assistant/admin/projects-overview#project-roles) can manage members in a project. Each member is assigned one or more [project roles](/guides/assistant/admin/projects-overview#project-roles) that determine their permissions within the project.

To assign and manage roles programmatically with the Admin API, or to manage roles for service accounts and API keys, see [Manage roles and access](/guides/assistant/admin/manage-rbac).

<Tip>
  For information about managing members at the **organization-level**, see [Manage organization members](/guides/assistant/admin/manage-organization-members).
</Tip>

## Add members to a project

<Note>
  Project owners can add existing organization members to a project and manage their project roles. Only [organization owners](/guides/assistant/admin/organizations-overview#organization-roles) can invite people who are not yet members of the organization.
</Note>

You can add members to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. Enter the member's email address or name.
4. Select a [**Project role**](/guides/assistant/admin/projects-overview#project-roles) for the member. The role determines the member's permissions within Pinecone.
5. Click **Invite**.

When you invite a member to join your project, Pinecone sends them an email containing a link that enables them to gain access to the project. If they already have a Pinecone account, they still receive an email, but they can also immediately view the project.

## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. In the row of the member you want to edit, click **ellipsis (...) menu > Edit role**.
4. Select a [**Project role**](/guides/assistant/admin/projects-overview#project-roles) for the member.
5. Click **Edit role**.

## Remove a member

You can remove a member from a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. In the row of the member you want to remove, click **ellipsis (...) menu > Remove member**.
4. Click **Remove member**.

<Note>
  To remove yourself from a project, click the **Leave project** button in your user's row and confirm.
</Note>
