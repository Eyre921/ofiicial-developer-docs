---
title: "Deploy with Terraform"
source: https://developers.deepgram.com/docs/terraform-deploy-sagemaker.md
path: docs/terraform-deploy-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deploy with Terraform

> Deploy a Deepgram SageMaker Endpoint with Terraform using an AWS Marketplace Model Package ARN. Includes IAM role, endpoint configuration, auto-scaling, and optional environment variable overrides.

This guide provides a complete Terraform configuration for deploying Deepgram on Amazon SageMaker. The configuration creates an IAM execution role, a SageMaker Model from your AWS Marketplace subscription, an Endpoint Configuration, and a live Endpoint. An optional module adds auto-scaling. The same configuration can deploy either a real-time endpoint (the default) or an asynchronous endpoint that processes large pre-recorded files from S3 and can scale to zero — set `enable_async_inference = true`.

Before running Terraform, you must subscribe to a Deepgram product on the AWS Marketplace and note the **Model Package ARN**. Subscribe via [the AWS Management Console](/docs/deploy-amazon-sagemaker#subscribe-to-deepgram-products-via-aws-marketplace-console) or [the AWS Marketplace API](#subscribe-to-a-deepgram-product-via-the-marketplace-api), then see [Find the Model Package ARN](#find-the-model-package-arn).

## Prerequisites

* [Terraform](https://developer.hashicorp.com/terraform/install) 1.5 or later
* AWS credentials configured for the target account (via environment variables, shared credentials file, or an IAM role)
* An active AWS Marketplace subscription to a [Deepgram SageMaker product](https://aws.amazon.com/marketplace/search/results?searchTerms=deepgram\&CREATOR=6efa21f9-9a33-4cae-ba44-756436fa71dd\&FULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL\&filters=CREATOR%2CFULFILLMENT_OPTION_TYPE). You can subscribe through the console or, if you provision infrastructure as code, [via the Marketplace API](#subscribe-to-a-deepgram-product-via-the-marketplace-api).
* The **Model Package ARN** for the subscribed product. See [Find the Model Package ARN](#find-the-model-package-arn) for how to locate it in the AWS Marketplace **Manage subscriptions** console.

## Subscribe to a Deepgram product via the Marketplace API

If you provision infrastructure as code, you can subscribe to a Deepgram SageMaker product entirely through the AWS Marketplace API instead of the console. This section is an alternative to [Subscribe to Deepgram Products via AWS Marketplace Console](/docs/deploy-amazon-sagemaker#subscribe-to-deepgram-products-via-aws-marketplace-console) — use whichever method fits your workflow, then continue to [Find the Model Package ARN](#find-the-model-package-arn).

The steps below use the AWS CLI, but AWS also publishes [SDKs for many languages](https://aws.amazon.com/developer/tools/) — including Python (Boto3), Node.js, Java, Go, and .NET — that expose the same Marketplace Discovery and Agreement Service APIs. Use whichever SDK fits your stack to build your own subscription automations and scripts.

Subscribing creates a billing agreement on your AWS account. You are not charged until you deploy a SageMaker Endpoint and send it traffic — the usage-based pricing term has no upfront cost — but `AcceptAgreementRequest` (the last step below) is not a dry run. It creates a real, active agreement.

### Permissions

The [AWSMarketplaceManageSubscriptions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html) policy referenced in [Prerequisites](/docs/deploy-amazon-sagemaker#prerequisites) covers product discovery (`SearchListings`, `GetOffer`, `GetOfferTerms`, `ListPurchaseOptions`, and similar) but does **not** include the AWS Marketplace Agreement Service actions this flow also needs: `CreateAgreementRequest`, `AcceptAgreementRequest`, `DescribeAgreement`, `SearchAgreements`, and `GetAgreementTerms`. Either attach [AWSMarketplaceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.html) or add those five actions to a custom policy alongside `AWSMarketplaceManageSubscriptions`.

#### Find the product ID

List Deepgram's SageMaker-deployable products, filtered by fulfillment type and seller:

```bash
aws marketplace-discovery search-listings \
  --region us-east-1 \
  --filters '[
    {"filterType": "FULFILLMENT_OPTION_TYPE", "filterValues": ["SAGEMAKER_MODEL"]},
    {"filterType": "PUBLISHER", "filterValues": ["6efa21f9-9a33-4cae-ba44-756436fa71dd"]}
  ]' \
  --query 'listingSummaries[].{name:listingName,productId:associatedEntities[0].product.productId}'
```

```json
[
  {
    "name": "Deepgram Voice AI Nova-3 Monolingual Speech-to-Text (STT) Streaming",
    "productId": "prod-tnv5pm6nlcm44"
  },
  {
    "name": "Deepgram Voice AI- Aura-2 Text-to-Speech- English",
    "productId": "prod-..."
  }
]
```

`6efa21f9-9a33-4cae-ba44-756436fa71dd` is Deepgram's AWS Marketplace seller profile ID. Note the `productId` for the listing you want to deploy (eg. `prod-tnv5pm6nlcm44` for Nova-3 Monolingual Streaming).

Calls the [`SearchListings`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Find the standard offer for that product

```bash
aws marketplace-discovery list-purchase-options \
  --region us-east-1 \
  --filters '[{"filterType": "PRODUCT_ID", "filterValues": ["prod-tnv5pm6nlcm44"]}]' \
  --query 'purchaseOptions[].{offerId:purchaseOptionId,name:purchaseOptionName,badges:badges}'
```

This can return more than one purchase option — for example, a private offer your account manager extended to you, alongside the standard public offer. **The standard public offer has no `PRIVATE_PRICING` badge and no custom `purchaseOptionName`** (AWS labels it `"Offer created on <timestamp>"`). Use a private offer's ID instead if your account has negotiated pricing.

Calls the [`ListPurchaseOptions`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Get the offer's proposal ID and pricing model

```bash
aws marketplace-discovery get-offer --region us-east-1 --offer-id <offer-id-from-previous-step>
```

Note the `agreementProposalId` and `pricingModel.pricingModelType` from the response — you need both for the next steps.

Calls the [`GetOffer`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Get the offer's terms

```bash
aws marketplace-discovery get-offer-terms --region us-east-1 --offer-id <offer-id>
```

The response lists one or more terms, each with an `id`. For a `USAGE`-priced Deepgram SageMaker product, expect `LegalTerm`, `SupportTerm`, and `UsageBasedPricingTerm` — collect all three `id` values. Deepgram's public SageMaker listings also include a `FreeTrialPricingTerm` (14 days); collect its `id` too if you want to claim the trial. See [Required terms by pricing model](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-agreement-api-buyer.html#car-required-terms-by-pricing-model) if the offer uses a different pricing model.

Calls the [`GetOfferTerms`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html) action of the [AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Discovery.html).

#### Generate a quote

```bash
aws marketplace-agreement create-agreement-request \
  --region us-east-1 \
  --agreement-proposal-identifier <agreementProposalId-from-step-3> \
  --intent NEW \
  --requested-terms '[
    {"id": "<LegalTerm id>"},
    {"id": "<SupportTerm id>"},
    {"id": "<UsageBasedPricingTerm id>"},
    {"id": "<FreeTrialPricingTerm id>"}
  ]'
```

Returns an `agreementRequestId` and a `chargeSummary`. For usage-based pricing, `newAgreementValue` is `"0.00"` — you're only quoted for the mandatory terms, not future usage.

Calls the [`CreateAgreementRequest`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_CreateAgreementRequest.html) action of the [AWS Marketplace Agreement Service API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html).

`FreeTrialPricingTerm` can be accepted only once per product. If your account has already used the trial for this product, omit that term's `id` from `requestedTerms` — including it again returns a `ValidationException`. If your account already has an active agreement for this product at all, the whole call fails with `ValidationException` / `UNSUPPORTED_ACTION` ("This action is not supported when an active agreement exists on the same resourceId"). Check first with the [`SearchAgreements`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SearchAgreements.html) action: `aws marketplace-agreement search-agreements --region us-east-1 --catalog AWSMarketplace --filters '[{"name":"PartyType","values":["Acceptor"]},{"name":"AgreementType","values":["PurchaseAgreement"]},{"name":"ResourceIdentifier","values":["<productId>"]}]'` — if an agreement with `"status": "ACTIVE"` already exists, you're already subscribed; skip to [Find the Model Package ARN](#find-the-model-package-arn).

#### Accept the quote to subscribe

```bash
aws marketplace-agreement accept-agreement-request \
  --region us-east-1 \
  --agreement-request-id <agreementRequestId-from-previous-step>
```

Returns the new `agreementId`. This is the subscribe action — it's equivalent to clicking **Subscribe** in the console.

Calls the [`AcceptAgreementRequest`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AcceptAgreementRequest.html) action of the [AWS Marketplace Agreement Service API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html).

#### Confirm the subscription is active

```bash
aws marketplace-agreement describe-agreement --region us-east-1 --agreement-id <agreementId>
```

`status` moves from `ACTIVE` immediately, but the underlying entitlement can take a few minutes to provision — the same delay you'd see waiting on the console's subscription page. Poll `aws marketplace-agreement get-agreement-entitlements --region us-east-1 --agreement-id <agreementId>` until it clears `PENDING`/`PROVISIONING_IN_PROGRESS` before continuing to [Find the Model Package ARN](#find-the-model-package-arn).

Calls the [`DescribeAgreement`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_DescribeAgreement.html) and [`GetAgreementEntitlements`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementEntitlements.html) actions of the [AWS Marketplace Agreement Service API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html).

## Find the Model Package ARN

The Terraform configuration references the **Model Package ARN** for the product version and AWS Region you plan to deploy. The AWS Marketplace surfaces the ARN through the CLI configuration view.

In the AWS Management Console, navigate to the [AWS Marketplace **Manage subscriptions** console](https://us-east-1.console.aws.amazon.com/marketplace/subscriptions)

On the **Active subscriptions** tab, find the subscription for the Deepgram product you want to deploy (eg. *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming*)

Click the **Configure** button in the **Actions** column on the right-hand side

In the **Setup** box, under **Service**, choose **AWS command line interface (CLI)**

Under the **Version** header, select the product version from the dropdown. If the listing has more than one version, read the version name and the release notes to understand the set of languages (or features) each version provides, and choose the version that matches your needs

Scroll down. On the right-hand side of the page, a list of **Model ARNs** is shown. Note the correct Model Package ARN for the AWS Region you plan to deploy to

## Project layout

```
deepgram-sagemaker-terraform/
├── main.tf           # Provider and resource definitions
├── variables.tf      # Input variables
├── outputs.tf        # Endpoint name, ARN, and status outputs
└── terraform.tfvars  # Your variable values (do not commit secrets)
```

## Variables

Create `variables.tf` with the input variables the configuration needs. The only required value is the Model Package ARN from your Marketplace subscription.

```hcl title="variables.tf"
variable "aws_region" {
  description = "AWS region where the SageMaker Endpoint will be deployed."
  type        = string
  default     = "us-east-1"
}

variable "model_package_arn" {
  description = "ARN of the Deepgram Model Package from AWS Marketplace."
  type        = string
}

variable "model_name" {
  description = "Name for the SageMaker Model resource."
  type        = string
  default     = "deepgram-stt"
}

variable "endpoint_name" {
  description = "Name for the SageMaker Endpoint."
  type        = string
  default     = "deepgram-stt-endpoint"
}

variable "instance_type" {
  description = "SageMaker instance type for the endpoint."
  type        = string
  default     = "ml.g5.2xlarge"
}

variable "initial_instance_count" {
  description = "Number of instances to launch at endpoint creation."
  type        = number
  default     = 1
}

variable "variant_name" {
  description = "Name of the production variant."
  type        = string
  default     = "AllTraffic"
}

variable "deepgram_engine_env" {
  description = "Map of DEEPGRAM_ENGINE_* environment variables for TOML overrides."
  type        = map(string)
  default     = {}
}

variable "deepgram_api_env" {
  description = "Map of DEEPGRAM_API_* environment variables for TOML overrides."
  type        = map(string)
  default     = {}
}

variable "enable_autoscaling" {
  description = "Enable auto-scaling for the endpoint."
  type        = bool
  default     = false
}

variable "autoscaling_min_capacity" {
  description = "Minimum instance count for auto-scaling."
  type        = number
  default     = 1
}

variable "autoscaling_max_capacity" {
  description = "Maximum instance count for auto-scaling."
  type        = number
  default     = 4
}

variable "autoscaling_target_value" {
  description = "Target concurrent requests per instance for the scaling policy."
  type        = number
  default     = 5.0
}

variable "enable_async_inference" {
  description = "Deploy an asynchronous endpoint (queued, S3 in/out) instead of a real-time endpoint. Async endpoints accept only asynchronous invocations."
  type        = bool
  default     = false
}

variable "async_s3_output_path" {
  description = "S3 URI for async transcription output, e.g. s3://my-bucket/output/. Required when enable_async_inference = true."
  type        = string
  default     = ""

  validation {
    condition     = var.async_s3_output_path == "" || can(regex("^s3://", var.async_s3_output_path))
    error_message = "async_s3_output_path must be an s3:// URI."
  }
}

variable "async_s3_failure_path" {
  description = "Optional S3 URI for async failure output, e.g. s3://my-bucket/failures/."
  type        = string
  default     = ""
}
```

> In async mode, `autoscaling_target_value` is interpreted as the target **`ApproximateBacklogSizePerInstance`** (queued requests per instance), and `autoscaling_min_capacity` may be set to `0` to enable scale-to-zero. In real-time mode it remains concurrent-requests-per-instance with a minimum of 1.

## Main configuration

Create `main.tf` with the provider, IAM role, and SageMaker resources. The configuration uses the Model Package ARN from your AWS Marketplace subscription to create the model without referencing a container image directly.

```hcl title="main.tf" maxLines=20
###############################################################################
# Provider
###############################################################################

terraform {
  required_version = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

###############################################################################
# IAM Role — SageMaker Execution
###############################################################################

data "aws_iam_policy_document" "sagemaker_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["sagemaker.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "sagemaker_execution" {
  name               = "${var.model_name}-execution-role"
  assume_role_policy = data.aws_iam_policy_document.sagemaker_assume_role.json
}

resource "aws_iam_role_policy_attachment" "sagemaker_full_access" {
  role       = aws_iam_role.sagemaker_execution.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
}

###############################################################################
# Async S3 access (only when enable_async_inference = true)
###############################################################################

locals {
  async_buckets = var.enable_async_inference ? toset(compact([
    try(split("/", replace(var.async_s3_output_path, "s3://", ""))[0], ""),
    try(split("/", replace(var.async_s3_failure_path, "s3://", ""))[0], ""),
  ])) : toset([])
}

resource "aws_iam_role_policy" "async_s3" {
  count = var.enable_async_inference ? 1 : 0

  name = "${var.model_name}-async-s3"
  role = aws_iam_role.sagemaker_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject", "s3:PutObject"]
        Resource = [for b in local.async_buckets : "arn:aws:s3:::${b}/*"]
      },
      {
        Effect   = "Allow"
        Action   = ["s3:ListBucket"]
        Resource = [for b in local.async_buckets : "arn:aws:s3:::${b}"]
      },
    ]
  })
}

###############################################################################
# Merge Deepgram environment variables
###############################################################################

locals {
  deepgram_env = merge(
    { for k, v in var.deepgram_engine_env : "DEEPGRAM_ENGINE_${k}" => v },
    { for k, v in var.deepgram_api_env : "DEEPGRAM_API_${k}" => v },
  )
}

###############################################################################
# SageMaker Model — from AWS Marketplace Model Package
###############################################################################

resource "aws_sagemaker_model" "deepgram" {
  name                     = var.model_name
  execution_role_arn       = aws_iam_role.sagemaker_execution.arn
  enable_network_isolation = true

  primary_container {
    model_package_name = var.model_package_arn
    environment        = local.deepgram_env
  }
}

###############################################################################
# SageMaker Endpoint Configuration
###############################################################################

resource "aws_sagemaker_endpoint_configuration" "deepgram" {
  name = "${var.endpoint_name}-config"

  production_variants {
    variant_name           = var.variant_name
    model_name             = aws_sagemaker_model.deepgram.name
    initial_instance_count = var.initial_instance_count
    instance_type          = var.instance_type
  }

  dynamic "async_inference_config" {
    for_each = var.enable_async_inference ? [1] : []
    content {
      output_config {
        s3_output_path  = var.async_s3_output_path
        s3_failure_path = var.async_s3_failure_path != "" ? var.async_s3_failure_path : null
      }
    }
  }

  lifecycle {
    precondition {
      condition     = !var.enable_async_inference || var.async_s3_output_path != ""
      error_message = "async_s3_output_path is required when enable_async_inference = true."
    }
  }
}

###############################################################################
# SageMaker Endpoint
###############################################################################

resource "aws_sagemaker_endpoint" "deepgram" {
  name                 = var.endpoint_name
  endpoint_config_name = aws_sagemaker_endpoint_configuration.deepgram.name
}

###############################################################################
# Auto-Scaling (optional)
###############################################################################

resource "aws_appautoscaling_target" "sagemaker" {
  count = var.enable_autoscaling ? 1 : 0

  max_capacity       = var.autoscaling_max_capacity
  min_capacity       = var.autoscaling_min_capacity
  resource_id        = "endpoint/${aws_sagemaker_endpoint.deepgram.name}/variant/${var.variant_name}"
  scalable_dimension = "sagemaker:variant:DesiredInstanceCount"
  service_namespace  = "sagemaker"
}

resource "aws_appautoscaling_policy" "sagemaker" {
  count = var.enable_autoscaling ? 1 : 0

  name               = "${var.endpoint_name}-concurrency-policy"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.sagemaker[0].resource_id
  scalable_dimension = aws_appautoscaling_target.sagemaker[0].scalable_dimension
  service_namespace  = aws_appautoscaling_target.sagemaker[0].service_namespace

  target_tracking_scaling_policy_configuration {
    target_value = var.autoscaling_target_value

    # Real-time: scale on concurrent requests per model.
    dynamic "predefined_metric_specification" {
      for_each = var.enable_async_inference ? [] : [1]
      content {
        predefined_metric_type = "SageMakerVariantConcurrentRequestsPerModelHighResolution"
      }
    }

    # Async: scale on queue depth per instance.
    dynamic "customized_metric_specification" {
      for_each = var.enable_async_inference ? [1] : []
      content {
        metric_name = "ApproximateBacklogSizePerInstance"
        namespace   = "AWS/SageMaker"
        statistic   = "Average"
        dimensions {
          name  = "EndpointName"
          value = aws_sagemaker_endpoint.deepgram.name
        }
      }
    }

    scale_in_cooldown  = 300
    scale_out_cooldown = 60
  }
}

###############################################################################
# Async scale-from-zero (only when async + autoscaling are enabled)
###############################################################################

resource "aws_appautoscaling_policy" "async_scale_from_zero" {
  count = var.enable_async_inference && var.enable_autoscaling ? 1 : 0

  name               = "${var.endpoint_name}-scale-from-zero"
  policy_type        = "StepScaling"
  resource_id        = aws_appautoscaling_target.sagemaker[0].resource_id
  scalable_dimension = aws_appautoscaling_target.sagemaker[0].scalable_dimension
  service_namespace  = aws_appautoscaling_target.sagemaker[0].service_namespace

  step_scaling_policy_configuration {
    adjustment_type         = "ChangeInCapacity"
    metric_aggregation_type = "Average"
    cooldown                = 300

    step_adjustment {
      metric_interval_lower_bound = 0
      scaling_adjustment          = 1
    }
  }
}

resource "aws_cloudwatch_metric_alarm" "async_has_backlog" {
  count = var.enable_async_inference && var.enable_autoscaling ? 1 : 0

  alarm_name          = "${var.endpoint_name}-has-backlog-without-capacity"
  namespace           = "AWS/SageMaker"
  metric_name         = "HasBacklogWithoutCapacity"
  statistic           = "Average"
  period              = 60
  evaluation_periods  = 2
  datapoints_to_alarm = 2
  threshold           = 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "missing"

  dimensions = {
    EndpointName = aws_sagemaker_endpoint.deepgram.name
  }

  alarm_actions = [aws_appautoscaling_policy.async_scale_from_zero[0].arn]
}
```

## Outputs

Create `outputs.tf` to surface the endpoint details after `terraform apply` completes.

```hcl title="outputs.tf"
output "endpoint_name" {
  description = "Name of the deployed SageMaker Endpoint."
  value       = aws_sagemaker_endpoint.deepgram.name
}

output "endpoint_arn" {
  description = "ARN of the deployed SageMaker Endpoint."
  value       = aws_sagemaker_endpoint.deepgram.arn
}

output "model_name" {
  description = "Name of the SageMaker Model."
  value       = aws_sagemaker_model.deepgram.name
}

output "execution_role_arn" {
  description = "ARN of the IAM execution role."
  value       = aws_iam_role.sagemaker_execution.arn
}

output "async_s3_output_path" {
  description = "S3 location where async transcription results are written (async mode only)."
  value       = var.enable_async_inference ? var.async_s3_output_path : null
}
```

## Example variable values

Create a `terraform.tfvars` file with your specific values. Replace the `model_package_arn` with the ARN from your AWS Marketplace subscription.

```hcl title="terraform.tfvars"
aws_region        = "us-east-1"
model_package_arn = "arn:aws:sagemaker:us-east-1:123456789012:model-package/deepgram-stt-nova-3/1"
model_name        = "deepgram-streaming-stt"
endpoint_name     = "my-deepgram-stt"
instance_type     = "ml.g5.2xlarge"

# Optional: Deepgram configuration overrides
deepgram_engine_env = {
  "01" = "max_active_requests=120"
}
deepgram_api_env = {
  "01" = "features.listen_v2=true"
}

# Optional: Enable auto-scaling
enable_autoscaling       = true
autoscaling_min_capacity = 1
autoscaling_max_capacity = 4
autoscaling_target_value = 5.0

# Optional: deploy an asynchronous endpoint instead of real-time
# enable_async_inference   = true
# async_s3_output_path     = "s3://my-deepgram-async/output/"
# async_s3_failure_path    = "s3://my-deepgram-async/failures/"
# enable_autoscaling       = true
# autoscaling_min_capacity = 0    # async supports scale-to-zero
# autoscaling_target_value = 5.0  # target ApproximateBacklogSizePerInstance
```

Do not commit `terraform.tfvars` to version control if it contains sensitive values. Add it to `.gitignore` or use environment variables instead.

## Deploy

#### Initialize the Terraform working directory

```bash
terraform init
```

#### Preview the resources Terraform will create

```bash
terraform plan
```

Verify the plan shows the expected resources: an IAM role, a SageMaker Model, an Endpoint Configuration, and an Endpoint.

#### Apply the configuration

```bash
terraform apply
```

Terraform creates the resources and waits for the SageMaker Endpoint to reach `InService` status. This typically takes several minutes.

#### Verify the endpoint

Confirm the endpoint is running:

```bash
aws sagemaker describe-endpoint \
  --endpoint-name $(terraform output -raw endpoint_name) \
  --region $(terraform output -raw aws_region 2>/dev/null || echo "us-east-1") \
  --query "EndpointStatus"
```

The output should be `"InService"`.

## Validate the endpoint

After the endpoint reaches `InService`, run a test inference to confirm it returns results. See [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint) for the full testing guide using the [dg-sagemaker](https://github.com/deepgram-devs/dg-sagemaker) test clients.

## Customize the deployment

### Instance types

Choose an instance type based on the Deepgram product you are deploying. GPU-accelerated instances are required.

| Product                       | Recommended instance type | Notes                                     |
| ----------------------------- | ------------------------- | ----------------------------------------- |
| Speech-to-Text (Nova-3, Flux) | `ml.g5.2xlarge`           | Single NVIDIA A10G GPU, 32 GB GPU RAM     |
| Text-to-Speech (Aura)         | `ml.g5.12xlarge`          | 4 NVIDIA A10G GPUs (TTS requires 2+ GPUs) |

For a full list of compatible instances, see the [Deployment Environments](/docs/self-hosted-deployment-environments) hardware specifications.

### Environment variable overrides

Pass Deepgram configuration overrides through the `deepgram_engine_env` and `deepgram_api_env` variables. Each map key becomes the suffix (for example, `"01"`, `"02"`), and the value is the TOML expression. See [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments) for the full reference.

```hcl
deepgram_engine_env = {
  "01" = "flux.max_streams=25"
  "02" = "chunking.streaming.step=0.5"
}
```

### VPC configuration

To deploy the endpoint inside a VPC, add a `vpc_config` block to the `aws_sagemaker_model` resource:

```hcl title="VPC configuration"
resource "aws_sagemaker_model" "deepgram" {
  name                     = var.model_name
  execution_role_arn       = aws_iam_role.sagemaker_execution.arn
  enable_network_isolation = true

  primary_container {
    model_package_name = var.model_package_arn
    environment        = local.deepgram_env
  }

  vpc_config {
    subnets            = ["subnet-0123456789abcdef0", "subnet-0123456789abcdef1"]
    security_group_ids = ["sg-0123456789abcdef0"]
  }
}
```

### Asynchronous endpoints

By default this configuration deploys a **real-time** endpoint for streaming and synchronous transcription. To instead deploy an **asynchronous** endpoint — for large pre-recorded files (up to 1 GB), queued processing, and scale-to-zero — set `enable_async_inference = true` and provide an `async_s3_output_path`.

Asynchronous inference is a distinct endpoint mode: an async endpoint accepts **only** asynchronous invocations (`InvokeEndpointAsync` with S3 input/output) and cannot serve streaming or synchronous requests. Switching `enable_async_inference` replaces the endpoint configuration and endpoint.

When async is enabled, the configuration also:

* grants the execution role `s3:GetObject`, `s3:PutObject`, and `s3:ListBucket` on the output and failure buckets;
* switches the autoscaling target metric to `ApproximateBacklogSizePerInstance` and allows `autoscaling_min_capacity = 0` for scale-to-zero;
* adds a scale-from-zero policy so the endpoint wakes on the first queued request instead of waiting for the backlog to exceed the target value.

For invocation details, see [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker#inference). For autoscaling details, see [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async).

## Tear down

To delete all resources created by this configuration:

```bash
terraform destroy
```

This removes the SageMaker Endpoint, Endpoint Configuration, Model, auto-scaling resources (if enabled), and the IAM execution role. You are no longer billed for SageMaker compute after the endpoint is deleted. Your AWS Marketplace subscription remains active.

***

## Related resources

* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker)
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)
* [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker-streaming)
* [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async)
* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Terraform AWS Provider — aws\_sagemaker\_model](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sagemaker_model)
* [Terraform AWS Provider — aws\_sagemaker\_endpoint](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sagemaker_endpoint)
