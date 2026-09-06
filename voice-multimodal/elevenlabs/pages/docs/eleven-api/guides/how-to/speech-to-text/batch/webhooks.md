---
title: "Asynchronous Speech to Text"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks.md
path: docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Asynchronous Speech to Text

**How-to guide** · Assumes you have completed the [Speech to Text quickstart](/docs/eleven-api/guides/cookbooks/speech-to-text).

## Overview

Webhooks allow you to receive automatic notifications when your Speech to Text transcription tasks are completed, eliminating the need to continuously poll the API for status updates. This is particularly useful for long-running transcription jobs or when processing large volumes of audio files.

When a transcription is completed, ElevenLabs will send a POST request to your specified webhook URL with the transcription results, including the transcript text, language detection, and any metadata.

## Using webhooks

This guide assumes you have [set up your API key and SDK](/docs/eleven-api/quickstart). Complete
the quickstart first if you haven't.

#### Create or edit a webhook

In the ElevenLabs dashboard, go to
[**Developers** > **Webhooks**](https://elevenlabs.io/app/developers/webhooks).
Click **Create webhook**, or edit an existing webhook.

![Create webhook dialog with Transcription completed selected](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/866f389106e74e16586a4d68cf8160f2d27568518ff4f984c2fab81cbd1674c9/assets/images/cookbooks/scribe/webhooks/create-webhook.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T233241Z&X-Amz-Expires=604800&X-Amz-Signature=9340d5b2b02a7d97b0efc7fcbf58103a6d61e8fcdbb34eae267f5e219e88be5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Configure the webhook with:

* **Name**: A descriptive name for your webhook
* **Callback URL**: Your publicly accessible HTTPS endpoint
* **Webhook Auth Method**: Either `HMAC` or `OAuth`. It is up to the client to implement the verification mechanism. ElevenLabs sends headers that allow for verification but we do not enforce it.
* **Events**: Select **Transcription completed**.

#### Make API calls with webhook parameter enabled

When making speech-to-text API calls, include the `webhook` parameter set to `true` to enable webhook notifications for that specific request.

```python maxLines=0
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def transcribe_with_webhook(audio_file):
  try:
    result = elevenlabs.speech_to_text.convert(
      file=audio_file,
      model_id="scribe_v2",
      webhook=True,
    )
    print(f"Transcription started: {result.request_id}")
    return result
  except Exception as e:
    print(f"Error starting transcription: {e}")
    raise e
```

```typescript maxLines=0
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

async function transcribeWithWebhook(audioFile) {
  try {
    const result = await elevenlabs.speechToText.convert({
      file: audioFile,
      modelId: 'scribe_v2',
      webhook: true,
    });

    console.log('Transcription started:', result.requestId);
    return result;
  } catch (error) {
    console.error('Error starting transcription:', error);
    throw error;
  }
}
```

## Webhook payload

When a transcription is completed, your webhook endpoint will receive a POST request with the transcription and webhook data:

```json
{
  type: 'speech_to_text_transcription',
  data: {
    request_id: 'some-request-id-123',
    webhook_metadata: { ... }, // if provided in the convert request
    transcription: {
      "language_code": "en",
      "language_probability": 0.98,
      "text": "Hello world!",
      "words": [
        {
          "text": "Hello",
          "start": 0.0,
          "end": 0.5,
          "type": "word",
          "speaker_id": "speaker_1"
        },
        {
          "text": " ",
          "start": 0.5,
          "end": 0.5,
          "type": "spacing",
          "speaker_id": "speaker_1"
        },
        {
          "text": "world!",
          "start": 0.5,
          "end": 1.2,
          "type": "word",
          "speaker_id": "speaker_1"
        }
      ]
    }
  }
}
```

Please refer to the [Speech-to-text API](/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime) reference to learn about the details of the response structure.

## Implementing your webhook endpoint

Here's an example of how to implement a webhook endpoint to handle incoming notifications:

```javascript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import 'dotenv/config';
import express from 'express';

const elevenlabs = new ElevenLabsClient();

const app = express();
app.use(express.json());

const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET;

app.post('/webhook/speech-to-text', (req, res) => {
  try {
    const signature = req.headers['elevenlabs-signature'];
    const payload = JSON.stringify(req.body);
    let event;

    try {
      // Verify the webhook signature.
      event = await elevenlabs.webhooks.constructEvent(payload, signature, WEBHOOK_SECRET);
    } catch (error) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    if (event.type === 'speech_to_text.completed') {
      const { requestId, status, text, language_code } = event.data;

      console.log(`Transcription ${requestId} completed`);
      console.log(`Language: ${language_code}`);
      console.log(`Text: ${text}`);

      processTranscription(requestId, text, language_code);
    } else if (status === 'failed') {
      console.error(`Transcription ${requestId} failed`);
      handleTranscriptionError(requestId);
    }

    res.status(200).json({ received: true });
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

async function processTranscription(requestId, text, language) {
  console.log('Processing completed transcription...');
}

async function handleTranscriptionError(requestId) {
  console.log('Handling transcription error...');
}

app.listen(3000, () => {
  console.log('Webhook server listening on port 3000');
});
```

## Security considerations

### Signature verification

Always verify webhook signatures to ensure requests came from ElevenLabs.

### HTTPS requirement

Webhook URLs must use HTTPS to ensure secure transmission of transcription data.

### Rate limiting

Implement rate limiting on your webhook endpoint to prevent abuse:

```javascript
import rateLimit from "express-rate-limit";

const webhookLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: "Too many webhook requests from this IP",
});

app.use("/webhook", webhookLimiter);
```

### Failure responses

Return appropriate HTTP status codes:

* `200-299`: Success - webhook processed successfully
* `400-499`: Client error - webhook will not be retried
* `500-599`: Server error - webhook will be retried

## Testing webhooks

### Local development

For local testing, use tools like [ngrok](https://ngrok.com/) to expose your local server:

```bash
ngrok http 3000
```

Use the provided HTTPS URL as your webhook endpoint during development.

### Webhook testing

You can test your webhook implementation by making a transcription request and monitoring your endpoint:

```javascript
async function testWebhook() {
  const audioFile = new File([audioBuffer], "test.mp3", { type: "audio/mp3" });

  const result = await elevenlabs.speechToText.convert({
    file: audioFile,
    modelId: "scribe_v2",
    webhook: true,
  });

  console.log("Test transcription started:", result.requestId);
}
```

## Next steps

#### [Server-side streaming](/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming)

Transcribe audio in real time using the WebSocket-based streaming API.

#### [API reference](/docs/api-reference/speech-to-text)

Full Speech to Text API reference and parameters.
