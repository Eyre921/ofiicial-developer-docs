---
title: "Terraform"
source: https://docs.pinecone.io/integrations/terraform
path: integrations/terraform
---

Manage Pinecone indexes, collections, projects, API keys, and access with the Terraform provider for repeatable infrastructure-as-code and DevOps workflows.

Terraform is an infrastructure-as-code tool that lets you create, update, and version infrastructure by defining resources in configuration files. This gives you a repeatable workflow for provisioning and managing your infrastructure.

This page describes how to use the [Terraform Provider for Pinecone](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs) to manage Pinecone indexes, collections, projects, API keys, service accounts, role bindings, invites, and users. It covers provider v5.1.1, which uses Pinecone API version `2026-07`.

## Requirements

Ensure you have the following:

* [Terraform](https://developer.hashicorp.com/terraform) >= v1.4.6
* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys) for managing indexes and collections
* A [Pinecone service account](https://app.pinecone.io/organizations/-/settings/access/service-accounts) for managing projects, API keys, service accounts, role bindings, invites, and users

> [!NOTE]
>
> [Go](https://go.dev/doc/install) >= v1.26 is required only if you build the provider from source. You don't need Go to install the provider from the Terraform Registry.

## Install the provider

1. Configure the Pinecone provider in your Terraform configuration file:

   ```hcl Terraform theme={null}
   terraform {
     required_providers {
       pinecone = {
         source  = "pinecone-io/pinecone"
         version = "~> 5.1"
       }
     }
   }
   ```

2. Run `terraform init` to install the provider from the [Terraform Registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest). Alternatively, you can download the latest binary for your target platform from the [GitHub repository](https://github.com/pinecone-io/terraform-provider-pinecone/releases).

### Upgrade from v4

v5 is a major version. Most configurations written for v4 plan with no changes, but a few that v4 accepted are now rejected at plan time, before anything changes:

* New [pod-based indexes](#pod-based-indexes) can't be created, and neither can indexes created from a collection.
* On a [legacy integrated index](#legacy-integrated-indexes), `embed` can't be added or removed, and `embed.model` and `embed.field_map` can't be changed.
* The `spec.serverless.schema` and `spec.byoc.schema` [metadata schema](#move-an-index-to-the-schema-style) is deprecated. New indexes accept it only together with `embed`.
* An index can't switch from dedicated [read capacity](#read-capacity) back to on-demand.
* `dimension`, `size`, and `vector_count` on `pinecone_collection` are read-only and can't be set.

To upgrade, change the version constraint to `~> 5.1`, run `terraform init -upgrade`, then run `terraform plan` and work through any errors. For each error and its fix, see the [version 5 upgrade guide](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs/guides/version-5-upgrade). For the full list of changes, see the [v5.0.0](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v5.0.0), [v5.1.0](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v5.1.0), and [v5.1.1](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v5.1.1) release notes.

## Authenticate

The provider uses two kinds of credentials, and each resource requires a specific one. The provider needs at least one of them and fails to configure if neither is set. If your configuration manages both indexes and organization-level resources, set both.

| Credential | Environment variables | Resources and data sources |
| :- | :- | :- |
| [API key](/admin/projects/manage-api-keys) | `PINECONE_API_KEY` | `pinecone_index`, `pinecone_collection` |
| [Service account](/admin/organizations/manage-service-accounts) | `PINECONE_CLIENT_ID`, `PINECONE_CLIENT_SECRET` | `pinecone_project`, `pinecone_api_key`, `pinecone_service_account`, `pinecone_role_binding`, `pinecone_invite`, `pinecone_user` |

Follow these steps to authenticate:

1. Set environment variables for authentication:

   ```bash theme={null}
   # For indexes and collections
   export PINECONE_API_KEY="YOUR_API_KEY"

   # For projects, API keys, service accounts, role bindings, invites, and users
   export PINECONE_CLIENT_ID="YOUR_CLIENT_ID"
   export PINECONE_CLIENT_SECRET="YOUR_CLIENT_SECRET"
   ```

2. Append the following to your Terraform configuration file:

   ```hcl Terraform theme={null}
   provider "pinecone" {}
   ```

> [!NOTE]
>
> You can also set the API key and service account credentials as [input variables](https://developer.hashicorp.com/terraform/language/values/variables).

## Manage resources

The Terraform Provider for Pinecone provides the following resources:

| Resource | Description | Credential |
| :- | :- | :- |
| [`pinecone_index`](#indexes) | Create, update, and delete indexes. | API key |
| [`pinecone_collection`](#collections) | Create and delete collections. | API key |
| [`pinecone_project`](#projects) | Create, update, and delete projects. | Service account |
| [`pinecone_api_key`](#api-keys) | Create, update, and delete API keys. | Service account |
| [`pinecone_service_account`](#service-accounts) | Create, update, and delete service accounts. | Service account |
| [`pinecone_role_binding`](#role-bindings) | Grant and revoke roles. | Service account |
| [`pinecone_invite`](#invites) | Send and revoke organization invitations. | Service account |
| [`pinecone_user`](#users) | Remove existing organization members. | Service account |

### Indexes

The `pinecone_index` resource lets you create, update, and delete [indexes](/guides/index-data/indexing-overview). It describes an index in one of two styles:

* **The `schema` style**, with `schema` and `deployment`. This is how API version `2026-07` describes indexes, and it's the style to use for new indexes.
* **The `spec` style**, with `dimension`, `metric`, `vector_type`, `spec`, and `embed`. This is how earlier versions of the provider described indexes, and it's planned for deprecation. Legacy integrated indexes and existing pod-based indexes still need it.

A configuration uses one style or the other. You can't combine `schema` or `deployment` with `dimension`, `metric`, `vector_type`, `spec`, or `embed`.

#### Document indexes

A `schema` of named fields creates a [document index](/guides/index-data/adopt-the-documents-api), which you read and write through the Documents API. Each field sets exactly one of `dense_vector`, `sparse_vector`, or `string`. A `string` field stores its text by default, and a field that stores its text is always indexed for [full-text search](/guides/search/full-text-search). A `string` field can also use [integrated embedding](#integrated-embedding).

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_documents" {
  name = "example-index-documents"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      embedding = { dense_vector = { dimension = 1536, metric = "dotproduct" } }
      terms     = { sparse_vector = {} }
      body      = { string = { full_text_search = { stemming = true, stop_words = true } } }
      title     = { string = { full_text_search = { ngram = { min_gram = 2, max_gram = 4, prefix_only = true } } } }
    }
  }
  deletion_protection = "disabled"
  tags = {
    environment = "development"
  }
}
```

You don't need to declare metadata fields. Pinecone indexes them automatically as you upsert documents. `full_text_search` accepts `language`, `stemming`, `stop_words`, and `ngram`. `ngram` can't be combined with `stemming` or `stop_words`.

Document indexes can run on managed (serverless) or [BYOC](#byoc-indexes) deployments.

#### Integrated embedding

With provider v5.1.0 or later, a `string` field can use [integrated embedding](/guides/search/integrated-embedding): Pinecone embeds the field's text with a hosted model when you upsert or update documents, and embeds your query text when you search. Set `embed` for a dense model, `sparse_embed` for a sparse model, or both. `{}` selects the default model: `llama-text-embed-v2` at its default dimension and metric for `embed`, and `pinecone-sparse-english-v0` for `sparse_embed`.

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_embedded" {
  name = "example-index-embedded"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      # Embedded with a dense model. Its stored text is indexed for full-text search, here with stemming.
      body = {
        string = {
          embed            = { model = "llama-text-embed-v2", dimension = 1024 }
          full_text_search = { stemming = true }
        }
      }
      # Embedded with the default sparse model, then discarded
      summary = {
        string = {
          sparse_embed = {}
          store_text   = false
        }
      }
    }
  }
}
```

Note the following behaviors:

* `embed` accepts `model`, `dimension`, `metric`, `read_parameters`, and `write_parameters`. `sparse_embed` accepts the same attributes except `dimension` and `metric`. For available models, see [Models](/models/overview).
* The read-only `effective_read_parameters` and `effective_write_parameters` attributes report the parameters the index uses, merged with the model's defaults.
* One field can set `full_text_search`, `embed`, and `sparse_embed` together. Set `full_text_search` to configure full-text search on a field that stores its text.
* `store_text = false` embeds the text and then discards it. Use it for fields you only search by similarity, or to keep sensitive text out of Pinecone. The field then can't use `full_text_search`, `$match_*` filters, or `include_fields`.
* An index has one dense slot and one sparse slot. At most one field can be a `dense_vector` field or set `embed`, and at most one can be a `sparse_vector` field or set `sparse_embed`.

#### Vector indexes

A schema made only of the reserved fields `_values` (dense) and `_sparse_values` (sparse) creates a [vector index](/guides/index-data/indexing-overview), which you read and write through the Vectors API. `_values` always needs both `dimension` and `metric`.

```hcl Terraform theme={null}
# Index that stores dense vectors
resource "pinecone_index" "example_index" {
  name = "example-index"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-west-2"
    }
  }
  schema = {
    fields = {
      _values = { dense_vector = { dimension = 1536, metric = "cosine" } }
    }
  }
}

# Index that stores sparse vectors
resource "pinecone_index" "example_index_sparse" {
  name = "example-index-sparse"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-west-2"
    }
  }
  schema = {
    fields = {
      _sparse_values = { sparse_vector = {} }
    }
  }
}
```

#### BYOC indexes

To create a [BYOC index](/guides/production/bring-your-own-cloud/create-an-index), set `deployment.byoc.environment` to the environment identifier Pinecone provides for your deployment. The Pinecone API accepts document indexes on BYOC as long as no field uses integrated embedding. With provider v5.1.0 or later, BYOC indexes default to on-demand [read capacity](#read-capacity), like serverless indexes.

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_byoc" {
  name = "example-index-byoc"
  deployment = {
    byoc = {
      environment = "YOUR_BYOC_ENVIRONMENT_ID"
    }
  }
  schema = {
    fields = {
      _values = { dense_vector = { dimension = 1536, metric = "cosine" } }
    }
  }
}
```

> [!NOTE]
>
> Provider v5.0.0 requires `read_capacity.dedicated` on new BYOC indexes. Upgrade to v5.1.0 or later to create on-demand BYOC indexes.
>
> Provider v5.1.0 and earlier reject document indexes and `cmek_id` on BYOC at plan time. Upgrade to v5.1.1 or later to use them.

#### Read capacity

Serverless and BYOC indexes support configurable read capacity through `read_capacity`. There are two modes: `on_demand`, which is the default, and `dedicated`, which provisions [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview). In the `schema` style, set `read_capacity` at the top level of the resource.

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_dedicated" {
  name = "example-index-dedicated"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      _values = { dense_vector = { dimension = 1536, metric = "cosine" } }
    }
  }
  read_capacity = {
    dedicated = {
      node_type = "b1"
      replicas  = 1
      shards    = 1
    }
  }
}
```

Set `node_type` to `b1` or `t1`. The first time you switch an index to dedicated mode, `node_type`, `replicas`, and `shards` are all required. To select on-demand explicitly, set `read_capacity = { on_demand = {} }`.

Creating an index with `read_capacity`, or changing `read_capacity`, waits until the configured replicas and shards are running. If the change fails, the apply fails with the API's error message. If a change to an existing index times out, it keeps going, and the next apply waits for it again.

> [!WARNING]
>
> An index can't switch from dedicated read capacity back to on-demand. The plan fails with `Read capacity can't return to on-demand`. To switch an index back, contact [Pinecone support](https://app.pinecone.io/organizations/-/settings/support/ticket).

#### Encryption

To encrypt an index with [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek), set `cmek_id` to the ID of your key. `cmek_id` is available only in the `schema` style, and only when you create the index. With provider v5.1.0 or earlier, it also requires a managed deployment.

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_cmek" {
  name    = "example-index-cmek"
  cmek_id = "YOUR_CMEK_KEY_ID"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      _values = { dense_vector = { dimension = 1536, metric = "cosine" } }
    }
  }
}
```

#### Update and recreate indexes

You can [update](/guides/manage-data/manage-indexes) the following attributes of an existing index in place:

* `deletion_protection`
* `tags`
* `read_capacity`
* `embed.read_parameters` and `embed.write_parameters` on a [legacy integrated index](#legacy-integrated-indexes)
* `spec.pod.replicas` and `spec.pod.pod_type` on an existing [pod-based index](#pod-based-indexes)

Changing `name`, `schema`, `deployment`, `cmek_id`, `dimension`, `metric`, `vector_type`, or `spec.serverless.cloud` and `region` replaces the index, which deletes the records it holds.

Some changes are rejected at plan time instead of replacing the index. These include removing integrated embedding from a field, changing `embed` on a legacy integrated index, and changing a pod-based index in a way that would need a new one. To recreate an index on purpose, taint it, then apply:

```bash theme={null}
terraform taint pinecone_index.example_index
terraform apply
```

`terraform apply -replace` doesn't get past these errors, because Terraform still plans the change against the existing index first. Use `terraform taint` instead.

#### Move an index to the schema style

You can move an existing vector index from the `spec` style to the `schema` style without replacing it. Rewrite the configuration to describe the same index, and the plan shows an in-place update that only changes Terraform state. The API isn't called.

```hcl Terraform theme={null}
# Before: the spec style
resource "pinecone_index" "example_index" {
  name      = "example-index"
  dimension = 1536
  metric    = "cosine"
  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-west-2"
    }
  }
}

# After: the schema style
resource "pinecone_index" "example_index" {
  name = "example-index"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-west-2"
    }
  }
  schema = {
    fields = {
      _values = { dense_vector = { dimension = 1536, metric = "cosine" } }
    }
  }
}
```

Each attribute maps as follows:

| `spec` style | `schema` style |
| :- | :- |
| `dimension` and `metric`, on an index that stores dense vectors | `schema.fields._values = { dense_vector = { dimension = ..., metric = ... } }` |
| `vector_type = "sparse"` | `schema.fields._sparse_values = { sparse_vector = {} }` |
| `spec.serverless.cloud` and `region` | `deployment.managed.cloud` and `region` |
| `spec.byoc.environment` | `deployment.byoc.environment` |
| `spec.serverless.read_capacity` or `spec.byoc.read_capacity` | `read_capacity` |
| `spec.serverless.schema` or `spec.byoc.schema` (deprecated) | Remove it. Pinecone indexes metadata automatically. |
| `name`, `deletion_protection`, `tags`, `timeouts` | Unchanged |

The dimension, metric, and location must match the existing index, or the plan fails with `The configuration describes a different index`. Set `metric` on `_values` even if the `spec` style left it to its default of `cosine`. If the plan shows a replacement, something besides the style changed, such as `name`. Check the configuration before you apply.

> [!WARNING]
>
> The move is one way. An index in the `schema` style can't move back to the `spec` style. Legacy integrated indexes and pod-based indexes can't move to the `schema` style.

#### Legacy integrated indexes

Indexes created with the top-level `embed` attribute are legacy integrated indexes. You read and write them through the legacy Records API. They still use the `spec` style, and existing configurations keep working. For new indexes, use [integrated embedding](#integrated-embedding) on a document index instead.

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_legacy_integrated" {
  name = "example-index-legacy-integrated"
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
  }
}
```

`embed` is fixed when you create the index. You can't add or remove it, or change `model` or `field_map`, on an existing index. You can update `read_parameters` and `write_parameters` in place.

#### Pod-based indexes

> [!WARNING]
>
> Pod-based indexes are legacy. Customers who signed up for a Standard or Enterprise plan on or after August 18, 2025 cannot create them. [Create a serverless index](/guides/index-data/create-an-index) instead. Serverless indexes use on-demand read capacity by default, or [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview) for sustained high query rates and workloads of millions of records or more.

API version `2026-07` doesn't support creating [pod-based indexes](/guides/indexes/pods/understanding-pod-based-indexes), so the provider can't create them either, including from a collection with `spec.pod.source_collection`. You can still [import](#import-existing-resources), scale, and delete existing pod-based indexes.

```hcl Terraform theme={null}
# An existing pod-based index, brought under management with terraform import
resource "pinecone_index" "example_index_pod" {
  name      = "example-index-pod"
  dimension = 1536
  spec = {
    pod = {
      environment = "us-west4-gcp"
      pod_type    = "p1.x2"
      replicas    = 2
      shards      = 1
    }
  }
}
```

Changing `replicas` or `pod_type` scales the index in place, and the apply waits until scaling finishes. `pod_type` can only grow within the same pod family, for example from `p1.x1` to `p1.x2`. Changes that would replace a pod-based index, such as to `name`, `dimension`, `metric`, `environment`, or `shards`, fail at plan time.

#### Timeouts

Index creation, updates, and deletion each time out after 10 minutes by default. Creation waits for the index and any read capacity it configures to be ready. Updates wait for read capacity changes and pod-based scaling to finish. To override the defaults, set a `timeouts` block:

```hcl Terraform theme={null}
resource "pinecone_index" "example_index_timeouts" {
  name = "example-index-timeouts"
  deployment = {
    managed = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
  schema = {
    fields = {
      _values = { dense_vector = { dimension = 1536, metric = "cosine" } }
    }
  }

  timeouts {
    create = "20m"
    update = "20m"
    delete = "15m"
  }
}
```

> [!NOTE]
>
> If creating an index times out, Terraform marks it tainted and replaces it on the next apply. When you create an index with dedicated read capacity, set `timeouts.create` high enough for the read nodes to be provisioned.

### Collections

The `pinecone_collection` resource lets you create and delete [collections](/guides/indexes/pods/understanding-collections). Collections are created from pod-based indexes, which can no longer be created, so set `source` to the name of an existing pod-based index.

```hcl Terraform theme={null}
resource "pinecone_collection" "example_collection" {
  name   = "example-collection"
  source = "YOUR_POD_BASED_INDEX_NAME"
}
```

`dimension`, `size`, and `vector_count` are read-only. Collections also accept a `timeouts` block for `create` and `delete`, each with a 10-minute default.

### Projects

The `pinecone_project` resource lets you create, update, and delete [projects](/admin/projects/understanding-projects). Once `force_encryption_with_cmek` is enabled, it can't be disabled. `max_pods` defaults to `0`, which allows serverless indexes only.

> [!WARNING]
>
> Pod-based indexes are legacy. Customers who signed up for a Standard or Enterprise plan on or after August 18, 2025 cannot create them. [Create a serverless index](/guides/index-data/create-an-index) instead. Serverless indexes use on-demand read capacity by default, or [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview) for sustained high query rates and workloads of millions of records or more.

Customers on those plans also can't set `max_pods` for a project.

```hcl Terraform theme={null}
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

The `pinecone_api_key` resource lets you create, update, and delete [API keys](/admin/projects/manage-api-keys). Valid `roles` values are `ProjectEditor`, `ProjectViewer`, `ControlPlaneEditor`, `ControlPlaneViewer`, `DataPlaneEditor`, and `DataPlaneViewer`. `roles` defaults to `["ProjectEditor"]`.

> [!NOTE]
>
> You can update only the name and roles of an API key. `project_id` is required when you create a key.

```hcl Terraform theme={null}
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

> [!WARNING]
>
> The generated secret is available as the read-only `key` attribute, which the API returns only once, at creation. Terraform stores it in plaintext in state. Marking it sensitive keeps it out of CLI output and logs, but does not encrypt it in state. Secure your state backend and never commit state to version control.

### Service accounts

The `pinecone_service_account` resource lets you create, update, and delete [service accounts](/admin/organizations/manage-service-accounts). A service account authenticates with an OAuth client ID and secret. Grant it roles with a [role binding](#role-bindings).

```hcl Terraform theme={null}
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

> [!WARNING]
>
> The `client_secret` attribute is returned only once, at creation or rotation, and Terraform stores it in plaintext in state. Marking it sensitive keeps it out of CLI output and logs, but does not encrypt it in state. Secure your state backend and never commit state to version control.

### Role bindings

The `pinecone_role_binding` resource lets you grant a role to a principal at organization or project scope. For details on the role model, see [Manage roles and access](/admin/security/manage-rbac).

* Set `principal_type` to `user`, `service_account`, or `api_key`, and `principal_id` to that principal's ID.
* Set `resource_type` to `organization` or `project`. For project scope, `resource_id` is required and must be the project ID. For organization scope, omit `resource_id`. The binding applies to the caller's organization.
* Organization-scoped `role` values are `OrgOwner`, `OrgManager`, `OrgBillingAdmin`, and `OrgMember`. Project-scoped values are `ProjectOwner`, `ProjectManager`, `ProjectMember`, `ProjectEditor`, `ProjectViewer`, `ControlPlaneEditor`, `ControlPlaneViewer`, `DataPlaneEditor`, and `DataPlaneViewer`.

```hcl Terraform theme={null}
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

> [!NOTE]
>
> Role bindings are immutable. Changing any attribute revokes the existing binding and creates a new one.

The `pinecone_role_binding` resource doesn't accept `principal_type = "invite"`. Pinecone moves an invite's bindings to the user principal when the invite is accepted, so Terraform can't manage them across that transition. To grant roles to someone who hasn't joined your organization yet, use [`pinecone_invite`](#invites), then manage their roles here with `principal_type = "user"` once they accept. The `pinecone_role_bindings` data source does accept `invite`, so you can still read what a pending invite granted.

### Invites

The `pinecone_invite` resource manages an [organization invitation](/admin/organizations/manage-organization-members), not the resulting membership. Creating it sends an invite to the given email with a set of initial roles. Deleting it revokes an invite that's still pending. The `role_bindings` list must include at least one organization-scoped role that grants membership.

```hcl Terraform theme={null}
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

> [!WARNING]
>
> Invites are immutable, so changing `email` or `role_bindings` sends a new invite. Don't change either one after the invite is accepted. The replacement re-invites an address that already belongs to a member, and the operation fails. Manage an existing member's roles with [`pinecone_role_binding`](#role-bindings) instead.

> [!NOTE]
>
> Pinecone doesn't return the roles an invite granted, so `role_bindings` is applied only at creation. Terraform can't detect drift on it or recover it on import. To read the bindings, use the `pinecone_role_bindings` data source with `principal_type = "invite"`.

### Users

The `pinecone_user` resource manages an existing [organization member](/admin/organizations/manage-organization-members). You can't create or update users through Terraform. They join your organization by accepting an [invite](#invites). Bring an existing user under management with [`terraform import`](#import-existing-resources). To change a user's roles, use a [role binding](#role-bindings).

> [!WARNING]
>
> Destroying a `pinecone_user` resource removes that person from your organization. A `terraform destroy`, or removing the resource from your configuration, revokes a colleague's access to every project in the organization.

```hcl Terraform theme={null}
resource "pinecone_user" "example_user" {
  id = "YOUR_USER_ID"
}
```

The `id` attribute is immutable. To manage a different user, run `terraform state rm` on this resource and import the intended one.

## Read existing resources

Data sources let you read resources that Terraform doesn't manage. Most resource types have a singular data source that fetches one object and a plural data source that lists many.

| Data source | Required | Optional filters | Credential |
| :- | :- | :- | :- |
| `pinecone_index` | `name` | — | API key |
| `pinecone_indexes` | — | — | API key |
| `pinecone_collection` | `name` | — | API key |
| `pinecone_collections` | — | — | API key |
| `pinecone_project` | `id` | — | Service account |
| `pinecone_projects` | — | — | Service account |
| `pinecone_service_account` | `id` | — | Service account |
| `pinecone_service_accounts` | — | — | Service account |
| `pinecone_role_binding` | `id` | — | Service account |
| `pinecone_role_bindings` | — | `principal_type`, `principal_id`, `resource_type`, `resource_id`, `role` | Service account |
| `pinecone_invite` | `id` | — | Service account |
| `pinecone_invites` | — | — | Service account |
| `pinecone_user` | `id` or `email` | — | Service account |
| `pinecone_users` | — | `email` | Service account |

```hcl Terraform theme={null}
# Read one index by name
data "pinecone_index" "example_index" {
  name = "example-index"
}

# The dimension of a vector index
output "example_index_dimension" {
  value = data.pinecone_index.example_index.schema.fields["_values"].dense_vector.dimension
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

* `pinecone_index` and `pinecone_indexes` report each index's full `schema`, including the reserved vector fields and the metadata fields added as you upsert data. They also report `deployment`, top-level `read_capacity`, `private_host`, `cmek_id`, `source_backup_id`, and `source_collection`.
* `dimension`, `metric`, and `vector_type` on the index data sources are derived from the schema, and are null when the schema doesn't determine a single value, as for an index with only full-text-search fields. They're planned for deprecation, so read `schema` instead.
* For `pinecone_user`, set exactly one of `id` or `email`. Email matching is case-insensitive.
* For `pinecone_role_bindings`, `principal_type` is required when you set `principal_id`, and `resource_type` is required when you set `resource_id`. You can't filter by a binding's own ID. Fetch it with the `pinecone_role_binding` data source instead.
* `pinecone_invites` returns only `pending` and `expired` invites. To read an accepted invite, fetch it by ID with `pinecone_invite`.
* The service account data sources never return client secrets.

## Import existing resources

All resources support the [`terraform import` command](https://developer.hashicorp.com/terraform/cli/commands/import):

| Resource | Import ID |
| :- | :- |
| `pinecone_index` | Index name |
| `pinecone_collection` | Collection name |
| `pinecone_project` | Project ID |
| `pinecone_api_key` | `PROJECT_ID:API_KEY_ID` |
| `pinecone_service_account` | Service account ID |
| `pinecone_role_binding` | Role binding ID |
| `pinecone_invite` | Invite ID |
| `pinecone_user` | User ID |

For example:

```bash theme={null}
terraform import pinecone_user.example_user YOUR_USER_ID
```

Import stores document indexes in state in the `schema` style, and every other index in the `spec` style, however the index was created. You can still import a vector index into a `schema` style configuration. The next plan [moves it](#move-an-index-to-the-schema-style) with the same state-only update.

> [!NOTE]
>
> Provider v5.0.0 doesn't record integrated embedding when it imports a document index. After you upgrade to v5.1.0, a plan for such an index fails with `Integrated embedding can't be removed from a field`. To fix it, add `embed = {}` or `sparse_embed = {}` to the field so the configuration matches the index. The provider reads the model and other settings from the index, so the plan then shows no changes.

Some attributes can't be imported because Pinecone returns them only once:

* `pinecone_api_key.key` and `pinecone_service_account.client_secret` stay empty in state for an imported resource. To issue and store a new service account secret, change `rotate_trigger`.
* `pinecone_invite.role_bindings` stays empty in state, and Terraform proposes a replacement on the next plan until you set it to match the original invite. Use the `pinecone_role_bindings` data source with `principal_type = "invite"` to see what the invite granted.

## Limitations

The provider manages infrastructure only. You reference BYOC environments that Pinecone provisions for you. The provider doesn't support the following:

* [Backups for serverless indexes](/guides/manage-data/backups-overview), including restoring an index from a backup
* Creating pod-based indexes, or creating an index from a collection
* [Private endpoints](/guides/production/configure-private-endpoints)
* [Assistants](/guides/assistant/overview)
* BYOC environment provisioning
* Data operations, such as upserting, querying, or deleting records and documents

## Resources

* For the full provider documentation, see the [Terraform Registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs).
* For more usage examples, see the [GitHub repository](https://github.com/pinecone-io/terraform-provider-pinecone/tree/main/examples).
* For support requests, create an issue in the [GitHub repository](https://github.com/pinecone-io/terraform-provider-pinecone).
