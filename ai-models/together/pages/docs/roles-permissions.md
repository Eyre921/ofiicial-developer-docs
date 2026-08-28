---
title: "Roles & permissions (RBAC)"
source: https://docs.together.ai/docs/roles-permissions
path: docs/roles-permissions
---

Understand organization and project role-based access control (RBAC), including the admin, developer, and editor roles, and what each can do across Together

Together uses role-based access control (RBAC) at both the [organization](/docs/organizations) and [project](/docs/projects) level. Every member of an organization is assigned an organization role, and every collaborator of a project is assigned a project role.

<Note>
  Roles and permissions are being progressively rolled out across Together's products and services. This page will be updated as more granular controls become available.
</Note>

## Organization roles

Organizations have two roles: **admin** and **developer**.

| Role          | Scope           | Description                                                                                                                                                                      |
| ------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **admin**     | Org-wide        | Full access to all organization settings, billing, members, and projects. Can see and join any project, regardless of its visibility.                                            |
| **developer** | Org (read-only) | Can see organization-level info and the list of open and closed projects. Joins open projects as an editor by default. Must be added to closed and private projects by an admin. |

<Info>
  The creator ("owner") of an organization is a special admin. They cannot be removed from the organization, their role cannot be changed from admin, and they cannot delete their own account.
</Info>

### Organization permissions

| Scope                             | Admin | Developer |
| --------------------------------- | ----- | --------- |
| Organization settings: Read       | Yes   | Yes       |
| Organization settings: Write      | Yes   | No        |
| Billing: Read                     | Yes   | Yes       |
| Billing: Write                    | Yes   | No        |
| Organization cost analytics: Read | Yes   | No        |
| Projects: Create                  | Yes   | No        |
| Members: Read                     | Yes   | Yes       |
| Members: Invite                   | Yes   | No        |
| Members: Remove                   | Yes   | No        |
| Members: Manage roles             | Yes   | No        |

### Roles and project visibility

A project's [visibility](/docs/projects#project-visibility) (open, closed, or private) controls which members can discover and join it. Your organization role affects what you can see:

* Organization admins can see and join any project, but must join a closed or private project before accessing its resources or settings.
* Organization developers must be added to a closed or private project by an admin.

## Project roles

Projects have two roles: **admin** and **editor**.

| Role       | Description                                                                                                                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **admin**  | Can access and update project settings, including the project's visibility and collaborators. Organization admins are granted project admin in any project they join. Organization developers can be promoted to project admin by an existing project admin. |
| **editor** | Can use the project's resources but cannot update project settings, change its visibility, or manage collaborators. Organization developers are added to projects as editors by default.                                                                     |

### Project permissions

| Scope                              | Admin | Editor |
| ---------------------------------- | ----- | ------ |
| Project settings: Read             | Yes   | Yes    |
| Project settings: Write            | Yes   | No     |
| Project visibility: Read           | Yes   | Yes    |
| Project visibility: Change         | Yes   | No     |
| Project cost analytics: Read       | Yes   | Yes    |
| API keys: Read                     | Yes   | Yes    |
| API keys: Create                   | Yes   | Yes    |
| API keys: Revoke                   | Yes   | Yes    |
| API keys: Regenerate (legacy only) | Yes   | Yes    |
| Collaborators: Read                | Yes   | Yes    |
| Collaborators: Add                 | Yes   | No     |
| Collaborators: Remove              | Yes   | No     |
| Collaborators: Manage roles        | Yes   | No     |

Changing a project's visibility between open, closed, and private takes effect immediately and keeps the project's existing collaborators.

## External collaborators (beta)

<Info>
  This feature is in beta. [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) to enable it.
</Info>

An external collaborator is someone who participates in a project without being a member of the project's parent organization. They can be assigned any project role but have no organization-level permissions beyond seeing the organization's name.

What external collaborators can do:

* Full access to any project they have been explicitly added to (based on their project role).
* View their own profile settings.

What they cannot do:

* Access billing settings.
* View the organization members list.
* See organization-level settings.

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

| Action                                      | Admin | Editor |
| ------------------------------------------- | ----- | ------ |
| SSH into cluster nodes                      | Yes   | Yes    |
| Run Kubernetes workloads (kubectl)          | Yes   | Yes    |
| Download cluster kubeconfig (OIDC disabled) | Yes   | Yes    |
| Download admin kubeconfig (OIDC enabled)    | Yes   | No     |
| Download OIDC kubeconfig (OIDC enabled)     | Yes   | Yes    |
| Access Kubernetes Dashboard                 | Yes   | Yes    |
| Submit Slurm jobs                           | Yes   | Yes    |
| Read and write to volumes                   | Yes   | Yes    |

<Info>
  **Control plane vs data plane:** Think of the control plane as "managing the infrastructure" and the data plane as "using the infrastructure." Editors have full access to use clusters for their work. Their only restriction is that they cannot create, delete, or resize clusters.
</Info>

### Fine-tuning, endpoints, serverless inference & other products

Role-based access control for fine-tuning, endpoints, serverless inference, and other Together products is still being rolled out. Today, all project collaborators (both admins and editors) have full access to these services.

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
