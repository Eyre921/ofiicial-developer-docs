---
title: "Stop campaign"
source: https://elevenlabs.io/docs/api-reference/campaigns/stop.md
path: docs/api-reference/campaigns/stop
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Stop campaign

POST https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/{campaign_id}/stop

Stop an outbound campaign for good: queued calls are cancelled and no lead is called again. Returns `202` with the campaign `stopping` while calls already placed are still finishing.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/stop

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `campaign_id` (string, required)

## Response

### 200

Successful Response

- `campaign_id` (string, required)
- `call_name` (string, required) — The campaign's name.
- `agent_id` (string, required)
- `channel_config` (CampaignResponseChannelConfig, required)
- `status` (enum, required) — `attention` means an open attention item holds back some of the campaign's calls while the rest go ahead. `stopping` means queued calls are cancelled and calls already placed are finishing.
  - Allowed values: `active`, `paused`, `stopping`, `stopped`, `completed`, `failed`, `attention`
- `policy` (CampaignPolicySnapshot, required) — The policy the campaign took when it was created.
- `variant` (enum, required)
  - Allowed values: `simple`, `advanced`
- `source` (enum, required, nullable) — Whether the campaign was created in the app or through the API.
  - Allowed values: `ui`, `api`
- `outcome` (CampaignResponseOutcome, required, nullable) — The result that counts as success for the campaign's calls.
- `created_at_unix` (integer, required)
- `scheduled_time_unix` (integer, required, nullable) — When the campaign starts calling; unset to start once created.
- `updated_at_unix` (integer, required)
- `branch_id` (string, required, nullable) — The agent branch the campaign calls with.
- `environment` (string, required, nullable) — The environment the agent's environment variables resolve in.
- `target_concurrency_limit` (integer, required, nullable) — The most calls the campaign places at once.
- `channel` (enum, required)
  - Allowed values: `phone`, `whatsapp`
- `mode` (enum, required)
  - Allowed values: `voice`, `message`
- `counts` (CampaignSummaryCounts, required)
- `agent_name` (string, required, default: )

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### CampaignResponseChannelConfig

- `channel`: `phone` (PhoneChannelConfig)
  - `agent_phone_number_id` (string, required) — The phone number to call from.
  - `mode_config` (PhoneVoiceConfig-Output, optional)
- `channel`: `whatsapp` (WhatsAppChannelConfig)
  - `mode_config` (WhatsAppChannelConfigModeConfig, required)
  - `whatsapp_phone_number_id` (string, required) — The WhatsApp phone number to call or message from.

### CampaignPolicySnapshot

The policy the campaign took when it was created, laid out like a submitted `policy`.

- `timezone` (string, required)
- `retry` (RetryPolicy, required)
- `calling_periods` (list of CallingPeriodPolicy, required)
- `data_collection` (DataCollectionPolicy, required)
- `followup_context` (FollowupContextPolicy, required) — Which `campaign__` dynamic variables follow-up calls get.

### CampaignResponseOutcome

The result that counts as success for the campaign's calls.

- `type`: `data_collection` (DataCollectionOutcome)
  - `data_collection_id` (string, required) — The agent's data collection item a successful call sets.
  - `equals` (list of CampaignResponseOutcomeDiscriminatorMappingDataCollectionEqualsItems, required) — Values that count as success, all of the item's type.
- `type`: `evaluation_criteria` (EvaluationCriterionOutcome)
  - `criteria_id` (string, required) — The agent's evaluation criterion a successful call meets.

### CampaignSummaryCounts

- `leads` (integer, required)
- `terminal_leads` (integer, required) — Leads that won't be called again.
- `open_attention` (integer, required) — Attention items not yet resolved.
- `delivery` (RecipientDeliveryCounts, optional, nullable) — How many messages reached each stage; set when getting one message campaign.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### PhoneVoiceConfig-Output

