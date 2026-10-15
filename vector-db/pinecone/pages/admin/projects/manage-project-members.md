---
title: "Manage project members"
source: https://docs.pinecone.io/admin/projects/manage-project-members
path: admin/projects/manage-project-members
---

Add, remove, and update Pinecone project members using role-based access control (RBAC) to manage permissions and project owner roles.

[Organization owners](/admin/organizations/understanding-organizations#organization-roles) or [project owners](/admin/projects/understanding-projects#project-roles) can manage members in a project. Each member is assigned one or more [project roles](/admin/projects/understanding-projects#project-roles) that determine their permissions within the project.

To assign and manage roles programmatically with the Admin API, or to manage roles for service accounts and API keys, see [Manage roles and access](/admin/security/manage-rbac).

<Tip>
  For information about managing members at the organization level, see [Manage organization members](/admin/organizations/manage-organization-members).
</Tip>

## Add members to a project

<Note>
  Project owners can add existing organization members to a project and manage their project roles. Only [organization owners](/admin/organizations/understanding-organizations#organization-roles) can invite people who aren't yet members of the organization.
</Note>

You can add members to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to [**Settings > Access**](https://app.pinecone.io/organizations/-/projects/-/access/members) and select the **Members** tab.
3. Enter the member's email address or name.
4. Select a [**Project role**](/admin/projects/understanding-projects#project-roles) for the member. The role determines the member's permissions within Pinecone.
5. Click **Invite**.

If the person is already a member of your organization, they get access to the project right away. Otherwise, Pinecone emails them an invite, and they join your organization as an organization member, with access to the project, when they accept it.

## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to [**Settings > Access**](https://app.pinecone.io/organizations/-/projects/-/access/members) and select the **Members** tab.
3. In the row of the member you want to edit, click **ellipsis (...) menu > Edit role**.
4. Select a [**Project role**](/admin/projects/understanding-projects#project-roles) for the member.
5. Click **Save**.

## Remove a member

You can remove a member from a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to [**Settings > Access**](https://app.pinecone.io/organizations/-/projects/-/access/members) and select the **Members** tab.
3. In the row of the member you want to remove, click **ellipsis (...) menu > Remove from project**.
4. Click **Remove member**.

<Note>
  To remove yourself from a project, in your user's row, click **ellipsis (...) menu > Leave project** and confirm.
</Note>
