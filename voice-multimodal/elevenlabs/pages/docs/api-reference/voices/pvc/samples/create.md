---
title: "Add samples to PVC voice"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/create.md
path: docs/api-reference/voices/pvc/samples/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Add samples to PVC voice

POST https://api.elevenlabs.io/v1/voices/pvc/{voice_id}/samples
Content-Type: multipart/form-data

Add audio samples to a PVC voice

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `voice_id` (string, required) — Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

### Body (multipart/form-data)

This endpoint expects a multipart form with multiple files.

- `files` (files, required) — Audio files used to create the voice.
- `remove_background_noise` (boolean, optional) — If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

## Response

### 200

Successful Response

- `list of SampleResponseModel`

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### SampleResponseModel

- `sample_id` (string, optional) — The ID of the sample.
- `file_name` (string, optional) — The name of the sample file.
- `mime_type` (string, optional) — The MIME type of the sample file.
- `size_bytes` (integer, optional) — The size of the sample file in bytes.
- `hash` (string, optional) — The hash of the sample file.
- `duration_secs` (double, optional, nullable)
- `remove_background_noise` (boolean, optional, nullable)
- `has_isolated_audio` (boolean, optional, nullable)
- `has_isolated_audio_preview` (boolean, optional, nullable)
- `speaker_separation` (SpeakerSeparationResponseModel, optional, nullable)
- `trim_start` (integer, optional, nullable)
- `trim_end` (integer, optional, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### SpeakerSeparationResponseModel

- `voice_id` (string, required) — The ID of the voice.
- `sample_id` (string, required) — The ID of the sample.
- `status` (enum, required) — The status of the speaker separation.
  - Allowed values: `not_started`, `pending`, `completed`, `failed`
- `speakers` (map from string to SpeakerResponseModel, optional, nullable) — The speakers of the sample.
- `selected_speaker_ids` (list of string, optional, nullable) — The IDs of the selected speakers.

### ValidationErrorLocItems

### SpeakerResponseModel

- `speaker_id` (string, required) — The ID of the speaker.
- `duration_secs` (double, required) — The duration of the speaker segment in seconds.
- `utterances` (list of UtteranceResponseModel, optional, nullable) — The utterances of the speaker.

### UtteranceResponseModel

- `start` (double, required) — The start time of the utterance in seconds.
- `end` (double, required) — The end time of the utterance in seconds.
