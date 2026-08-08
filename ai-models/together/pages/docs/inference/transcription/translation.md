---
title: "Audio translation"
source: https://docs.together.ai/docs/inference/transcription/translation
path: docs/inference/transcription/translation
---

Translate speech in any language into English text.

Audio translation converts speech from any language to English text:

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.translations.create(
      file=Path("french_audio.mp3"),
      model="openai/whisper-large-v3",
  )
  print(f"English translation: {response.text}")
  ```

  ```typescript TypeScript theme={null}
  import { createReadStream } from 'fs';

  const response = await together.audio.translations.create({
    file: createReadStream('french_audio.mp3'),
    model: 'openai/whisper-large-v3',
  });
  console.log(`English translation: ${response.text}`);
  ```
</CodeGroup>

## Translation with context

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  response = client.audio.translations.create(
      file=Path("business_meeting_spanish.mp3"),
      model="openai/whisper-large-v3",
      prompt="This is a business meeting discussing quarterly sales results.",
  )
  ```
</CodeGroup>

## Limits and errors

`/v1/audio/translations` shares the same code path as transcription: the 80 MB direct-upload cap, 1 GB URL-fetch cap, and 4-hour duration cap all apply, and the same error codes are returned. For audio above 80 MB, submit an HTTPS URL on the `file` field instead. See [Limits](/docs/inference/transcription/overview#limits) and [Errors and troubleshooting](/docs/inference/transcription/features#errors-and-troubleshooting).
