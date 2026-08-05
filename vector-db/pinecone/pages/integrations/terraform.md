---
title: "Terraform"
source: https://docs.pinecone.io/integrations/terraform
path: integrations/terraform
---

Connect Pinecone and Terraform to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

Terraform is an infrastructure as code tool that lets you create, update, and version infrastructure by defining resources in configuration files. This allows for a repeated workflow for provisioning and managing your infrastructure.

This page describes how to use the [Terraform Provider for Pinecone](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs) to manage Pinecone indexes, collections, projects, API keys, service accounts, role bindings, invites, and users.

## Requirements

Ensure you have the following:

* [Terraform](https://developer.hashicorp.com/terraform) >= v1.4.6
* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys) for managing indexes and collections
* A [Pinecone service account](https://app.pinecone.io/organizations/-/settings/access/service-accounts) for managing projects, API keys, service accounts, role bindings, invites, and users

<Note>
  [Go](https://go.dev/doc/install) >= v1.24 is required only if you build the provider from source. You don't need Go to install the provider from the Terraform Registry.
</Note>

## Install the provider

1. Configure the Pinecone provider in your Terraform configuration file:

   ```terraform theme={null}
   terraform {
     required_providers {
       pinecone = {
         source  = "pinecone-io/pinecone"
         version = "~> 4.0"
       }
     }
   }
   ```

````

1. Run `terraform init` to install the provider from the [Terraform Registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest). Alternatively, you can download the latest binary for your target platform from the [GitHub repository](https://github.com/pinecone-io/terraform-provider-pinecone/releases).

<Note>
Upgrading from v2 doesn't require configuration changes. No arguments were removed or renamed in v3 or v4, so existing configuration keeps working. Both releases only add resources, data sources, and index options. For the full list, see the [v3.0.0](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v3.0.0) and [v4.0.0](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v4.0.0) release notes.
</Note>

## Authenticate 

The provider uses two kinds of credentials, and each resource requires a specific one. The provider needs at least one of them and fails to configure if neither is set. If your configuration manages both indexes and organization-level resources, set both.

| Credential | Environment variables | Resources and data sources |
| :--- | :--- | :--- |
| [API key](/guides/projects/manage-api-keys) | `PINECONE_API_KEY` | `pinecone_index`, `pinecone_collection` |
| [Service account](/guides/organizations/manage-service-accounts) | `PINECONE_CLIENT_ID`, `PINECONE_CLIENT_SECRET` | `pinecone_project`, `pinecone_api_key`, `pinecone_service_account`, `pinecone_role_binding`, `pinecone_invite`, `pinecone_user` |

To authenticate:

1. Set environment variables for authentication:

    ```bash
    # For indexes and collections  
    export PINECONE_API_KEY="YOUR_API_KEY"

    # For projects, API keys, service accounts, role bindings, invites, and users
    export PINECONE_CLIENT_ID="YOUR_CLIENT_ID"
    export PINECONE_CLIENT_SECRET="YOUR_CLIENT_SECRET"
````

1. Append the following to your Terraform configuration file:

   ```terraform theme={null}
   provider "pinecone" {}
   ```

````

<Note>
You can also set the API key and service account credentials as [input variables](https://developer.hashicorp.com/terraform/language/values/variables).
</Note>

## Manage resources

The Terraform Provider for Pinecone provides the following resources:

| Resource | Description | Credential |
| :--- | :--- | :--- |
| [`pinecone_index`](#indexes) | Create, update, and delete indexes. | API key |
| [`pinecone_collection`](#collections) | Create and delete collections. | API key |
| [`pinecone_project`](#projects) | Create, update, and delete projects. | Service account |
| [`pinecone_api_key`](#api-keys) | Create, update, and delete API keys. | Service account |
| [`pinecone_service_account`](#service-accounts) | Create, update, and delete service accounts. | Service account |
| [`pinecone_role_binding`](#role-bindings) | Grant and revoke roles. | Service account |
| [`pinecone_invite`](#invites) | Send and revoke organization invitations. | Service account |
| [`pinecone_user`](#users) | Remove existing organization members. | Service account |

### Indexes

The `pinecone_index` resource lets you create, update, and delete [indexes](/guides/index-data/indexing-overview). 

```terraform
# Index for dense vectors
resource "pinecone_index" "example_index" {
  name        = "example-index"
  dimension   = 1536
  metric      = "cosine"
  vector_type = "dense"
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-west-2"
    }
  }
  deletion_protection = "disabled"
  tags = {
    environment = "development"
  }
}

# Index for dense vectors with integrated embedding
resource "pinecone_index" "example_index_integrated" {
  name = "example-index-integrated"
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-west-2"
    }
  }
  embed = {
    model = "llama-text-embed-v2"
    field_map = {
      text = "chunk_text"
    }
    read_parameters = {
      input_type = "query"
    }
    write_parameters = {
      input_type = "passage"
    }
  }
}
````

