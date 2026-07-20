---
title: "Manage roles and access"
source: https://docs.pinecone.io/guides/production/manage-rbac
path: guides/production/manage-rbac
---

Assign and manage roles for users, service accounts, and API keys using the Pinecone console or the Admin API.

Pinecone uses [role-based access controls (RBAC)](/guides/production/security-overview#role-based-access-controls-rbac) to manage access to resources. Users, service accounts, and API keys are all *principals*, and a principal's access is determined by the *roles* assigned to it for a *resource* (an organization or a project).

This page shows how to assign and manage roles in the [Pinecone console](https://app.pinecone.io) and programmatically with the Admin API.

<Note>
  For the roles available at each scope and the permissions they grant, see [Organization roles](/guides/organizations/understanding-organizations#organization-roles) and [Project roles](/guides/projects/understanding-projects#project-roles).
</Note>

## Common role assignments

A user must have an organization role to belong to the organization, and gains access to a project through one or more project roles. A principal's effective permissions are the union of all the roles it holds, so you can combine roles to grant exactly the access a user needs.

The following table maps common scenarios to the roles to assign:

| Scenario                                                           | Organization role | Project role(s)                                                                       |
| :----------------------------------------------------------------- | :---------------- | :------------------------------------------------------------------------------------ |
| Administer the organization and every project                      | `OrgOwner`        | None (inherits owner access to all projects)                                          |
| Create and manage projects, but not billing or members             | `OrgManager`      | Assign per project as needed                                                          |
| Manage billing, subscriptions, and usage                           | `OrgBillingAdmin` | None                                                                                  |
| Lead a single project, including its members and API keys          | `OrgMember`       | `ProjectOwner`                                                                        |
| Build and query in a project, without managing members or API keys | `OrgMember`       | `ProjectManager`                                                                      |
| Read and write index data only                                     | `OrgMember`       | `ProjectMember` and `DataPlaneEditor`                                                 |
| Read-only access to a project's resources and data                 | `OrgMember`       | `ProjectMember`, `ControlPlaneViewer`, and `DataPlaneViewer`                          |
| Work across two projects at different access levels                | `OrgMember`       | `ProjectManager` on one project and `ProjectMember` with `DataPlaneViewer` on another |

<Note>
  Assigning an organization role adds the user to the organization; assigning a project role grants access to that specific project. To assign these roles in the console, see [Manage organization members](/guides/organizations/manage-organization-members) and [Manage project members](/guides/projects/manage-project-members).
</Note>

### Invite a developer to a project

Invite a user as an organization member and grant them the `ProjectManager` role so they can build and query in a single project without managing its members or API keys.

In the console, add the user from [Manage project members](/guides/projects/manage-project-members) and select the **Project manager** role. With the Admin API, include both roles in the `role_bindings` array when you invite the user:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/invites" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "email": "developer@example.com",
    "role_bindings": [
      {
        "resource_type": "organization",
        "role": "OrgMember"
      },
      {
        "resource_type": "project",
        "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
        "role": "ProjectManager"
      }
    ]
  }'
```

For more information, see [Assign roles when creating a principal](#assign-roles-when-creating-a-principal).

### Grant an existing user read-only data access

To give a user who is already in your organization read-only access to a project's data, assign the `ProjectMember` role for baseline project access and the `DataPlaneViewer` role for read-only data. Each role binding is a separate request.

First, add the user to the project with the `ProjectMember` role:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/role-bindings" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "principal_type": "user",
    "principal_id": "c7b1f0a2-3d4e-5f6a-7b8c-9d0e1f2a3b4c",
    "resource_type": "project",
    "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
    "role": "ProjectMember"
  }'
```

Then, grant read-only data access with the `DataPlaneViewer` role:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/role-bindings" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "principal_type": "user",
    "principal_id": "c7b1f0a2-3d4e-5f6a-7b8c-9d0e1f2a3b4c",
    "resource_type": "project",
    "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
    "role": "DataPlaneViewer"
  }'
```

### Extend a user's access with an additional role

Because effective permissions are the union of all roles, you can broaden access by adding another role rather than replacing the existing one. The user from the previous example holds `ProjectMember` and `DataPlaneViewer`; add `ControlPlaneViewer` to also allow read-only access to the project's indexes, assistants, backups, and collections:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/role-bindings" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "principal_type": "user",
    "principal_id": "c7b1f0a2-3d4e-5f6a-7b8c-9d0e1f2a3b4c",
    "resource_type": "project",
    "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
    "role": "ControlPlaneViewer"
  }'
```

The user now holds `ProjectMember`, `DataPlaneViewer`, and `ControlPlaneViewer` on the project, giving read-only access to all of its resources and data. For more information, see [Create a role binding](#create-a-role-binding).

## Manage roles in the console

You can assign and change roles when you manage principals in the console:

* [Manage organization members](/guides/organizations/manage-organization-members)
* [Manage project members](/guides/projects/manage-project-members)
* [Manage organization service accounts](/guides/organizations/manage-service-accounts) and [project service accounts](/guides/projects/manage-service-accounts)
* [Manage API keys](/guides/projects/manage-api-keys)

## Manage roles with the Admin API

The Admin API represents each role assignment as a *role binding* that grants one role to one principal for one resource scope. You can assign roles when you create a principal, or manage role bindings directly after creation.

<Note>
  An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to authenticate with the Admin API.
</Note>

### Assign roles when creating a principal

When you invite a user or create a service account, grant roles with the `role_bindings` field. Set `resource_type` to `organization` or `project`; for `project` scope, include the project's `resource_id`.

Invite a user as an organization member with a project role:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/invites" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "email": "newhire@example.com",
    "role_bindings": [
      {
        "resource_type": "organization",
        "role": "OrgMember"
      },
      {
        "resource_type": "project",
        "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
        "role": "ProjectMember"
      }
    ]
  }'
```

Create a service account with an access role:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/service-accounts" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "name": "ci-prod",
    "role_bindings": [
      {
        "resource_type": "project",
        "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
        "role": "DataPlaneEditor"
      }
    ]
  }'
```

For API keys, assign [project roles](/guides/projects/understanding-projects#project-roles) with the `roles` field instead. For more information, see [Manage API keys](/guides/projects/manage-api-keys).

### Create a role binding

To grant a role to an existing principal, create a role binding:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/role-bindings" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  -d '{
    "principal_type": "service_account",
    "principal_id": "f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "resource_type": "project",
    "resource_id": "a2f7dddb-1597-4eff-9f71-535fde243f58",
    "role": "DataPlaneEditor"
  }'
```

For more information, see [Create a role binding](/reference/api/2026-04/admin/create_role_binding).

### List role bindings

Role bindings are not included in the responses for users, invites, or service accounts. To list the roles assigned to a principal, filter by `principal_type` and `principal_id`:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl "https://api.pinecone.io/admin/role-bindings?principal_type=service_account&principal_id=f8a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
```

For more information, see [List role bindings](/reference/api/2026-04/admin/list_role_bindings) and [Fetch a role binding](/reference/api/2026-04/admin/fetch_role_binding).

### Delete a role binding

To revoke a role, delete its role binding:

```bash curl theme={null}
PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

curl -X DELETE "https://api.pinecone.io/admin/role-bindings/9a8e3528-b9c0-4358-84ce-84c28e91b566" \
  -H "Accept: application/json" \
  -H "X-Pinecone-Api-Version: 2026-04" \
  -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
```

<Warning>
  You cannot delete the last `OrgOwner` role binding for an organization. An organization must always have at least one owner.
</Warning>

For more information, see [Delete a role binding](/reference/api/2026-04/admin/delete_role_binding).
