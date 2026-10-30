---
title: "Projects overview"
source: https://docs.pinecone.io/admin/projects/understanding-projects
path: admin/projects/understanding-projects
---

Learn how Pinecone projects organize indexes, cloud environments, API keys, and members, including project roles and per-role permission summaries.

A Pinecone project belongs to an [organization](/admin/organizations/understanding-organizations) and contains [indexes](/guides/index-data/indexing-overview), [assistants](/guides/assistant/overview), and users. Only a user who belongs to the project can access the indexes and assistants in that project. Each project also has at least one project owner.

## Project environments

You choose a cloud environment for each index in a project. This lets you manage related resources across environments and access them with the same API key.

## Project roles

If you're an [organization owner](/admin/organizations/understanding-organizations#organization-roles) or project owner, you can manage who has access to a project. To grant a principal (a user, [service account](/admin/projects/manage-service-accounts), or [API key](/admin/projects/manage-api-keys)) access, assign it one or more roles scoped to the project. A principal can hold more than one role, and its effective permissions are the union of all the roles it holds.

The roles you assign depend on the principal type:

* **Users and service accounts** are typically assigned a membership role (`ProjectOwner`, `ProjectManager`, or `ProjectMember`), optionally combined with one or more access roles.
* **API keys** are typically assigned `ProjectEditor` or `ProjectViewer`, or one or more access roles. API keys can't be assigned `ProjectOwner`, `ProjectManager`, or `ProjectMember`, which include access to project settings, members, and API keys. To access these items programmatically, use a [service account](/admin/projects/manage-service-accounts).

| Role | Permissions |
| :- | :- |
| Project owner (`ProjectOwner`) | Full access to the project, including members, API keys, and all resources and data. |
| Project manager (`ProjectManager`) | Read and write access to all resources and data. Read-only access to project settings, members, and API keys. |
| Project member (`ProjectMember`) | Read-only access to project settings, members, and API keys. No resource or data access unless granted additional access roles. |
| Project editor (`ProjectEditor`) | Read and write access to all resources and data. No access to project settings, members, or API keys. |
| Project viewer (`ProjectViewer`) | Read-only access to all resources and data. No access to project settings, members, or API keys. |
| Control plane editor (`ControlPlaneEditor`) | Read and write access to control plane resources, such as indexes, assistants, backups, and collections. |
| Control plane viewer (`ControlPlaneViewer`) | Read-only access to control plane resources. |
| Data plane editor (`DataPlaneEditor`) | Read and write access to data plane data, such as records, namespaces, and assistant files. |
| Data plane viewer (`DataPlaneViewer`) | Read-only access to data plane data. |

The owner, manager, and member roles have these project settings, resource, and data permissions:

| Permission | Owner | Manager | Member |
| :- | :-: | :-: | :-: |
| View project settings, members, and API keys | ✓ | ✓ | ✓ |
| Update project settings and configuration | ✓ | | |
| Delete the project | ✓ | | |
| Manage project members and their roles | ✓ | | |
| Create and delete API keys | ✓ | | |
| View indexes, assistants, backups, and collections | ✓ | ✓ | |
| Create, configure, and delete indexes, assistants, backups, and collections | ✓ | ✓ | |
| Read index data (query, fetch, list, and view stats) | ✓ | ✓ | |
| Write index data (upsert, update, delete, and import) | ✓ | ✓ | |

For pod-based indexes, the roles have these additional permissions:

> [!WARNING]
>
> Pod-based indexes are legacy. Customers who signed up for a Standard or Enterprise plan on or after August 18, 2025 cannot create them. [Create a serverless index](/guides/index-data/create-an-index) instead. Serverless indexes use on-demand read capacity by default, or [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview) for sustained high query rates and workloads of millions of records or more.

| Permission | Owner | Manager | Member |
| :- | :-: | :-: | :-: |
| View project pod limits | ✓ | ✓ | ✓ |
| Update project pod limits | ✓ | | |
| Update index size | ✓ | ✓ | |

> [!NOTE]
>
> Pod-based indexes don't support role-based access control and always grant data plane read and write access to project members.

### Role permissions

These tables list the operations each general, control plane, and data plane role covers:

#### General permissions

| Role | Permissions |
| :- | :- |
| `ProjectEditor` | Permissions to read and write all project data. |
| `ProjectViewer` | Permissions to read all project data. |

#### Control plane permissions

| Role | Permissions |
| :- | :- |
| `ControlPlaneEditor` | Permissions to list, describe, create, delete, and configure indexes, backups, collections, and assistants. |
| `ControlPlaneViewer` | Permissions to list and describe indexes, backups, collections, and assistants. |
| None | No control plane permissions. |

#### Data plane permissions

| Role | Permissions |
| :- | :- |
| `DataPlaneEditor` | <ul><li>Indexes: Permissions to query, import, fetch, add, update, and delete index data.</li><li>Pinecone Assistant: Permissions to add, list, view, and delete files; chat with an assistant, and evaluate responses.</li><li>Standalone embedding and reranking: Permissions to generate embeddings and rerank documents.</li></ul> |
| `DataPlaneViewer` | <ul><li>Indexes: Permissions to query, fetch, list ID, and view stats.</li><li>Pinecone Assistant: Permissions to list and view files, chat with an assistant, and evaluate responses.</li><li>Standalone embedding and reranking: Permissions to generate embeddings and rerank documents.</li></ul> |
| None | No data plane permissions. |

## API keys

Each Pinecone [project](/admin/projects/understanding-projects) has one or more API keys. To [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.

For more information, see [Manage API keys](/admin/projects/manage-api-keys).

## Project IDs

Each Pinecone project has a unique project ID.

To find the ID of a project, go to the project list in the [Pinecone console](https://app.pinecone.io/organizations/-/projects).

## See also

* [Organizations overview](/admin/organizations/understanding-organizations)
* [Manage organization members](/admin/organizations/manage-organization-members)
