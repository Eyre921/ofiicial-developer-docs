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

Before running Terraform, you must subscribe to a Deepgram product on the AWS Marketplace and note the **Model Package ARN**. See [Subscribe to Deepgram Products](/docs/deploy-amazon-sagemaker#subscribe-to-deepgram-products) for instructions.

## Prerequisites

* [Terraform](https://developer.hashicorp.com/terraform/install) 1.5 or later
* AWS credentials configured for the target account (via environment variables, shared credentials file, or an IAM role)
* An active AWS Marketplace subscription to a [Deepgram SageMaker product](https://aws.amazon.com/marketplace/search/results?searchTerms=deepgram\&CREATOR=6efa21f9-9a33-4cae-ba44-756436fa71dd\&FULFILLMENT_OPTION_TYPE=SAGEMAKER_MODEL\&filters=CREATOR%2CFULFILLMENT_OPTION_TYPE)
* The **Model Package ARN** for the subscribed product (found in the SageMaker console under **Marketplace Model Packages** → **AWS Marketplace Subscriptions**)

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

```bash
terraform init
```

```bash
terraform plan
```

Verify the plan shows the expected resources: an IAM role, a SageMaker Model, an Endpoint Configuration, and an Endpoint.

```bash
terraform apply
```

Terraform creates the resources and waits for the SageMaker Endpoint to reach `InService` status. This typically takes several minutes.

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
