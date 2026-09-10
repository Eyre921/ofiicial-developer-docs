---
title: "Personalized Trends"
source: https://docs.x.com/x-api/trends/personalized-trends/introduction
path: x-api/trends/personalized-trends/introduction
---

The X API v2 Personalized Trends endpoint returns trending topics tailored to the authenticated user based on their location, interests, and account activity.

The Personalized Trends endpoint returns trending topics tailored to the authenticated user, based on their location and interests.

## Overview

<CardGroup>
  <Card title="Personalized" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305">
    Trends tailored to the user
  </Card>

  <Card title="Location-aware" icon="location-dot">
    Based on user's location
  </Card>

  <Card title="Real-time" icon="bolt">
    Current trending topics
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                       | Description             |
| :----- | :----------------------------- | :---------------------- |
| GET    | `/2/users/personalized_trends` | Get personalized trends |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/users/personalized_trends" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN"
```

## Example response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": [
    {
      "trend_name": "#AI",
      "tweet_count": 125000
    },
    {
      "trend_name": "Machine Learning",
      "tweet_count": 85000
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
  * User Access Tokens via [OAuth 2.0 PKCE](/resources/fundamentals/authentication#oauth-2-0-authorization-code-flow-with-pkce-2)
  * Premium User Subscription
</Note>

<CardGroup>
  <Card title="Trends by WOEID" icon="globe" href="/x-api/trends/trends-by-woeid/introduction">
    Get trends for a specific location
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/trends/personalized-trends">
    Full endpoint documentation
  </Card>
</CardGroup>