- `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
- `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `twilio_machine_detection` (TwilioMachineDetectionConfig, optional, nullable) — Configuration for Twilio's carrier-level answering machine detection (AMD). Omit or set to null to disable it. Ignored for non-Twilio providers and for inbound calls. The resulting verdict is delivered as its own `answering_machine_detection` webhook event, which requires that event to be enabled on the workspace or agent webhook settings; it is not part of the conversation or the post-call webhook. Detection runs asynchronously so it never delays the start of the conversation, and the verdict can arrive at any point during the call -- with `detect_message_end`, even after it has ended. Twilio bills separately for AMD.
- `mode` ("voice", optional, default: voice)

### WhatsAppChannelConfigModeConfig

- `mode`: `message` (WhatsAppMessageConfig)
  - `template` (WhatsAppTemplate, required) — The Meta template as it was approved at submission.
- `mode`: `voice` (WhatsAppVoiceConfig)
  - `whatsapp_call_permission_request_template_language_code` (string, required) — The language code of that template.
  - `whatsapp_call_permission_request_template_name` (string, required) — The approved template that asks the contact for permission to call.

### RetryPolicy

- `retry_delay_seconds` (integer, optional, default: 600) — How long to wait before a short retry.
- `max_short_retries` (integer, optional, default: 1) — Retries a calling window allows after a failed call. Once used up, the next retry waits for the following window, which starts afresh.
- `max_total_calls` (integer, optional, default: 6) — The most calls a lead gets, counting the first.
- `max_callbacks` (integer, optional, default: 2) — The most callbacks to honor for one number.
- `max_redirects` (integer, optional, default: 2) — The most times a lead follows a request to call another number.
- `interval_placement` (enum, optional, default: start) — Where in a later calling window a pushed-back call lands: at its `start`, at a `random` time, or `rotate`d `rotate_step_seconds` past where the last call in that window failed.
  - Allowed values: `start`, `random`, `rotate`
- `rotate_step_seconds` (integer, optional, default: 900) — How far `rotate` placement moves each call. Only used by `rotate`.
- `max_consecutive_failures_per_number` (integer, optional, nullable) — Calls to one number that may fail in a row before the lead moves on to its next listed number, or ends when there is none. An answered call, or a redirect to a new number, restarts the count. Unset leaves only `max_total_calls`.

### CallingPeriodPolicy

- `weekdays` (list of integer, required)
- `intervals` (list of CallingIntervalPolicy, required) — Windows on each of those days. They may not overlap on any day.

### DataCollectionPolicy

- `callback_time` (string, optional, nullable)
- `redirect_phone_number` (string, optional, nullable)
- `stop` (string, optional, nullable)
- `mappings` (map from string to string, optional) — Copies data collection results into dynamic variables for later calls: each key is a data collection item ID and its value the variable's name.

### FollowupContextPolicy

Which `campaign__` dynamic variables follow-up calls get.

- `call_type` (boolean, optional, default: true) — Pass the call type as `campaign__call_type`.
- `previous_conversation_id` (boolean, optional, default: true) — Pass the last conversation's ID as `campaign__previous_conversation_id`.
- `previous_summary` (boolean, optional, default: true) — Pass the last conversation's summary as `campaign__previous_summary`.
- `previous_transcript` (boolean, optional, default: true) — Pass the last conversation's transcript as `campaign__previous_transcript`.

### CampaignResponseOutcomeDiscriminatorMappingDataCollectionEqualsItems

- string
- integer
- double
- boolean

### RecipientDeliveryCounts

- `sent` (integer, optional, default: 0)
- `delivered` (integer, optional, default: 0)
- `read` (integer, optional, default: 0)
- `replied` (integer, optional, default: 0)
- `failed` (integer, optional, default: 0)

### ValidationErrorLocItems

- string
- integer

### TwilioMachineDetectionConfig

How to run Twilio's carrier-level answering machine detection (AMD) on a call.

