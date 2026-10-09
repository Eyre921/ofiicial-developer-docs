---
title: "Amazon Bedrock Setup"
source: https://docs.fireworks.ai/nexus/provider-keys/bedrock
path: nexus/provider-keys/bedrock
---

Connect a Bedrock IAM role or API key so FireRouter can call supported models through your AWS account.

An Amazon Bedrock Provider Key lets FireRouter use an IAM role or API key from your AWS account for supported models. Fireworks stores the credential securely. Bedrock usage and charges remain in your AWS account.

Bedrock uses the same account-admin workflow as Anthropic and OpenAI, but each model also needs a Bedrock model ID and region. See <a href="/nexus/provider-keys">Provider Keys</a> for shared states, rotation, and security.

<Warning>
  Before setup, confirm that your AWS account can invoke every model you plan to add. Some third-party or restricted models require explicit Bedrock model access, a Marketplace agreement, or approval from AWS or the model provider. Anthropic may also require a one-time use-case form.
</Warning>

## Supported models

| Model | Served model ID | Example Bedrock Runtime model ID | AWS reference |
| - | - | - | - |
| Claude Opus 5 | `claude-opus-5` | `global.anthropic.claude-opus-5` | <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html#model-card-anthropic-claude-opus-5-programmatic-access">Model ID</a> · <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html#model-card-anthropic-claude-opus-5-regional-availability">Regions</a> |
| Claude Opus 5.5 | `claude-opus-5-5` | `global.anthropic.claude-opus-5-5` | <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html#model-card-anthropic-claude-opus-5-5-programmatic-access">Model ID</a> · <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html#model-card-anthropic-claude-opus-5-5-regional-availability">Regions</a> |
| GPT-5.6 Sol | `gpt-5.6-sol` | `global.openai.gpt-5.6-sol` | <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html#model-card-openai-gpt-56-sol-programmatic-access">Model ID</a> · <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html#model-card-openai-gpt-56-sol-regional-availability">Regions</a> |
| GPT-6 Sol | `gpt-6-sol` | `global.openai.gpt-6-sol` (confirm in your account) | <a href="https://aws.amazon.com/blogs/machine-learning/bring-more-intelligence-to-everyday-work-with-gpt-6-sol-and-gpt-6-luna-on-amazon-bedrock/">AWS launch announcement</a>. AWS has not yet published a model card for this model. |
| GPT-6 Astra | `gpt-6-astra` | `global.openai.gpt-6-astra` | <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html#model-card-openai-gpt-6-astra-programmatic-access">Model ID</a> · <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html#model-card-openai-gpt-6-astra-regional-availability">Regions</a> |

Where each column is used:

* **Model:** the name shown in the dashboard model picker. You select it; you never type an ID.
* **Served model ID:** the ID in the response `model` field, such as `claude-opus-5-5`. Your application still sends a router slug such as `firerouter/claude-opus-5-5`. `firectl` uses the served ID as `routes[].firerouter_model_id`. You do not type it in the dashboard.
* **Bedrock model ID:** the AWS identifier. Copy it exactly from AWS. Paste it into each route's **Model ID** field, or set `routes[].bedrock.model_id`. Any geo/global profile or ARN that AWS lists for the model also works, as long as your region can invoke it.
* **Region:** the AWS source region. In Fireworks, select it in each route's **Region** field, or set `routes[].bedrock.aws_region`. The supported regions are `us-east-1`, `us-east-2`, `us-west-1`, and `us-west-2`.

## Prepare AWS

In the AWS account that will pay for inference, <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html">request or verify access to each model</a>.

* For Anthropic models, complete the one-time use-case form and Marketplace agreement if AWS requires them.
* For restricted models, complete any additional AWS or provider approval.
* Confirm that the account can invoke the selected model or inference profile.

