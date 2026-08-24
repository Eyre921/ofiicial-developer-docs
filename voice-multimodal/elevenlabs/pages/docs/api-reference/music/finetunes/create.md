---
title: "Create Music Finetune"
source: https://elevenlabs.io/docs/api-reference/music/finetunes/create.md
path: docs/api-reference/music/finetunes/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Music Finetune

POST https://api.elevenlabs.io/v1/music/finetunes
Content-Type: multipart/form-data

Create a new music finetune

Reference: https://elevenlabs.io/docs/api-reference/music/finetunes/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `name` (string, required) — Name for the finetune (5-200 characters).
- `primary_genre` (string, required) — Primary musical genre of the finetune.
- `files` (files, optional) — Audio files to train on.
- `tags` (list of string, optional) — Tags to associate with the finetune.
- `visibility` (enum, optional) — Finetune visibility. Only 'private' and 'workspace' can be set.
- `model_id` (enum, optional) — The model to create a finetune for.

## Response

### 201

Successful Response

- `id` (string, required) — Unique identifier of the finetune.
- `name` (string, required) — Name of the finetune.
- `tags` (list of string, required) — Tags associated with the finetune.
- `model_id` (string, required) — The base music model the finetune was trained on.
- `created_at` (string, required) — When the finetune was created (UTC).
- `visibility` (enum, required) — Who can access this finetune: `private` (only you), `workspace` (members of your workspace), `public` (ElevenLabs-curated, available to everyone).
  - Allowed values: `private`, `workspace`, `public`
- `created_by` (enum, required) — Who created the finetune: `self`, `workspace`, or `elevenlabs`.
  - Allowed values: `self`, `workspace`, `elevenlabs`
- `status` (enum, required) — Training lifecycle status: pending, in_progress, completed, failed, and blocked.
  - Allowed values: `pending`, `in_progress`, `completed`, `failed`, `blocked`
- `training_progress` (double, required) — Training progress from 0.0 to 1.0.
- `primary_genre` (string, optional, nullable) — Primary musical genre of the finetune.
- `failure_reason` (enum, optional, nullable) — Reason the finetune failed or was blocked, if applicable.
  - Allowed values: `audio_processing_failed`, `copyright_violation`, `training_failed`
