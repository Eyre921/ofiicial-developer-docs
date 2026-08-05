---
title: "Five9"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/c-caa-s-integrations/five9.md
path: docs/eleven-agents/phone-numbers/c-caa-s-integrations/five9
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Five9

Before following this guide, consider reading the [SIP trunking
guide](/docs/eleven-agents/phone-numbers/sip-trunking) to understand how ElevenLabs supports SIP
trunks and custom SIP headers.

## Overview

This guide explains how to integrate ElevenAgents with the Five9 Virtual Contact Center (VCC) using Five9 AI Agent Connect. Five9 transfers a live call to an ElevenLabs phone number, the ElevenLabs agent handles the conversation, and ElevenLabs returns routing or disposition data to Five9 so the Five9 flow can continue.

## How the Five9 integration works

Five9 AI Agent Connect uses an external transfer over SIP, with call context exchanged through custom SIP `X-` headers in both directions:

1. **Inbound transfer**: The Five9 IVR External Transfer Module transfers the call to an ElevenLabs phone number, sending call context as SIP `X-` headers on the INVITE.
2. **Conversation**: ElevenLabs answers the call and routes it to the correct agent, optionally through a router agent, then handles the conversation with the caller.
3. **Return path**: When the conversation ends, ElevenLabs attaches routing and disposition data to the SIP BYE as `X-` headers.
4. **Post-AI routing**: Five9 maps the returned headers into call variables and continues the call flow, such as transferring to a live agent, ending the call, or recording a disposition.

## Requirements

Before setting up the Five9 integration, ensure you have:

1. An active Five9 VCC domain with AI Agent Connect enabled.
2. Administrator access to the Five9 configuration, or a Five9 implementation team to make the changes.
3. An ElevenLabs account and an [agent](/docs/eleven-agents/quickstart) to handle the transferred calls.
4. A [SIP trunk phone number](/docs/eleven-agents/phone-numbers/sip-trunking) imported in ElevenLabs to use as the Five9 transfer destination.

AI Agent Connect is a paid add-on to Five9 VCC and is not enabled by default. Contact your Five9
Account Manager to enable it for your domain before starting this integration.

Both teams should agree on the transfer phone number, the header names sent in each direction, the
routing values, and the test plan before configuration begins.

## ElevenLabs setup

#### Import the transfer phone number

Follow the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) to import the phone number Five9 will transfer calls to. Custom SIP headers and BYE headers require a SIP trunk phone number.

Import the number in E.164 format with a `+1` country code (for example, `+18005550100`). Five9 sends the transfer in this format, and a mismatch will cause the transfer to fail.

#### Assign an agent

