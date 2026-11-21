---
title: "AWS Marketplace (x402) and Deepgram"
source: https://developers.deepgram.com/docs/aws-marketplace-x402.md
path: docs/aws-marketplace-x402
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# AWS Marketplace (x402) and Deepgram

> Pay for Deepgram Nova-3, Flux TTS, and Aura-2 per request with x402 and Amazon Bedrock AgentCore payments, billed through AWS Marketplace. No Deepgram API key needed.

Agents can buy Deepgram Nova-3 speech-to-text and Deepgram Flux TTS and Aura-2 text-to-speech one request at a time, with no contract or Deepgram API key to manage. An agent calls `https://x402.deepgram.com`, pays each request's price quote with [Amazon Bedrock AgentCore payments](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html), and gets the result. Charges are billed in USD to your AWS account under AWS Marketplace.

#### [Example code](https://github.com/deepgram-devs/deepgram-agentcore-payments-examples)

Runnable Python (boto3, Strands, LangGraph) and TypeScript examples, plus a one-time AWS account setup script.

## How to pay with AgentCore payments

The endpoints are sold pay-per-request through AWS Marketplace using [x402](https://www.x402.org/). To call them, set up [AgentCore payments](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-how-it-works.html) in your AWS account: a Payment Manager with an AWS Billing connector, and a payment session with a spend limit. Your agent uses it to obtain the AWS Marketplace payment token.

1. Send your request to one of the endpoints below. The API returns HTTP `402 Payment Required`. The `PAYMENT-REQUIRED` header (base64 JSON) holds an AWS Marketplace x402 price quote: the `accepts` entry with `network` `aws:base`, whose `extra.quoteToken` is the signed quote.
2. Pass that `accepts` entry, unchanged, to AgentCore payments [`ProcessPayment`](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-process-payment.html#payments-process-payment-aws-billing) with `paymentType` `AWS_BILLING_X402`. It returns a payment token.
3. Retry the same request with the payment token in the `PAYMENT-SIGNATURE` header, plus a `DPoP` header if you bound the token to a key.
4. A successful call returns `200` with your result. The `PAYMENT-RESPONSE` header contains your AWS Marketplace payment ID.

> **Note**
>
> The AgentCore payments plugins for Strands Agents and LangGraph currently handle stablecoin (`CRYPTO_X402`) payments only. To pay AWS Marketplace quotes from those frameworks, call `ProcessPayment` from a tool, as the [examples](https://github.com/deepgram-devs/deepgram-agentcore-payments-examples) do.

## How to call the x402 endpoints

Three batch endpoints, all `POST` and priced per request. Rates follow [Deepgram pricing](https://deepgram.com/pricing), and the `402` quote states the exact USD price of each request. Streaming (WebSocket) endpoints aren't available through AWS Marketplace.

### Speech-to-text

**Endpoint:** `POST https://x402.deepgram.com/v1/listen`

* **Price:** Deepgram's [pay-as-you-go pre-recorded rates](https://deepgram.com/pricing) for Deepgram Nova-3 (monolingual, or multilingual with `language=multi`), plus any add-ons you use (`keyterm`, `redact`, `detect_entities`).
* **Query parameters:** Deepgram [`/v1/listen`](/reference/speech-to-text/listen-pre-recorded) parameters, e.g. `model=nova-3`, `language`, `smart_format=true`, `diarize=true`. `callback` isn't supported; results are returned synchronously.
* **Body, hosted audio (recommended, any length):** `Content-Type: application/json`, `{"url": "https://..."}`. The URL must be fetchable by the API, e.g. an [S3 presigned URL](/docs/using-aws-s3-presigned-urls-with-the-deepgram-api).
* **Body, raw audio up to \~4.5 MB:** `Content-Type: audio/wav` (or `audio/mpeg`, `audio/flac`, `audio/ogg`), body = audio bytes.
* **Response:** Deepgram transcript JSON.

```bash
curl -i -X POST "https://x402.deepgram.com/v1/listen?model=nova-3&smart_format=true" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://dpgr.am/spacewalk.wav"}'
# -> 402 with PAYMENT-REQUIRED. Pay it, then repeat the same request with a
# PAYMENT-SIGNATURE header (plus a DPoP header if your payment token is DPoP-bound).
```

### Text-to-speech: Flux TTS (recommended)

**Endpoint:** `POST https://x402.deepgram.com/v2/speak`

* **Price:** Deepgram's [pay-as-you-go Flux TTS rate](https://deepgram.com/pricing), per 1,000 input characters.
* **Query parameters:** `model` (required; a Flux TTS voice `flux-{voice}-{language}`, e.g. `flux-haley-en`), optional `encoding` (`mp3` default, `opus`, `flac`, `aac`, `linear16`, `mulaw`, `alaw`), `sample_rate`, `container`, `bit_rate`, `speed`.
* **Body:** `Content-Type: application/json`, `{"text": "..."}`.
* **Response:** audio bytes (MP3 by default).

```bash
# -D - prints the headers (including PAYMENT-REQUIRED) to the terminal; only the body goes to hello.mp3.
curl -D - -X POST "https://x402.deepgram.com/v2/speak?model=flux-haley-en" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your appointment is confirmed for 3pm tomorrow."}' -o hello.mp3
```

### Text-to-speech: Aura-2

**Endpoint:** `POST https://x402.deepgram.com/v1/speak`

* **Price:** Deepgram's [pay-as-you-go Aura-2 rate](https://deepgram.com/pricing), per 1,000 input characters.
* **Query parameters:** `model` (an `aura-2` voice, e.g. `aura-2-thalia-en`), optional `encoding`, `sample_rate`, `container`.
* **Body:** `Content-Type: application/json`, `{"text": "..."}`.
* **Response:** audio bytes (MP3 by default).

```bash
curl -D - -X POST "https://x402.deepgram.com/v1/speak?model=aura-2-thalia-en" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from Deepgram."}' -o hello.mp3
```

## Paying a quote in Python

This sample shows the core of the flow with boto3 1.44.7 or later (`pip install boto3 requests`). `PAYMENT_MANAGER_ARN`, `PAYMENT_SESSION_ID`, and `USER_ID` are placeholders for a Payment Manager with an AWS Billing connector and a payment session created for that user. The [examples repo](https://github.com/deepgram-devs/deepgram-agentcore-payments-examples) has a setup script for both, and its [client](https://github.com/deepgram-devs/deepgram-agentcore-payments-examples/blob/main/python/deepgram_x402.py) adds DPoP and error handling.

```python
import base64, json, uuid
import boto3, requests

URL = "https://x402.deepgram.com/v1/speak?model=aura-2-thalia-en"
BODY = {"text": "Hello from Deepgram."}

# No status checks here: see the examples client for 402/200 handling.
first = requests.post(URL, json=BODY)  # 402
required = json.loads(base64.b64decode(first.headers["PAYMENT-REQUIRED"]))
accepted = next(a for a in required["accepts"] if a["network"] == "aws:base")

region = PAYMENT_MANAGER_ARN.split(":")[3]  # call AgentCore in the Payment Manager's Region
payment = boto3.client("bedrock-agentcore", region_name=region).process_payment(
    paymentManagerArn=PAYMENT_MANAGER_ARN,
    paymentSessionId=PAYMENT_SESSION_ID,
    userId=USER_ID,  # the user the payment session was created for
    paymentInstrumentId="aws.agentcorepayments.awsbilling.v1",
    paymentType="AWS_BILLING_X402",
    paymentInput={"awsBillingX402": {"version": str(required["x402Version"]), "payload": accepted}},
    clientToken=str(uuid.uuid4()),
)
token = payment["paymentOutput"]["awsBillingX402"]["paymentToken"]

signature = {"x402Version": 2, "resource": required["resource"], "accepted": accepted,
             "payload": {"paymentToken": token}}
paid = requests.post(URL, json=BODY, headers={
    "PAYMENT-SIGNATURE": base64.b64encode(json.dumps(signature).encode()).decode()})
open("hello.mp3", "wb").write(paid.content)
```

## Notes

* A paid quote is valid for 5 minutes. A failed request (e.g. a `400` for an unsupported parameter) doesn't use up the payment. Retry with corrected parameters, as long as the new request costs no more than what you paid.
* Supported models: Nova-3 (speech-to-text), Flux TTS voices on `/v2/speak`, and Aura-2 voices on `/v1/speak`.
* Payment tokens can be bound to a key with [DPoP (RFC 9449)](https://datatracker.ietf.org/doc/html/rfc9449). The proof must be signed for `POST` and the request URL without its query string, and include `ath`, the hash of the payment token.
* AgentCore payments: [setup](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-create-manager.html), [IAM roles](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-iam-roles.html), [troubleshooting AWS Billing errors](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments-troubleshooting.html#payments-troubleshooting-aws-billing).
