---
title: "Amazon Bedrock Setup"
source: https://docs.fireworks.ai/nexus/provider-keys/bedrock
path: nexus/provider-keys/bedrock
---

Connect a Bedrock IAM role or API key so Nexus Auto can call supported models through your AWS account.

Bedrock usage and charges stay in your AWS account.

* Setup follows the same admin workflow as [Provider Keys](/nexus/provider-keys), plus a Bedrock model ID and region for each model.
* Fireworks stores the credential.

> [!WARNING]
>
> Before you start, confirm your AWS account can invoke every model you plan to add. Some models need explicit Bedrock model access, a Marketplace agreement, or approval from AWS or the model provider. Anthropic may also require a one-time use-case form.

* Shared states, rotation, and security are on [Provider Keys](/nexus/provider-keys).

## Supported models

| Model | Example Bedrock model ID | AWS reference |
| - | - | - |
| Claude Opus 5 | `global.anthropic.claude-opus-5` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html#model-card-anthropic-claude-opus-5-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html#model-card-anthropic-claude-opus-5-regional-availability) |
| Claude Opus 5.5 | `global.anthropic.claude-opus-5-5` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html#model-card-anthropic-claude-opus-5-5-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html#model-card-anthropic-claude-opus-5-5-regional-availability) |
| GPT-5.6 Sol | `global.openai.gpt-5.6-sol` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html#model-card-openai-gpt-56-sol-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html#model-card-openai-gpt-56-sol-regional-availability) |
| GPT-6 Sol | `global.openai.gpt-6-sol` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-sol.html#model-card-openai-gpt-6-sol-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-sol.html#model-card-openai-gpt-6-sol-regional-availability) |
| GPT-6.1 Sol | `global.openai.gpt-6.1-sol` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html#model-card-openai-gpt-6-1-sol-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html#model-card-openai-gpt-6-1-sol-regional-availability) |
| GPT-6 Astra | `global.openai.gpt-6-astra` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html#model-card-openai-gpt-6-astra-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html#model-card-openai-gpt-6-astra-regional-availability) |

* Copy the Bedrock model ID exactly from AWS. Any geo or global profile, or ARN, that AWS lists for the model also works if your region can invoke it, unless your account uses US data residency (below).
* Supported regions: `us-east-1`, `us-east-2`, `us-west-1`, and `us-west-2`.

### US data residency

If your Fireworks account enforces [US data residency](/accounts/data-residency), each route must keep requests in the US:

* Use a `us.` inference profile, such as `us.anthropic.claude-opus-5-5`, or an in-Region model ID with no geo prefix.
* `global.` profiles are rejected, even in a US region, because AWS can serve them from any region. Requests to that model return `403` with `reason_code: residency`.
* A model with only a `global.` profile on Bedrock, such as GPT-6 Sol, can't be served on Bedrock for your account.

Served model IDs (the ID in the response `model` field, and `routes[].nexus_model_id` in `firectl`):

| Model | Served model ID |
| - | - |
| Claude Opus 5 | `claude-opus-5` |
| Claude Opus 5.5 | `claude-opus-5-5` |
| GPT-5.6 Sol | `gpt-5.6-sol` |
| GPT-6 Sol | `gpt-6-sol` |
| GPT-6.1 Sol | `gpt-6.1-sol` |
| GPT-6 Astra | `gpt-6-astra` |

* **Model:** the name in the dashboard model picker. You select it and never type an ID.
* **Served model ID:** applications still send `auto`, or the served model ID itself to pin that model. You don't type it in the dashboard.
* **Bedrock model ID:** paste it into each route's **Model ID** field, or set `routes[].bedrock.model_id`.
* **Region:** the AWS source region. Select it in each route's **Region** field, or set `routes[].bedrock.aws_region`.

## Prepare AWS

In the AWS account that pays for inference, [request or verify access to each model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html). Complete any use-case form, Marketplace agreement, or provider approval AWS asks for, then confirm the account can invoke the model or inference profile.

Then create one credential, either an IAM role or an API key.

