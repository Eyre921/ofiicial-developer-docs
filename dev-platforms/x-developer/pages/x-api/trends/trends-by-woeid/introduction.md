---
title: "Trends by WOEID"
source: https://docs.x.com/x-api/trends/trends-by-woeid/introduction
path: x-api/trends/trends-by-woeid/introduction
---

The Trends by WOEID endpoint returns trending topics for a specific geographic location. Reference for the X API v2 standard tier covering trends by woeid.

The Trends by WOEID endpoint returns trending topics for a specific geographic location, identified by a Yahoo! Where On Earth ID (WOEID).

## Overview

<CardGroup>
  <Card title="Location-specific" icon="location-dot">
    Trends for any supported location
  </Card>

  <Card title="Global coverage" icon="globe">
    Countries, cities, and regions
  </Card>

  <Card title="Real-time" icon="bolt">
    Current trending topics
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                                                      | Description            |
| :----- | :------------------------------------------------------------ | :--------------------- |
| GET    | [`/2/trends/by/woeid/:id`](/x-api/trends/get-trends-by-woeid) | Get trends for a WOEID |

***

## Common WOEIDs

| Location       | WOEID    |
| :------------- | :------- |
| Worldwide      | 1        |
| United States  | 23424977 |
| United Kingdom | 23424975 |
| Japan          | 23424856 |
| New York       | 2459115  |
| Los Angeles    | 2442047  |
| London         | 44418    |
| Tokyo          | 1118370  |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/trends/by/woeid/1" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

## Example response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": [
    {
      "trend_name": "#AI"
    },
    {
      "trend_name": "Breaking News"
    }
  ]
}
```

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * Your App's [Bearer Token](/resources/fundamentals/authentication)
</Note>

<CardGroup>
  <Card title="Personalized trends" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305" href="/x-api/trends/personalized-trends/introduction">
    Get trends for the authenticated user
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/trends/trends-by-woeid">
    Full endpoint documentation
  </Card>
</CardGroup>