<Tabs>
  <Tab title="IAM role">
    Set `sts:ExternalId` to your exact Fireworks account ID.

    <Steps>
      <Step title="Configure the trust policy">
        In **AWS IAM → Roles → Create role**, choose **Custom trust policy** and paste:

        ```json theme={null}
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::843780049090:role/firerouter-byok"
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

        <Frame>
          <img alt="Configuring the Fireworks principal ARN and account-specific External ID in an AWS IAM custom trust policy" />
        </Frame>
      </Step>

      <Step title="Add Bedrock permissions">
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

        <Frame>
          <img alt="Adding an inline Bedrock invocation policy in the AWS IAM Create role wizard" />
        </Frame>
      </Step>

      <Step title="Create the role">
        In **Step 3**, name the role `FireworksBedrockBYOK` or use another name that begins with `FireworksBedrock`. Use the default IAM path; custom role paths are not supported. Review the trust policy and permissions, then create the role.

        <Frame>
          <img alt="Reviewing the FireworksBedrockBYOK role name and trust policy before creating the AWS IAM role" />
        </Frame>

        Copy the role ARN from the role summary.

        <Frame>
          <img alt="AWS IAM role summary showing the FireworksBedrockBYOK role ARN and inline policy" />
        </Frame>
      </Step>
    </Steps>

    <Accordion title="Create the role with AWS CLI">
      Set the External ID to your exact Fireworks account ID:

      ```bash wrap theme={null}
      export AWS_PROFILE="customer-admin"
      export ROLE_NAME="FireworksBedrockBYOK"
      export FIREWORKS_PRINCIPAL_ARN="arn:aws:iam::843780049090:role/firerouter-byok"
      export EXTERNAL_ID="<FIREWORKS_ACCOUNT_ID>"
      ```

      Create the role and trust policy:

      ```bash wrap theme={null}
      cat >/tmp/fireworks-bedrock-trust.json <<EOF
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
              "AWS": "${FIREWORKS_PRINCIPAL_ARN}"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
              "StringEquals": {
                "sts:ExternalId": "${EXTERNAL_ID}"
              }
            }
          }
        ]
      }
      EOF

      export CUSTOMER_ROLE_ARN="$(
        aws iam create-role \
          --profile "$AWS_PROFILE" \
          --role-name "$ROLE_NAME" \
          --assume-role-policy-document file:///tmp/fireworks-bedrock-trust.json \
          --query 'Role.Arn' \
          --output text
      )"
      ```

      Add the Bedrock permission policy:

      ```bash wrap theme={null}
      cat >/tmp/fireworks-bedrock-permissions.json <<'EOF'
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
      EOF

      aws iam put-role-policy \
        --profile "$AWS_PROFILE" \
        --role-name "$ROLE_NAME" \
        --policy-name FireworksBedrockBYOKPolicy \
        --policy-document file:///tmp/fireworks-bedrock-permissions.json

      echo "$CUSTOMER_ROLE_ARN"
      ```
    </Accordion>
  </Tab>

  <Tab title="API key">
    Generate a long-term key in **Amazon Bedrock console → API keys**, then copy it. See <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-generate.html">Generate an Amazon Bedrock API key</a>.

    <Note>
      Short-term keys are valid only in the Region where they were generated and for at most 12 hours. Fireworks does not refresh them. Use a long-term key.
    </Note>
  </Tab>
</Tabs>

## Connect in the dashboard

<Tabs>
  <Tab title="IAM role">
    <Steps>
      <Step title="Connect the key">
        Open **Settings → <a href="https://app.fireworks.ai/settings/provider-keys">Provider Keys</a>**. On the **Amazon Bedrock** row, click **Connect**.

        Select **IAM Role**. Keep the External ID exactly as shown, then complete the AWS steps. Paste the IAM role ARN, not the permission policy ARN, and click **Continue**.

        <Frame>
          <img alt="Connecting an Amazon Bedrock IAM role in the Provider Keys dashboard" />
        </Frame>

        In **Add models to Amazon Bedrock**, select the models that should use this credential, then click **Connect**. You must select at least one.

        <Frame>
          <img alt="Selecting models for an Amazon Bedrock Provider Key" />
        </Frame>

        The card shows **Connecting** for about a minute while we finish setup.
      </Step>

      <Step title="Fill in the model routes">
        Connecting stores the credential but does not route any traffic yet. Once the card is connected, the models you picked appear as empty rows that you must complete.

        1. For each row under **Models using Bedrock**, paste the AWS **Model ID** and select a **Region**.
        2. Click **Save**. Save stays disabled until every row has both values.

        <Frame>
          <img alt="Bedrock model rows with Model ID and Region fields after saving an IAM role connection" />
        </Frame>

        After saving, each row displays its Model ID and Region. Traffic for those models is now billed to your AWS account. Every other model keeps its current provider.
      </Step>
    </Steps>
  </Tab>

  <Tab title="API key">
    <Steps>
      <Step title="Connect the key">
        Open **Settings → <a href="https://app.fireworks.ai/settings/provider-keys">Provider Keys</a>**. On the **Amazon Bedrock** row, click **Connect**.

        Select **API Key**, paste the Bedrock key, and click **Continue**.

        <Frame>
          <img alt="Connecting a Bedrock API key in the Provider Keys dashboard" />
        </Frame>

        In **Add models to Amazon Bedrock**, select the models that should use this credential, then click **Connect**. You must select at least one.

        <Frame>
          <img alt="Selecting models for an Amazon Bedrock Provider Key" />
        </Frame>

        The card shows **Connecting** for about a minute while we finish setup.
      </Step>

      <Step title="Fill in the model routes">
        Connecting stores the credential but does not route any traffic yet. Once the card is connected, the models you picked appear as empty rows that you must complete.

        1. For each row under **Models using Bedrock**, paste the AWS **Model ID** and select a **Region**.
        2. Click **Save**. Save stays disabled until every row has both values.

        <Frame>
          <img alt="Bedrock model rows with Model ID and Region fields before saving" />
        </Frame>

        After saving, each row displays its Model ID and Region. Traffic for those models is now billed to your AWS account. Every other model keeps its current provider.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### Change model routes later

Use **Add model** or the trash icon on a row to add or remove models. Use **Edit models** to change the Model ID or Region of existing rows. Then click **Save**.

Use **Update Key** to replace the API key or IAM role ARN without changing the routes. This is the **Replace** action described in <a href="/nexus/provider-keys#replace-or-remove-a-key">Provider Keys</a>. Use **Remove** to delete the Bedrock credential and all of its routes.

<Frame>
  <img alt="Amazon Bedrock card menu with Add model, Edit models, Update Key, and Remove" />
</Frame>

## Manage with `firectl`

### Upload the key

<Tabs>
  <Tab title="IAM role">
    ```bash wrap theme={null}
    firectl provider-key upload \
      --provider-type bedrock \
      --aws-iam-role-arn arn:aws:iam::123456789012:role/FireworksBedrockBYOK \
      --display-name production-bedrock
    ```

    Fireworks returns the full role ARN in `KEY_HINT` for list output and `key_hint` for JSON. A role ARN is an identifier, not a secret.
  </Tab>

  <Tab title="API key">
    Save the bearer key to a local file, then upload it with `--from-file`. This keeps the key out of your shell history and process list. See <a href="/nexus/provider-keys#manage-keys-with-firectl">Manage keys with `firectl`</a>.

    ```bash wrap theme={null}
    firectl provider-key upload \
      --provider-type bedrock \
      --from-file ./bedrock.key \
      --display-name production-bedrock
    ```

    Delete the local file after upload.
  </Tab>
</Tabs>

Save the returned key ID as `KEY_ID`. `upload` only stores the credential; it does not route traffic.

### Write the routes file

Create `routes.json`. Each entry maps one FireRouter model to one Bedrock region and model ID. The file holds only model and region values, not the key.

```json theme={null}
{
  "routes": [
    {
      "firerouter_model_id": "claude-opus-5-5",
      "bedrock": {
        "aws_region": "us-east-1",
        "model_id": "global.anthropic.claude-opus-5-5"
      }
    },
    {
      "firerouter_model_id": "gpt-5.6-sol",
      "bedrock": {
        "aws_region": "us-east-1",
        "model_id": "global.openai.gpt-5.6-sol"
      }
    }
  ]
}
```

Rules:

* Use only the served model IDs in <a href="#supported-models">Supported models</a>.
* Each model appears once and maps to one `(aws_region, model_id)` target.
* Copy `model_id` exactly from AWS; geo/global prefixes and ARNs are significant.

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

Unbind and delete are the same as other providers. See <a href="/nexus/provider-keys#delete-a-key">Delete a key</a>.

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
