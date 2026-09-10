---
title: "Spaces Lookup"
source: https://docs.x.com/x-api/spaces/lookup/introduction
path: x-api/spaces/lookup/introduction
---

The Spaces lookup endpoints let you retrieve information about live or scheduled Spaces. Reference for the X API v2 standard tier covering lookup.

The Spaces lookup endpoints let you retrieve information about live or scheduled Spaces. Look up Spaces by their ID or find Spaces created by specific users.

## Overview

<CardGroup>
  <Card title="By ID" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-microphone.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=84616ff8f3d942047a71ee5e0a5adab9">
    Get details for a specific Space
  </Card>

  <Card title="Multiple Spaces" icon="microphone-lines">
    Look up multiple Spaces at once
  </Card>

  <Card title="By creator" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305">
    Find Spaces by their hosts
  </Card>

  <Card title="Buyers" icon="ticket">
    Get users who purchased tickets
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                                              | Description                    |
| :----- | :-------------------------------------------------------------------- | :----------------------------- |
| GET    | [`/2/spaces/:id`](/x-api/spaces/get-space-by-id)                      | Get Space by ID                |
| GET    | [`/2/spaces`](/x-api/spaces/get-spaces-by-ids)                        | Get Spaces by IDs              |
| GET    | [`/2/spaces/by/creator_ids`](/x-api/spaces/get-spaces-by-creator-ids) | Get Spaces by creator user IDs |
| GET    | [`/2/spaces/:id/buyers`](/x-api/spaces/get-space-ticket-buyers)       | Get ticket buyers for a Space  |
| GET    | [`/2/spaces/:id/tweets`](/x-api/spaces/get-space-posts)               | Get Posts shared in a Space    |

***

## Response fields

By default, the response includes `id` and `state`. Request additional fields:

| Field               | Description               |
| :------------------ | :------------------------ |
| `title`             | Space title               |
| `host_ids`          | Host user IDs             |
| `speaker_ids`       | Speaker user IDs          |
| `participant_count` | Number of participants    |
| `scheduled_start`   | Scheduled start time      |
| `started_at`        | Actual start time         |
| `ended_at`          | End time                  |
| `is_ticketed`       | Whether Space has tickets |

### Space states

| State       | Description          |
| :---------- | :------------------- |
| `live`      | Currently active     |
| `scheduled` | Scheduled for future |
| `ended`     | Has ended            |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/spaces/1DXxyRYNejbKM?\
space.fields=title,host_ids,participant_count,scheduled_start,state" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * Your App's [keys and tokens](/resources/fundamentals/authentication)
</Note>

<CardGroup>
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/spaces/lookup/quickstart">
    Make your first Spaces lookup request
  </Card>

  <Card title="Search Spaces" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834" href="/x-api/spaces/search/introduction">
    Find Spaces by keyword
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/spaces/space-lookup-by-space-id">
    Full endpoint documentation
  </Card>

  <Card title="Sample code" icon="github" href="https://github.com/xdevplatform/Twitter-API-v2-sample-code">
    Working code examples
  </Card>
</CardGroup>
