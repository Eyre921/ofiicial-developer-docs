---
title: "Deploy Deepgram on Amazon SageMaker"
source: https://developers.deepgram.com/docs/deploy-amazon-sagemaker.md
path: docs/deploy-amazon-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Deploy Deepgram on Amazon SageMaker

This guide deploys a Deepgram AWS Marketplace Model Package as a [SageMaker AI Endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) using the AWS CLI or the AWS SDK for Python (Boto3). The SageMaker Endpoint resource represents the compute instances that run the Deepgram Voice AI services. For an overview of running Deepgram on SageMaker, including benefits, tradeoffs, and pricing, see [Amazon SageMaker](/docs/amazon-sagemaker).

Prefer to have an AI coding assistant run these steps for you? Install the Deepgram SageMaker skill — see [Agent-assisted setup](/docs/amazon-sagemaker#agent-assisted-setup).

You need a **Model Package ARN** before you start. Subscribe to a Deepgram product on the AWS Marketplace and copy the ARN for your product version and AWS Region — see [Find the Model Package ARN](/docs/subscribe-aws-marketplace#find-the-model-package-arn).

## Prerequisites

* An AWS account
* AWS IAM permissions to SageMaker and Marketplace
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html): AWSMarketplaceManageSubscriptions
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html): AmazonSageMakerFullAccess
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) or [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html), configured with credentials for the target account
* An active AWS Marketplace subscription to a [Deepgram SageMaker product](/docs/supported-products-sagemaker) and its **Model Package ARN**. See [Subscribe on AWS Marketplace](/docs/subscribe-aws-marketplace).
* Service quota for the GPU instance type you plan to use. See [Requesting SageMaker Quota](/docs/request-sagemaker-quota).

