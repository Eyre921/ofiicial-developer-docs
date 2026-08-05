---
title: "Roles & permissions (RBAC)"
source: https://docs.together.ai/docs/roles-permissions
path: docs/roles-permissions
---

Understand Organization and Project role-based access control (RBAC), including Admin, Developer, and Editor roles, and what each can do across Together

Together uses role-based access control (RBAC) at both the [Organization](/docs/organizations) and [Project](/docs/projects) level. Every Member of an Organization is assigned an Organization role, and every Collaborator of a Project is assigned a Project role.

<Note>
  Roles and permissions are being progressively rolled out across Together's products and services. This page will be updated as more granular controls become available.
</Note>

## Organization roles

Organizations have two roles: **Admin** and **Developer**.

| Role          | Scope           | Description                                                                                    |
| ------------- | --------------- | ---------------------------------------------------------------------------------------------- |
| **Admin**     | Org-wide        | Full access to all Organization settings, billing, Members, and Projects.                      |
| **Developer** | Org (read-only) | Can see Organization-level info and the Projects list. Joins Projects as an Editor by default. |

<Info>
  The creator ("Owner") of an Organization is a special Admin. They cannot be removed from the Organization, their role cannot be changed from Admin, and they cannot delete their own account.
</Info>

### Organization permissions

| Scope                        | Admin | Developer |
| ---------------------------- | ----- | --------- |
| Organization settings: Read  | Yes   | Yes       |
| Organization settings: Write | Yes   | No        |
| Billing: Read                | Yes   | Yes       |
| Billing: Write               | Yes   | No        |
| Projects: Read               | Yes   | Yes       |
| Projects: Create             | Yes   | No        |
| Members: Read                | Yes   | Yes       |
| Members: Invite              | Yes   | No        |
| Members: Remove              | Yes   | No        |
| Members: Manage roles        | Yes   | No        |

## Project roles

Projects have two roles: **Admin** and **Editor**.

| Role       | Description                                                                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Admin**  | Can access and update Project settings. Organization Admins are granted Project Admin in any Project they join. Organization Developers can be promoted to Project Admin by an existing Project Admin. |
| **Editor** | Can use the Project's resources but cannot access or update Project settings. Organization Developers are added to Projects as Editors by default.                                                     |

### Project permissions

| Scope                       | Admin | Editor |
| --------------------------- | ----- | ------ |
| Project settings: Read      | Yes   | Yes    |
| Project settings: Write     | Yes   | No     |
| Project cost analytics      | Yes   | Yes    |
| API keys: Read              | Yes   | Yes    |
| API keys: Create            | Yes   | Yes    |
| API keys: Revoke            | Yes   | Yes    |
| Collaborators: Read         | Yes   | Yes    |
| Collaborators: Add          | Yes   | No     |
| Collaborators: Remove       | Yes   | No     |
| Collaborators: Manage roles | Yes   | No     |

## External collaborators (beta)

<Info>
  This feature is in beta. [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) to enable it.
</Info>

An External Collaborator is someone who participates in a Project without being a Member of the Project's parent Organization. They can be assigned any Project role but have no Organization-level permissions beyond seeing the Organization's name.

What External Collaborators can do:

* Full access to any Project they have been explicitly added to (based on their Project role)
* View their own profile settings

What they cannot do:

* Access billing settings
* View the Organization Members list
* See Organization-level settings

## Product-specific permissions

### GPU clusters (control plane)

The control plane covers infrastructure operations: creating, modifying, and deleting clusters and volumes.

| Action                          | Admin | Editor |
| ------------------------------- | ----- | ------ |
| Create clusters                 | Yes   | No     |
| Delete clusters                 | Yes   | No     |
| Scale clusters                  | Yes   | No     |
| Modify cluster configurations   | Yes   | No     |
| Create and resize volumes       | Yes   | No     |
| View cluster status and details | Yes   | Yes    |
| View volume details             | Yes   | Yes    |

### GPU clusters (data plane)

The data plane covers using clusters for actual work: running jobs, accessing nodes, executing workloads.

| Action                             | Admin | Editor |
| ---------------------------------- | ----- | ------ |
| SSH into cluster nodes             | Yes   | Yes    |
| Run Kubernetes workloads (kubectl) | Yes   | Yes    |
| Access Kubernetes Dashboard        | Yes   | Yes    |
| Submit Slurm jobs                  | Yes   | Yes    |
| Read and write to volumes          | Yes   | Yes    |

<Info>
  **Control plane vs data plane:** Think of the control plane as "managing the infrastructure" and the data plane as "using the infrastructure." Editors have full access to use clusters for their work. Their only restriction is that they cannot create, delete, or resize clusters.
</Info>

### Fine-tuning, endpoints, serverless inference & other products

Role-based access control for fine-tuning, endpoints, serverless inference, and other Together products is still being rolled out. Today, all Project Collaborators (both Admin and Editor) have full access to these services.

## What's coming

Together is actively rolling out RBAC across more services. Granular permissions for fine-tuning, dedicated model inference, and serverless inference are coming soon.

<Note>
  Have a specific RBAC requirement? [Let us know](https://portal.usepylon.com/together-ai/forms/support-request). Customer feedback directly shapes Together's roadmap.
</Note>

## Related

<CardGroup>
  <Card title="Projects" icon="folder" href="/docs/projects">
    Create workspaces and manage team access
  </Card>

  <Card title="Together's IAM Model" icon="diagram-project" href="/docs/identity-access-management">
    How users, credentials, and resources are organized
  </Card>
</CardGroup>