- `mode` (enum, optional, default: enable) — How thorough the detection should be. `enable` returns a verdict as soon as Twilio can tell a human from a machine. `detect_message_end` also waits for the voicemail greeting to finish, which is what produces the `machine_end_*` verdicts, but returns a result later.
  - Allowed values: `enable`, `detect_message_end`
- `actions` (list of TwilioMachineDetectionRule, optional) — Actions to take on the call per AMD verdict. Each action can appear in at most one rule, so list all of its verdicts together. Verdicts without a rule leave the call running.

### WhatsAppTemplate

- `name` (string, required)
- `language` (string, required) — https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/supported-languages
- `components` (list of WhatsAppTemplateComponent, required)
- `parameter_format` (enum, optional, default: POSITIONAL)
  - Allowed values: `POSITIONAL`, `NAMED`
- `category` (string, optional, nullable) — https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

### CallingIntervalPolicy

- `start` (string, required) — Local start time, as `HH:MM`.
- `end` (string, required) — Local end time, as `HH:MM`; `24:00` ends at midnight.

### TwilioMachineDetectionRule

Action to take on a live call for the given AMD verdicts.

- `action` (enum, required)
  - Allowed values: `hang_up`
- `answered_by` (list of enum, required) — Verdicts that trigger the action.
  - Allowed values: `human`, `fax`, `unknown`, `machine_start`, `machine_end_beep`, `machine_end_silence`, `machine_end_other`

### WhatsAppTemplateComponent

- `type` (string, required)
- `format` (string, optional, nullable)
- `text` (string, optional, nullable)
- `buttons` (list of WhatsAppTemplateComponentButton, optional, nullable)

### WhatsAppTemplateComponentButton

- `type` (string, required)
- `text` (string, optional, nullable)
- `url` (string, optional, nullable)

## Examples

**Response**

```json
{
  "campaign_id": "string",
  "call_name": "string",
  "agent_id": "string",
  "channel_config": {
    "channel": "phone",
    "agent_phone_number_id": "string",
    "mode_config": {
      "ringing_timeout_secs": 60,
      "twilio_call_recording_enabled": false,
      "twilio_machine_detection": {
        "mode": "enable",
        "actions": [
          {
            "action": "hang_up",
            "answered_by": [
              "human"
            ]
          }
        ]
      },
      "mode": "voice"
    }
  },
  "status": "active",
  "policy": {
    "timezone": "string",
    "retry": {
      "retry_delay_seconds": 600,
      "max_short_retries": 1,
      "max_total_calls": 6,
      "max_callbacks": 2,
      "max_redirects": 2,
      "interval_placement": "start",
      "rotate_step_seconds": 900,
      "max_consecutive_failures_per_number": 1
    },
    "calling_periods": [
      {
        "weekdays": [
          1
        ],
        "intervals": [
          {
            "start": "string",
            "end": "string"
          }
        ]
      }
    ],
    "data_collection": {
      "callback_time": "string",
      "redirect_phone_number": "string",
      "stop": "string",
      "mappings": {}
    },
    "followup_context": {
      "call_type": true,
      "previous_conversation_id": true,
      "previous_summary": true,
      "previous_transcript": true
    }
  },
  "variant": "simple",
  "source": "ui",
  "outcome": {
    "type": "evaluation_criteria",
    "criteria_id": "string"
  },
  "created_at_unix": 1,
  "scheduled_time_unix": 1,
  "updated_at_unix": 1,
  "branch_id": "string",
  "environment": "string",
  "target_concurrency_limit": 1,
  "channel": "phone",
  "mode": "voice",
  "counts": {
    "leads": 1,
    "terminal_leads": 1,
    "open_attention": 1,
    "delivery": {
      "sent": 0,
      "delivered": 0,
      "read": 0,
      "replied": 0,
      "failed": 0
    }
  },
  "agent_name": ""
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop"

response = requests.post(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop';
const options = {method: 'POST'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/stop")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
