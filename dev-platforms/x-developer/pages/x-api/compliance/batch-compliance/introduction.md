---
title: "Batch Compliance"
source: https://docs.x.com/x-api/compliance/batch-compliance/introduction
path: x-api/compliance/batch-compliance/introduction
---

Use the X API v2 Batch Compliance endpoints to upload Post ID or user ID datasets and retrieve current compliance status for deletions, suspensions, and edits.

The Batch Compliance endpoints let you upload datasets of Post IDs or user IDs and receive their current compliance status. Use this to identify deleted Posts, suspended accounts, and other compliance events.

## Overview

<CardGroup>
  <Card title="Post compliance" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=9fde7d51b4f18c96d3a38a81d519761f">
    Check status of Posts in bulk
  </Card>

  <Card title="User compliance" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305">
    Check status of users in bulk
  </Card>

  <Card title="Asynchronous" icon="clock">
    Submit jobs and retrieve results later
  </Card>

  <Card title="Large datasets" icon="database">
    Process millions of IDs
  </Card>
</CardGroup>

***

## How it works

1. **Create a job** — Specify the type (Posts or users) and upload URL
2. **Upload IDs** — Upload your dataset to the provided URL
3. **Wait for processing** — Job processes asynchronously
4. **Download results** — Get compliance status for each ID

***

## Endpoints

| Method | Endpoint                                                               | Description                 |
| :----- | :--------------------------------------------------------------------- | :-------------------------- |
| POST   | [`/2/compliance/jobs`](/x-api/compliance/create-compliance-job)        | Create a new compliance job |
| GET    | [`/2/compliance/jobs/:id`](/x-api/compliance/get-compliance-job-by-id) | Get job status              |
| GET    | [`/2/compliance/jobs`](/x-api/compliance/get-compliance-jobs)          | List all jobs               |

***

## Job types

| Type     | Description                  |
| :------- | :--------------------------- |
| `tweets` | Check Post compliance status |
| `users`  | Check user compliance status |

***

## Compliance events

### Post events

| Event       | Description                  |
| :---------- | :--------------------------- |
| `deleted`   | Post was deleted by user     |
| `bounced`   | Post failed compliance check |
| `protected` | Account became protected     |
| `suspended` | Account was suspended        |
| `scrub_geo` | Geo data was removed         |

### User events

| Event         | Description              |
| :------------ | :----------------------- |
| `deleted`     | Account was deleted      |
| `suspended`   | Account was suspended    |
| `protected`   | Account became protected |
| `deactivated` | Account was deactivated  |

***

## Example: Create a job

```bash theme={null}
curl -X POST "https://api.x.com/2/compliance/jobs" \
  -H "Authorization: Bearer $BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "tweets",
    "name": "my-compliance-job"
  }'
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
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/compliance/batch-compliance/quickstart">
    Create your first compliance job
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/compliance/batch-compliance/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/compliance/create-compliance-job">
    Full endpoint documentation
  </Card>
</CardGroup>
