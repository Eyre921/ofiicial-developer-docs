---
title: "IAM model"
source: https://docs.together.ai/docs/identity-access-management
path: docs/identity-access-management
---

How users, credentials, and resources are organized across the Together platform

Together's Identity and Access Management (IAM) model controls how your team collaborates on the platform, and how your workloads are authenticated. It determines who can access what, how credentials are scoped, and how resources are organized.

## Core concepts

Together's IAM is built around five concepts that work together:

| Concept                                                         | What it is                                                                                                     |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Organization](/docs/organizations)                             | Your company's account on Together. One org = one bill.                                                        |
| [Project](/docs/projects)                                       | An isolated workspace within your organization. Resources, collaborators, and API keys are scoped to projects. |
| [Resource](#resources)                                          | Anything you create: fine-tuned models, dedicated endpoints, clusters, evaluations, files.                     |
| [Member](#organization-members-and-project-collaborators)       | A user with access to your organization.                                                                       |
| [Collaborator](#organization-members-and-project-collaborators) | A user with access to a specific project (organization member or external user).                               |
| [API key](/docs/api-keys-authentication)                        | A project-scoped credential for authenticating API requests.                                                   |

## How it all fits together

```mermaid theme={null}
%%{init: {"flowchart": {"rankSpacing": 60, "nodeSpacing": 30}}}%%
flowchart TD
    U[User] -->|belongs to| O[Organization]
    U -->|joins or added to| P[Projects]
    O -->|contains| P
    EU[External user] -.->|added to| P
    P -->|scopes| K[API keys]
    P -->|contains| R[Resources]
    P -->|scopes| A[Analytics]
    R --> R1[Clusters]
    R --> R2[Fine-tuned models]
    R --> R3[Endpoints]
    R --> R4[Evaluations]
    R --> R5[Files]
    K ~~~ R1
    A ~~~ R5

    classDef box fill:#cbd5e1,stroke:#64748b,stroke-width:1.5px,color:#132133;
    class U,EU,O,P,K,R,A,R1,R2,R3,R4,R5 box;
```

**The key principle:** Projects are the collaboration boundary. Collaborators get access to a project, and that gives them access to everything inside it (clusters, models, endpoints, etc.). Access decisions happen at the project level, not on individual resources.

## Resources

A resource is anything you create or provision on Together:

* **GPU clusters:** Clusters for training and inference.
* **Fine-tuned models:** Models you've customized with your data.
* **Dedicated model inference:** Always-on inference endpoints.
* **Evaluations:** Model evaluation runs.
* **Files:** Training data, datasets, and other uploads.

Resources belong to a project. Everyone with access to that project can see and use those resources, subject to their [role permissions](/docs/roles-permissions).

## Organization members and project collaborators

Together uses different terminology at each level:

* **Organization members** are users who belong to your organization. They are [invited via email](https://api.together.ai/settings/organization/~current/members) or provisioned through SSO. Each member is assigned an admin or developer role at the organization level.
* **Project collaborators** are users who have been granted access to [a specific project](https://api.together.ai/settings/projects/~current/collaborators). Collaborators can be organization members or [external collaborators](/docs/roles-permissions#external-collaborators) who participate in a project without belonging to the parent organization.

Each collaborator is assigned an admin or editor role at the project level. For a detailed breakdown of what each role can do, see [Roles & Permissions](/docs/roles-permissions).

## Product-specific access guides

Together's IAM model applies consistently across all products. These guides cover product-specific workflows:

<CardGroup>
  <Card title="GPU Clusters" icon="server" href="/docs/gpu-clusters-management#managing-cluster-access">
    Add and remove collaborators from GPU cluster projects, understand in-cluster Kubernetes permissions
  </Card>
</CardGroup>

## Next steps

<CardGroup>
  <Card title="Organizations" icon="building" href="/docs/organizations">
    Set up your organization and manage membership
  </Card>

  <Card title="Projects" icon="folder" href="/docs/projects">
    Create workspaces and scope resources
  </Card>

  <Card title="Roles & Permissions" icon="shield" href="/docs/roles-permissions">
    Understand role-based capabilities (RBAC)
  </Card>

  <Card title="API Keys" icon="key" href="/docs/api-keys-authentication">
    Create and manage project-scoped credentials
  </Card>

  <Card title="Single Sign-On" icon="lock" href="/docs/sso">
    Connect your Identity Provider
  </Card>
</CardGroup>