For an index with integrated embedding, `dimension` defaults to the model's dimension. The `model` can't be changed once set, but you can update `field_map`, `read_parameters`, and `write_parameters`. The read-only `embed.effective_read_parameters` and `embed.effective_write_parameters` attributes report the parameters the API applied, including server-side defaults you didn't set.

<Note>
  You can [update](/guides/manage-data/manage-indexes) only the deletion protection, tags, integrated inference embedding settings, and [read capacity](#read-capacity) of an index. Changing any other attribute — including `name`, `dimension`, `metric`, the cloud and region, or the [metadata schema](#metadata-schema) — replaces the index.
</Note>

#### BYOC indexes

To create a [BYOC index](/guides/production/bring-your-own-cloud), set `spec.byoc.environment` to the environment identifier Pinecone provides for your deployment:

```terraform theme={null}
resource "pinecone_index" "example_index_byoc" {
  name      = "example-index-byoc"
  dimension = 1536
  spec = {
    byoc = {
      environment = "YOUR_BYOC_ENVIRONMENT_ID"
    }
  }
}
```

#### Pod-based indexes

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

To create a [pod-based index](/guides/indexes/pods/understanding-pod-based-indexes), set `spec.pod`:

```terraform theme={null}
resource "pinecone_index" "example_index_pod" {
  name      = "example-index-pod"
  dimension = 1536
  spec = {
    pod = {
      environment = "us-west4-gcp"
      pod_type    = "s1.x1"
      replicas    = 1
      shards      = 1
      metadata_config = {
        indexed = ["genre"]
      }
    }
  }
}
```

<Warning>
  Changing `replicas`, `shards`, or `pod_type` replaces the index, which deletes the records it holds. To scale a pod-based index in place, use the [console or API](/guides/indexes/pods/manage-pod-based-indexes) instead.
</Warning>

#### Read capacity

Serverless and BYOC indexes support configurable read capacity through `read_capacity` inside the `serverless` or `byoc` spec. There are two modes: `on_demand`, which is the default, and `dedicated`, which provisions [dedicated read nodes](/guides/index-data/dedicated-read-nodes).

```terraform theme={null}
# On-demand read capacity, stated explicitly
resource "pinecone_index" "example_index_on_demand" {
  name      = "example-index-on-demand"
  dimension = 1536
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-east-1"
      read_capacity = {
        on_demand = {}
      }
    }
  }
}

# Dedicated read capacity
resource "pinecone_index" "example_index_dedicated" {
  name      = "example-index-dedicated"
  dimension = 1536
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-east-1"
      read_capacity = {
        dedicated = {
          node_type = "b1"
          replicas  = 1
          shards    = 1
        }
      }
    }
  }
}
```

Set `node_type` to `b1` or `t1`. The first time you switch an index to dedicated mode, `node_type`, `replicas`, and `shards` are all required.

#### Metadata schema

Serverless and BYOC indexes support a `schema` block that controls [metadata indexing](/guides/index-data/create-an-index#metadata-indexing). By default, all metadata is indexed. When `schema` is present, only the fields you list with `filterable = true` are indexed.

```terraform theme={null}
resource "pinecone_index" "example_index_schema" {
  name      = "example-index-schema"
  dimension = 1536
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-east-1"
      schema = {
        fields = {
          "category" = { filterable = true }
          "language" = { filterable = true }
        }
      }
    }
  }
}
```

<Warning>
  You can set `schema` only when you create an index. Changing it replaces the index, which deletes the records it holds.
</Warning>

#### Timeouts

Index creation and deletion both time out after 5 minutes by default. To override this, set a `timeouts` block:

```terraform theme={null}
resource "pinecone_index" "example_index_timeouts" {
  name      = "example-index-timeouts"
  dimension = 1536
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }

  timeouts {
    create = "10m"
    delete = "10m"
  }
}
```

### Collections

The `pinecone_collection` resource lets you create and delete [collections](/guides/indexes/pods/understanding-collections) for pod-based indexes. Set `source` to the name of the source index.

```terraform theme={null}
resource "pinecone_index" "example_index" {
  name      = "example-index"
  dimension = 10
  spec = {
    pod = {
      environment = "us-west4-gcp"
      pod_type    = "s1.x1"
    }
  }
}

resource "pinecone_collection" "example_collection" {
  name   = "example-collection"
  source = pinecone_index.example_index.name
}
```

Collections also accept a `timeouts` block, with the same 5-minute defaults as indexes.

### Projects

The `pinecone_project` resource lets you create, update, and delete [projects](/guides/projects/understanding-projects). Once `force_encryption_with_cmek` is enabled, it can't be disabled. `max_pods` defaults to `0`, which allows serverless indexes only.

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

Customers on those plans also can't set `max_pods` for a project.

```terraform theme={null}
# Basic project
resource "pinecone_project" "example_project" {
  name = "example-project"
}

# Project with CMEK encryption enabled
resource "pinecone_project" "example_project_encrypted" {
  name                       = "example-project-encrypted"
  force_encryption_with_cmek = true
}

# Project with custom max pods
resource "pinecone_project" "example_project_custom_pods" {
  name     = "example-project-custom-pods"
  max_pods = 10
}

output "project_organization_id" {
  description = "The organization the project belongs to"
  value       = pinecone_project.example_project.organization_id
}
```

### API keys

The `pinecone_api_key` resource lets you create, update, and delete [API keys](/guides/projects/manage-api-keys). Valid `roles` values are `ProjectEditor`, `ProjectViewer`, `ControlPlaneEditor`, `ControlPlaneViewer`, `DataPlaneEditor`, and `DataPlaneViewer`. `roles` defaults to `["ProjectEditor"]`.

<Note>
  You can update only the name and roles of an API key. `project_id` is required when you create a key.
</Note>

```terraform theme={null}
# API key with default roles (ProjectEditor)
resource "pinecone_api_key" "example_key" {
  name       = "example-key"
  project_id = "YOUR_PROJECT_ID"
}

# API key with custom roles
resource "pinecone_api_key" "example_key_custom_roles" {
  name       = "example-key-custom-roles"
  project_id = "YOUR_PROJECT_ID"
  roles      = ["ProjectViewer", "DataPlaneViewer"]
}

output "api_key_roles" {
  description = "The roles assigned to the API key"
  value       = pinecone_api_key.example_key.roles
}
```

<Warning>
  The generated secret is available as the read-only `key` attribute, which the API returns only once, at creation. Terraform stores it in plaintext in state. Marking it sensitive keeps it out of CLI output and logs, but does not encrypt it in state. Secure your state backend and never commit state to version control.
</Warning>

### Service accounts

The `pinecone_service_account` resource lets you create, update, and delete [service accounts](/guides/organizations/manage-service-accounts). A service account authenticates with an OAuth client ID and secret. Grant it roles with a [role binding](#role-bindings).

```terraform theme={null}
resource "pinecone_service_account" "example_service_account" {
  name = "example-service-account"
}

resource "pinecone_role_binding" "example_service_account_org_member" {
  principal_id   = pinecone_service_account.example_service_account.id
  principal_type = "service_account"
  resource_type  = "organization"
  role           = "OrgMember"
}

# Rotate the client secret by changing rotate_trigger to a new value
resource "pinecone_service_account" "example_service_account_rotatable" {
  name           = "example-service-account-rotatable"
  rotate_trigger = "2026-01-01"
}

output "example_service_account_client_secret" {
  value     = pinecone_service_account.example_service_account.client_secret
  sensitive = true
}
```

To rotate a client secret, change `rotate_trigger` from one non-empty value to another. Setting it for the first time, or clearing it, establishes a baseline without rotating, so an existing credential is never invalidated unintentionally.

<Warning>
  The `client_secret` attribute is returned only once, at creation or rotation, and Terraform stores it in plaintext in state. Marking it sensitive keeps it out of CLI output and logs, but does not encrypt it in state. Secure your state backend and never commit state to version control.
</Warning>

### Role bindings

The `pinecone_role_binding` resource lets you grant a role to a principal at organization or project scope. For details on the role model, see [Manage roles and access](/guides/production/manage-rbac).

* Set `principal_type` to `user`, `service_account`, or `api_key`, and `principal_id` to that principal's ID.
* Set `resource_type` to `organization` or `project`. For project scope, `resource_id` is required and must be the project ID. For organization scope, omit `resource_id`. The binding applies to the caller's organization.
* Organization-scoped `role` values are `OrgOwner`, `OrgManager`, `OrgBillingAdmin`, and `OrgMember`. Project-scoped values are `ProjectOwner`, `ProjectManager`, `ProjectMember`, `ProjectEditor`, `ProjectViewer`, `ControlPlaneEditor`, `ControlPlaneViewer`, `DataPlaneEditor`, and `DataPlaneViewer`.

```terraform theme={null}
# Organization-scoped role
resource "pinecone_role_binding" "example_org_member" {
  principal_id   = "YOUR_SERVICE_ACCOUNT_ID"
  principal_type = "service_account"
  resource_type  = "organization"
  role           = "OrgMember"
}

# Project-scoped role
resource "pinecone_role_binding" "example_project_editor" {
  principal_id   = "YOUR_USER_ID"
  principal_type = "user"
  resource_type  = "project"
  resource_id    = "YOUR_PROJECT_ID"
  role           = "ProjectEditor"
}
```

<Note>
  Role bindings are immutable. Changing any attribute revokes the existing binding and creates a new one.
</Note>

The `pinecone_role_binding` resource doesn't accept `principal_type = "invite"`. Pinecone moves an invite's bindings to the user principal when the invite is accepted, so Terraform can't manage them across that transition. To grant roles to someone who hasn't joined your organization yet, use [`pinecone_invite`](#invites), then manage their roles here with `principal_type = "user"` once they accept. The `pinecone_role_bindings` data source does accept `invite`, so you can still read what a pending invite granted.

### Invites

The `pinecone_invite` resource manages an [organization invitation](/guides/organizations/manage-organization-members), not the resulting membership. Creating it sends an invite to the given email with a set of initial roles. Deleting it revokes an invite that is still pending. The `role_bindings` list must include at least one organization-scoped role that grants membership.

```terraform theme={null}
# Invite a user as an organization member
resource "pinecone_invite" "example_member" {
  email = "teammate@example.com"

  role_bindings = [
    {
      resource_type = "organization"
      role          = "OrgMember"
    }
  ]
}

# Invite a user with both organization membership and a project-scoped role
resource "pinecone_invite" "example_project_editor" {
  email = "contractor@example.com"

  role_bindings = [
    {
      resource_type = "organization"
      role          = "OrgMember"
    },
    {
      resource_type = "project"
      role          = "ProjectEditor"
      resource_id   = "YOUR_PROJECT_ID"
    }
  ]
}
```

The read-only `status` attribute reports `pending`, `expired`, or `processed`. Invites expire 7 days after creation, and the provider doesn't expose a way to change that. Once an invite is accepted, its status is `processed` and Terraform stops acting on it. Destroying an accepted invite is a no-op.

<Warning>
  Invites are immutable, so changing `email` or `role_bindings` sends a new invite. Don't change either one after the invite is accepted — the replacement re-invites an address that already belongs to a member, and the operation fails. Manage an existing member's roles with [`pinecone_role_binding`](#role-bindings) instead.
</Warning>

<Note>
  Pinecone doesn't return the roles an invite granted, so `role_bindings` is applied only at creation. Terraform can't detect drift on it or recover it on import. To read the bindings, use the `pinecone_role_bindings` data source with `principal_type = "invite"`.
</Note>

### Users

The `pinecone_user` resource manages an existing [organization member](/guides/organizations/manage-organization-members). You can't create or update users through Terraform. They join your organization by accepting an [invite](#invites). Bring an existing user under management with [`terraform import`](#import-existing-resources). To change a user's roles, use a [role binding](#role-bindings).

<Warning>
  Destroying a `pinecone_user` resource removes that person from your organization. A `terraform destroy`, or removing the resource from your configuration, revokes a colleague's access to every project in the organization.
</Warning>

```terraform theme={null}
resource "pinecone_user" "example_user" {
  id = "YOUR_USER_ID"
}
```

The `id` attribute is immutable. To manage a different user, run `terraform state rm` on this resource and import the intended one.

## Read existing resources

Data sources let you read resources that Terraform doesn't manage. Most resource types have a singular data source that fetches one object and a plural data source that lists many.

| Data source                 | Required        | Optional filters                                                         | Credential      |
| :-------------------------- | :-------------- | :----------------------------------------------------------------------- | :-------------- |
| `pinecone_index`            | `name`          | —                                                                        | API key         |
| `pinecone_indexes`          | —               | —                                                                        | API key         |
| `pinecone_collection`       | `name`          | —                                                                        | API key         |
| `pinecone_collections`      | —               | —                                                                        | API key         |
| `pinecone_project`          | `id`            | —                                                                        | Service account |
| `pinecone_projects`         | —               | —                                                                        | Service account |
| `pinecone_service_account`  | `id`            | —                                                                        | Service account |
| `pinecone_service_accounts` | —               | —                                                                        | Service account |
| `pinecone_role_binding`     | `id`            | —                                                                        | Service account |
| `pinecone_role_bindings`    | —               | `principal_type`, `principal_id`, `resource_type`, `resource_id`, `role` | Service account |
| `pinecone_invite`           | `id`            | —                                                                        | Service account |
| `pinecone_invites`          | —               | —                                                                        | Service account |
| `pinecone_user`             | `id` or `email` | —                                                                        | Service account |
| `pinecone_users`            | —               | `email`                                                                  | Service account |

```terraform theme={null}
# Read one index by name
data "pinecone_index" "example_index" {
  name = "example-index"
}

# List every index in the project
data "pinecone_indexes" "all" {}

# Look up a user by email, then grant them a project role
data "pinecone_user" "example_user" {
  email = "teammate@example.com"
}

resource "pinecone_role_binding" "example_user_project_viewer" {
  principal_id   = data.pinecone_user.example_user.id
  principal_type = "user"
  resource_type  = "project"
  resource_id    = "YOUR_PROJECT_ID"
  role           = "ProjectViewer"
}

# List the role bindings held by one principal
data "pinecone_role_bindings" "example_service_account_bindings" {
  principal_type = "service_account"
  principal_id   = "YOUR_SERVICE_ACCOUNT_ID"
}
```

Note the following behaviors:

* For `pinecone_user`, set exactly one of `id` or `email`. Email matching is case-insensitive.
* For `pinecone_role_bindings`, `principal_type` is required when you set `principal_id`, and `resource_type` is required when you set `resource_id`. You can't filter by a binding's own ID. Fetch it with the `pinecone_role_binding` data source instead.
* `pinecone_invites` returns only `pending` and `expired` invites. To read an accepted invite, fetch it by ID with `pinecone_invite`.
* The service account data sources never return client secrets.

## Import existing resources

All resources support the [`terraform import` command](https://developer.hashicorp.com/terraform/cli/commands/import):

| Resource                   | Import ID               |
| :------------------------- | :---------------------- |
| `pinecone_index`           | Index name              |
| `pinecone_collection`      | Collection name         |
| `pinecone_project`         | Project ID              |
| `pinecone_api_key`         | `PROJECT_ID:API_KEY_ID` |
| `pinecone_service_account` | Service account ID      |
| `pinecone_role_binding`    | Role binding ID         |
| `pinecone_invite`          | Invite ID               |
| `pinecone_user`            | User ID                 |

For example:

```bash theme={null}
terraform import pinecone_user.example_user YOUR_USER_ID
```

Some attributes can't be imported because Pinecone returns them only once:

* `pinecone_api_key.key` and `pinecone_service_account.client_secret` stay empty in state for an imported resource. To issue and store a new service account secret, change `rotate_trigger`.
* `pinecone_invite.role_bindings` stays empty in state, and Terraform proposes a replacement on the next plan until you set it to match the original invite. Use the `pinecone_role_bindings` data source with `principal_type = "invite"` to see what the invite granted.

## Limitations

The Terraform Provider for Pinecone doesn't support the following:

* [Backups for serverless indexes](/guides/manage-data/backups-overview)
* [Private endpoints](/guides/production/configure-private-endpoints)
* [Assistants](/guides/assistant/overview)
* BYOC environment provisioning (you reference an existing environment by its identifier, which Pinecone provisions for you).
* Full-text search fields (the index `schema` block accepts only `filterable`, so you can't configure fields for [full-text search](/guides/search/full-text-search)).

## See also

* Documentation can be found on the [Terraform
  Registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs).
* See the [GitHub repository](https://github.com/pinecone-io/terraform-provider-pinecone/tree/main/examples)
  for additional usage examples.
* For support requests, create an issue in the [GitHub
  repository](https://github.com/pinecone-io/terraform-provider-pinecone).
