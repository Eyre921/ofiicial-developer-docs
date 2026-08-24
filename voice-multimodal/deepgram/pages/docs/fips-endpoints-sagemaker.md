---
title: "Use FIPS Endpoints"
source: https://developers.deepgram.com/docs/fips-endpoints-sagemaker.md
path: docs/fips-endpoints-sagemaker
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Use FIPS Endpoints

> How to configure boto3, the AWS SDKs, and the AWS CLI to reach Deepgram on Amazon SageMaker over FIPS 140-3 endpoints, including bidirectional streaming on port 8443, asynchronous endpoints on s3-fips, the IAM Identity Center caveat, and how to confirm a run used FIPS endpoints.

Amazon SageMaker AI publishes FIPS 140-3 endpoints alongside its standard ones. Switching to them changes only the hostname your client connects to; the endpoint, the model, and the request payload stay the same. For what these endpoints do and do not cover, see [Security and Compliance](/docs/security-and-compliance-sagemaker#fips-140-3-endpoints).

## Select FIPS endpoints

The AWS SDKs give you three ways to select FIPS endpoints, from broadest to narrowest scope:

| Mechanism                                         | Scope                           | Use when                                                                                         |
| ------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------ |
| `AWS_USE_FIPS_ENDPOINT=true` environment variable | Every client in the process     | The whole process should use FIPS endpoints and you do not authenticate with IAM Identity Center |
| `use_fips_endpoint = true` in `~/.aws/config`     | Every client using that profile | You want FIPS tied to a profile rather than a shell                                              |
| Per-client configuration in code                  | One client                      | You want explicit, reviewable control — **recommended**                                          |

If you authenticate with AWS IAM Identity Center (SSO), use per-client configuration. Authenticate over the standard IAM Identity Center endpoint, then apply FIPS to the service you call. The environment variable and the profile setting instead apply FIPS to every client in the process, including the one that resolves your SSO credentials, and the AWS SDKs then derive an IAM Identity Center hostname that does not resolve. Credential resolution fails before your request reaches SageMaker, and a cached credential masks the failure, so it appears intermittent.

## Configure clients in code

Apply `use_fips_endpoint` to each client you build. Both the control plane (`sagemaker`) and the inference client (`sagemaker-runtime`) need it:

```python
import boto3
from botocore.config import Config

REGION = "us-west-2"
fips = Config(use_fips_endpoint=True)

sagemaker = boto3.client("sagemaker", region_name=REGION, config=fips)
runtime = boto3.client("sagemaker-runtime", region_name=REGION, config=fips)

print(sagemaker.meta.endpoint_url)
# https://api-fips.sagemaker.us-west-2.amazonaws.com
print(runtime.meta.endpoint_url)
# https://runtime-fips.sagemaker.us-west-2.amazonaws.com
```

Invoke the endpoint exactly as you would otherwise:

```python
response = runtime.invoke_endpoint(
    EndpointName="<your-endpoint-name>",
    ContentType="application/json",
    Accept="*/*",
    Body=audio_bytes,
    CustomAttributes="model=nova-3&language=en&smart_format=true",
)
```

## Streaming over FIPS endpoints

Bidirectional streaming reaches the runtime host on **port 8443**, and the FIPS runtime host serves that port as well. The HTTP/2 bidirectional streaming client takes an explicit endpoint, so point it at the FIPS hostname and keep the port:

```typescript
import {
  SageMakerRuntimeHTTP2Client,
} from "@aws-sdk/client-sagemaker-runtime-http2";

const region = "us-west-2";
const client = new SageMakerRuntimeHTTP2Client({
  region,
  endpoint: `https://runtime-fips.sagemaker.${region}.amazonaws.com:8443`,
});
```

The equivalent in Python, using `aws_sdk_sagemaker_runtime_http2`:

```python
endpoint_uri = f"https://runtime-fips.sagemaker.{region}.amazonaws.com:8443"
```

If you omit the port, the connection is accepted but the response never arrives: the client hangs instead of reporting an error. Set the endpoint explicitly, with the port, on every bidirectional streaming client.

For the full streaming request shape — payload parts, control messages, and result handling — see [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker).

## Asynchronous endpoints

Asynchronous endpoints read their input and write their output to Amazon S3, so configure the S3 client for FIPS as well. Otherwise the invocation travels over FIPS while the payload does not:

```python
s3 = boto3.client("s3", region_name=REGION, config=fips)
runtime = boto3.client("sagemaker-runtime", region_name=REGION, config=fips)

print(s3.meta.endpoint_url)
# https://s3-fips.us-west-2.amazonaws.com
```

## AWS CLI

The AWS CLI honors `AWS_USE_FIPS_ENDPOINT` and `use_fips_endpoint`, and also accepts `--endpoint-url`:

```bash
aws sagemaker describe-endpoint \
  --endpoint-name <your-endpoint-name> \
  --region us-west-2 \
  --endpoint-url https://api-fips.sagemaker.us-west-2.amazonaws.com
```

## Confirm a run used FIPS endpoints

Print the resolved endpoint URL rather than assuming the setting took effect. `meta.endpoint_url` reports what the client will actually call, after every configuration source has been applied:

```python
for name, client in {"control plane": sagemaker, "inference": runtime}.items():
    url = client.meta.endpoint_url
    print(f"{name:14} {url}  FIPS={'-fips.' in url}")
```

This check matters most in the IAM Identity Center case above, where a misconfigured run can reach SageMaker over standard endpoints while your logs claim FIPS.

## Related resources

* [Security and Compliance](/docs/security-and-compliance-sagemaker) — what FIPS endpoints cover, FedRAMP coverage, network isolation, and VPC options
* [Deploy Deepgram on Amazon SageMaker](/docs/deploy-amazon-sagemaker) — full request examples for each transport