> [tab] IAM role
>
> **1. Configure the trust policy**
>
> In **AWS IAM → Roles → Create role**, choose **Custom trust policy** and paste this. Set `sts:ExternalId` to your exact Fireworks account ID.
>
> ```json theme={null}
> {
>   "Version": "2012-10-17",
>   "Statement": [
>     {
>       "Effect": "Allow",
>       "Principal": {
>         "AWS": "arn:aws:iam::843780049090:role/nexus-bedrock-byok"
>       },
>       "Action": "sts:AssumeRole",
>       "Condition": {
>         "StringEquals": {
>           "sts:ExternalId": "<FIREWORKS_ACCOUNT_ID>"
>         }
>       }
>     }
>   ]
> }
> ```
>
> ![Configuring the Fireworks principal ARN and account-specific External ID in an AWS IAM custom trust policy](https://mintcdn.com/fireworksai/ujMDJFNEX7NdyBj0/images/fireworks-nexus/provider-keys/bedrock/iam-role-trust-policy.png?fit=max\&auto=format\&n=ujMDJFNEX7NdyBj0\&q=85\&s=977912ddca8bbf7719bd5adb75aea2ca)
>
> **2. Add Bedrock permissions**
>
> In **Step 2: Add permissions**, select **Create inline policy** and paste:
>
> ```json theme={null}
> {
>   "Version": "2012-10-17",
>   "Statement": [
>     {
>       "Effect": "Allow",
>       "Action": [
>         "bedrock:InvokeModel",
>         "bedrock:InvokeModelWithResponseStream"
>       ],
>       "Resource": "*"
>     }
>   ]
> }
> ```
>
> `Resource: "*"` covers all Bedrock inference targets and the default project. SCPs, permission boundaries, and explicit denies still apply.
>
> **3. Create the role**
>
> Name the role `FireworksBedrockBYOK`, or any name that starts with `FireworksBedrock`. Keep the default IAM path. Create the role, then copy its ARN from the role summary.
>
> * Custom role paths are not supported.
> * Review the trust policy and permissions in **Step 3** before creating the role.
>
> Create the role with AWS CLI. Set the External ID to your exact Fireworks account ID:
>
> ```bash wrap theme={null}
> export AWS_PROFILE="customer-admin"
> export ROLE_NAME="FireworksBedrockBYOK"
> export FIREWORKS_PRINCIPAL_ARN="arn:aws:iam::843780049090:role/nexus-bedrock-byok"
> export EXTERNAL_ID="<FIREWORKS_ACCOUNT_ID>"
> ```
>
> Create the role and trust policy:
>
> ```bash wrap theme={null}
> cat >/tmp/fireworks-bedrock-trust.json <<EOF
> {
>   "Version": "2012-10-17",
>   "Statement": [
>     {
>       "Effect": "Allow",
>       "Principal": {
>         "AWS": "${FIREWORKS_PRINCIPAL_ARN}"
>       },
>       "Action": "sts:AssumeRole",
>       "Condition": {
>         "StringEquals": {
>           "sts:ExternalId": "${EXTERNAL_ID}"
>         }
>       }
>     }
>   ]
> }
> EOF
>
> export CUSTOMER_ROLE_ARN="$(
>   aws iam create-role \
>     --profile "$AWS_PROFILE" \
>     --role-name "$ROLE_NAME" \
>     --assume-role-policy-document file:///tmp/fireworks-bedrock-trust.json \
>     --query 'Role.Arn' \
>     --output text
> )"
> ```
>
> Add the Bedrock permission policy:
>
> ```bash wrap theme={null}
> cat >/tmp/fireworks-bedrock-permissions.json <<'EOF'
> {
>   "Version": "2012-10-17",
>   "Statement": [
>     {
>       "Effect": "Allow",
>       "Action": [
>         "bedrock:InvokeModel",
>         "bedrock:InvokeModelWithResponseStream"
>       ],
>       "Resource": "*"
>     }
>   ]
> }
> EOF
>
> aws iam put-role-policy \
>   --profile "$AWS_PROFILE" \
>   --role-name "$ROLE_NAME" \
>   --policy-name FireworksBedrockBYOKPolicy \
>   --policy-document file:///tmp/fireworks-bedrock-permissions.json
>
> echo "$CUSTOMER_ROLE_ARN"
> ```

> [tab] API key
>
> [Generate a long-term key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-generate.html) in **Amazon Bedrock console → API keys**, then copy it.
>
> Don't use a short-term key. It works only in the Region where it was generated, expires within 12 hours, and Fireworks doesn't refresh it.

## Connect in the dashboard

**1. Connect the credential**

Open **Settings → [Provider Keys](https://nexus.fireworks.ai/settings/provider-keys)** and click **Connect** on the **Amazon Bedrock** row.

* **IAM Role:** keep the External ID exactly as shown. Paste the role ARN, not the permission policy ARN.
* **API Key:** paste the Bedrock key.

Click **Continue**.

![Connecting an Amazon Bedrock IAM role in the Provider Keys dashboard](https://mintcdn.com/fireworksai/Vlf8OtCu4-U4nVi7/images/fireworks-nexus/provider-keys/bedrock/connect-iam-role.gif?s=242f3a45151be8bb98d6c637bdd8d618)

**2. Pick models**

In **Add models to Amazon Bedrock**, select at least one model, then click **Connect**. The card shows **Connecting** for about a minute.

**3. Fill in the model routes**

Connecting stores the credential but routes no traffic yet. For each row under **Models using Bedrock**, paste the AWS **Model ID**, select a **Region**, and click **Save**.

Traffic for those models now bills to your AWS account. Every other model keeps its current provider.

* Once the card is connected, the picked models appear as empty rows to complete.
* **Save** stays disabled until every row has both a Model ID and a Region.
* After saving, each row displays its Model ID and Region.

### Change model routes later

* **Add model** or the trash icon adds or removes a model. **Edit models** changes a Model ID or Region. Then click **Save**.
* **Update Key** replaces the API key or IAM role ARN and keeps the routes. This is the **Replace** action on [Provider Keys](/nexus/provider-keys#replace-or-remove-a-key).
* **Remove** deletes the Bedrock credential and all its routes.

![Amazon Bedrock card menu with Add model, Edit models, Update Key, and Remove](https://mintcdn.com/fireworksai/JD1KCHWcNDNUqemu/images/fireworks-nexus/provider-keys/bedrock/manage.gif?s=52a66d8d835b3a439407e62b9037041b)

## Manage with `firectl`

`firectl` is the older way to set up Bedrock and remains supported for existing route files and scripts. For new setups, use [Provider Keys](https://nexus.fireworks.ai/settings/provider-keys) in Nexus settings.

| Task | Command |
| - | - |
| Upload an IAM role | `firectl provider-key upload --provider-type bedrock --aws-iam-role-arn ROLE_ARN` |
| Upload an API key | `firectl provider-key upload --provider-type bedrock --from-file PATH` |
| Bind with routes | `firectl provider-key-binding bind bedrock KEY_ID --routes-file ./routes.json` |
| Check routes | `firectl provider-key-binding get bedrock -o json` |

### Upload the key

IAM role:

```bash wrap theme={null}
firectl provider-key upload \
  --provider-type bedrock \
  --aws-iam-role-arn arn:aws:iam::123456789012:role/FireworksBedrockBYOK \
  --display-name production-bedrock
```

Fireworks returns the full role ARN in `KEY_HINT` for list output and `key_hint` for JSON. A role ARN is an identifier, not a secret.

API key: save the bearer key to a local file, then upload it with `--from-file`. This keeps the key out of shell history and the process list. See [Manage keys with `firectl`](/nexus/provider-keys#manage-keys-with-firectl). Delete the local file after upload.

```bash wrap theme={null}
firectl provider-key upload \
  --provider-type bedrock \
  --from-file ./bedrock.key \
  --display-name production-bedrock
```

Save the returned key ID as `KEY_ID`. `upload` stores the credential but does not route traffic.

### Write the routes file

`routes.json` maps each Nexus Auto model to one Bedrock region and model ID. It holds only model and region values, not the key.

```json theme={null}
{
  "routes": [
    {
      "nexus_model_id": "claude-opus-5-5",
      "bedrock": {
        "aws_region": "us-east-1",
        "model_id": "global.anthropic.claude-opus-5-5"
      }
    },
    {
      "nexus_model_id": "gpt-5.6-sol",
      "bedrock": {
        "aws_region": "us-east-1",
        "model_id": "global.openai.gpt-5.6-sol"
      }
    }
  ]
}
```

Rules:

* Use only the served model IDs in [Supported models](#supported-models).
* Each model appears once and maps to one `(aws_region, model_id)` target.
* Copy `model_id` exactly from AWS. Geo/global prefixes and ARNs are significant.
* Older route files that use the deprecated `firerouter_model_id` field still work.

### Bind the key and routes

```bash wrap theme={null}
firectl provider-key-binding bind \
  bedrock KEY_ID \
  --routes-file ./routes.json
```

* **Always pass the complete route file.** Every bind replaces the whole route set. Omitted routes are deleted.
* **Confirm removed routes.** If a bind removes routes, `firectl` asks for confirmation. Pass `--yes` to skip the prompt.

Confirm both the state and the route list with `get`. `CONNECTED` with empty `routes` serves no Bedrock traffic. Before the first bind, `get` returns `NOT_FOUND`.

Unbind and delete work the same as other providers. See [Delete a key](/nexus/provider-keys#manage-keys-with-firectl).

## Troubleshooting

* **AssumeRole is denied (IAM role):** the trust policy needs the exact Fireworks principal ARN and your Fireworks account ID as `sts:ExternalId`. The role name must start with `FireworksBedrock` and use the default IAM path.
* **Model not found or region unavailable:** copy the exact model or profile ID from AWS, and confirm the region can invoke it.
* **`403` with `reason_code: residency`:** your account uses US data residency and the route uses a `global.` or non-US profile. Switch it to a `us.` profile. See [US data residency](#us-data-residency).
* **Connected but traffic doesn't reach Bedrock:** make sure the route list isn't empty and requests use a route containing one of the configured served model IDs.

- IAM changes can take a few seconds to apply.
- **InvokeModel is denied:** check the role permission policy, SCPs, permission boundaries, model access, and Marketplace or provider approval in the same AWS account.
- **API key is unauthorized or expired:** generate a replacement, then upload and bind it. Expiring or revoking a key in AWS does not change the Fireworks state.
- **Model not found:** never derive the Bedrock ID from the served model ID.
- **"This ARN isn't in the right format." (dashboard):** paste the full IAM role ARN from the role summary page. A permission policy ARN or a role name alone won't work.
- **"Test failed" on a model row (dashboard):** see model not found and region unavailable. If every model fails, see AssumeRole is denied.
- **Save button stays disabled (dashboard):** a row is missing its Model ID or Region.
- **A route disappeared (`firectl`):** every bind replaces the whole route set. Include all routes you want to keep.
