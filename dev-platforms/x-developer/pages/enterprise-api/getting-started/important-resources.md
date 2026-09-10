---
title: "Important resources for Enterprise API customers"
source: https://docs.x.com/enterprise-api/getting-started/important-resources
path: enterprise-api/getting-started/important-resources
---

Essential resources for X Enterprise API customers, including onboarding guides, account managers, support contacts, status pages, and SDKs.

Bookmark these essential resources for X API development.

***

## Documentation

<CardGroup>
  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/introduction">
    Complete endpoint documentation with parameters and examples.
  </Card>

  <Card title="Data Dictionary" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/fundamentals/data-dictionary">
    Object schemas for posts, users, media, and more.
  </Card>

  <Card title="Authentication" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-key.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=de93497af2dde62afd3a06e896d330f5" href="/resources/fundamentals/authentication/overview">
    OAuth 1.0a and OAuth 2.0 implementation guides.
  </Card>

  <Card title="Rate Limits" icon="gauge-high" href="/x-api/fundamentals/rate-limits">
    Per-endpoint limits and best practices.
  </Card>
</CardGroup>

***

## Tools

| Tool                                                                                                                                         | Description                           |
| :------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------ |
| [Developer Console](https://console.x.com)                                                                                                   | Manage apps, credentials, and billing |
| [Postman Collection](https://www.postman.com/xapidevelopers/x-api-public-workspace/collection/34902927-2efc5689-99c6-4ab6-8091-996f35c2fd80) | Interactive API testing               |
| [Python SDK](/xdks/python/overview)                                                                                                          | Official Python library               |
| [TypeScript SDK](/xdks/typescript/overview)                                                                                                  | Official TypeScript library           |
| [OpenAPI Spec](https://api.x.com/2/openapi.json)                                                                                             | Machine-readable API specification    |

***

## Learning

<CardGroup>
  <Card title="Tutorials" icon="graduation-cap" href="/tutorials">
    Step-by-step guides for common use cases.
  </Card>

  <Card title="Sample Code" icon="github" href="https://github.com/xdevplatform">
    Example apps and code samples.
  </Card>

  <Card title="What to Build" icon="lightbulb" href="/x-api/what-to-build">
    Ideas and inspiration for projects.
  </Card>

  <Card title="Migration Guide" icon="route" href="/x-api/migrate/overview">
    Upgrade from v1.1 to v2.
  </Card>
</CardGroup>

***

## Community and support

<CardGroup>
  <Card title="Developer Forum" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat-unread.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=ce6313d8c0b7b4e5363f2ce80b89f7e4" href="https://devcommunity.x.com">
    Ask questions and share solutions with the community.
  </Card>

  <Card title="Support Hub" icon="circle-question" href="https://developer.x.com/en/support">
    FAQs, troubleshooting, and contact options.
  </Card>

  <Card title="@XDevelopers" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-logo-x.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=53e3153f3b8d6efdad31484ef133b274" href="https://x.com/XDevelopers">
    Official updates and announcements.
  </Card>

  <Card title="@API" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-logo-x.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=53e3153f3b8d6efdad31484ef133b274" href="https://x.com/api">
    API-specific news and tips.
  </Card>
</CardGroup>

***

## Stay updated

| Resource                                                             | What you'll get                      |
| :------------------------------------------------------------------- | :----------------------------------- |
| [Changelog](/changelog)                                              | All platform changes and updates     |
| [Newsletter](/newsletter)                                            | Monthly roundup of news and features |
| [Forum Announcements](https://devcommunity.x.com/c/announcements/22) | Important platform notices           |
| [API Status](https://developer.x.com/status)                         | Real-time service availability       |

<Tip>
  Follow [@XDevelopers](https://x.com/XDevelopers) and turn on notifications to catch breaking changes and new features.
</Tip>

***

## Quick reference

### Response structure

All v2 responses follow this structure:

```json theme={null}
{
  "data": { ... },      // Primary object(s)
  "includes": { ... },  // Expanded objects (if requested)
  "meta": { ... },      // Pagination info
  "errors": [ ... ]     // Partial errors (if any)
}
```

### Common parameters

| Parameter          | Use                          |
| :----------------- | :--------------------------- |
| `tweet.fields`     | Request specific post fields |
| `user.fields`      | Request specific user fields |
| `expansions`       | Include related objects      |
| `max_results`      | Limit results per page       |
| `pagination_token` | Get next/previous page       |

### Authentication methods

| Method       | Use case                                |
| :----------- | :-------------------------------------- |
| Bearer Token | Read-only public data                   |
| OAuth 2.0    | User actions with fine-grained scopes   |
| OAuth 1.0a   | User actions (legacy, full permissions) |

[Full authentication guide →](/resources/fundamentals/authentication/overview)
