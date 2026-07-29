---
title: "Create a meeting note"
source: https://developers.notion.com/reference/create-meeting-note
path: reference/create-meeting-note
---

post /v1/blocks/meeting_notes
Creates AI meeting notes from an uploaded audio or video file.

Creates a [meeting notes block](/reference/block#meeting-notes) and begins processing its source media. The response includes the ID of the created block. A full block response also includes its current processing status.

Source types allow you to directly attach a file upload, or create a meeting note block from an existing audio or video file block:

| Source                | Body parameters                                                                                                                                               | Behavior                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Completed file upload | Set `source.type` to `file_upload`, provide `source.file_upload_id`, set `parent.type` to `page_id`, and provide `parent.page_id`.                            | Creates the meeting notes block in the parent page.       |
| Existing block        | Set `source.type` to `block` and provide `source.block_id` for an audio, video, or file block backed by a Notion-hosted audio or video upload. Omit `parent`. | Creates the meeting notes block next to the source block. |

For a file upload source, upload the media and wait until the [file upload](/reference/file-upload) has a status of `uploaded` before calling this endpoint. See [Uploading small files](/guides/data-apis/uploading-small-files) for the complete upload flow.

<Note>
  For a `.m4a` audio file, use the `audio/mp4` content type. WebM audio is not supported.
</Note>

### Processing status

Processing continues asynchronously after the endpoint returns. Use [Retrieve a block](/reference/retrieve-a-block) with the returned block ID and check `meeting_notes.status`. When summary generation is enabled, wait for `notes_ready` before retrieving the generated summary and notes from the IDs in `meeting_notes.children`.

By default, Notion starts summary generation after transcription. Set `options.kickoff_summary` to `false` to transcribe the media without generating a summary.

If you provide a `title` and enable summary generation, treat the title as provisional. Notion may replace it when processing completes.

<Warning>
  This endpoint is not idempotent. Retrying a request may create duplicate meeting notes blocks.
</Warning>

### Requirements

The integration must have the **Insert content** capability. **Read content** is also required to use an existing block as the source or receive the full meeting notes block in the response. Without **Read content**, a request using a file upload source returns only the created block's `object` and `id`.

The user associated with the integration must also have access to AI meeting notes. See the [capabilities guide](/reference/capabilities) and [Notion pricing](https://www.notion.com/pricing).

### Errors

Returns a 400 HTTP response if AI meeting notes are not available to the integration's user or if the request contains an invalid source, parent, or processing option.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) for more information.
