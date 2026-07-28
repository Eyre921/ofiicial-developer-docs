---
title: "Projects"
source: https://docs.together.ai/docs/projects
path: docs/projects
---

Create isolated workspaces to organize resources, manage team access, and scope API keys.

A Project is an isolated workspace within your [Organization](/docs/organizations). Resources, API keys, and Collaborator membership are all scoped to Projects. Think of a Project as the collaboration boundary: when you give someone access to a Project, they can use everything inside it.

<Note>
  Multi-Project support is currently in early access. Every Organization includes a [Default Project](#default-project). To enable additional Projects, [contact support](https://portal.usepylon.com/together-ai/forms/support-request).

  Not all resources are Multi-Project supported yet. See [Early Access Limitations](#early-access-limitations) for the full list and how unsupported resources behave.
</Note>

## How Projects Work

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

Each Project contains its own set of resources. Collaborators of Project A cannot see or access anything in Project B, and vice versa. This lets you separate work by team, environment (dev/staging/prod), workload type, or customer.

## Default Project

Every Organization has a **Default Project**. A few things to know about it:

* All Organization Members are automatically granted access to the Default Project.
* All historical account usage and resources that pre-date Projects are attributed to this Project (work in progress).
* All Playground usage is attributed to this Project.
* It has an "Organization Default Key" that is only accessible to the Organization Owner (see [API Keys & Authentication](/docs/api-keys-authentication#organization-default-key-deprecated)).
* Because all Organization Members have access, do not use the Default Project for sensitive resources. Create a separate Project for those.

## Project Slugs

A **project slug** is a short, URL-safe, human-readable identifier for a Project. It's globally unique across Together and distinct from the Project's internal `project_id`, the permanent identifier behind ownership, permissions, and billing. The slug is the friendly handle; the `project_id` never changes.

You choose a slug when creating a new Project, and you can copy any Project's slug from the Projects list in [**Organization Settings**](https://api.together.ai/settings/organization/~current).

When you create an endpoint with [dedicated model inference](/docs/dedicated-endpoints/overview), the Project's slug becomes part of its endpoint string, `<project-slug>/<endpoint-name>`. You choose only the endpoint name; the slug prefix is added automatically and makes the endpoint string globally unique.

### Changing a Project Slug

Project Admins can change an existing Project's slug from [**Project Settings**](https://api.together.ai/settings/projects/~current): find the **Project Slug** field and select **Change**. The new slug takes effect immediately.

<Warning>
  Changing a slug breaks existing API requests, scripts, and integrations that reference resources by their slug-qualified path (for example, `<slug>/<endpoint-name>`) — there is no redirect from the old slug. Update any references that rely on the old slug.
</Warning>

## Managing Project Collaborators

You can manage Project Collaborators from [**Settings > Project > Collaborators**](https://api.together.ai/settings/projects/~current/collaborators).

### Adding Collaborators

1. Go to [**Settings > Project > Collaborators**](https://api.together.ai/settings/projects/~current/collaborators).
2. Select **Add Collaborator**.
3. Enter the user's email address.
4. Select **Confirm**.

New Collaborators are added with the **Editor** role by default, unless they are an Organization Admin (who are Admins for every Project by default). An Admin can change their role after they have been added.

<Info>
  The user must already belong to your [Organization](/docs/organizations), unless they are being added as an [External Collaborator](/docs/roles-permissions#external-collaborators).
</Info>

### Removing Collaborators

1. Go to [**Settings > Project > Collaborators**](https://api.together.ai/settings/projects/~current/collaborators).
2. Find the Collaborator you want to remove.
3. Select the three-dot menu next to their name.
4. Select **Remove User**.
5. Confirm the removal.

<Warning>
  Removing a Collaborator revokes their access to all resources in the Project, including clusters, volumes, SSH access, and management capabilities. This takes effect within minutes.
</Warning>

### External Collaborators

<Info>
  This feature is in beta. [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) to enable it.
</Info>

To add users from outside your Organization as Collaborators, enable **Allow external collaborators** on the Project's [**Settings > Project**](https://api.together.ai/settings/projects/~current) page.

Once enabled, you can add External Collaborators the same way as any other Collaborator. See [External Collaborators](/docs/roles-permissions#external-collaborators) to learn more about their permissions.

## Project API Keys

Each Project has [its own API keys](https://api.together.ai/settings/projects/~current/api-keys). These keys authenticate API requests and are scoped to the Project's resources.

For details on creating, managing, and rotating API keys, see [API Keys & Authentication](/docs/api-keys-authentication).

## Early Access Limitations

Project scoping is rolling out incrementally. API key support is ahead of UI support, and we will be updating this continuously as more support becomes available.

### Support by resource

| Resource                      | API key support | UI support |
| ----------------------------- | --------------- | ---------- |
| GPU Clusters                  | ✅               | ✅          |
| API Keys                      | ✅               | ✅          |
| Serverless inference          | ✅               | ✅          |
| Dedicated model inference     | ✅               | ✅          |
| Dedicated container inference | ✅               | ✅          |
| Uploaded models and adapters  | ✅               | ✅          |
| Fine-tuning                   | ✅               | ❌          |
| Files                         | ✅               | ❌          |
| Evaluations                   | ✅               | ❌          |
| Batch                         | ✅               | ❌          |
| Code Interpreter              | ✅               | N/A        |
| Storage                       | ❌               | ❌          |

Here's what to expect when using a resource that isn't yet supported:

### For Organization Members and Project Collaborators

If you use a product that isn't multi-Project aware, usage attributes back to the **Default Project** of the Organization. In-app views and API responses for those resources may be inaccurate. They might return all resources belonging to the Organization or only resources in the Default Project, not the Project you're working in.

### For External Collaborators

The behavior is more significant for [External Collaborators](/docs/roles-permissions#external-collaborators). Because many product decisions are based on the user's Organization, usage in unsupported products may attribute back to the **External Collaborator's own Organization** rather than the Project and parent Organization they are collaborating within. This means billing and resource attribution can be incorrect for external collaborators using products that don't yet work across multiple Projects.

<Warning>
  If you have External Collaborators using unsupported resources, usage may be billed to their Organization instead of yours. If your External Collaborators are internal company employees, consider migrating them into your Organization using [SSO](/docs/sso) or [Org Invites](/docs/organizations#inviting-members). [Contact support](https://portal.usepylon.com/together-ai/forms/support-request) for help with migration.
</Warning>

We're actively expanding multi-Project support to all products. This section will be updated as more products are supported.

## Common Project Structures

Teams organize Projects differently depending on their needs:

| Strategy       | Example                                     | Best for                                               |
| -------------- | ------------------------------------------- | ------------------------------------------------------ |
| By team        | `ml-research`, `platform-eng`, `applied-ai` | Large Organizations with distinct teams                |
| By environment | `development`, `staging`, `production`      | Teams that want resource isolation across environments |
| By workload    | `training`, `inference`, `evaluation`       | Teams that want to separate compute budgets            |
| By customer    | `customer-a`, `customer-b`                  | Service providers managing multiple clients            |

## Next Steps

<CardGroup>
  <Card title="Roles & Permissions" icon="shield" href="/docs/roles-permissions">
    What Admins and Editors can do within a Project
  </Card>

  <Card title="API Keys" icon="key" href="/docs/api-keys-authentication">
    Create Project-scoped credentials
  </Card>

  <Card title="Cluster Access" icon="server" href="/docs/gpu-clusters-management#managing-cluster-access">
    Product-specific guide for managing cluster access
  </Card>
</CardGroup>
