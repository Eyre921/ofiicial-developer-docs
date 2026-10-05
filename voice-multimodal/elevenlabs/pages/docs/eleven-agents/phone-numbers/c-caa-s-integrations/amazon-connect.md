---
title: "Amazon Connect"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/c-caa-s-integrations/amazon-connect.md
path: docs/eleven-agents/phone-numbers/c-caa-s-integrations/amazon-connect
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Amazon Connect

> **Warning**
>
> The Amazon Connect integration is in limited availability. Amazon Connect's third-party AI agent
> support must be enabled for your AWS account, and the ElevenLabs transport is enabled per
> workspace. Contact your ElevenLabs representative before routing customer traffic.

## Overview

The Amazon Connect integration connects an Amazon Connect contact flow directly to an agent in
ElevenAgents over Amazon Connect's third-party AI agent protocol, an extension of the open
[A2A protocol](https://a2a-protocol.org/). Amazon Connect owns telephony, routing, and the queue;
ElevenAgents owns the conversation. No SIP trunk, Twilio number, or middleware is required. AWS
documents the feature under
[Agent-to-agent collaboration](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-collaboration.html);
this guide covers the ElevenLabs specifics and the AWS steps needed to reach an ElevenLabs agent.

The same flow serves inbound calls and outbound contacts started with `StartOutboundVoiceContact`.
When the ElevenLabs agent finishes, Amazon Connect continues your contact flow and branches on the
outcome it received.

## How the integration works

1. A contact flow reaches a **Get customer input** block that invokes an Amazon Lex V2 bot with the
   `AMAZON.QInConnectIntent` intent.
2. Amazon Connect's orchestration AI agent hands the conversation off immediately to the
   third-party application you registered for ElevenLabs.
3. Amazon Connect opens a WebSocket to the ElevenLabs endpoint in the application's `AccessUrl`,
   authenticating with the API key stored in AWS Secrets Manager.
4. Amazon Connect signals that the caller's channel is live, then Amazon Connect and ElevenLabs
   exchange 16-bit linear PCM audio as A2A messages. Amazon Connect proposes the sample rate and
   ElevenLabs adopts it, so no audio format changes are needed on the agent.
5. When the agent ends the call or hands the caller to a human, ElevenLabs finishes the session with
   a `Complete` or `Escalate` outcome and the flow continues from the Lex block; see
   [Transferring to a human](#transferring-to-a-human).

## Requirements

Before you begin, ensure you have:

1. An Amazon Connect instance on the Connect Customer tier with third-party AI agent support
   enabled for the account and Region.
2. An Amazon Q in Connect assistant associated with the instance.
3. AWS permissions to create KMS keys, Secrets Manager secrets, AppIntegrations applications,
   Connect security profiles, Amazon Q in Connect AI agents, Lex V2 bots, and contact flows.
4. An ElevenLabs workspace with the Amazon Connect transport enabled.
5. An ElevenLabs agent and a dedicated API key.
6. AWS CLI v2 and [awscurl](https://github.com/okigan/awscurl) (`pip install awscurl`) for the
   calls whose request shapes are not in released CLI versions yet.

> **Note**
>
> Keep every AWS resource in the same account and Region as the Amazon Connect instance. The steps
> below use the AWS CLI where it supports the call and `awscurl` (a SigV4-signed HTTP request) where
> it does not. They follow AWS's [Set up collaboration with an external AI agent](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-setup-external.html) and add the
> ElevenLabs-specific values.

## Configure ElevenLabs

#### Create or select an agent

Create the agent in ElevenAgents. Give it a first message if it should speak as soon as the
hand-off completes; Amazon Connect plays nothing of its own during the session.

#### Enable End call

In **Agent → Tools → System tools**, enable **End call** so the agent can finish the session when
the caller's request is resolved. Amazon Connect then continues your flow with the `Complete`
outcome.

#### Add an Amazon Connect transfer rule (optional)

To let the agent hand the caller to a human, give it the **Transfer to number** system tool with a
transfer rule whose provider configuration is `amazon_connect`. The rule has no destination: the
session ends with the `Escalate` outcome and your contact flow chooses the queue. Transfer rules are
configured through the API. Add the tool with a `PATCH` on the agent:

```bash
curl -X PATCH "https://api.elevenlabs.io/v1/convai/agents/agent_7101k5zvyjhmfg983brhmhkd98n6" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{
    "conversation_config": {"agent": {"prompt": {"built_in_tools": {
      "end_call": {"type": "system", "name": "end_call", "description": "",
                   "params": {"system_tool_type": "end_call"}},
      "transfer_to_number": {
        "type": "system", "name": "transfer_to_number", "description": "",
        "params": {
          "system_tool_type": "transfer_to_number",
          "transfers": [],
          "transfer_rules": [{
            "condition": "the caller asks to speak with a human",
            "provider_configs": [
              {"type": "amazon_connect", "config": {"type": "amazon_connect_escalate"}}
            ]
          }]
        }
      }
    }}}}
  }'
```

Send the agent's full `built_in_tools` object, including tools it already has such as `end_call`.
The agent picks the rule by its `condition`; the option it echoes back is the fixed token
`amazon_connect`, so one Amazon Connect rule per tool is enough. Phone numbers and SIP URIs
configured for other providers are not offered on Amazon Connect calls.

> **Note**
>
> Transfer rules are an API-managed setting. Configure and update the **Transfer to number** tool of
> an agent that uses them through the API, as above; the dashboard's tool editor works with the
> per-number transfer list.

#### Create a dedicated API key

Create an API key in the same workspace as the agent and scope it to ElevenAgents. You will store
it in AWS Secrets Manager in the next section; do not paste it anywhere else.

#### Note the WebSocket URL

Amazon Connect connects to a URL that contains your agent ID:

| Environment    | AccessUrl                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| Default        | `wss://api.elevenlabs.io/v1/convai/conversation/amazon-connect/agent_7101k5zvyjhmfg983brhmhkd98n6`                    |
| Data residency | `wss://api.<region>.residency.elevenlabs.io/v1/convai/conversation/amazon-connect/agent_7101k5zvyjhmfg983brhmhkd98n6` |

> **Info**
>
> If your ElevenLabs account is on an isolated residency environment, replace `<region>` with your
> region code. See [data residency](/docs/overview/administration/data-residency) for the available
> regions.

## Register the ElevenLabs application in AWS

Everything in this section is an API call. Set the values you will reuse once:

```bash
export AWS_REGION=<REGION>          # Region of your Amazon Connect instance
export ACCOUNT_ID=<ACCOUNT_ID>
export INSTANCE_ID=<INSTANCE_ID>    # Amazon Connect instance ID
export INSTANCE_ARN=arn:aws:connect:$AWS_REGION:$ACCOUNT_ID:instance/$INSTANCE_ID
export AGENT_ID=<AGENT_ID>          # ElevenLabs agent ID
```

#### Create an Amazon Q in Connect assistant

Skip this step if the instance already has an assistant. Otherwise create one and associate it
with the instance:

```bash
aws qconnect create-assistant --name elevenlabs-assistant --type AGENT --region $AWS_REGION
aws connect create-integration-association --instance-id $INSTANCE_ID \
  --integration-type WISDOM_ASSISTANT --integration-arn <ASSISTANT_ARN> --region $AWS_REGION
```

Record the assistant ID and ARN.

#### Store the API key

Amazon Connect reads the key from Secrets Manager with its own service principal, so the secret
must be encrypted with a customer-managed KMS key that grants `connect.amazonaws.com` decrypt
access. The default `aws/secretsmanager` key cannot be used.

**`kms-key-policy.json`**

```json title="kms-key-policy.json"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccountAdmin",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::<ACCOUNT_ID>:root" },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowConnectDecrypt",
      "Effect": "Allow",
      "Principal": { "Service": "connect.amazonaws.com" },
      "Action": ["kms:Decrypt", "kms:DescribeKey"],
      "Resource": "*"
    }
  ]
}
```

Save the ElevenLabs API key in a file so that it never appears in your shell history, then create
the key and the secret:

```bash
KMS_KEY_ID=$(aws kms create-key --description "ElevenLabs agent API key" \
  --policy file://kms-key-policy.json --region $AWS_REGION \
  --query KeyMetadata.KeyId --output text)
SECRET_ARN=$(aws secretsmanager create-secret --name elevenlabs/agent-api-key \
  --kms-key-id "$KMS_KEY_ID" --secret-string file://elevenlabs-api-key.txt \
  --region $AWS_REGION --query ARN --output text)
rm elevenlabs-api-key.txt
```

Grant Amazon Connect read access to the secret:

**`secret-resource-policy.json`**

```json title="secret-resource-policy.json"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowConnectRead",
      "Effect": "Allow",
      "Principal": { "Service": "connect.amazonaws.com" },
      "Action": ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"],
      "Resource": "<SECRET_ARN>"
    }
  ]
}
```

```bash
aws secretsmanager put-resource-policy --secret-id "$SECRET_ARN" \
  --resource-policy file://secret-resource-policy.json --region $AWS_REGION
```

![Secrets Manager secret encrypted with the customer-managed key and its resource policy for
connect.amazonaws.com](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3fc91a773575a547f3ac6d3a24d14cffac4535227057e4e8e4eb3ccfc71f27a0/assets/images/agents/amazon-connect-secret.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=0e716b06a324758af46f154aaa3816e848f08b9d3de6cd5086746c39dc203bb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Create the third-party application

Register the ElevenLabs WebSocket URL as an AppIntegrations application of type `A2A_SERVER`.
`AuthConfig` is mandatory for this type.

**`create-application.json`**

```json title="create-application.json"
{
  "Name": "elevenlabs-agent",
  "Namespace": "elevenlabs-agent",
  "Description": "ElevenLabs agent over the Amazon Connect A2A extension",
  "ApplicationType": "A2A_SERVER",
  "ApplicationSourceConfig": {
    "ExternalUrlConfig": {
      "AccessUrl": "wss://api.elevenlabs.io/v1/convai/conversation/amazon-connect/<AGENT_ID>"
    }
  },
  "AuthConfig": {
    "AuthType": "API_KEY",
    "CredentialProviderIdentifier": "<SECRET_ARN>"
  }
}
```

```bash
awscurl --service app-integrations --region $AWS_REGION -X POST \
  -H 'Content-Type: application/json' --data @create-application.json \
  "https://app-integrations.$AWS_REGION.amazonaws.com/applications"
```

The response contains the application `Id` and `Arn`; export them as `APPLICATION_ID` and
`APPLICATION_ARN`. The Amazon Connect console does not list `A2A_SERVER` applications, so verify
with the API:

```bash
aws appintegrations get-application --arn "$APPLICATION_ARN" --region $AWS_REGION
```

#### Associate the application with your instance

```bash
awscurl --service connect --region $AWS_REGION -X PUT -H 'Content-Type: application/json' \
  --data "{\"IntegrationArn\": \"$APPLICATION_ARN\", \"IntegrationType\": \"APPLICATION\"}" \
  "https://connect.$AWS_REGION.amazonaws.com/instance/$INSTANCE_ID/integration-associations"
aws connect list-integration-associations --instance-id $INSTANCE_ID \
  --integration-type APPLICATION --region $AWS_REGION
```

#### Allow the application in a security profile

The security profile attached to the orchestration AI agent must list the application under its
allowed AI agents, or the hand-off fails at runtime.

```bash
SECURITY_PROFILE_ID=$(aws connect create-security-profile --instance-id $INSTANCE_ID \
  --security-profile-name elevenlabs-a2a --permissions QConnectAIAgents.View Wisdom.View \
  --region $AWS_REGION --query SecurityProfileId --output text)
awscurl --service connect --region $AWS_REGION -X POST -H 'Content-Type: application/json' \
  --data "{\"AllowedAIAgents\": [{\"Arn\": \"$APPLICATION_ARN\", \"Type\": \"THIRD_PARTY\"}]}" \
  "https://connect.$AWS_REGION.amazonaws.com/security-profiles/$INSTANCE_ID/$SECURITY_PROFILE_ID"
```

The admin website shows the profile and its permissions but not the allowed AI agents; those are
only visible through the API.

![Dedicated security profile in the Amazon Connect admin website with AI agent view
permissions](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2d9c7dd52c77bfeefd3c4f5beb99681d578014c407cf37dbc7d2e2f457c40ee8/assets/images/agents/amazon-connect-security-profile.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=8d622f3c55bc1a48c343c5a3e73b91c15adaa0d2a4ce0904dd3ddd722215bae1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Create and publish the orchestration AI agent

The orchestration agent hands every voice conversation to the application immediately, with audio
streaming enabled. Voice sessions require immediate hand-off; text streaming
(`audioStreamingEnabled` set to false) and `delegateAgentConfiguration` are not supported by
ElevenLabs. An audio immediate hand-off orchestrator must also declare the reserved `Complete`
tool of type `RETURN_TO_CONTROL` in `toolConfigurations`; without it the create request fails with
`An audio frontline orchestrator (with an audio immediate handoff) must configure the reserved
'Complete' RETURN_TO_CONTROL tool`.

**`create-ai-agent.json`**

```json title="create-ai-agent.json"
{
  "name": "elevenlabs-handoff",
  "type": "ORCHESTRATION",
  "visibilityStatus": "PUBLISHED",
  "configuration": {
    "orchestrationAIAgentConfiguration": {
      "connectInstanceArn": "<INSTANCE_ARN>",
      "locale": "en_US",
      "multiAgentConfigurations": [
        {
          "handoffAgentConfiguration": {
            "agentTarget": { "applicationId": "<APPLICATION_ARN>" },
            "instruction": {
              "instruction": "Immediately hand off every voice conversation to the ElevenLabs agent."
            },
            "audioStreamingEnabled": true,
            "immediateHandoff": true
          }
        }
      ],
      "toolConfigurations": [
        {
          "toolName": "Complete",
          "toolType": "RETURN_TO_CONTROL",
          "description": "Close the conversation when the customer has no more questions.",
          "instruction": {
            "instruction": "Mark the conversation as complete when the customer has no additional questions or needs."
          },
          "inputSchema": {
            "type": "object",
            "properties": {
              "reason": { "type": "string", "description": "Reason for completion" }
            },
            "required": ["reason"]
          },
          "userInteractionConfiguration": { "isUserConfirmationRequired": false }
        }
      ]
    }
  }
}
```

```bash
awscurl --service wisdom --region $AWS_REGION -X POST -H 'Content-Type: application/json' \
  --data @create-ai-agent.json \
  "https://wisdom.$AWS_REGION.amazonaws.com/assistants/<ASSISTANT_ID>/aiagents"
aws qconnect create-ai-agent-version --assistant-id <ASSISTANT_ID> \
  --ai-agent-id <AI_AGENT_ID> --region $AWS_REGION
```

Publishing returns a versioned ARN (`<AI_AGENT_ARN>:1`); the contact flow references it. Attach
the security profile to both the unversioned and the versioned agent:

```bash
for ARN in <AI_AGENT_ARN> <AI_AGENT_ARN>:1; do
  aws connect associate-security-profiles --instance-id $INSTANCE_ID --entity-arn "$ARN" \
    --entity-type AI_AGENT --security-profiles Id=$SECURITY_PROFILE_ID --region $AWS_REGION
done
```

![Orchestration AI agent in the AI agent designer with the dedicated security profile
attached](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3ade9397b18d3af79fc4f3ae63fef06cec9e17d59109e5c226d403339c32f052/assets/images/agents/amazon-connect-ai-agent-security-profile.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=0e4e2424defb3b3885c074914510e985415904d2f60a3c6c9d79c487f2a45368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Build the contact flow

#### Create the Lex bot

1. Create a Lex V2 bot whose only intent is the built-in `AMAZON.QInConnectIntent`, configured
   with your assistant ARN. Do not add other intents.
2. Enable speech-to-speech on the bot locale. Bidirectional audio streaming only works with
   Sonic speech-to-speech bots.
3. Allow the bot's IAM role to use the assistant. Without this the hand-off fails inside AWS with
   `HTTP 403` before any request reaches ElevenLabs. Attach a policy like:

**`lex-role-policy.json`**

```json title="lex-role-policy.json"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["wisdom:CreateSession", "wisdom:GetAssistant"],
      "Resource": ["<ASSISTANT_ARN>", "<ASSISTANT_ARN>/*"]
    },
    {
      "Effect": "Allow",
      "Action": ["wisdom:SendMessage", "wisdom:GetNextMessage"],
      "Resource": "arn:aws:wisdom:<REGION>:<ACCOUNT_ID>:session/<ASSISTANT_ID>/*"
    }
  ]
}
```

4. Build the bot, create a version and an alias, and associate the alias with the instance:

```bash
aws connect associate-bot --instance-id $INSTANCE_ID \
  --lex-v2-bot AliasArn=<LEX_ALIAS_ARN> --region $AWS_REGION
```

![Lex V2 bot intents list with the Q in Connect hand-off intent and the built-in fallback
intent](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6d857b4a57a6289c26249b80bad8181b68af5b7654db9ae0adbf0ea830091ca4/assets/images/agents/amazon-connect-lex-intents.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=b79b57b792d3479ccf28a0a7e6fde2f01328191a7debcd46fc7f4260f9648250&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add the assistant and the Lex block

In the flow designer, add these blocks in order:

1. **Set logging behavior**: enabled. The flow log is how you verify the hand-off below.
2. **Connect assistant**: select your Amazon Q in Connect assistant.
3. **Get customer input**: on the **Amazon Lex** tab choose **Enter an ARN** and paste the bot
   alias ARN. Leave the text-to-speech prompt as a single space so that Amazon Connect plays
   nothing before the hand-off. Under **Session attributes**, add two attributes set manually:

| Destination key                       | Value                                            |
| ------------------------------------- | ------------------------------------------------ |
| `x-amz-lex:q-in-connect:ai-agent-arn` | The versioned orchestration agent ARN (`...:1`). |
| `x-amz-lex:qic-audio-passthrough`     | `true`                                           |

![Session attributes of the Get customer input block: the versioned AI agent ARN and the audio
passthrough flag](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/812e85e379bcf3eb422497d27fe7740da8e3482222ca858089ad1b4de2f92e4b/assets/images/agents/amazon-connect-lex-session-attributes.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=20498b52d2d85a8cbf0ccc0c9b615db3a35b7b25510fd3e789e3e3435a24e1fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Note**
>
> `x-amz-lex:qic-audio-passthrough` gates the third-party voice path during AWS's prelaunch period.
> AWS states the attribute is no longer needed once the feature is public; leaving it in place is
> harmless.

#### Branch on the outcome

Amazon Connect surfaces the ElevenLabs outcome to the flow as the `$.Lex.SessionAttributes.Tool`
attribute. Add a **Check contact attributes** block after the Lex block, set **Namespace** to
**Lex**, **Key** to **Session attributes**, and **Session Attribute Key** to `Tool`, then add one
**Equals** condition per outcome and route **No Match** to an error prompt:

| Branch     | Meaning                                                                                | Suggested route                       |
| ---------- | -------------------------------------------------------------------------------------- | ------------------------------------- |
| `Complete` | The agent ended the call, for example with the **End call** tool.                      | Disconnect                            |
| `Escalate` | The agent asked for a human (see [Transferring to a human](#transferring-to-a-human)). | Set working queue → Transfer to queue |
| No Match   | Any other value.                                                                       | Play prompt → Disconnect              |

![Check contact attributes block configured on the Lex session attribute Tool with Equals
conditions for each outcome](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e73068b736d4023417602a17c480112a3d7f5617694390fc8a88f03c4b7855e1/assets/images/agents/amazon-connect-check-attributes-block.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=793570a4d7befc0e39f6303fa4413a606e1d8efc7a8714ba03abd20672792ed9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Warning**
>
> Amazon Connect writes the outcome in title case (`Escalate`, `Complete`), not as the upper-case
> finish type sent on the wire, so these two conditions are all the block needs. A session that
> fails after the hand-off finishes with the `COMPLETE_WITH_ERROR` type; the Lex block then takes
> its **Error** output or the comparison falls through to **No Match**, so route both to the error
> prompt. In an exported flow, the Lex block's **Default** output is its `NoMatchingCondition`
> transition; make sure it leads to the comparison block rather than an error message.

![Contact flow with the Get customer input block leading to a Check contact attributes block that
routes Escalate to a queue, Complete to a disconnect, and No Match to an error
prompt](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/71e5a3ec507c431ff692545db58376e07db0605efb8bb42f4e17e709a1a0dedf/assets/images/agents/amazon-connect-contact-flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=6d62c5935407b13afb06d743ba77a6dd7ce63d055f9e077a1b58d9f6fbc7f8ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Publish and assign

Publish the flow, then point a claimed phone number at it:

```bash
aws connect associate-phone-number-contact-flow --instance-id $INSTANCE_ID \
  --phone-number-id <PHONE_NUMBER_ID> --contact-flow-id <CONTACT_FLOW_ID> --region $AWS_REGION
```

For outbound calls, start the contact with the same flow; Amazon Connect dials the customer and
hands the answered call to ElevenLabs:

```bash
aws connect start-outbound-voice-contact --instance-id $INSTANCE_ID \
  --contact-flow-id <CONTACT_FLOW_ID> --destination-phone-number <E164_NUMBER> \
  --source-phone-number <YOUR_CONNECT_NUMBER> --region $AWS_REGION
```

## Test the integration

#### Place a call

Call the number. The agent's first message plays a few seconds after the flow reaches the Lex
block; the hand-off inside AWS takes about three seconds before ElevenLabs is contacted. Have a
short conversation and say goodbye: the agent calls **End call**, the ElevenLabs session ends with
`Complete`, and your flow continues from the Lex block. If you added a transfer rule, ask for a
human instead: the agent calls **Transfer to number**, the session ends with `Escalate`, and the
flow takes that branch.

#### Check the conversation in ElevenLabs

Open the conversation in **Conversations**. Its source is Amazon Connect and the **Client data**
tab lists the `amazon_connect_*` dynamic variables the session received.

![Client data tab of an Amazon Connect conversation listing the Amazon Connect dynamic
variables](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ced3be27e366822341940e3fa5f96c2cd7376b1e63e86ace2dac31d778039417/assets/images/agents/amazon-connect-conversation-history.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20261005%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261005T112149Z&X-Amz-Expires=604800&X-Amz-Signature=9a156c08c313561c29e625aca252a7d4821a7f220b33999b72a233a8fa56b0e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Check the flow log in AWS

With logging enabled, every block writes an entry to the instance's flow log group. The **Get
customer input** block records the outcome it received from ElevenLabs:

```bash
aws logs filter-log-events --log-group-name /aws/connect/<INSTANCE_ALIAS> \
  --start-time $(( $(date +%s) - 600 ))000 --region $AWS_REGION \
  --query 'events[].message' --output text | tr '\t' '\n' | grep -o '"Results": *"[A-Za-z_]*"'
```

Expect `"Results": "Complete"`, or `"Results": "Escalate"` after a transfer, for the Lex block,
followed by the blocks on that branch.

## Dynamic variables

Amazon Connect sends the contact's system attributes with every session. ElevenLabs exposes them,
together with the session identifiers, as dynamic variables:

| Dynamic variable                                             | Description                                                          |
| ------------------------------------------------------------ | -------------------------------------------------------------------- |
| `system__caller_id`                                          | The customer's phone number (Amazon Connect's customer endpoint).    |
| `system__called_number`                                      | The Amazon Connect phone number the contact is on (system endpoint). |
| `system__call_id`                                            | The Amazon Connect contact ID.                                       |
| `amazon_connect_system_attributes_channel`                   | The contact channel, for example `VOICE`.                            |
| `amazon_connect_system_attributes_customer_endpoint_address` | The customer endpoint address as sent by Amazon Connect.             |
| `amazon_connect_system_attributes_system_endpoint_address`   | The system endpoint address as sent by Amazon Connect.               |
| `amazon_connect_interaction_mode`                            | The collaboration mode, for example `HANDOFF`.                       |
| `amazon_connect_contact_id`                                  | The Amazon Connect contact ID.                                       |
| `amazon_connect_contact_arn`                                 | The full contact ARN.                                                |
| `amazon_connect_context_id`                                  | The A2A session (context) ID.                                        |
| `amazon_connect_instance_id`                                 | The instance ID.                                                     |
| `amazon_connect_instance_arn`                                | The instance ARN.                                                    |

On Amazon Connect sessions `system__caller_id` is always the customer and `system__called_number`
is always the Amazon Connect number, for both inbound and outbound contacts.

Every other member of the contact context Amazon Connect sends is exposed the same way: nested
names are joined with underscores and converted to snake case under the `amazon_connect_` prefix.
Custom contact attributes set in your flow with **Set contact attributes** are not part of the
context Amazon Connect currently sends, even when the AI agent's security profile can view contact
attributes; if AWS starts including them, they will appear automatically under the same prefix. You
cannot choose which contact data Amazon Connect shares; AWS passes a fixed set of context.

To pass additional context, use the
[conversation initiation webhook](/docs/eleven-agents/customization/personalization#conversation-initiation-webhooks).
For Amazon Connect sessions the webhook is called before the agent speaks with `caller_id` set to
the customer's number, `called_number` set to the Amazon Connect number, and `call_id` set to the
Amazon Connect contact ID, so a Lambda in your flow can store contact attributes keyed by contact ID
and the webhook can return them as dynamic variables and configuration overrides.

## Transferring to a human

Give the agent the **Transfer to number** system tool with an `amazon_connect` transfer rule, as
shown in [Configure ElevenLabs](#configure-elevenlabs). When the rule's condition is met, the agent
calls the tool and ElevenLabs finishes the session with the `Escalate` outcome and the reason the
agent gave. Your flow's `Escalate` branch then handles the contact with **Set working queue** and
**Transfer to queue**. The rule carries no destination, so the queue is chosen in the flow, not by
the agent; queue treatment, whisper flows, and agent selection stay in Amazon Connect.

The **End call** tool produces a `Complete` outcome. Post-call analysis and the post-call webhook
run as usual after either outcome.

### Giving the human agent a summary

Amazon Connect exposes only the outcome to your flow: `$.Lex.SessionAttributes.Tool` (and the Lex
intent name) carry `Escalate`, and nothing else from the ElevenLabs session, not the transfer
reason, reaches the flow. To brief the human who takes the call, store the summary on the contact
yourself and let an agent whisper flow read it out:

1. Expose an endpoint that calls Amazon Connect's `UpdateContactAttributes` API. A minimal Lambda
   behind an HTTP API is enough; the caller must be allowed `connect:UpdateContactAttributes` on the
   instance's contacts:

   ```python
   import json, os, boto3

   connect = boto3.client("connect")

   def handler(event, _context):
       if (event.get("headers") or {}).get("x-shared-secret") != os.environ["SHARED_SECRET"]:
           return {"statusCode": 401, "body": ""}
       body = json.loads(event.get("body") or "{}")
       connect.update_contact_attributes(
           InstanceId=os.environ["INSTANCE_ID"],
           InitialContactId=body["contact_id"],
           Attributes={"handoff_summary": body["summary"][:1000]},
       )
       return {"statusCode": 200, "body": json.dumps({"ok": True})}
   ```

2. Give the agent a [webhook tool](/docs/eleven-agents/customization/tools/webhook-tools) that
   `POST`s to that endpoint with `contact_id` filled from the `amazon_connect_contact_id` dynamic
   variable and a `summary` the model writes. Keep the shared secret in a workspace secret and send
   it as a request header. In the system prompt, tell the agent to call this tool first and to call
   **Transfer to number** only after it has returned; a model that emits both calls in one turn
   races the transfer against the summary. With that instruction, the attribute was on the contact
   about a second after the agent's request in our tests, three seconds before Amazon Connect
   resumed the flow.

3. In the contact flow's `Escalate` branch, add a **Set whisper flow** block before **Transfer to
   queue** that points at an agent whisper flow whose **Play prompt** reads
   `$.Attributes.handoff_summary`. Amazon Connect speaks it to the human agent while the caller
   hears the queue treatment, then bridges the two. Do not set `handoff_summary` again in a later
   block of the flow: an empty value there replaces what the endpoint wrote.

The same attribute is available to a **Check contact attributes** block for routing decisions.
The post-call webhook fires after the flow has already continued, so it suits CRM updates rather
than routing decisions.

## Traces

Amazon Connect
[requires external agents to send trace data](https://docs.aws.amazon.com/connect/latest/adminguide/a2a-trace-enforcement.html)
for every collaboration. When Amazon Connect subscribes to tracing on the session, ElevenLabs sends
an OpenTelemetry trace for each agent turn containing the caller's transcript, the agent's response,
each tool call with its result, and per-span timing. Amazon Connect stores these traces with the
contact; see
[AI agent traces](https://docs.aws.amazon.com/connect/latest/adminguide/ai-agent-traces.html) for
how to view them. Transcripts and tool results in these traces are subject to the same redaction
settings as the rest of your contact data in Amazon Connect, so review your data-handling
requirements before enabling the integration. Like
[post-call webhooks](/docs/eleven-agents/workflows/post-call-webhooks), traces are delivered to
your own systems: agents in [zero retention mode](/docs/eleven-agents/customization/privacy/zrm)
still send them, because zero retention governs what ElevenLabs stores, not what your Amazon
Connect instance receives.

## Audio

Amazon Connect proposes 16-bit mono linear PCM at 8, 16, or 24 kHz on each session and ElevenLabs
adopts the proposal, so the agent's configured audio formats are not used for Amazon Connect
sessions. Caller barge-in is detected by ElevenLabs and reported to Amazon Connect so buffered
playback is flushed immediately. Keypad input collected by Amazon Connect is delivered to the agent
as DTMF digits. Amazon Connect's own silence marker is ignored; use the agent's turn timeout to
re-prompt a quiet caller.

## Limitations and unsupported features

* Client tools and the **Play keypad touch tone** system tool are not supported. **Transfer to
  number** works only through an Amazon Connect transfer rule: the agent cannot dial a phone number
  or SIP URI from an Amazon Connect call, and the flow decides which queue receives an escalated
  caller.
* Data collection results are not returned to the flow, and Amazon Connect decides which contact
  data it shares. Use the conversation initiation webhook keyed by `amazon_connect_contact_id` for
  additional context, a webhook tool that calls `UpdateContactAttributes` for routing data, and the
  post-call webhook for everything else.
* Configuration overrides such as `system__override_first_message` cannot be passed from the flow.
  Return them from the conversation initiation webhook instead.
* Voice sessions require immediate hand-off. The Amazon Connect chat channel, text streaming, and
  behind-the-scenes (`delegateAgentConfiguration`) collaboration are not supported.
* Traces sent to Amazon Connect cover the caller's transcript, the agent's responses, tool calls
  with their results, and timing. Tool call parameters are not included.
* Amazon Connect's third-party agent support is only available where AWS has enabled it and may
  incur additional AWS charges.

## Troubleshooting

#### The flow fails with 'A2A WebSocket upgrade ... failed (HTTP 403)'

* The error is raised inside AWS before any request reaches ElevenLabs. Check CloudTrail for
  `AccessDenied` on `wisdom:SendMessage` from the Lex service role: the role attached to the bot
  needs `wisdom:CreateSession`, `wisdom:GetAssistant`, `wisdom:SendMessage`, and
  `wisdom:GetNextMessage` on the assistant and its sessions.
* Confirm the security profile allows the application and is associated with the published
  orchestration agent version referenced by the flow.
* Confirm the secret's KMS key and resource policy grant `connect.amazonaws.com` access.

#### The flow fails with 'the hand-off to the target agent could not be completed'

* Amazon Connect gives the WebSocket connection roughly 20 seconds to come up. Confirm the
  `AccessUrl` is reachable from AWS: `wss://`, the right agent ID, no network allow-list in the
  way.
* If you proxy the connection through your own infrastructure, keep that proxy warm. A cold
  serverless instance can take longer than the hand-off window, and Amazon Connect gives up before
  ElevenLabs ever sees the request.

#### The Lex block takes its Error branch and the caller hears nothing

* Confirm both session attributes are set on the **Get customer input** block:
  `x-amz-lex:q-in-connect:ai-agent-arn` with the published, versioned agent ARN and
  `x-amz-lex:qic-audio-passthrough` set to `true`.
* Confirm the security profile that allows the application is attached to that agent version.
* Read the block's entry in the flow log; it carries the error Amazon Connect encountered.

#### The session ends immediately after connecting

* Confirm the `AccessUrl` uses `wss://`, contains the correct agent ID, and points at the region
  your workspace lives in.
* Confirm the API key is active, belongs to the agent's workspace, and has no IP restrictions.
* Confirm the Amazon Connect transport is enabled for your workspace.

#### The caller hears the flow's error prompt after the agent finishes

In the Lex block, make sure the **Default** output leads to the block that compares
`$.Lex.SessionAttributes.Tool`, and compare against the title-case values `Escalate` and
`Complete`.

#### The agent never speaks and the session ends after a few seconds

Confirm the collaborator is configured with `audioStreamingEnabled` set to true. With text
streaming, Amazon Connect sends text turns and expects text responses, which ElevenLabs does not
support; the ElevenLabs logs show `INIT_SESSION carries no audio configuration`.

#### Dynamic variables are missing

Amazon Connect provides the contact system attributes and identifiers listed above. Custom contact
attributes set in the flow do not reach the agent; pass them through the conversation initiation
webhook instead. If the agent's first message or prompt references a variable that is never
provided, the session fails at startup.
