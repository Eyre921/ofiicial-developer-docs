---
title: "Amazon Bedrock Setup"
source: https://docs.fireworks.ai/nexus/provider-keys/bedrock
path: nexus/provider-keys/bedrock
---

Connect a Bedrock IAM role or API key so Nexus Auto can call supported models through your AWS account.

An Amazon Bedrock Provider Key lets Nexus Auto call supported models with an IAM role or API key from your AWS account. Fireworks stores the credential. Bedrock usage and charges stay in your AWS account.

Bedrock uses the same account-admin workflow as Anthropic and OpenAI, but each model also needs a Bedrock model ID and region. See [Provider Keys](/nexus/provider-keys) for shared states, rotation, and security.

> [!WARNING]
>
> Before setup, confirm that your AWS account can invoke every model you plan to add. Some third-party or restricted models require explicit Bedrock model access, a Marketplace agreement, or approval from AWS or the model provider. Anthropic may also require a one-time use-case form.

## Supported models

| Model | Served model ID | Example Bedrock Runtime model ID | AWS reference |
| - | - | - | - |
| Claude Opus 5 | `claude-opus-5` | `global.anthropic.claude-opus-5` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html#model-card-anthropic-claude-opus-5-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html#model-card-anthropic-claude-opus-5-regional-availability) |
| Claude Opus 5.5 | `claude-opus-5-5` | `global.anthropic.claude-opus-5-5` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html#model-card-anthropic-claude-opus-5-5-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html#model-card-anthropic-claude-opus-5-5-regional-availability) |
| GPT-5.6 Sol | `gpt-5.6-sol` | `global.openai.gpt-5.6-sol` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html#model-card-openai-gpt-56-sol-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html#model-card-openai-gpt-56-sol-regional-availability) |
| GPT-6 Sol | `gpt-6-sol` | `global.openai.gpt-6-sol` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-sol.html#model-card-openai-gpt-6-sol-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-sol.html#model-card-openai-gpt-6-sol-regional-availability) |
| GPT-6.1 Sol | `gpt-6.1-sol` | `global.openai.gpt-6.1-sol` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html#model-card-openai-gpt-6-1-sol-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html#model-card-openai-gpt-6-1-sol-regional-availability) |
| GPT-6 Astra | `gpt-6-astra` | `global.openai.gpt-6-astra` | [Model ID](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html#model-card-openai-gpt-6-astra-programmatic-access) · [Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html#model-card-openai-gpt-6-astra-regional-availability) |

Where each column is used:

* **Model:** the name shown in the dashboard model picker. You select it; you never type an ID.
* **Served model ID:** the ID in the response `model` field, such as `claude-opus-5-5`. Your application still sends `auto`, or the model ID itself to pin that model. `firectl` uses the served ID as `routes[].nexus_model_id`. You do not type it in the dashboard.
* **Bedrock model ID:** the AWS identifier. Copy it exactly from AWS. Paste it into each route's **Model ID** field, or set `routes[].bedrock.model_id`. Any geo/global profile or ARN that AWS lists for the model also works, as long as your region can invoke it.
* **Region:** the AWS source region. In Fireworks, select it in each route's **Region** field, or set `routes[].bedrock.aws_region`. The supported regions are `us-east-1`, `us-east-2`, `us-west-1`, and `us-west-2`.

## Prepare AWS

In the AWS account that will pay for inference, [request or verify access to each model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

* For Anthropic models, complete the one-time use-case form and Marketplace agreement if AWS requires them.
* For restricted models, complete any additional AWS or provider approval.
* Confirm that the account can invoke the selected model or inference profile.

**IAM role**

Set `sts:ExternalId` to your exact Fireworks account ID.

**1. Configure the trust policy**

In **AWS IAM → Roles → Create role**, choose **Custom trust policy** and paste:

```json theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::843780049090:role/nexus-bedrock-byok"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<FIREWORKS_ACCOUNT_ID>"
        }
      }
    }
  ]
}
```

![Configuring the Fireworks principal ARN and account-specific External ID in an AWS IAM custom trust policy](https://mintcdn.com/fireworksai/ujMDJFNEX7NdyBj0/images/fireworks-nexus/provider-keys/bedrock/iam-role-trust-policy.png?fit=max\&auto=format\&n=ujMDJFNEX7NdyBj0\&q=85\&s=977912ddca8bbf7719bd5adb75aea2ca)

**2. Add Bedrock permissions**

In **Step 2: Add permissions**, select **Create inline policy** and paste:

```json theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*"
    }
  ]
}
```

`Resource: "*"` covers all Bedrock inference targets and the default project. SCPs, permission boundaries, and explicit denies still apply.

![Adding an inline Bedrock invocation policy in the AWS IAM Create role wizard](https://mintcdn.com/fireworksai/ujMDJFNEX7NdyBj0/images/fireworks-nexus/provider-keys/bedrock/iam-role-permissions.png?fit=max\&auto=format\&n=ujMDJFNEX7NdyBj0\&q=85\&s=2fb6955992a2124b3d3652a4680c8b45)

**3. Create the role**

In **Step 3**, name the role `FireworksBedrockBYOK` or use another name that begins with `FireworksBedrock`. Use the default IAM path; custom role paths are not supported. Review the trust policy and permissions, then create the role.

![Reviewing the FireworksBedrockBYOK role name and trust policy before creating the AWS IAM role](https://mintcdn.com/fireworksai/ujMDJFNEX7NdyBj0/images/fireworks-nexus/provider-keys/bedrock/iam-role-review.png?fit=max\&auto=format\&n=ujMDJFNEX7NdyBj0\&q=85\&s=ce2cbb20fe7c9ebcced2054215a82aa4)

Copy the role ARN from the role summary.

![AWS IAM role summary showing the FireworksBedrockBYOK role ARN and inline policy](https://mintcdn.com/fireworksai/5EvfarxWLqhpXYL9/images/fireworks-nexus/provider-keys/bedrock/iam-role-summary.png?fit=max\&auto=format\&n=5EvfarxWLqhpXYL9\&q=85\&s=82e0dbc8c85917cc761c7d17048b4b40)

> **Create the role with AWS CLI**
>
> Set the External ID to your exact Fireworks account ID:
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

**API key**

Generate a long-term key in **Amazon Bedrock console → API keys**, then copy it. See [Generate an Amazon Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-generate.html).

> [!NOTE]
>
> Short-term keys are valid only in the Region where they were generated and for at most 12 hours. Fireworks does not refresh them. Use a long-term key.

## Connect in the dashboard

**IAM role**

**1. Connect the key**

Open **Settings → [Provider Keys](https://app.fireworks.ai/settings/provider-keys)**. On the **Amazon Bedrock** row, click **Connect**.

Select **IAM Role**. Keep the External ID exactly as shown, then complete the AWS steps. Paste the IAM role ARN, not the permission policy ARN, and click **Continue**.

![Connecting an Amazon Bedrock IAM role in the Provider Keys dashboard](https://mintcdn.com/fireworksai/Vlf8OtCu4-U4nVi7/images/fireworks-nexus/provider-keys/bedrock/connect-iam-role.gif?s=242f3a45151be8bb98d6c637bdd8d618)

In **Add models to Amazon Bedrock**, select the models that should use this credential, then click **Connect**. You must select at least one.

![Selecting models for an Amazon Bedrock Provider Key](https://mintcdn.com/fireworksai/JD1KCHWcNDNUqemu/images/fireworks-nexus/provider-keys/bedrock/paste-key.gif?s=246b94c64f1430eb0cf535a058160dae)

The card shows **Connecting** for about a minute while Fireworks finishes setup.

**2. Fill in the model routes**

Connecting stores the credential but does not route traffic yet. Once the card is connected, the models you picked appear as empty rows for you to complete.

1. For each row under **Models using Bedrock**, paste the AWS **Model ID** and select a **Region**.
2. Click **Save**. Save stays disabled until every row has both values.

![Bedrock model rows with Model ID and Region fields after saving an IAM role connection](https://mintcdn.com/fireworksai/Vlf8OtCu4-U4nVi7/images/fireworks-nexus/provider-keys/bedrock/fill-routes-saved.gif?s=aa80530686a9af1582f78c4410190170)

After saving, each row displays its Model ID and Region. Traffic for those models is now billed to your AWS account. Every other model keeps its current provider.

**API key**

**1. Connect the key**

Open **Settings → [Provider Keys](https://app.fireworks.ai/settings/provider-keys)**. On the **Amazon Bedrock** row, click **Connect**.

Select **API Key**, paste the Bedrock key, and click **Continue**.

![Connecting a Bedrock API key in the Provider Keys dashboard](https://mintcdn.com/fireworksai/Vlf8OtCu4-U4nVi7/images/fireworks-nexus/provider-keys/bedrock/connect-api-key.gif?s=8d09d6d7e550e8df456342535e6c966a)

In **Add models to Amazon Bedrock**, select the models that should use this credential, then click **Connect**. You must select at least one.

![Selecting models for an Amazon Bedrock Provider Key](https://mintcdn.com/fireworksai/JD1KCHWcNDNUqemu/images/fireworks-nexus/provider-keys/bedrock/paste-key.gif?s=246b94c64f1430eb0cf535a058160dae)

The card shows **Connecting** for about a minute while Fireworks finishes setup.

**2. Fill in the model routes**

Connecting stores the credential but does not route traffic yet. Once the card is connected, the models you picked appear as empty rows for you to complete.

1. For each row under **Models using Bedrock**, paste the AWS **Model ID** and select a **Region**.
2. Click **Save**. Save stays disabled until every row has both values.

![Bedrock model rows with Model ID and Region fields before saving](https://mintcdn.com/fireworksai/JD1KCHWcNDNUqemu/images/fireworks-nexus/provider-keys/bedrock/fill-routes.gif?s=22d2174e64925389d090620a2bc5e144)

After saving, each row displays its Model ID and Region. Traffic for those models is now billed to your AWS account. Every other model keeps its current provider.

### Change model routes later

Use **Add model** or the trash icon on a row to add or remove models. Use **Edit models** to change the Model ID or Region of existing rows. Then click **Save**.

Use **Update Key** to replace the API key or IAM role ARN without changing the routes. This is the **Replace** action described in [Provider Keys](/nexus/provider-keys#replace-or-remove-a-key). Use **Remove** to delete the Bedrock credential and all of its routes.

![Amazon Bedrock card menu with Add model, Edit models, Update Key, and Remove](https://mintcdn.com/fireworksai/JD1KCHWcNDNUqemu/images/fireworks-nexus/provider-keys/bedrock/manage.gif?s=52a66d8d835b3a439407e62b9037041b)

## Manage with `firectl`

### Upload the key

**IAM role**

```bash wrap theme={null}
firectl provider-key upload \
  --provider-type bedrock \
  --aws-iam-role-arn arn:aws:iam::123456789012:role/FireworksBedrockBYOK \
  --display-name production-bedrock
```

Fireworks returns the full role ARN in `KEY_HINT` for list output and `key_hint` for JSON. A role ARN is an identifier, not a secret.

**API key**

Save the bearer key to a local file, then upload it with `--from-file`. This keeps the key out of your shell history and process list. See [Manage keys with `firectl`](/nexus/provider-keys#manage-keys-with-firectl).

```bash wrap theme={null}
firectl provider-key upload \
  --provider-type bedrock \
  --from-file ./bedrock.key \
  --display-name production-bedrock
```

Delete the local file after upload.

Save the returned key ID as `KEY_ID`. `upload` stores the credential but does not route traffic.

### Write the routes file

Create `routes.json`. Each entry maps one Nexus Auto model to one Bedrock region and model ID. The file holds only model and region values, not the key.

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
* Copy `model_id` exactly from AWS; geo/global prefixes and ARNs are significant.
* Older route files that use the deprecated `firerouter_model_id` field still work.

### Bind the key and routes

```bash wrap theme={null}
firectl provider-key-binding bind \
  bedrock KEY_ID \
  --routes-file ./routes.json
```

* **Always pass the complete route file.** Every bind replaces the whole route set; omitted routes are deleted.
* **Confirm removed routes.** If a bind removes routes, `firectl` asks for confirmation. Pass `--yes` to skip the prompt.

Confirm both the state and the route list. `CONNECTED` with empty `routes` serves no Bedrock traffic. Before the first bind, `get` returns `NOT_FOUND`.

```bash wrap theme={null}
firectl provider-key-binding get bedrock -o json
```

Unbind and delete are the same as other providers. See [Delete a key](/nexus/provider-keys#delete-a-key).

## Troubleshooting

* **AssumeRole is denied (IAM role):** check that the trust policy uses the exact Fireworks principal ARN and your Fireworks account ID as `sts:ExternalId`. The role name must start with `FireworksBedrock` and use the default IAM path. IAM changes can take a few seconds to apply.
* **InvokeModel is denied:** check the role permission policy, SCPs, permission boundaries, model access, and Marketplace or provider approval in the same AWS account.
* **API key is unauthorized or expired:** generate a replacement, then upload and bind it. Expiring or revoking a key in AWS does not change the Fireworks state.
* **Model not found:** copy the exact model or profile ID from AWS. Never derive it from the served model ID.
* **Region unavailable:** confirm the region can invoke that exact inference profile.
* **"This ARN isn't in the right format." (dashboard):** paste the full IAM role ARN from the role summary page. A permission policy ARN or a role name alone won't work.
* **"Test failed" on a model row (dashboard):** see "Model not found" and "Region unavailable" above. If every model fails, see "AssumeRole is denied."
* **Save button stays disabled (dashboard):** a row is missing its Model ID or Region.
* **A route disappeared (`firectl`):** every bind replaces the whole route set. Include all routes you want to keep.
* **Connected but traffic does not reach Bedrock:** confirm the route list is not empty and that requests use a route containing one of the configured served model IDs.
