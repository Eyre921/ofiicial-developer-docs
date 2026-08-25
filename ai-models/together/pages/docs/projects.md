---
title: "Projects"
source: https://docs.together.ai/docs/projects
path: docs/projects
---

Create isolated workspaces to organize resources, manage team access, and scope API keys.

A project is an isolated workspace within your [organization](/docs/organizations). Resources, API keys, and collaborator membership are all scoped to projects. Think of a project as the collaboration boundary: when you give someone access to a project, they can use everything inside it. Every organization includes a [default project](#default-project), and you can create additional projects to separate work by team, environment, or workload.

## How projects work

```
Organization
  Project A
    Cluster 1
    Cluster 2
    Fine-tuned Model
    Volume (shared storage)
  Project B
    Cluster 3
    Endpoint
    Evaluation
```

Each project contains its own set of resources. Collaborators of project A cannot see or access anything in project B, and vice versa. This lets you separate work by team, environment (dev/staging/prod), workload type, or customer.

## Project visibility

Every project is assigned a level of visibility:

* **open:** Members of the organization can discover and join the project.
* **closed:** Members can discover the project, but can't join. Access is managed by project and organization admins.
* **private:** Only existing project collaborators and organization admins can see it. Access is managed by project and organization admins.

When you create a project, you explicitly choose its visibility, with open as the default. A project admin or organization admin can change a project's visibility between the three states at any time from [**Project Settings**](https://api.together.ai/settings/projects/~current), and switching a project from open to closed or private keeps its existing collaborators.

Access to closed and private projects is managed by admins. A project admin adds you through the same [add-collaborator flow](#adding-collaborators) used for any project, and you become a collaborator immediately. When a project is closed, organization members who aren't collaborators can see it in their project list but can't join it.

Organization admins are exempt from these limits. They can see every project in the organization, including closed and private projects they haven't joined, and they can join any project without an invitation. To reach a closed or private project's resources or settings, an organization admin has to join it first.

## Default project

Every organization has a **default project**. A few things to know about it:

* All organization members are automatically granted access to the default project.
* All historical account usage and resources that pre-date projects are attributed to this project.
* No one can leave the default project.
* Because all organization members have access, do not use the default project for sensitive resources. Create a separate project for those.

## Project slugs

A **project slug** is a short, URL-safe, human-readable identifier for a project. It's globally unique across Together and distinct from the project's internal `project_id`, the permanent identifier behind ownership, permissions, and billing. The slug is the friendly handle. The `project_id` never changes.

You choose a slug when creating a new project, and you can copy any project's slug from the projects list in [**Organization Settings**](https://api.together.ai/settings/organization/~current).

When you create an endpoint with [dedicated model inference](/docs/dedicated-endpoints/overview), the project's slug becomes part of its endpoint string, `<project_slug>/<endpoint_name>`. You choose only the endpoint name. The slug prefix is added automatically and makes the endpoint string globally unique.

### Changing a project slug

Project admins can change an existing project's slug from [**Project Settings**](https://api.together.ai/settings/projects/~current): find the **Project Slug** field and select **Change**. The new slug takes effect immediately.

<Warning>
  Changing a slug breaks existing API requests, scripts, and integrations that reference resources by their slug-qualified path (for example, `<slug>/<endpoint_name>`). There is no redirect from the old slug. Update any references that rely on the old slug.
</Warning>

## Managing project collaborators

You can manage project collaborators from [**Settings > Project > Collaborators**](https://api.together.ai/settings/projects/~current/collaborators).

### Adding collaborators

1. Go to [**Settings > Project > Collaborators**](https://api.together.ai/settings/projects/~current/collaborators).
2. Select **Add Collaborator**.
3. Enter the user's email address.
4. Select **Confirm**.

New collaborators are added with the **editor** role by default, unless they are an organization admin (who are admins for every project by default). An admin can change their role after they have been added.

<Info>
  The user must already belong to your [organization](/docs/organizations), unless they are being added as an [external collaborator](/docs/roles-permissions#external-collaborators-beta).
</Info>

### Removing collaborators

1. Go to [**Settings > Project > Collaborators**](https://api.together.ai/settings/projects/~current/collaborators).
2. Find the collaborator you want to remove.
3. Select the three-dot menu next to their name.
4. Select **Remove User**.
5. Confirm the removal.

<Warning>
  Removing a collaborator revokes their access to all resources in the project, including clusters, volumes, SSH access, and management capabilities. This takes effect within minutes.
</Warning>

### External collaborators

<Info>
  This feature is in beta. [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) to enable it.
</Info>

To add users from outside your organization as collaborators, enable **Allow external collaborators** on the project's [**Settings > Project**](https://api.together.ai/settings/projects/~current) page.

Once enabled, you can add external collaborators the same way as any other collaborator. See [External collaborators](/docs/roles-permissions#external-collaborators-beta) to learn more about their permissions.

## Project API keys

Each project has [its own API keys](https://api.together.ai/settings/projects/~current/api-keys). These keys authenticate API requests and are scoped to the project's resources.

For details on creating, managing, and rotating API keys, see [API Keys & Authentication](/docs/api-keys-authentication).

## Known limitations

Costs in the projects list and in cost analytics may be inaccurate for any project running [legacy v1 dedicated endpoints](/docs/dedicated-endpoints/migrate-from-v1).

<Warning>
  If you have external collaborators using unsupported resources, usage may be billed to their organization instead of yours. If your external collaborators are internal company employees, consider migrating them into your organization using [SSO](/docs/sso) or [organization invites](/docs/organizations#invitation-based-oauth). [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) for help with migration.
</Warning>

## Common project structures

Teams organize projects differently depending on their needs:

| Strategy       | Example                                     | Best for                                               |
| -------------- | ------------------------------------------- | ------------------------------------------------------ |
| By team        | `ml-research`, `platform-eng`, `applied-ai` | Large organizations with distinct teams                |
| By environment | `development`, `staging`, `production`      | Teams that want resource isolation across environments |
| By workload    | `training`, `inference`, `evaluation`       | Teams that want to separate compute budgets            |
| By customer    | `customer-a`, `customer-b`                  | Service providers managing multiple clients            |

## Next steps

<CardGroup>
  <Card title="Roles & Permissions" icon="shield" href="/docs/roles-permissions">
    What admins and editors can do within a project
  </Card>

  <Card title="API Keys" icon="key" href="/docs/api-keys-authentication">
    Create project-scoped credentials
  </Card>

  <Card title="Cluster Access" icon="server" href="/docs/gpu-clusters-management#managing-cluster-access">
    Product-specific guide for managing cluster access
  </Card>
</CardGroup>
