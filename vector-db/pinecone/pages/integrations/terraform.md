---
title: "Terraform"
source: https://docs.pinecone.io/integrations/terraform
path: integrations/terraform
---

Connect Pinecone and Terraform to ship vector search and RAG: embed, index, and query at scale with managed infrastructure.

Terraform is an infrastructure as code tool that lets you create, update, and version infrastructure by defining resources in configuration files. This allows for a repeated workflow for provisioning and managing your infrastructure.

This page describes how to use the [Terraform Provider for Pinecone](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs) to manage Pinecone indexes, collections, API keys, and projects.

## Requirements

Ensure you have the following:

* [Terraform](https://developer.hashicorp.com/terraform) >= v1.4.6
* [Go](https://go.dev/doc/install) >= v1.23.7
* A [Pinecone API key](https://app.pinecone.io/organizations/-/keys) for managing indexes and collections
* A [Pinecone service account](https://app.pinecone.io/organizations/-/settings/access/service-accounts) for managing API keys and projects

## Install the provider

1. Configuring the Pinecone provider in your Terraform configuration file:

   ```hcl theme={null}
   terraform { 
     required_providers { 
       pinecone = { 
         source = "pinecone-io/pinecone" 
         version = "~> 2.0.0"
       } 
     } 
   } 
   ```

2. Run `terraform init` to install the provider from the [Terraform registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest). Alternatively, you can download the latest binary for your target platfrom the [GitHub repository](https://github.com/pinecone-io/terraform-provider-pinecone/releases).

## Authenticate

For managing indexes and collections, you authenticate with a [Pinecone API key](https://app.pinecone.io/organizations/-/keys). For managing API keys and projects, you authenticate with [Pinecone service account](https://app.pinecone.io/organizations/-/settings/access/service-accounts) credentials (client ID and client secret).

1. Set environment variables for authentication:

   ```bash theme={null}
   # For indexes and collections  
   export PINECONE_API_KEY="YOUR_API_KEY"

   # For API keys and projects
   export PINECONE_CLIENT_ID="YOUR_CLIENT_ID"
   export PINECONE_CLIENT_SECRET="YOUR_CLIENT_SECRET"
   ```

2. Append the following to your Terraform configuration file:

   ```hcl theme={null}
   provider "pinecone" {}
   ```

<Note>
  You can also set the API key and/or service account credential as [input variables](https://developer.hashicorp.com/terraform/language/values/variables).
</Note>

## Manage resources

The Terraform Provider for Pinecone allows Terraform to manage indexes, collections, API keys, and projects.

### Indexes

The `pinecone_index` resource lets you create, update, and delete [indexes](/guides/index-data/indexing-overview).

<Note>
  You can [update](/guides/manage-data/manage-indexes) only the index deletion protection, tags, and integrated inference embedding settings of an index.
</Note>

```terraform theme={null}
# Index for dense vectors
resource "pinecone_index" "example-index" {
  name = "example-index"
  dimension = 1536
  metric = "cosine"
  vector_type = "dense"
  spec = {
    serverless = {
      cloud = "aws"
      region = "us-west-2"
    }
  }
  deletion_protection = "disabled"
  tags = {
    environment = "development"
  }
}

# Index for dense vectors with integrated embedding
resource "pinecone_index" "example-index-integrated" {
  name = "example-index-integrated"
  spec = {
    serverless = {
      cloud = "aws"
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

### Collections

The `pinecone_collection` resource lets you create and delete [collections](/guides/indexes/pods/understanding-collections) for pod-based indexes.

```terraform theme={null}
resource "pinecone_index" "example-index" {
  name = "example-index"
  dimension = 10
  spec = {
    pod = {
      environment = "us-west4-gcp"
      pod_type = "s1.x1"
    }
  }
}

resource "pinecone_collection" "example-collection" {
  name = "example-collection"
  source = pinecone_index.example-index.name
```

### API keys

The `pinecone_api_key` resource lets you create, update, and delete [API keys](/guides/projects/manage-api-keys).

<Note>
  You can update only the name and roles of an API key.
</Note>

```terraform theme={null}
# API key with default roles (ProjectEditor)
resource "pinecone_api_key" "example-key" {
  name = "example-key"
  project_id = "YOUR_PROJECT_ID"
}

# API key with custom roles
resource "pinecone_api_key" "example-key-custom_roles" {
  name = "example-key-custom-roles"
  project_id = "YOUR_PROJECT_ID"
  roles = ["ProjectViewer", "DataPlaneViewer"]
}

output "api_key_roles" {
  description = "The roles assigned to the API key"
  value       = pinecone_api_key.example.roles
}
```

### Projects

The `pinecone_project` resource lets you create, update, and delete [projects](/guides/projects/understanding-projects).

<Warning>
  Customers who signed up for a Standard or Enterprise plan on or after August 18, 2025 cannot create [pod-based indexes](/guides/indexes/pods/understanding-pod-based-indexes) and cannot set the max pods for a project.
</Warning>

```terraform theme={null}
# Basic project
resource "pinecone_project" "example-project" {
  name = "example-project"
}

# Project with CMEK encryption enabled
resource "pinecone_project" "example-project-encrypted" {
  name = "example-project-encrypted"
  force_encryption_with_cmek = true
}

# Project with custom max pods
resource "pinecone_project" "example-project-custom-pods" {
  name = "example-project-custom-pods"
  max_pods = 10
}
```

## Limitations

The Terraform Provider for Pinecone does not support the following resources:

* [Backups for serverless indexes](/guides/manage-data/backups-overview)
* [Service accounts](/guides/projects/manage-service-accounts)
* [Private endpoints](/guides/production/configure-private-endpoints)
* [Assistants](/guides/assistant/overview)

## See also

* Documentation can be found on the [Terraform
  Registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs).
* See the [GitHub respository](https://github.com/pinecone-io/terraform-provider-pinecone/tree/main/examples)
  for additional usage examples.
* For support requests, create an issue in the [GitHub
  repository](https://github.com/pinecone-io/terraform-provider-pinecone).
