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

You need a **Model Package ARN** before you start. Subscribe to a Deepgram product on the AWS Marketplace and copy the ARN for your product version and AWS Region — see [Find the Model Package ARN](/docs/subscribe-aws-marketplace#find-the-model-package-arn).

## Prerequisites

* An AWS account
* AWS IAM permissions to SageMaker and Marketplace
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html): AWSMarketplaceManageSubscriptions
  * [**IAM Policy**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html): AmazonSageMakerFullAccess
* The [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) or [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html), configured with credentials for the target account
* An active AWS Marketplace subscription to a [Deepgram SageMaker product](/docs/supported-products-sagemaker) and its **Model Package ARN**. See [Subscribe on AWS Marketplace](/docs/subscribe-aws-marketplace).
* Service quota for the GPU instance type you plan to use. See [Requesting SageMaker Quota](/docs/request-sagemaker-quota).

## Choose an endpoint type

Deploy a **real-time** endpoint for live streaming and synchronous (single-file) transcription, or an **asynchronous** endpoint for large pre-recorded files (up to 1 GB) and scale-to-zero. An asynchronous endpoint accepts only `InvokeEndpointAsync` requests and cannot serve streaming or synchronous traffic, so deploy one endpoint per invocation style you need. See [Auto-Scaling SageMaker Endpoints](/docs/auto-scaling-sagemaker) for a full comparison.

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

