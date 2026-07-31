---
title: "Create an index"
source: https://docs.pinecone.io/reference/api/2026-04/control-plane/create_index
path: reference/api/2026-04/control-plane/create_index
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_control_2026-04.oas.yaml post /indexes
Create a Pinecone index. This is where you specify the measure of similarity, the dimension of vectors to be stored in the index, which cloud provider you would like to deploy with, and more.
To restore from a backup, set `spec.serverless.source_backup_id` and specify the target `cloud` and `region`. Same-cloud cross-region restore is supported when available for the backup's source region. Cross-cloud restore is not supported.
For guidance and examples, see [Create an index](https://docs.pinecone.io/guides/index-data/create-an-index).


## Cloud regions

For serverless indexes, the `cloud` and `region` fields in `spec.serverless` accept the following values:

| Cloud   | Region                       | [Supported plans](https://www.pinecone.io/pricing/) | [Availability phase](/release-notes/feature-availability) |
| ------- | ---------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| `aws`   | `us-east-1` (Virginia)       | Starter, Builder, Standard, Enterprise              | General availability                                      |
| `aws`   | `us-west-2` (Oregon)         | Builder, Standard, Enterprise                       | General availability                                      |
| `aws`   | `eu-west-1` (Ireland)        | Builder, Standard, Enterprise                       | General availability                                      |
| `aws`   | `eu-central-1` (Frankfurt)   | Builder, Standard, Enterprise                       | General availability                                      |
| `aws`   | `ap-southeast-1` (Singapore) | Builder, Standard, Enterprise                       | General availability                                      |
| `gcp`   | `us-central1` (Iowa)         | Builder, Standard, Enterprise                       | General availability                                      |
| `gcp`   | `europe-west4` (Netherlands) | Builder, Standard, Enterprise                       | General availability                                      |
| `azure` | `eastus2` (Virginia)         | Builder, Standard, Enterprise                       | General availability                                      |

The cloud and region cannot be changed after a serverless index is created.

<Note>
  On the Starter plan, you can create serverless indexes in the `us-east-1` region of AWS only. To create indexes in other regions, [upgrade to the Builder, Standard, or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

For BYOC indexes, set `spec.byoc.environment` to the environment ID provisioned for your account instead. See [Bring your own cloud](/guides/production/bring-your-own-cloud) for details.

<RequestExample>
  ```shell curl theme={null}
  # EXAMPLE REQUEST 1: Serverless index (on-demand)
  PINECONE_API_KEY="YOUR_API_KEY"
  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "name": "example-serverless-index",
          "vector_type": "dense",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "serverless": {
                  "cloud": "aws",
                  "region": "us-east-1"
              }
          },
          "tags": {
              "tag0": "value0"
          },
          "deletion_protection": "disabled"
        }'

  # EXAMPLE REQUEST 2: Serverless index (dedicated)
  PINECONE_API_KEY="YOUR_API_KEY"
  curl "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
  		"name": "example-serverless-dedicated-index",
  		"dimension": 1536,
  		"metric": "cosine",
  		"deletion_protection": "enabled",
  		"tags": {
  			"tag0": "value0"
  		},
  		"vector_type": "dense",
  		"spec": {
  			"serverless": {
  				"cloud": "aws",
  				"region": "us-east-1",
  				"read_capacity": {
  					"mode": "Dedicated",
  					"dedicated": {
  						"node_type": "b1",
  						"scaling": "Manual",
  						"manual": {
  							"shards": 2,
  							"replicas": 1
  						}
  					}
  				}
  			}
  		}
  	}'

  # EXAMPLE REQUEST 3: BYOC index
  PINECONE_API_KEY="YOUR_API_KEY"
  curl -s "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
          "name": "example-byoc-index",
          "vector_type": "dense",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "byoc": {
                  "environment": "aws-us-east-1-b921"
              }
          },
          "tags": {
              "tag0": "value0"
          },
          "deletion_protection": "disabled"
        }'
  ```
</RequestExample>

<ResponseExample>
  ```jsonc curl theme={null}
  // EXAMPLE RESPONSE 1: Serverless index (on-demand)
  {
    "name": "example-serverless-ondemand-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": false,
      "state": "Initializing"
    },
    "host": "example-serverless-ondemand-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "OnDemand",
          "status": {
            "state": "Ready",
            "current_shards": null,
            "current_replicas": null
          }
        }
      }
    },
    "deletion_protection": "disabled",
    "tags": {
      "tag0": "value0"
    }
  }

  // EXAMPLE RESPONSE 2: Serverless index (dedicated)
  {
  	"name": "example-serverless-dedicated-index",
  	"vector_type": "dense",
  	"metric": "cosine",
  	"dimension": 1536,
  	"status": {
  		"ready": false,
  		"state": "Initializing"
  	},
  	"host": "example-serverless-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
  	"spec": {
  		"serverless": {
  			"region": "us-east-1",
  			"cloud": "aws",
  			"read_capacity": {
  				"mode": "Dedicated",
  				"dedicated": {
  					"node_type": "b1",
  					"scaling": "Manual",
  					"manual": {
  						"shards": 2,
  						"replicas": 1
  					}
  				},
  				"status": {
  					"state": "Migrating",
  					"current_shards": null,
  					"current_replicas": null
  				}
  			}
  		}
  	},
  	"deletion_protection": "enabled",
  	"tags": {
  		"tag0": "value0"
  	}
  }

  // EXAMPLE RESPONSE 3: BYOC index
  {
      "name": "example-byoc-index",
      "vector_type": "dense",
      "metric": "cosine",
      "dimension": 1536,
      "status": {
          "ready": true,
          "state": "Ready"
      },
      "host": "example-byoc-index-govk0nt.svc.private.aped-4627-b74a.pinecone.io",
      "spec": {
          "byoc": {
              "environment": "aws-us-east-1-b921"
          }
      },
      "deletion_protection": "disabled",
      "tags": {
          "tag0": "value0"
      }
  }
  ```
</ResponseExample>
