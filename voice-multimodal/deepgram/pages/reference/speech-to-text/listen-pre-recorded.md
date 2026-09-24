---
title: "Pre-Recorded Audio"
source: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded.md
path: reference/speech-to-text/listen-pre-recorded
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Pre-Recorded Audio

POST https://api.deepgram.com/v1/listen
Content-Type: application/json

Transcribe audio and video using Deepgram's speech-to-text REST API

Reference: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`
- `Authorization` header (bearer token, required) — Use `Authorization: Bearer <JWT>` Example: `Authorization: Bearer eyJhbGciOiJ...`

## Request

### Query parameters

- `callback` (string, optional) — URL to which we'll make the callback request
- `callback_method` (enum, optional, default: POST) — HTTP method by which the callback request will be made
  - Allowed values: `POST`, `PUT`
- `extra` (V1ListenPostParametersExtra, optional) — Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
- `sentiment` (boolean, optional, default: false) — Recognizes the sentiment throughout a transcript or text
- `summarize` (V1ListenPostParametersSummarize, optional) — Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only.
- `tag` (V1ListenPostParametersTag, optional) — Label your requests for the purpose of identification during usage reporting
- `topics` (boolean, optional, default: false) — Detect topics throughout a transcript or text
- `custom_topic` (V1ListenPostParametersCustomTopic, optional) — Custom topics you want the model to detect within your input audio or text if present Submit up to `100`.
- `custom_topic_mode` (enum, optional, default: extended) — Sets how the model will interpret strings submitted to the `custom_topic` param. When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param
  - Allowed values: `extended`, `strict`
- `intents` (boolean, optional, default: false) — Recognizes speaker intent throughout a transcript or text
- `custom_intent` (V1ListenPostParametersCustomIntent, optional) — Custom intents you want the model to detect within your input audio if present
- `custom_intent_mode` (enum, optional, default: extended) — Sets how the model will interpret intents submitted to the `custom_intent` param. When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in the `custom_intent` param.
  - Allowed values: `extended`, `strict`
- `detect_entities` (boolean, optional, default: false) — Identifies and extracts key entities from content in submitted audio
- `detect_language` (V1ListenPostParametersDetectLanguage, optional) — Identifies the dominant language spoken in submitted audio
- `diarize` (boolean, optional, default: false, deprecated) — Deprecated: use `diarize_model` instead. Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0.
- `diarize_model` (enum, optional) — Select and enable a specific diarization model version. Specifying this parameter enables diarization and selects the model — you do not need to also set the deprecated `diarize=true` parameter. For batch, supported values are `latest` (currently v2), `v1`, and `v2`. For streaming, supported values are `latest` (currently v1) and `v1`; `v2` returns a validation error on streaming requests.
  - Allowed values: `latest`, `v1`, `v2`
- `dictation` (boolean, optional, default: false) — Dictation mode for controlling formatting with dictated speech
- `encoding` (enum, optional) — Specify the expected encoding of your submitted audio
  - Allowed values: `linear16`, `flac`, `mulaw`, `amr-nb`, `amr-wb`, `opus`, `speex`, `g729`
- `filler_words` (boolean, optional, default: false) — Filler Words can help transcribe interruptions in your audio, like "uh" and "um"
- `keyterm` (list of string, optional) — Key term prompting improves recognition of specialized terminology and brands. Only compatible with Nova-3. `keyterm` accepts plain terms only. Unlike the legacy `keywords` feature, it does not support weights or intensifiers. Appending one (for example, `keyterm=term:0.15`) is not rejected—the weight is silently ignored and the entire value is treated as a literal keyterm. To boost multiple separate keyterms, repeat the `keyterm` parameter (for example, `keyterm=term1&keyterm=term2`). To boost one multi-word phrase as a single keyterm, join the words with `%20` or `+` (for example, `keyterm=customer%20service`). Do not separate keyterms with commas, semicolons, or line breaks.
- `keywords` (V1ListenPostParametersKeywords, optional) — Keywords can boost or suppress specialized terminology and brands. `keywords` is not supported with Nova-3 models; use `keyterm` instead.
- `language` (string, optional, default: en) — The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available
- `measurements` (boolean, optional, default: false) — Spoken measurements will be converted to their corresponding abbreviations
- `model` (V1ListenPostParametersModel, optional, default: base-general) — AI model used to process submitted audio
- `multichannel` (boolean, optional, default: false) — Transcribe each audio channel independently
- `numerals` (boolean, optional, default: false) — Numerals converts numbers from written format to numerical format
- `paragraphs` (boolean, optional, default: false) — Splits audio into paragraphs to improve transcript readability
- `profanity_filter` (boolean, optional, default: false) — Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely
- `punctuate` (boolean, optional, default: false) — Add punctuation and capitalization to the transcript
- `redact` (V1ListenPostParametersRedact, optional, default: false) — Redaction removes sensitive information from your transcripts
- `replace` (V1ListenPostParametersReplace, optional) — Search for terms or phrases in submitted audio and replaces them
- `search` (V1ListenPostParametersSearch, optional) — Search for terms or phrases in submitted audio
- `smart_format` (boolean, optional, default: false) — Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability
- `utterances` (boolean, optional, default: false) — Segments speech into meaningful semantic units
- `utt_split` (double, optional, default: 0.8) — Seconds to wait before detecting a pause between words in submitted audio
- `version` (V1ListenPostParametersVersion, optional, default: latest) — Version of an AI model to use
- `mip_opt_out` (boolean, optional, default: false) — Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip

### Body (application/json)

This endpoint expects a ListenV1RequestUrl.

- `url` (string, required)

## Response

### 200

Returns either transcription results, or a request_id when using a callback.

- `listen_v1_media_transcribe_Response_200`

## Errors

### 400 Bad Request Error

Invalid Request

- `metadata` (ListenV1ResponseMetadata, required)
- `results` (ListenV1ResponseResults, required)

## Types

### V1ListenPostParametersExtra

### V1ListenPostParametersSummarize

### V1ListenPostParametersTag

### V1ListenPostParametersCustomTopic

### V1ListenPostParametersCustomIntent

### V1ListenPostParametersDetectLanguage

### V1ListenPostParametersKeywords

### V1ListenPostParametersModel

### V1ListenPostParametersRedact

### V1ListenPostParametersReplace

### V1ListenPostParametersSearch

### V1ListenPostParametersVersion

### ListenV1Response

The standard transcription response

- `metadata` (ListenV1ResponseMetadata, required)
- `results` (ListenV1ResponseResults, required)

### ListenV1AcceptedResponse

Accepted response for asynchronous transcription requests

- `request_id` (string, required) — Unique identifier for tracking the asynchronous request

### ListenV1ResponseMetadata

- `request_id` (string, required)
- `sha256` (string, required)
- `created` (string, required)
- `duration` (double, required)
- `channels` (integer, required)
- `models` (list of string, required)
- `model_info` (ListenV1ResponseMetadataModelInfo, required)
- `diarize_info` (ListenV1ResponseMetadataDiarizeInfo, optional) — The diarizer that produced the speaker labels. Present only when a diarizer ran.
- `summary_info` (ListenV1ResponseMetadataSummaryInfo, optional)
- `sentiment_info` (ListenV1ResponseMetadataSentimentInfo, optional)
- `topics_info` (ListenV1ResponseMetadataTopicsInfo, optional)
- `intents_info` (ListenV1ResponseMetadataIntentsInfo, optional)
- `tags` (list of string, optional)
- `transaction_key` (string, optional, default: deprecated, deprecated)

### ListenV1ResponseResults

- `channels` (list of ListenV1ResponseResultsChannelsItems, required)
- `utterances` (list of ListenV1ResponseResultsUtterancesItems, optional)
- `summary` (ListenV1ResponseResultsSummary, optional)
- `topics` (SharedTopics, optional) — Output whenever `topics=true` is used
- `intents` (SharedIntents, optional) — Output whenever `intents=true` is used
- `sentiments` (SharedSentiments, optional) — Output whenever `sentiment=true` is used

### ListenV1ResponseMetadataModelInfo

### ListenV1ResponseMetadataDiarizeInfo

The diarizer that produced the speaker labels. Present only when a diarizer ran.

- `model_uuid` (string, required) — The diarizer model UUID
- `arch` (string, required) — The diarizer arch, such as `v1` or `v2`

### ListenV1ResponseMetadataSummaryInfo

- `model_uuid` (string, optional)
- `input_tokens` (integer, optional)
- `output_tokens` (integer, optional)

### ListenV1ResponseMetadataSentimentInfo

- `model_uuid` (string, optional)
- `input_tokens` (integer, optional)
- `output_tokens` (integer, optional)

### ListenV1ResponseMetadataTopicsInfo

- `model_uuid` (string, optional)
- `input_tokens` (integer, optional)
- `output_tokens` (integer, optional)

### ListenV1ResponseMetadataIntentsInfo

- `model_uuid` (string, optional)
- `input_tokens` (integer, optional)
- `output_tokens` (integer, optional)

### ListenV1ResponseResultsChannelsItems

- `search` (list of ListenV1ResponseResultsChannelsItemsSearchItems, optional)
- `alternatives` (list of ListenV1ResponseResultsChannelsItemsAlternativesItems, optional)
- `detected_language` (string, optional)

### ListenV1ResponseResultsUtterancesItems

- `start` (float, optional)
- `end` (float, optional)
- `confidence` (float, optional)
- `channel` (integer, optional)
- `transcript` (string, optional)
- `words` (list of ListenV1ResponseResultsUtterancesItemsWordsItems, optional)
- `speaker` (integer, optional)
- `id` (string, optional)

### ListenV1ResponseResultsSummary

- `result` (string, optional)
- `short` (string, optional)

### SharedTopics

Output whenever `topics=true` is used

- `results` (SharedTopicsResults, optional)

### SharedIntents

Output whenever `intents=true` is used

- `results` (SharedIntentsResults, optional)

### SharedSentiments

Output whenever `sentiment=true` is used

- `segments` (list of SharedSentimentsSegmentsItems, optional)
- `average` (SharedSentimentsAverage, optional)

### ListenV1ResponseResultsChannelsItemsSearchItems

- `query` (string, optional)
- `hits` (list of ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItems

- `transcript` (string, optional)
- `confidence` (float, optional)
- `words` (list of ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems, optional)
- `paragraphs` (ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs, optional)
- `entities` (list of ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems, optional)
- `summaries` (list of ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems, optional)
- `topics` (list of ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems, optional)

### ListenV1ResponseResultsUtterancesItemsWordsItems

- `word` (string, optional)
- `start` (float, optional)
- `end` (float, optional)
- `confidence` (float, optional)
- `speaker` (integer, optional)
- `speaker_confidence` (float, optional)
- `punctuated_word` (string, optional)

### SharedTopicsResults

- `topics` (SharedTopicsResultsTopics, optional)

### SharedIntentsResults

- `intents` (SharedIntentsResultsIntents, optional)

### SharedSentimentsSegmentsItems

- `text` (string, optional)
- `start_word` (double, optional)
- `end_word` (double, optional)
- `sentiment` (string, optional)
- `sentiment_score` (double, optional)

### SharedSentimentsAverage

- `sentiment` (string, optional)
- `sentiment_score` (double, optional)

### ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems

- `confidence` (float, optional)
- `start` (float, optional)
- `end` (float, optional)
- `snippet` (string, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems

- `word` (string, optional)
- `start` (float, optional)
- `end` (float, optional)
- `confidence` (float, optional)
- `speaker` (integer, optional) — The speaker of the word, present when diarization is enabled
- `speaker_confidence` (float, optional) — Confidence in the speaker assignment. Returned only for pre-recorded diarization; not available for streaming

### ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs

- `transcript` (string, optional)
- `paragraphs` (list of ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems

- `label` (string, optional)
- `value` (string, optional)
- `raw_value` (string, optional)
- `confidence` (float, optional)
- `start_word` (float, optional)
- `end_word` (float, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems

- `summary` (string, optional)
- `start_word` (float, optional)
- `end_word` (float, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems

- `text` (string, optional)
- `start_word` (float, optional)
- `end_word` (float, optional)
- `topics` (list of string, optional)

### SharedTopicsResultsTopics

- `segments` (list of SharedTopicsResultsTopicsSegmentsItems, optional)

### SharedIntentsResultsIntents

- `segments` (list of SharedIntentsResultsIntentsSegmentsItems, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems

- `sentences` (list of ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems, optional)
- `speaker` (integer, optional)
- `num_words` (integer, optional)
- `start` (float, optional)
- `end` (float, optional)

### SharedTopicsResultsTopicsSegmentsItems

- `text` (string, optional)
- `start_word` (double, optional)
- `end_word` (double, optional)
- `topics` (list of SharedTopicsResultsTopicsSegmentsItemsTopicsItems, optional)

### SharedIntentsResultsIntentsSegmentsItems

- `text` (string, optional)
- `start_word` (double, optional)
- `end_word` (double, optional)
- `intents` (list of SharedIntentsResultsIntentsSegmentsItemsIntentsItems, optional)

### ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems

- `text` (string, optional)
- `start` (float, optional)
- `end` (float, optional)

### SharedTopicsResultsTopicsSegmentsItemsTopicsItems

- `topic` (string, optional)
- `confidence_score` (float, optional)

### SharedIntentsResultsIntentsSegmentsItemsIntentsItems

- `intent` (string, optional)
- `confidence_score` (float, optional)

## Examples

### Remote File

**Request**

```json
{
  "url": "https://dpgr.am/spacewalk.wav"
}
```

**Response**

```json
{
  "metadata": {
    "channels": 1,
    "created": "2024-05-12T18:57:13.426Z",
    "diarize_info": {
      "arch": "v2",
      "model_uuid": "9a1c8b3e-2f44-4c8a-b1d0-example0000"
    },
    "duration": 25.933313,
    "model_info": {
      "30089e05-99d1-4376-b32e-c263170674af": {
        "arch": "nova-2",
        "name": "2-general-nova",
        "version": "2024-01-09.29447"
      }
    },
    "models": [
      "30089e05-99d1-4376-b32e-c263170674af"
    ],
    "request_id": "a847f427-4ad5-4d67-9b95-db801e58251c",
    "sha256": "154e291ecfa8be6ab8343560bcc109008fa7853eb5372533e8efdefc9b504c33"
  },
  "results": {
    "channels": [
      {
        "alternatives": [
          {
            "confidence": 0.9840088,
            "transcript": "Yeah, as as much as, it's worth having a talk to the neighbors.",
            "words": [
              {
                "confidence": 0.9975586,
                "end": 0.32,
                "speaker": 0,
                "speaker_confidence": 0.98,
                "start": 0.08,
                "word": "yeah"
              },
              {
                "confidence": 0.9862061,
                "end": 0.48,
                "speaker": 0,
                "speaker_confidence": 0.98,
                "start": 0.32,
                "word": "as"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

**SDK Code**

```python Remote File
import requests

url = "https://api.deepgram.com/v1/listen"

payload = { "url": "https://dpgr.am/spacewalk.wav" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript Remote File
const url = 'https://api.deepgram.com/v1/listen';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"url":"https://dpgr.am/spacewalk.wav"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Remote File
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v1/listen"

	payload := strings.NewReader("{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Remote File
require 'uri'
require 'net/http'

url = URI("https://api.deepgram.com/v1/listen")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}"

response = http.request(request)
puts response.read_body
```

```java Remote File
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/listen")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}")
  .asString();
```

```php Remote File
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/listen', [
  'body' => '{
  "url": "https://dpgr.am/spacewalk.wav"
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Remote File
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/listen");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://dpgr.am/spacewalk.wav\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Remote File
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["url": "https://dpgr.am/spacewalk.wav"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/listen")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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

### Local File

**SDK Code**

```python Local File
import requests

url = "https://api.deepgram.com/v1/listen"

headers = {"Authorization": "Token <apiKey>"}

response = requests.post(url, headers=headers)

print(response.json())
```

```javascript Local File
const url = 'https://api.deepgram.com/v1/listen';
const options = {method: 'POST', headers: {Authorization: 'Token <apiKey>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Local File
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v1/listen"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Authorization", "Token <apiKey>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Local File
require 'uri'
require 'net/http'

url = URI("https://api.deepgram.com/v1/listen")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'

response = http.request(request)
puts response.read_body
```

```java Local File
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/listen")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php Local File
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/listen', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp Local File
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/listen");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift Local File
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/listen")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers

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
