---
title: "Link a full-page meeting note to a calendar event"
source: https://developers.notion.com/reference/update-meeting-note-page
path: reference/update-meeting-note-page
---

patch /v1/meeting_notes/{meeting_note_id}
Links an existing full-page meeting note to a calendar event.

Links a full-page meeting note to a calendar event and returns the meeting note in `meeting_note` as a [meeting notes block](/reference/block#meeting-notes). The link replaces any event the meeting note is already linked to.

The REST API has no calendar endpoint yet. To find an event's IDs, use [`notion-calendar-list-events`](/guides/mcp/tools-calendars-reference#list-calendar-events) in Notion MCP. Pass its `calendar.accountId`, `calendar.calendarId`, and `eventId` as `calendar.account_id`, `calendar.calendar_id`, and `event_id`.

By default, this endpoint doesn't link a meeting note to an event that already has other meeting notes. It returns a 409 with their IDs in `additional_data.other_meeting_note_ids`. Pass `allow_other_meeting_notes: true` to link anyway.

On success, `other_meeting_note_ids` lists the other meeting notes you can read that are linked to the same event. For a meeting note inside a page, the ID is the page's. Notion checks at most 50 meeting notes, so the list may be incomplete.

### Workers

A [Notion Worker](/workers/get-started/overview) calling this endpoint needs a connected calendar, and the event's calendar must be one the Worker can read. The Worker acts as itself, so the meeting note must be shared with it.

If this endpoint returns a 409, delete the meeting note the Worker created or pass `allow_other_meeting_notes: true`.

### Requirements

This endpoint accepts personal access tokens and Workers. The integration must have the **Read content** and **Update content** capabilities. See the [capabilities guide](/reference/capabilities).

### Errors

Returns a 400 HTTP response if the block isn't a full-page meeting note, or if a Worker has no working calendar connection.

Returns a 403 HTTP response if the token isn't a personal access token or a Worker, if the user can't edit the meeting note, or if a Worker can't read the event's calendar.

Returns a 404 HTTP response if the meeting note doesn't exist or the integration can't access it.

Returns a 409 HTTP response if the event has other meeting notes and `allow_other_meeting_notes` isn't `true`.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) for more information.
