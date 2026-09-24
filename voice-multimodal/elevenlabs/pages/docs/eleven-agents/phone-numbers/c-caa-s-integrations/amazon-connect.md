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
5. When the agent ends the call, ElevenLabs finishes the session with a `Complete` outcome and the
   flow continues from the Lex block. An `Escalate` outcome, which routes the caller to a human
   queue, is supported on the wire and will be exposed through the transfer tool; see
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

#### Create a dedicated API key

Create an API key in the same workspace as the agent and scope it to ElevenAgents. You will store
it in AWS Secrets Manager in the next section; do not paste it anywhere else.

#### Note the WebSocket URL

Amazon Connect connects to a URL that contains your agent ID:

| Environment    | AccessUrl                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------- |
| Default        | `wss://api.elevenlabs.io/v1/convai/conversation/amazon-connect/<agent_id>`                    |
| Data residency | `wss://api.<region>.residency.elevenlabs.io/v1/convai/conversation/amazon-connect/<agent_id>` |

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
connect.amazonaws.com](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3fc91a773575a547f3ac6d3a24d14cffac4535227057e4e8e4eb3ccfc71f27a0/assets/images/agents/amazon-connect-secret.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=c9c4206538154e11e005a47aa70812934dcb17158370d1e7fe25d339c1d75cdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
permissions](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/2d9c7dd52c77bfeefd3c4f5beb99681d578014c407cf37dbc7d2e2f457c40ee8/assets/images/agents/amazon-connect-security-profile.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=aecd277606e3909257cfdef90764677bed9416a7783b6ac7190c491262e2bae5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Create and publish the orchestration AI agent

The orchestration agent hands every voice conversation to the application immediately, with audio
streaming enabled. Voice sessions require immediate hand-off; text streaming
(`audioStreamingEnabled` set to false) and `delegateAgentConfiguration` are not supported by
ElevenLabs.

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
attached](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3ade9397b18d3af79fc4f3ae63fef06cec9e17d59109e5c226d403339c32f052/assets/images/agents/amazon-connect-ai-agent-security-profile.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=543809a1a2e97f08c4d482664445e47ccadf2fbc156668f2e67bd786a72a56ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
intent](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6d857b4a57a6289c26249b80bad8181b68af5b7654db9ae0adbf0ea830091ca4/assets/images/agents/amazon-connect-lex-intents.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=0f052849cf2ce03d396b21f3bd264a1176a4d97a4c374517a1606619e5ba1760&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
passthrough flag](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/812e85e379bcf3eb422497d27fe7740da8e3482222ca858089ad1b4de2f92e4b/assets/images/agents/amazon-connect-lex-session-attributes.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=2c8ed6a898cb446121552a0d279f1eae39830c0802368839f5675dbf7b37e540&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Note**
>
> `x-amz-lex:qic-audio-passthrough` gates the third-party voice path during AWS's prelaunch period.
> AWS states the attribute is no longer needed once the feature is public; leaving it in place is
> harmless.

#### Branch on the outcome

Amazon Connect surfaces the ElevenLabs outcome to the flow as the `$.Lex.SessionAttributes.Tool`
attribute. Add a **Check contact attributes** block after the Lex block, set **Namespace** to
**Lex**, **Key** to **Session attributes**, and **Session Attribute Key** to `Tool`, then add an
**Equals** condition per outcome:

| Value      | Meaning                                                                                | Suggested route                       |
| ---------- | -------------------------------------------------------------------------------------- | ------------------------------------- |
| `Complete` | The agent ended the call, for example with the **End call** tool.                      | Disconnect                            |
| `Escalate` | The agent asked for a human (see [Transferring to a human](#transferring-to-a-human)). | Set working queue → Transfer to queue |

![Check contact attributes block configured on the Lex session attribute Tool with Equals
conditions for each outcome](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/aa004d8a78522f66f256e879abcf1888a01e2e1bc22b8e712d197a9c4bd8b566/assets/images/agents/amazon-connect-check-attributes-block.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=bca01d41561cb637506c46857be10bacfbbe97d2c4d8e447243b33f31d7f65bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> **Warning**
>
> Amazon Connect writes these values in title case (`Escalate`, `Complete`), not as the upper-case
> outcome type the agent sends. In an exported flow, the Lex block's **Default** output is its
> `NoMatchingCondition` transition; make sure it leads to the comparison block rather than an error
> message.

![Contact flow with the Get customer input block leading to a Check contact attributes block that
routes Escalate to a queue and Complete to a
disconnect](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/70dd68ee4561c165f12cfa4c62512d153f9a922f2d99f2479c92c09abc0e83c4/assets/images/agents/amazon-connect-contact-flow.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=aaff69591bc0de3e905882d87e6916413b4bf9a1a931076c540ddfbbeccd6222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The flow above compares against both spellings of each outcome so it keeps working if the casing
changes.

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
`Complete`, and your flow continues from the Lex block.

#### Check the conversation in ElevenLabs

Open the conversation in **Conversations**. Its source is Amazon Connect and the **Client data**
tab lists the `amazon_connect_*` dynamic variables the session received.

![Client data tab of an Amazon Connect conversation listing the Amazon Connect dynamic
variables](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ced3be27e366822341940e3fa5f96c2cd7376b1e63e86ace2dac31d778039417/assets/images/agents/amazon-connect-conversation-history.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260924T233144Z&X-Amz-Expires=604800&X-Amz-Signature=07e97d856ee1240bc5c1bda03660e374beb42abf0b29fa5f88dd21c7601ce758&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Check the flow log in AWS

With logging enabled, every block writes an entry to the instance's flow log group. The **Get
customer input** block records the outcome it received from ElevenLabs:

```bash
aws logs filter-log-events --log-group-name /aws/connect/<INSTANCE_ALIAS> \
  --start-time $(( $(date +%s) - 600 ))000 --region $AWS_REGION \
  --query 'events[].message' --output text | tr '\t' '\n' | grep -o '"Results": *"[A-Za-z_]*"'
```

Expect `"Results": "Complete"` for the Lex block, followed by the blocks on your `Complete` branch.

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
[conversation initiation webhook](/docs/eleven-agents/customization/personalization/twilio-personalization).
For Amazon Connect sessions the webhook is called before the agent speaks with `caller_id` set to
the customer's number, `called_number` set to the Amazon Connect number, and `call_id` set to the
Amazon Connect contact ID, so a Lambda in your flow can store contact attributes keyed by contact ID
and the webhook can return them as dynamic variables and configuration overrides.

## Transferring to a human

Amazon Connect routes a contact to a human queue when the ElevenLabs session ends with an
`Escalate` outcome, which your flow's `Escalate` branch handles with **Set working queue** and
**Transfer to queue**. Any queue treatment, whisper flow, or agent selection is handled by Amazon
Connect.

> **Note**
>
> The agent-side trigger for `Escalate` is being added to the **Transfer to number** tool as an
> Amazon Connect transfer type, so that one tool covers human handoff on every provider. Until it
> ships, ElevenLabs agents on Amazon Connect can end the call (`Complete`) but cannot escalate to a
> human. Keep the `Escalate` branch in your flow; it starts working without further flow changes.

The **End call** tool produces a `Complete` outcome. Post-call analysis and the post-call webhook
run as usual after either outcome.

Only the outcome type and a reason string travel back to Amazon Connect. To hand routing data to
the flow, give the agent a [webhook tool](/docs/eleven-agents/customization/tools/server-tools)
that calls Amazon Connect's `UpdateContactAttributes` API with `amazon_connect_contact_id` and the
values to store, and instruct the agent to call it before ending the call. The flow can then read
those attributes with a **Check contact attributes** block after the Lex block. The post-call
webhook fires after the flow has already continued, so it suits CRM updates rather than routing
decisions.

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
  number** does not yet support Amazon Connect; human handoff arrives as an Amazon Connect
  transfer type in that tool.
* Data collection results are not returned to the flow, and Amazon Connect decides which contact
  data it shares. Use the conversation initiation webhook keyed by `amazon_connect_contact_id` for
  additional context, a webhook tool that calls `UpdateContactAttributes` for routing data, and the
  post-call webhook for everything else.
* Configuration overrides such as `system__override_first_message` cannot be passed from the flow.
  Return them from the conversation initiation webhook instead.
* Voice sessions require immediate hand-off. The Amazon Connect chat channel, text streaming, and
  behind-the-scenes (`delegateAgentConfiguration`) collaboration are not supported yet.
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
