---
title: "Manage your time — technical reference"
source: https://developers.notion.com/guides/mcp/tools-calendars-reference
path: guides/mcp/tools-calendars-reference
---

Find parameters and permissions for Notion MCP calendars, events, coworker schedules, contacts, and meeting rooms.

## List calendars

`notion-calendar-list-calendars`

Lists calendars grouped by connected account. Use this to get calendar identifiers before another Calendar operation.

Calendar tools use your connected Calendar accounts. They're available on all Notion plans in user-authorized MCP connections, but not workspace-owned connections.

## List calendar events

`notion-calendar-list-events`

Lists your events across connected calendars within a time range.

Pass `timeMin` and `timeMax` to set the range. `timeZone` sets the time zone used for returned event times.

## List coworkers' events

`notion-calendar-list-coworkers-events`

Reads detailed events for coworkers in the same organization within a time range.

## Find calendar resources

`notion-calendar-list-calendar-resources`

Finds rooms or other calendar resources for specific times. Requires a Google Workspace account with admin permissions to view Calendar resources.

## Find contacts

`notion-calendar-list-contacts`

Finds contacts by name or email across your connected Calendar accounts.

## Create calendar events

`notion-calendar-create-events`

Creates one or more events on writable calendars. Creating events may notify attendees.

Choose each event's `calendar` using a reference from `notion-calendar-list-calendars`. If you omit `calendar`, the event is created on the primary/default calendar.

## Update calendar events

`notion-calendar-update-events`

Updates identified events, including their timing, attendees, recurrence, resources, or RSVP status. Updates may notify attendees.

Use `notion-calendar-list-events` to get each event's `calendar` reference and `eventId`; pass them in `updates[].event`. Set `updates[].updateType` to `UPDATE` to edit event details or `RSVP` to change your response.

## Cancel calendar events

`notion-calendar-cancel-events`

Cancels identified events you can manage. Cancellation may notify attendees. To decline an event you don't organize, use `notion-calendar-update-events` with `updateType: "RSVP"` instead.

Pass each event's `calendar` reference and `eventId` in `events`. Get these from `notion-calendar-list-events`; an event title alone isn't sufficient.
