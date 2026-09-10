---
title: "Developer Support"
source: https://docs.x.com/support
path: support
---

Find support channels for the X API, including the developer community forum, Stack Overflow, GitHub issues, status page, and contact options.

Whether you're troubleshooting an issue, looking for guidance, or want to connect with other developers, we've got you covered.

***

## Community and help

<CardGroup>
  <Card title="Developer Forums" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat-unread.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=ce6313d8c0b7b4e5363f2ce80b89f7e4" href="https://devcommunity.x.com">
    Ask questions, share your projects, and get help from the X developer community and team. This is the best place to get support for technical questions.
  </Card>

  <Card title="API Status" icon="signal" href="https://developer.x.com/status">
    Check the current operational status of X API v2, Enterprise APIs, and the Developer Console.
  </Card>
</CardGroup>

***

## Contact and forms

<CardGroup>
  <Card title="Enterprise API Interest" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bank.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=6dd9ad48fa88936abb112b49e022abff" href="/forms/enterprise-api-interest">
    Interested in enterprise-level API access? Submit your interest and our team will reach out.
  </Card>

  <Card title="Billing Support" icon="credit-card" href="/forms/billing-support">
    Get help with billing questions for Self-serve and Enterprise API subscriptions.
  </Card>

  <Card title="Policy Support" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-shield-check.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=768533bde161ac68862de87449f011c3" href="https://help.x.com/forms/platform">
    Questions about policies, compliance, or need approval for specific use cases? Contact our policy team.
  </Card>
</CardGroup>

***

## Documentation and resources

<CardGroup>
  <Card title="Getting Started" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/getting-started/make-your-first-request">
    New to the X API? Start here to get your API keys and make your first request.
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/introduction">
    Complete reference for all X API v2 endpoints, parameters, and response formats.
  </Card>

  <Card title="Authentication Guide" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-key.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=de93497af2dde62afd3a06e896d330f5" href="/fundamentals/authentication/overview">
    Learn about OAuth 1.0a, OAuth 2.0, and how to authenticate your API requests.
  </Card>

  <Card title="SDKs & Libraries" icon="cube" href="/tools-and-libraries">
    Official Python and TypeScript SDKs to speed up your development.
  </Card>

  <Card title="Rate Limits" icon="gauge" href="/x-api/fundamentals/rate-limits">
    Understand rate limits and how to handle them in your application.
  </Card>

  <Card title="Error Codes" icon="https://mintcdn.com/x-preview/szd6PKNMlRQoyyAo/icons/xds/icon-info-circle.svg?fit=max&auto=format&n=szd6PKNMlRQoyyAo&q=85&s=8ec54c5126797535385f8241158b81ca" href="/x-api/fundamentals/response-codes-and-errors">
    Reference for API error codes and how to resolve common issues.
  </Card>
</CardGroup>

***

## Policies and guidelines

<CardGroup>
  <Card title="Developer Guidelines" icon="scale-balanced" href="/developer-guidelines">
    Practical guide to what's allowed and what's not when building with the X API.
  </Card>

  <Card title="Developer Agreement" icon="file-contract" href="/developer-terms/agreement">
    The binding legal terms for X API access.
  </Card>

  <Card title="Developer Policy" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-shield-check.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=768533bde161ac68862de87449f011c3" href="/developer-terms/policy">
    Rules and expectations for building on X.
  </Card>

  <Card title="Restricted Use Cases" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-block.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=702a65b4001948aebcc42635b8e2eac7" href="/developer-terms/restricted-use-cases">
    Activities that are prohibited or require special approval.
  </Card>
</CardGroup>

***

## Troubleshooting tips

<AccordionGroup>
  <Accordion title="I'm getting 401 Unauthorized errors" icon="lock">
    * Double-check your API keys and tokens are correct
    * Ensure you're using the right authentication method for the endpoint (OAuth 1.0a vs OAuth 2.0)
    * Verify your app has the required permissions (read, write, DM access)
    * Check that your tokens haven't expired—regenerate if needed
  </Accordion>

  <Accordion title="I'm hitting rate limits" icon="gauge">
    * Check the `x-rate-limit-*` headers in API responses to monitor your usage
    * Implement exponential backoff when you receive 429 errors
    * Cache responses where possible to reduce API calls
    * Consider upgrading your access tier for higher limits
    * See the [Rate Limits guide](/x-api/fundamentals/rate-limits) for detailed information
  </Accordion>

  <Accordion title="My app was suspended" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-block.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=702a65b4001948aebcc42635b8e2eac7">
    * Review the [Developer Guidelines](/developer-guidelines) to understand what may have caused the suspension
    * Check your email for any communication from X about the suspension
    * Submit an appeal through the [Policy Support form](https://help.x.com/forms/platform)
    * Common causes: automated likes, unsolicited DMs/mentions, scraping, rate limit abuse
  </Accordion>

  <Accordion title="I need higher API access or limits" icon="arrow-up">
    * Review the [pricing tiers](/x-api/getting-started/pricing) to find the right plan
    * For enterprise needs, submit the [Enterprise API Interest form](/forms/enterprise-api-interest)
    * For access upgrades, use the [Use Case Upgrade form](/forms/use-case/upgrade)
  </Accordion>

  <Accordion title="I can't find the endpoint I need" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834">
    * Browse the full [API Reference](/x-api/introduction)
    * Check if the functionality exists in [v1.1 endpoints](/x-api/migrate/overview) that may not be in v2 yet
    * Ask in the [Developer Forums](https://devcommunity.x.com) if you're unsure
  </Accordion>
</AccordionGroup>

***

## Stay updated

<CardGroup>
  <Card title="Changelog" icon="https://mintcdn.com/x-preview/szd6PKNMlRQoyyAo/icons/xds/icon-history.svg?fit=max&auto=format&n=szd6PKNMlRQoyyAo&q=85&s=6afe17587c08ee621e37afde19a07ff1" href="/changelog">
    Latest API updates, new features, and changes.
  </Card>

  <Card title="@XDevelopers" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-logo-x.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=53e3153f3b8d6efdad31484ef133b274" href="https://x.com/XDevelopers">
    Follow for announcements and developer news.
  </Card>

  <Card title="Incidents" icon="https://mintcdn.com/x-preview/jLbdFJYHCS9a6gmb/icons/xds/icon-warning.svg?fit=max&auto=format&n=jLbdFJYHCS9a6gmb&q=85&s=3760ceda7c43e1ffbd9f8b7ccbf83cca" href="/incidents">
    History of past incidents and their resolutions.
  </Card>
</CardGroup>
