---
title: "Create a full-page meeting note"
source: https://developers.notion.com/reference/create-meeting-note-page
path: reference/create-meeting-note-page
---

post /v1/meeting_notes
Creates a full-page meeting note, or gets or creates the meeting note for a calendar event.

Creates a full-page meeting note and returns it in `meeting_note` as a [meeting notes block](/reference/block#meeting-notes) with `is_full_page` set to `true`. To create AI meeting notes from an uploaded recording instead, use [Create a meeting note](/reference/create-meeting-note).

| Body parameters | Behavior |
| - | - |
| `parent` | Creates the meeting note in the parent page or data source. In a data source that isn't a meetings database, Notion adds a page and puts the meeting note inside it. |
| No `parent` and no `calendar_event` | Creates the meeting note in the user's meeting notes database. Notion creates that database if the user doesn't have one. |
| `calendar_event` | Returns the event's existing meeting note, or creates one. Notion files and titles it like the event's other meeting notes. |

`markdown` sets the content of the meeting note's Notes tab. You can't pass `parent`, `title`, or `markdown` with `calendar_event`. The API can't add content to the meeting note after this call.

To find an event's IDs for `calendar_event`, see [Link a full-page meeting note to a calendar event](/reference/update-meeting-note-page).

The response's `created` field is `true` when Notion created a new meeting note and `false` when it returned an existing one. Without `calendar_event`, every call creates a new meeting note.

When an event has a meeting note that the user can't read, Notion creates a new one. The event then has two meeting notes.

With `calendar_event`, the existing meeting note can be a meeting notes block inside a page, with `is_full_page` set to `false`.

### Workers

A [Notion Worker](/workers/get-started/overview) calling this endpoint needs a connected calendar. It acts as itself: the parent must be shared with the Worker, and the Worker is recorded as the meeting note's creator. A Worker must pass `parent` and can't pass `calendar_event`. To link its meeting note to an event, call [Link a full-page meeting note to a calendar event](/reference/update-meeting-note-page) next.

### Requirements

This endpoint accepts personal access tokens and Workers. The integration must have the **Read content** and **Insert content** capabilities. See the [capabilities guide](/reference/capabilities).

### Errors

Returns a 400 HTTP response if the request combines `calendar_event` with `parent`, `title`, or `markdown`, or if a Worker passes `calendar_event` or omits `parent`. Also returns a 400 if a Worker has no working calendar connection.

Returns a 403 HTTP response if the token isn't a personal access token or a Worker, or if the user can't edit the parent.

Returns a 404 HTTP response if the parent doesn't exist or the integration can't access it.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) for more information.