**Asynchronous endpoints** additionally need `s3:GetObject` and `s3:PutObject` on the objects in your output and failure buckets, and `s3:ListBucket` on the buckets themselves. Attach an inline policy such as the following to the execution role, replacing `<bucket>` with your bucket name:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::<bucket>/*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::<bucket>"
    }
  ]
}
```

## Deploy with the AWS CLI or Boto3

#### Set variables

Choose names for the three SageMaker resources, and set the Model Package ARN, execution role ARN, and instance type.

* **`MODEL_PACKAGE_ARN`** identifies the Deepgram product version and AWS Region you subscribed to. It is region-specific, so copy the ARN for the Region you deploy in. To find it, open the AWS Marketplace **Manage subscriptions** console, click **Configure** on your Deepgram subscription, choose **AWS command line interface (CLI)** under **Service**, select the product version, and copy the ARN for your Region from the **Model ARNs** list. See [Find the Model Package ARN](/docs/subscribe-aws-marketplace#find-the-model-package-arn) for the full steps.
* **`EXECUTION_ROLE_ARN`** is the role you created in [Create an IAM execution role](#create-an-iam-execution-role).
* **`INSTANCE_TYPE`**: `ml.g6.2xlarge` is the recommended type for Speech-to-Text; see [Instance types](/docs/supported-products-sagemaker#instance-types) for Text-to-Speech and the other supported families.

#### AWS CLI

```bash
export AWS_REGION="us-east-1"
export MODEL_NAME="deepgram-streaming-stt"
export ENDPOINT_CONFIG_NAME="deepgram-streaming-stt-config"
export ENDPOINT_NAME="my-deepgram-streaming-stt"
export MODEL_PACKAGE_ARN="arn:aws:sagemaker:us-east-1:123456789012:model-package/deepgram-stt-nova-3/1"
export EXECUTION_ROLE_ARN="arn:aws:iam::123456789012:role/deepgram-sagemaker-execution"
export INSTANCE_TYPE="ml.g6.2xlarge"
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
INSTANCE_TYPE = "ml.g6.2xlarge"

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

The Endpoint Configuration sets the instance type, instance count, and — critically — the host inference AMI version the instances boot with.

**`InferenceAmiVersion` is required.** Current Deepgram model packages run a CUDA 13 runtime that needs NVIDIA driver 580 or later. Without `InferenceAmiVersion=al2023-ami-sagemaker-inference-gpu-4-1`, SageMaker boots the default AMI for the instance family (an older driver on `g4dn` and `g5`) and the container fails its CUDA preflight check. See [Inference AMI Versions](#inference-ami-versions).

#### AWS CLI

**`Real-time endpoint`**

```bash title="Real-time endpoint"
aws sagemaker create-endpoint-config \
  --region "$AWS_REGION" \
  --endpoint-config-name "$ENDPOINT_CONFIG_NAME" \
  --production-variants "VariantName=AllTraffic,ModelName=$MODEL_NAME,InitialInstanceCount=1,InstanceType=$INSTANCE_TYPE,InferenceAmiVersion=al2023-ami-sagemaker-inference-gpu-4-1,ModelDataDownloadTimeoutInSeconds=600,ContainerStartupHealthCheckTimeoutInSeconds=300"
```

For an **asynchronous** endpoint, add `--async-inference-config` with the S3 prefixes for results and failures:

**`Asynchronous endpoint`**

```bash title="Asynchronous endpoint"
aws sagemaker create-endpoint-config \
  --region "$AWS_REGION" \
  --endpoint-config-name "$ENDPOINT_CONFIG_NAME" \
  --production-variants "VariantName=AllTraffic,ModelName=$MODEL_NAME,InitialInstanceCount=1,InstanceType=$INSTANCE_TYPE,InferenceAmiVersion=al2023-ami-sagemaker-inference-gpu-4-1,ModelDataDownloadTimeoutInSeconds=600,ContainerStartupHealthCheckTimeoutInSeconds=300" \
  --async-inference-config "OutputConfig={S3OutputPath=s3://<bucket>/output/,S3FailurePath=s3://<bucket>/failures/}"
```

#### Boto3

**`Real-time endpoint`**

```python title="Real-time endpoint"
sagemaker.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": MODEL_NAME,
        "InitialInstanceCount": 1,
        "InstanceType": INSTANCE_TYPE,
        "InferenceAmiVersion": "al2023-ami-sagemaker-inference-gpu-4-1",
        "ModelDataDownloadTimeoutInSeconds": 600,
        "ContainerStartupHealthCheckTimeoutInSeconds": 300,
    }],
)
```

For an **asynchronous** endpoint, add `AsyncInferenceConfig` with the S3 prefixes for results and failures:

**`Asynchronous endpoint`**

```python title="Asynchronous endpoint"
sagemaker.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": MODEL_NAME,
        "InitialInstanceCount": 1,
        "InstanceType": INSTANCE_TYPE,
        "InferenceAmiVersion": "al2023-ami-sagemaker-inference-gpu-4-1",
        "ModelDataDownloadTimeoutInSeconds": 600,
        "ContainerStartupHealthCheckTimeoutInSeconds": 300,
    }],
    AsyncInferenceConfig={
        "OutputConfig": {
            "S3OutputPath": "s3://<bucket>/output/",
            "S3FailurePath": "s3://<bucket>/failures/",
        },
    },
)
```

Keep `VariantName=AllTraffic`: the [Update an Amazon SageMaker Endpoint](/docs/update-amazon-sagemaker-endpoint) procedure and the [Terraform](/docs/terraform-deploy-sagemaker) configuration use the same variant name. `ModelDataDownloadTimeoutInSeconds=600` and `ContainerStartupHealthCheckTimeoutInSeconds=300` give the model package time to download and the container time to load models before SageMaker marks the endpoint failed; large multilingual Nova-3 bundles may need a `ModelDataDownloadTimeoutInSeconds` above `600`.

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

Send a first request to confirm the endpoint transcribes audio — see [Validate a Deepgram SageMaker Endpoint](/docs/test-amazon-sagemaker-endpoint). For the streaming, synchronous, and asynchronous invocation APIs and the Deepgram SDK SageMaker transport, see [Invoke a Deepgram SageMaker Endpoint](/docs/invoke-sagemaker-endpoint).

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

**(Asynchronous endpoints only) Configure async invocation.**

If you are deploying an **asynchronous** endpoint, expand the **Async invocation config** section and toggle it on, then set the **S3 output path** — the S3 location (for example, `s3://your-bucket/output/`) where transcription results are written. The remaining fields are optional.

For a **real-time** endpoint (streaming and synchronous invocation), leave **Async invocation config** turned **off** and continue to the next step unchanged.

To autoscale an asynchronous endpoint — including scaling to zero when idle — see [Auto-Scaling Asynchronous Endpoints](/docs/auto-scaling-sagemaker-async).

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
