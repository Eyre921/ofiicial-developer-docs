---
title: "Spaces Search"
source: https://docs.x.com/x-api/spaces/search/introduction
path: x-api/spaces/search/introduction
---

The Spaces Search endpoint lets you search for live or scheduled Spaces by keyword. Reference for the X API v2 standard tier covering search.

The Spaces Search endpoint lets you search for live or scheduled Spaces by keyword. Find Spaces about topics of interest.

## Overview

<CardGroup>
  <Card title="Keyword search" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834">
    Search Spaces by title
  </Card>

  <Card title="Discover Spaces" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-microphone.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=84616ff8f3d942047a71ee5e0a5adab9">
    Find live and upcoming Spaces
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                                          | Description       |
| :----- | :------------------------------------------------ | :---------------- |
| GET    | [`/2/spaces/search`](/x-api/spaces/search-spaces) | Search for Spaces |

***

## Parameters

| Parameter      | Description                     |
| :------------- | :------------------------------ |
| `query`        | Search query (required)         |
| `state`        | Filter by `live` or `scheduled` |
| `space.fields` | Additional Space fields         |
| `expansions`   | Related objects to include      |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/spaces/search?\
query=AI&\
state=live&\
space.fields=title,host_ids,participant_count" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

## Example response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": [
    {
      "id": "1DXxyRYNejbKM",
      "state": "live",
      "title": "Discussing AI and the Future",
      "host_ids": ["1234567890"],
      "participant_count": 245
    }
  ],
  "meta": {
    "result_count": 1
  }
}
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
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/spaces/search/quickstart">
    Search for your first Space
  </Card>

  <Card title="Spaces lookup" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-microphone.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=84616ff8f3d942047a71ee5e0a5adab9" href="/x-api/spaces/lookup/introduction">
    Look up Spaces by ID
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/spaces/search-spaces">
    Full endpoint documentation
  </Card>
</CardGroup>