If a single agent handles all calls from Five9, assign it directly to the phone number in the [Phone Numbers dashboard](https://elevenlabs.io/app/agents/phone-numbers).

If multiple agents share one transfer number, assign a router agent instead and follow [Routing multiple agents through one number](#routing-multiple-agents-through-one-number).

#### Configure the returned headers

Map the dynamic variables your agent sets during the conversation to the SIP BYE header names Five9 expects. See [Configuring BYE headers](#configuring-bye-headers).

#### Run test calls

Place test calls with Five9 and confirm the inbound headers arrive as dynamic variables and the BYE headers are returned as expected. Inbound header values are visible in the conversation history under the **Phone Call** tab.

## Routing multiple agents through one number

To route calls to several ElevenLabs agents through a single Five9 transfer number, assign a **router agent** to the phone number and have Five9 send the target agent in a header such as `X-AgentID`.

Inbound `X-` headers are exposed as [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables), so `X-AgentID` is available to the router agent as `{{sip_agentid}}`. Configure the router agent with the [agent transfer](/docs/eleven-agents/customization/tools/system-tools/agent-transfer) tool and add a transfer rule for each `X-AgentID` value you expect, mapping it to the agent that should take the call.

This avoids provisioning a separate phone number for every agent.

## Headers sent from Five9 to ElevenLabs

Five9 can send call metadata as SIP `X-` headers on the INVITE. Header names are normalized by removing the `X-` prefix, converting to lowercase, replacing hyphens with underscores, and adding the `sip_` prefix.

| Header            | Dynamic variable        | Description                                                   |
| ----------------- | ----------------------- | ------------------------------------------------------------- |
| `X-CallANI`       | `{{sip_callani}}`       | The caller's phone number.                                    |
| `X-CallDNIS`      | `{{sip_calldnis}}`      | The dialed phone number.                                      |
| `X-CallID`        | `{{sip_callid}}`        | Unique Five9 call identifier.                                 |
| `X-CallSessionID` | `{{sip_callsessionid}}` | Identifier for the current session.                           |
| `X-CallCampaign`  | `{{sip_callcampaign}}`  | Name of the Five9 campaign.                                   |
| `X-AgentID`       | `{{sip_agentid}}`       | Target ElevenLabs agent, used for routing via a router agent. |

Use these variables in agent prompts, first messages, and tools to personalize the conversation.

The reserved headers `X-Call-ID` and `X-Caller-ID` map to the `system__call_sid` and
`system__caller_id` [system dynamic
variables](/docs/eleven-agents/customization/personalization/dynamic-variables#system-dynamic-variables).
Five9 sends the unhyphenated `X-CallID` and `X-CallANI`, which normalize to `sip_callid` and
`sip_callani` instead. Confirm which variables are populated during test calls before referencing
them in prompts.

## Headers returned from ElevenLabs to Five9

ElevenLabs returns routing and reporting data on the SIP BYE. The following header names are the recommended convention for Five9 AI Agent Connect:

| Header             | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| `X-RouteType`      | The action Five9 should take, for example `SkillTransfer`.       |
| `X-RouteValue`     | The target for the action, for example a Five9 skill name.       |
| `X-RouteReason`    | Context for the routing decision, such as the customer's intent. |
| `X-ConversationId` | The ElevenLabs conversation identifier, for log correlation.     |

You can return any additional `X-` header your Five9 flow needs. Each header value comes from a dynamic variable on the agent, so the agent must set these variables during the conversation.

## Configuring BYE headers

BYE headers return the final values of the agent's dynamic variables to Five9. Map each dynamic variable name to a header name using `attributes_to_headers` on the phone number's `inbound_trunk_config`. Both variables your agent sets and [system dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables#system-dynamic-variables) such as `system__conversation_id` can be mapped:

```python title="Python"
import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, InboundSipTrunkConfigRequestModel

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

elevenlabs.conversational_ai.phone_numbers.update(
    phone_number_id="phnum_8901k4t9z5defmb8vh3e9361y7nj",
    inbound_trunk_config=InboundSipTrunkConfigRequestModel(
        attributes_to_headers={
            "route_type": "X-RouteType",
            "route_value": "X-RouteValue",
            "route_reason": "X-RouteReason",
            "system__conversation_id": "X-ConversationId",
        }
    ),
)
```

```typescript title="JavaScript"
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

await elevenlabs.conversationalAi.phoneNumbers.update("phnum_8901k4t9z5defmb8vh3e9361y7nj", {
  inboundTrunkConfig: {
    attributesToHeaders: {
      route_type: "X-RouteType",
      route_value: "X-RouteValue",
      route_reason: "X-RouteReason",
      system__conversation_id: "X-ConversationId",
    },
  },
});
```

```bash title="cURL"
curl -X PATCH "https://api.elevenlabs.io/v1/convai/phone-numbers/phnum_8901k4t9z5defmb8vh3e9361y7nj" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "inbound_trunk_config": {
      "attributes_to_headers": {
        "route_type": "X-RouteType",
        "route_value": "X-RouteValue",
        "route_reason": "X-RouteReason",
        "system__conversation_id": "X-ConversationId"
      }
    }
  }'
```

The header value is the dynamic variable's value at the end of the conversation, including values set during the call through agent tools or webhook overrides. A call that ends with the agent setting `route_type` to `SkillTransfer` and `route_value` to `billing_support` produces the following BYE headers:

```
X-RouteType: SkillTransfer
X-RouteValue: billing_support
X-RouteReason: Customer needs help with an invoice
X-ConversationId: conv_7401k6a2b8cxyzmn9pq3r5s7t1uv
```

Five9 then routes the caller to the `billing_support` skill.

## Recommended routing values

Keep `X-RouteType` values simple and predictable so the Five9 flow can branch on them directly.

| `X-RouteType`     | Example `X-RouteValue` | Description                                        |
| ----------------- | ---------------------- | -------------------------------------------------- |
| `SkillTransfer`   | `billing_support`      | Transfer the call to a specific Five9 skill queue. |
| `PhoneTransfer`   | `+18005550199`         | Transfer the call to an external phone number.     |
| `Hangup`          | Empty                  | Terminate the call after the AI interaction.       |
| `DispositionOnly` | `Resolved`             | End the call and record a specific disposition.    |

## Five9 setup

Your Five9 implementation team will typically:

1. Enable AI Agent Connect for your Five9 domain.
2. Configure the Five9 IVR transfer flow.
3. Add the ElevenLabs phone number as the transfer destination.
4. Configure the External Transfer Module.
5. Configure the outbound `X-` headers sent to ElevenLabs.
6. Configure the inbound `X-` headers returned by ElevenLabs.
7. Map the returned headers into Five9 call variables.
8. Configure the post-AI routing logic that branches on those variables.
9. Test calls end to end.

## Troubleshooting

#### Transferred calls fail to connect

* Confirm the ElevenLabs phone number is imported as a SIP trunk number and has an agent assigned.
* Verify the transfer destination configured in the Five9 External Transfer Module matches the imported number.
* Check that your firewall allows SIP signaling traffic on the configured transport and port, and that RTP ports are not blocked.

#### Inbound headers are not available as dynamic variables

* Confirm Five9 sends the headers with an `X-` prefix on the INVITE.
* Check the normalized variable name. `X-AgentID` becomes `{{sip_agentid}}`, not `{{X-AgentID}}` or `{{agent_id}}`.
* Inspect the conversation history under the **Phone Call** tab to see which headers arrived.
* Custom headers cannot override the `system__call_sid` and `system__caller_id` system variables.

#### BYE headers are missing or empty

* Verify `attributes_to_headers` is set on `inbound_trunk_config` for the phone number receiving the call.
* Confirm the keys are dynamic variable names and the values are header names, not the reverse.
* Ensure the agent actually sets those dynamic variables during the conversation. An unset variable produces no header value.

#### Router agent transfers to the wrong agent

* Confirm Five9 sends `X-AgentID` on every transferred call.
* Check that each `X-AgentID` value has a matching transfer rule on the router agent.
* Verify the router agent's transfer rules reference `{{sip_agentid}}`.

## Useful links

* [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking)
* [SIP reference](/docs/eleven-agents/phone-numbers/sip-reference)
* [Agent transfer tool](/docs/eleven-agents/customization/tools/system-tools/agent-transfer)
* [Dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables)
* [Update phone number API reference](/docs/api-reference/phone-numbers/update)