**AWS field employees:** you can access Deepgram models through the [AWS Marketplace Field Demonstration Program](https://docs.aws.amazon.com/marketplace/latest/userguide/field-demonstration-program.html). Deepgram is an eligible provider. Refer to your internal AWS documentation for enrollment details, and reach out to a [Deepgram representative](https://deepgram.com/contact-us) if you need assistance activating the program.

## Choose an endpoint type

Deploy a **real-time** endpoint. It serves both live streaming (`InvokeEndpointWithBidirectionalStream`) and synchronous single-file transcription (`InvokeEndpoint`, up to 25 MB per request).

**Asynchronous endpoints are temporarily not supported.** Asynchronous inference (`AsyncInferenceConfig` / `InvokeEndpointAsync`) is temporarily unavailable for Marketplace-hosted Deepgram, so this page covers real-time endpoints only. Need asynchronous processing? Contact a [Deepgram representative](https://deepgram.com/contact-us).

## Choose instance types

Deploy on an ordered **instance pool** rather than a single instance type. A single type has no fallback: when AWS is short of that GPU in the Availability Zone, the endpoint goes `Failed` with `Request to service failed` a few minutes in, or `InsufficientInstanceCapacity`, and this happens routinely for popular GPU types. With [instance pools](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-heterogeneous.html), SageMaker tries each type in priority order and falls back to the next when one is capacity-constrained.

Order the pool as follows:

1. **The listing's recommended type first** (for example `ml.g6.2xlarge` for Speech-to-Text). It is the type Deepgram validated the model on and the best price/performance.
2. **Same-or-newer generation with similar per-instance capacity next** (`g6` → `g6e` → `g7`). Keeping capacity similar matters if you auto-scale, because the predefined scaling metrics are per instance and do not account for a mixed fleet.
3. **Older generations last, as insurance** (`g5`, and `g4dn` where supported).
4. **Never include a type the product does not support**: `g4dn` for Flux, `g5`/`g4dn` for Flux TTS, or any single-GPU type for Aura-2. See [Instance types](/docs/supported-products-sagemaker#instance-types).
5. **Up to 5 types.** Three is the sweet spot.

`VariantInstanceProvisionTimeoutInSeconds` is the per-type wait: SageMaker tries each type for that long before moving to the next. `300` is recommended (AWS allows `60`–`3600`), so a three-type pool can stay in `Creating` for up to about 15 minutes before it fails.

**Quota does not fall back — capacity does.** SageMaker validates the quota of every type in the pool when the endpoint is created. Every type in the pool needs a quota of at least `1` in the region, otherwise `CreateEndpoint` fails with `ResourceLimitExceeded` regardless of which type would have been used. Check and request quota for each type first; see [Requesting SageMaker Quota](/docs/request-sagemaker-quota).

Prefer a single instance type only for a stated reason: a [Machine Learning Savings Plan](https://aws.amazon.com/savingsplans/ml-pricing/) or reservation on that type, or an auto-scaling concurrency target you measured on a specific GPU.

## Create an IAM execution role

SageMaker assumes an [execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) to run the Model Package on your behalf. You only need to create a single SageMaker execution role, and can reuse this IAM Role to deploy multiple SageMaker Endpoints.

#### AWS CLI

```bash
aws iam create-role \
  --role-name deepgram-sagemaker-execution \
  --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"sagemaker.amazonaws.com"},"Action":"sts:AssumeRole"}]}'

aws iam attach-role-policy \
  --role-name deepgram-sagemaker-execution \
  --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
```

#### Boto3

```python
import json
import boto3

iam = boto3.client("iam")

role = iam.create_role(
    RoleName="deepgram-sagemaker-execution",
    AssumeRolePolicyDocument=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "sagemaker.amazonaws.com"},
            "Action": "sts:AssumeRole",
        }],
    }),
)
iam.attach_role_policy(
    RoleName="deepgram-sagemaker-execution",
    PolicyArn="arn:aws:iam::aws:policy/AmazonSageMakerFullAccess",
)
execution_role_arn = role["Role"]["Arn"]
```

A newly created IAM role can take around 10 seconds to become assumable. If `CreateModel` fails with `Could not assume role` immediately after `create-role`, the error is transient — wait a few seconds and retry.

## Deploy with the AWS CLI or Boto3

#### Set variables

Choose names for the three SageMaker resources, and set the Model Package ARN and execution role ARN.

* **`MODEL_PACKAGE_ARN`** identifies the Deepgram product version and AWS Region you subscribed to. It is region-specific, so copy the ARN for the Region you deploy in. To find it, open the AWS Marketplace **Manage subscriptions** console, click **Configure** on your Deepgram subscription, choose **AWS command line interface (CLI)** under **Service**, select the product version, and copy the ARN for your Region from the **Model ARNs** list. See [Find the Model Package ARN](/docs/subscribe-aws-marketplace#find-the-model-package-arn) for the full steps.
* **`EXECUTION_ROLE_ARN`** is the role you created in [Create an IAM execution role](#create-an-iam-execution-role).
* The instance pool is set in the Endpoint Configuration step. `ml.g6.2xlarge` is the recommended first type for Speech-to-Text; see [Choose instance types](#choose-instance-types) and [Instance types](/docs/supported-products-sagemaker#instance-types) for Text-to-Speech and the other supported families.

#### AWS CLI

```bash
export AWS_REGION="us-east-1"
export MODEL_NAME="deepgram-streaming-stt"
export ENDPOINT_CONFIG_NAME="deepgram-streaming-stt-config"
export ENDPOINT_NAME="my-deepgram-streaming-stt"
export MODEL_PACKAGE_ARN="arn:aws:sagemaker:us-east-1:123456789012:model-package/deepgram-stt-nova-3/1"
export EXECUTION_ROLE_ARN="arn:aws:iam::123456789012:role/deepgram-sagemaker-execution"
```

#### Boto3

```python
import boto3

AWS_REGION = "us-east-1"
MODEL_NAME = "deepgram-streaming-stt"
ENDPOINT_CONFIG_NAME = "deepgram-streaming-stt-config"
ENDPOINT_NAME = "my-deepgram-streaming-stt"
MODEL_PACKAGE_ARN = "arn:aws:sagemaker:us-east-1:123456789012:model-package/deepgram-stt-nova-3/1"
EXECUTION_ROLE_ARN = "arn:aws:iam::123456789012:role/deepgram-sagemaker-execution"

sagemaker = boto3.client("sagemaker", region_name=AWS_REGION)
```

#### Create the Model

The SageMaker Model wraps the Marketplace Model Package and the execution role.

#### AWS CLI

```bash
aws sagemaker create-model \
  --region "$AWS_REGION" \
  --model-name "$MODEL_NAME" \
  --execution-role-arn "$EXECUTION_ROLE_ARN" \
  --primary-container "ModelPackageName=$MODEL_PACKAGE_ARN" \
  --enable-network-isolation
```

#### Boto3

```python
sagemaker.create_model(
    ModelName=MODEL_NAME,
    ExecutionRoleArn=EXECUTION_ROLE_ARN,
    PrimaryContainer={"ModelPackageName": MODEL_PACKAGE_ARN},
    EnableNetworkIsolation=True,
)
```

`EnableNetworkIsolation=true` is mandatory for AWS Marketplace model packages — SageMaker rejects the Model otherwise. Network isolation is also why the container cannot reach external services; see [Limitations](/docs/amazon-sagemaker#limitations).

To pass `DEEPGRAM_API_*` or `DEEPGRAM_ENGINE_*` configuration overrides, add an `Environment` map to the container definition. See [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments).

#### Create the Endpoint Configuration

The Endpoint Configuration sets the instance pool, instance count, and — critically — the host inference AMI version the instances boot with.

**`InferenceAmiVersion` is required.** Current Deepgram model packages run a CUDA 13 runtime that needs NVIDIA driver 580 or later. Without `InferenceAmiVersion=al2023-ami-sagemaker-inference-gpu-4-1`, SageMaker boots the default AMI for the instance family (an older driver on `g4dn` and `g5`) and the container fails its CUDA preflight check. See [Inference AMI Versions](#inference-ami-versions).

The examples use an ordered instance pool, as recommended in [Choose instance types](#choose-instance-types). Adjust the types and order for your product.

#### AWS CLI

**`Instance pool (recommended)`**

```bash title="Instance pool (recommended)"
aws sagemaker create-endpoint-config \
  --region "$AWS_REGION" \
  --endpoint-config-name "$ENDPOINT_CONFIG_NAME" \
  --production-variants '[{"VariantName":"AllTraffic","ModelName":"'"$MODEL_NAME"'","InitialInstanceCount":1,
    "InstancePools":[{"InstanceType":"ml.g6.2xlarge","Priority":1},{"InstanceType":"ml.g6e.2xlarge","Priority":2},{"InstanceType":"ml.g5.2xlarge","Priority":3}],
    "VariantInstanceProvisionTimeoutInSeconds":300,
    "InferenceAmiVersion":"al2023-ami-sagemaker-inference-gpu-4-1",
    "ModelDataDownloadTimeoutInSeconds":600,"ContainerStartupHealthCheckTimeoutInSeconds":300}]'
```

To deploy on a **single instance type** instead (see [when to prefer a single type](#choose-instance-types)), replace `InstancePools` and `VariantInstanceProvisionTimeoutInSeconds` with `InstanceType`:

**`Single instance type`**

```bash title="Single instance type"
aws sagemaker create-endpoint-config \
  --region "$AWS_REGION" \
  --endpoint-config-name "$ENDPOINT_CONFIG_NAME" \
  --production-variants "VariantName=AllTraffic,ModelName=$MODEL_NAME,InitialInstanceCount=1,InstanceType=ml.g6.2xlarge,InferenceAmiVersion=al2023-ami-sagemaker-inference-gpu-4-1,ModelDataDownloadTimeoutInSeconds=600,ContainerStartupHealthCheckTimeoutInSeconds=300"
```

#### Boto3

**`Instance pool (recommended)`**

```python title="Instance pool (recommended)"
sagemaker.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": MODEL_NAME,
        "InitialInstanceCount": 1,
        "InstancePools": [
            {"InstanceType": "ml.g6.2xlarge", "Priority": 1},
            {"InstanceType": "ml.g6e.2xlarge", "Priority": 2},
            {"InstanceType": "ml.g5.2xlarge", "Priority": 3},
        ],
        "VariantInstanceProvisionTimeoutInSeconds": 300,
        "InferenceAmiVersion": "al2023-ami-sagemaker-inference-gpu-4-1",
        "ModelDataDownloadTimeoutInSeconds": 600,
        "ContainerStartupHealthCheckTimeoutInSeconds": 300,
    }],
)
```

To deploy on a **single instance type** instead (see [when to prefer a single type](#choose-instance-types)), replace `InstancePools` and `VariantInstanceProvisionTimeoutInSeconds` with `InstanceType`:

**`Single instance type`**

```python title="Single instance type"
sagemaker.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": MODEL_NAME,
        "InitialInstanceCount": 1,
        "InstanceType": "ml.g6.2xlarge",
        "InferenceAmiVersion": "al2023-ami-sagemaker-inference-gpu-4-1",
        "ModelDataDownloadTimeoutInSeconds": 600,
        "ContainerStartupHealthCheckTimeoutInSeconds": 300,
    }],
)
```

Keep `VariantName=AllTraffic`: the [Update an Amazon SageMaker Endpoint](/docs/update-amazon-sagemaker-endpoint) procedure and the [Terraform](/docs/terraform-deploy-sagemaker) configuration use the same variant name.

`ModelDataDownloadTimeoutInSeconds` and `ContainerStartupHealthCheckTimeoutInSeconds` are ceilings, not fixed waits: they set how long SageMaker allows the model package to download and the container to load models before it marks the endpoint failed. `600` and `300` suit most products. Large multilingual Nova-3 bundles may need `ModelDataDownloadTimeoutInSeconds` of `1800`.

#### Create the Endpoint

#### AWS CLI

```bash
aws sagemaker create-endpoint \
  --region "$AWS_REGION" \
  --endpoint-name "$ENDPOINT_NAME" \
  --endpoint-config-name "$ENDPOINT_CONFIG_NAME"
```

#### Boto3

```python
sagemaker.create_endpoint(
    EndpointName=ENDPOINT_NAME,
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
)
```

#### Wait for InService

It takes several minutes for the endpoint to download the model package, start the container, and pass its health check.

#### AWS CLI

```bash
aws sagemaker wait endpoint-in-service \
  --region "$AWS_REGION" \
  --endpoint-name "$ENDPOINT_NAME"

aws sagemaker describe-endpoint \
  --region "$AWS_REGION" \
  --endpoint-name "$ENDPOINT_NAME" \
  --query EndpointStatus
```

#### Boto3

```python
sagemaker.get_waiter("endpoint_in_service").wait(EndpointName=ENDPOINT_NAME)

status = sagemaker.describe_endpoint(EndpointName=ENDPOINT_NAME)["EndpointStatus"]
print(status)  # InService
```

If the endpoint moves to `Failed` or stays in `Creating`, see [Troubleshooting](/docs/troubleshooting-sagemaker).

#### Verify

Send a first request to confirm the endpoint transcribes audio — see [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint). For the streaming and synchronous invocation APIs and the Deepgram SDK SageMaker transport, see [Invoke a Deepgram SageMaker Endpoint](/docs/invoke-sagemaker-endpoint).

## Inference AMI Versions

A SageMaker Endpoint Configuration can pin an **inference AMI version** — the SageMaker-managed host image supplying the NVIDIA driver and container runtime your instances boot with. It is independent of the Deepgram container: it determines which driver the container runs against. If you do not set it, SageMaker selects a default for your instance type, which on older GPU families is an older driver.

| AMI version                              | NVIDIA driver | CUDA |
| ---------------------------------------- | ------------- | ---- |
| `al2-ami-sagemaker-inference-gpu-2`      | 535           | 12.2 |
| `al2-ami-sagemaker-inference-gpu-2-1`    | 535           | 12.2 |
| `al2-ami-sagemaker-inference-gpu-3-1`    | 550           | 12.4 |
| `al2023-ami-sagemaker-inference-gpu-4-1` | 580           | 13.0 |

Deepgram recommends the latest available version, `al2023-ami-sagemaker-inference-gpu-4-1`, which provides the NVIDIA 580 driver. Deepgram containers select the correct CUDA compatibility layer at startup based on the host driver they detect, so a newer host driver requires no change to your deployment.

Support for older driver versions may be removed in the latest Deepgram Model Package. Pin an up-to-date inference AMI version rather than relying on the SageMaker default for your instance type.

For the full list of AMI versions and their driver and CUDA versions, see [`InferenceAmiVersion`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html#sagemaker-Type-ProductionVariant-InferenceAmiVersion) in the SageMaker API reference. For the driver each instance family runs by default, see the [SageMaker GPU driver table](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-gpu-drivers.html#inference-gpu-drivers-versions).

The [CLI and Boto3 steps above](#deploy-with-the-aws-cli-or-boto3) already pin `InferenceAmiVersion` to `al2023-ami-sagemaker-inference-gpu-4-1` on the production variant. Terraform users set the same value through the `inference_ami_version` variable — see [Deploy with Terraform](/docs/terraform-deploy-sagemaker#inference-ami-versions). The SageMaker AI console does not expose this setting, which is why the console path below is not recommended.

## Deploy with the SageMaker AI console (not recommended)

The SageMaker AI console cannot set `InferenceAmiVersion`. Endpoints created through the console boot the instance family's default AMI, and current Deepgram model packages fail to start on the older NVIDIA driver it provides. Use the [AWS CLI or Boto3 steps](#deploy-with-the-aws-cli-or-boto3) or [Terraform](/docs/terraform-deploy-sagemaker) instead. If you have already created an endpoint through the console, fix it by creating a new Endpoint Configuration with the CLI and [updating the endpoint](/docs/update-amazon-sagemaker-endpoint).

#### Console steps

In the AWS Management Console, navigate to the [AWS Marketplace **Manage subscriptions** console](https://us-east-1.console.aws.amazon.com/marketplace/subscriptions)

On the **Active subscriptions** tab, find the subscription for the Deepgram product you want to deploy (eg. *Deepgram Voice AI- Nova-3 Monolingual Speech-to-Text (STT) Streaming*)

Click the **Configure** button in the **Actions** column on the right-hand side

In the **Setup** box, under **Service**, choose **Amazon SageMaker AI console**

Under the **Version** header, select the product version from the dropdown. If the listing has more than one version, read the version name and the release notes to understand the set of languages (or features) each version provides, and choose the version that matches your needs

Select the AWS **Region** you want to deploy to

Under **Amazon SageMaker options**, keep **Create real-time inference endpoint** selected

Click the **Create endpoint** button. You'll be redirected to the Amazon SageMaker AI console

Provide a name for the model (eg. `deepgram-streaming-stt`)

Under **IAM Role**, select the [SageMaker execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) that you created

Click the **Next** button

Provide an **Endpoint Name**, such as `my-deepgram-streaming-stt`

Leave **Async invocation config** turned **off**. Asynchronous endpoints are temporarily not supported for Marketplace-hosted Deepgram.

Under **Variants** ➡️ **Production**, scroll all the way to the right, and click **Edit**

If desired, select **Choose Other Instance Type** and select the instance type you want to deploy to (eg. `ml.g6.2xlarge`), then click **Save**

Click the **Create Endpoint Configuration** button

Click the **Submit** button, to create the SageMaker AI Endpoint

After following these steps, you should see a new Endpoint in your AWS account.
If you don't see the Endpoint, ensure that you have selected the correct AWS region in the [AWS Management Console](https://console.aws.amazon.com/sagemaker/home?#/endpoints).
It may take several minutes for the Endpoint to change to status `InService`.
Once the Endpoint status has changed to `InService`, you can monitor the Amazon CloudWatch Logs for the Endpoint to ensure normal operation of the Deepgram services.

## Tear down

Delete the three resources in reverse order. Billing for SageMaker compute and Deepgram usage stops when the endpoint is deleted; your AWS Marketplace subscription remains active and can be reused for the next deployment.

#### AWS CLI

```bash
aws sagemaker delete-endpoint --region "$AWS_REGION" --endpoint-name "$ENDPOINT_NAME"
aws sagemaker delete-endpoint-config --region "$AWS_REGION" --endpoint-config-name "$ENDPOINT_CONFIG_NAME"
aws sagemaker delete-model --region "$AWS_REGION" --model-name "$MODEL_NAME"
```

#### Boto3

```python
sagemaker.delete_endpoint(EndpointName=ENDPOINT_NAME)
sagemaker.delete_endpoint_config(EndpointConfigName=ENDPOINT_CONFIG_NAME)
sagemaker.delete_model(ModelName=MODEL_NAME)
```

## Related resources

* [Supported Products](/docs/supported-products-sagemaker)
* [Subscribe on AWS Marketplace](/docs/subscribe-aws-marketplace)
* [Deploy with Terraform](/docs/terraform-deploy-sagemaker)
* [Configure Amazon SageMaker Deployments](/docs/configure-sagemaker-deployments)
* [Invoke a Deepgram SageMaker Endpoint](/docs/invoke-sagemaker-endpoint)
* [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint)
* [Update an Amazon SageMaker Endpoint](/docs/update-amazon-sagemaker-endpoint)
* [Troubleshooting](/docs/troubleshooting-sagemaker)
