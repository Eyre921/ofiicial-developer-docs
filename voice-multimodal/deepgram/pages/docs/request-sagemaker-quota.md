---
title: "Requesting SageMaker Quota"
source: https://developers.deepgram.com/docs/request-sagemaker-quota.md
path: docs/request-sagemaker-quota
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Requesting SageMaker Quota

> How to check and increase AWS service quotas for SageMaker endpoint instance types (ml.g5.2xlarge, ml.g6.2xlarge, ml.g6e.2xlarge) required by Deepgram deployments.

AWS enforces default [service quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) on the number of SageMaker endpoint instances you can run per account per region. Before you can deploy Deepgram on Amazon SageMaker, you may need to request a quota increase for the GPU-accelerated instance types that Deepgram requires.

## Instance types used by Deepgram

Deepgram SageMaker deployments use the following instance types. Each maps to a separate service quota.

| Instance type    | GPU         | Quota name                          |
| ---------------- | ----------- | ----------------------------------- |
| `ml.g5.2xlarge`  | NVIDIA A10G | `ml.g5.2xlarge for endpoint usage`  |
| `ml.g6.2xlarge`  | NVIDIA L4   | `ml.g6.2xlarge for endpoint usage`  |
| `ml.g6e.2xlarge` | NVIDIA L40S | `ml.g6e.2xlarge for endpoint usage` |

Quota values represent the maximum number of instances of that type you can run simultaneously across all SageMaker endpoints in a single AWS region. A quota of `0` means you cannot deploy that instance type until you request an increase.

## Check your current quota

Before requesting an increase, check the quota you already have.

#### AWS Management Console

#### Open Service Quotas

Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and navigate to [Service Quotas](https://console.aws.amazon.com/servicequotas/home).

#### Select Amazon SageMaker

In the left-hand menu, select **AWS services**, then search for and select **Amazon SageMaker**.

#### Search for the instance quota

In the search bar, enter the instance type you want to check (for example, `g5.2xlarge`). *Find the item named similar to ml.g5.2xlarge for endpoint usage.*

#### AWS CLI

Run the following command, replacing the `--query-text` value with the instance type you want to check:

```bash
aws service-quotas list-service-quotas \
  --service-code sagemaker \
  --query "Quotas[?contains(QuotaName, 'ml.g5.2xlarge') && contains(QuotaName, 'endpoint')]" \
  --output table
```

To check all three instance types at once:

```bash
for INSTANCE in g5.2xlarge g6.2xlarge g6e.2xlarge; do
  echo "=== ml.$INSTANCE ==="
  aws service-quotas list-service-quotas \
    --service-code sagemaker \
    --query "Quotas[?contains(QuotaName, 'ml.$INSTANCE') && contains(QuotaName, 'endpoint')].{Name:QuotaName,Value:Value}" \
    --output table
done
```

## Request a quota increase

If your current quota is `0` or too low for your deployment, submit a quota increase request.

#### AWS Management Console

#### Open the quota detail page

In the [Service Quotas console for Amazon SageMaker](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas), search for the instance type (for example, `g5.2xlarge`) and select the quota named **ml.g5.2xlarge for endpoint usage**.

#### Request an increase

Select **Request increase at account level**.

#### Enter the new quota value

In the **Increase quota value** field, enter the number of instances you need. For example, enter `4` if you plan to run up to four `ml.g5.2xlarge` endpoint instances in this region.

#### Submit the request

Select **Request**. AWS reviews most SageMaker quota requests within a few hours, though some may take several business days.

#### Repeat for each instance type

If you need quota for additional instance types (`ml.g6.2xlarge`, `ml.g6e.2xlarge`), repeat these steps for each.

#### AWS CLI

Use `request-service-quota-increase` to submit a request. You need the **quota code** for each instance type.

First, look up the quota code:

```bash
aws service-quotas list-service-quotas \
  --service-code sagemaker \
  --query "Quotas[?contains(QuotaName, 'ml.g5.2xlarge') && contains(QuotaName, 'endpoint')].{Code:QuotaCode,Name:QuotaName,Value:Value}" \
  --output table
```

Then submit the increase request using the quota code from the previous command:

```bash
aws service-quotas request-service-quota-increase \
  --service-code sagemaker \
  --quota-code <QUOTA_CODE> \
  --desired-value 4
```

Replace `<QUOTA_CODE>` with the code returned by the lookup command, and `4` with the number of instances you need.

To check the status of your request:

```bash
aws service-quotas list-requested-service-quota-change-history \
  --service-code sagemaker \
  --query "RequestedQuotas[?contains(QuotaName, 'g5.2xlarge')].{Status:Status,Desired:DesiredValue,QuotaName:QuotaName}" \
  --output table
```

## Choosing the right quota value

The quota value determines how many instances of that type you can run simultaneously. Consider the following when choosing a value:

* **Number of Deepgram products** — each product (for example, English STT, Spanish STT, TTS) runs as a separate SageMaker endpoint.
* **Auto-scaling** — if you configure [auto-scaling](/docs/auto-scaling-sagemaker-streaming), set the quota high enough to accommodate the maximum instance count across all endpoints.
* **Multi-region deployments** — quotas are per region. Request increases in every region where you plan to deploy.

Do not request more instances than you plan to use. Running SageMaker endpoint instances incurs charges for as long as they remain active.

## Troubleshooting

| Symptom                                           | Cause                                                             | Resolution                                                                                                                    |
| ------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `ResourceLimitExceeded` when creating an endpoint | The instance quota for the selected type is `0` or fully consumed | Request a quota increase for that instance type                                                                               |
| Quota request remains `PENDING` for several days  | AWS is reviewing the request                                      | Open a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home) referencing the quota request ID |
| Quota increase approved but endpoint still fails  | Quota was increased in a different region                         | Verify the region in the AWS Management Console matches the region where you are creating the endpoint                        |
