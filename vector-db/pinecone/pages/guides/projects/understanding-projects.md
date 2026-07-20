---
title: "Understanding projects"
source: https://docs.pinecone.io/guides/projects/understanding-projects
path: guides/projects/understanding-projects
---

Learn about projects, environments, and member roles.

A Pinecone project belongs to an [organization](/guides/organizations/understanding-organizations) and contains a number of [indexes](/guides/index-data/indexing-overview) and users. Only a user who belongs to the project can access the indexes in that project. Each project also has at least one project owner.

## Project environments

You choose a cloud environment for each index in a project. This makes it easy to manage related resources across environments and use the same API key to access them.

## Project roles

If you are an [organization owner](/guides/organizations/understanding-organizations#organization-roles) or project owner, you can manage who has access to a project. You grant a principal—a user, [service account](/guides/projects/manage-service-accounts), or [API key](/guides/projects/manage-api-keys)—access by assigning it one or more roles scoped to the project. A principal can hold more than one role, and its effective permissions are the union of all the roles it holds.

The roles you assign depend on the principal type:

* **Users and service accounts** are typically assigned a membership role—`ProjectOwner`, `ProjectManager`, or `ProjectMember`—optionally combined with one or more access roles.
* **API keys** are typically assigned `ProjectEditor` or `ProjectViewer`, or one or more access roles. API keys cannot be assigned `ProjectOwner`, `ProjectManager`, or `ProjectMember`, which include access to project settings, members, and API keys. To access these items programmatically, use a [service account](/guides/projects/manage-service-accounts).

The following project roles are available:

| Role                                        | Permissions                                                                                                                     |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------ |
| Project owner (`ProjectOwner`)              | Full access to the project, including members, API keys, and all resources and data.                                            |
| Project manager (`ProjectManager`)          | Read and write access to all resources and data. Read-only access to project settings, members, and API keys.                   |
| Project member (`ProjectMember`)            | Read-only access to project settings, members, and API keys. No resource or data access unless granted additional access roles. |
| Project editor (`ProjectEditor`)            | Read and write access to all resources and data. No access to project settings, members, or API keys.                           |
| Project viewer (`ProjectViewer`)            | Read-only access to all resources and data. No access to project settings, members, or API keys.                                |
| Control plane editor (`ControlPlaneEditor`) | Read and write access to control plane resources, such as indexes, assistants, backups, and collections.                        |
| Control plane viewer (`ControlPlaneViewer`) | Read-only access to control plane resources.                                                                                    |
| Data plane editor (`DataPlaneEditor`)       | Read and write access to data plane data, such as records, namespaces, and assistant files.                                     |
| Data plane viewer (`DataPlaneViewer`)       | Read-only access to data plane data.                                                                                            |

The following table details the project settings, resource, and data permissions for the owner, manager, and member roles:

| Permission                                                                  | Owner | Manager | Member |
| :-------------------------------------------------------------------------- | :---: | :-----: | :----: |
| View project settings, members, and API keys                                |   ✓   |    ✓    |    ✓   |
| Update project settings and configuration                                   |   ✓   |         |        |
| Delete the project                                                          |   ✓   |         |        |
| Manage project members and their roles                                      |   ✓   |         |        |
| Create and delete API keys                                                  |   ✓   |         |        |
| View indexes, assistants, backups, and collections                          |   ✓   |    ✓    |        |
| Create, configure, and delete indexes, assistants, backups, and collections |   ✓   |    ✓    |        |
| Read index data (query, fetch, list, and view stats)                        |   ✓   |    ✓    |        |
| Write index data (upsert, update, delete, and import)                       |   ✓   |    ✓    |        |

Specific to pod-based indexes:

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

| Permission                | Owner | Manager | Member |
| :------------------------ | :---: | :-----: | :----: |
| View project pod limits   |   ✓   |    ✓    |    ✓   |
| Update project pod limits |   ✓   |         |        |
| Update index size         |   ✓   |    ✓    |        |

<Note>
  Pod-based indexes do not support role-based access control and will always grant data plane read and write access to project members.
</Note>

### Role permissions

The following tables detail the operations covered by the general, control plane, and data plane roles:

#### General permissions

| Role            | Permissions                                     |
| :-------------- | :---------------------------------------------- |
| `ProjectEditor` | Permissions to read and write all project data. |
| `ProjectViewer` | Permissions to read all project data.           |

#### Control plane permissions

| Role                 | Permissions                                                                                                 |
| :------------------- | :---------------------------------------------------------------------------------------------------------- |
| `ControlPlaneEditor` | Permissions to list, describe, create, delete, and configure indexes, backups, collections, and assistants. |
| `ControlPlaneViewer` | Permissions to list and describe indexes, backups, collections, and assistants.                             |
| None                 | No control plane permissions.                                                                               |

#### Data plane permissions

| Role              | Permissions                                                                                                                                                                                                                                                                                                            |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DataPlaneEditor` | <ul><li>Indexes: Permissions to query, import, fetch, add, update, and delete index data.</li><li>Pinecone Assistant: Permissions to add, list, view, and delete files; chat with an assistant, and evaluate responses.</li><li>Pinecone Inference: Permissions to generate embeddings and rerank documents.</li></ul> |
| `DataPlaneViewer` | <ul><li>Indexes: Permissions to query, fetch, list ID, and view stats.</li><li>Pinecone Assistant: Permissions to list and view files, chat with an assistant, and evaluate responses.</li><li>Pinecone Inference: Permissions to generate embeddings and rerank documents.</li></ul>                                  |
| None              | No data plane permissions.                                                                                                                                                                                                                                                                                             |

## API keys

Each Pinecone [project](/guides/projects/understanding-projects) has one or more API keys. In order to [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.

For more information, see [Manage API keys](/guides/projects/manage-api-keys).

## Project IDs

Each Pinecone project has a unique project ID.

To find the ID of a project, go to the project list in the [Pinecone console](https://app.pinecone.io/organizations/-/projects).

## See also

* [Understanding organizations](/guides/organizations/understanding-organizations)
* [Manage organization members](/guides/organizations/manage-organization-members)
