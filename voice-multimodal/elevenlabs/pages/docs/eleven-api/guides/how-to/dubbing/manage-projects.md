---
title: "Manage dubbing projects"
source: https://elevenlabs.io/docs/eleven-api/guides/how-to/dubbing/manage-projects.md
path: docs/eleven-api/guides/how-to/dubbing/manage-projects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Manage dubbing projects

**How-to guide** · Assumes you are familiar with creating dubbing projects, as shown in the
[Dubbing quickstart](/docs/eleven-api/guides/cookbooks/dubbing).

This guide covers the operations you need to manage existing projects: listing them with pagination, retrieving a single project or language, refreshing an expired download URL, and deleting projects and languages you no longer need.

## List projects

The list endpoint is cursor-paginated. Pass `page_size` (up to 100) and an optional `status` filter, then pass the response's `next_cursor` back as `cursor` to fetch the next page. A `next_cursor` of `null` means you have reached the end.

```python
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Fetch every ready project, one page at a time
cursor = None
while True:
    page = elevenlabs.dubbing.project.list(
        page_size=50,
        status="ready",
        cursor=cursor,
    )
    for project in page.projects:
        print(project.project_id, project.reference)
    if page.next_cursor is None:
        break
    cursor = page.next_cursor
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

// Fetch every ready project, one page at a time
let cursor: string | undefined = undefined;
while (true) {
  const page = await elevenlabs.dubbing.project.list({
    pageSize: 50,
    status: "ready",
    cursor,
  });
  for (const project of page.projects) {
    console.log(project.projectId, project.reference);
  }
  if (!page.nextCursor) break;
  cursor = page.nextCursor;
}
```

## Retrieve a project or language

Fetch a single project to read its status and media metadata, or a single language to read its status and outputs.

```python
project_id = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3"
language_id = "lang_1001kwkyxp0je6ktn4knsfrasx5s"

project = elevenlabs.dubbing.project.get(project_id)
print(project.status, project.language_ids)

language = elevenlabs.dubbing.project.language.get(project_id, language_id)
print(language.status, language.target_language)
```

```typescript
const projectId = "proj_1601kwkyxp0hfzvtmyxwqxx6mcy3";
const languageId = "lang_1001kwkyxp0je6ktn4knsfrasx5s";

const project = await elevenlabs.dubbing.project.get(projectId);
console.log(project.status, project.languageIds);

const language = await elevenlabs.dubbing.project.language.get(projectId, languageId);
console.log(language.status, language.targetLanguage);
```

## Refresh an expired download URL

The signed URL in `outputs.lossless_audio` is valid for about an hour. It is not a permanent link, so store the downloaded file rather than the URL. To download a completed dub again later, fetch the language to obtain a fresh URL.

```python
import requests

language = elevenlabs.dubbing.project.language.get(project_id, language_id)
audio = requests.get(language.outputs.lossless_audio)
with open("dubbed.wav", "wb") as f:
    f.write(audio.content)
```

```typescript
import { writeFile } from "fs/promises";

const language = await elevenlabs.dubbing.project.language.get(projectId, languageId);
const response = await fetch(language.outputs!.losslessAudio!);
const buffer = Buffer.from(await response.arrayBuffer());
await writeFile("dubbed.wav", buffer);
```

## Delete projects and languages

Delete a single language target to remove one dub while keeping the project, or delete the project to remove it and all of its languages. Deletion is permanent.

```python
# Remove a single language target
elevenlabs.dubbing.project.language.delete(project_id, language_id)

# Remove the project and all of its languages
elevenlabs.dubbing.project.delete(project_id)
```

```typescript
// Remove a single language target
await elevenlabs.dubbing.project.language.delete(projectId, languageId);

// Remove the project and all of its languages
await elevenlabs.dubbing.project.delete(projectId);
```
