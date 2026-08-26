---
title: "Using webhooks with Trigger.dev"
source: https://trigger.dev/docs/guides/frameworks/webhooks-guides-overview
path: docs/guides/frameworks/webhooks-guides-overview
---

Guides for using webhooks with Trigger.dev.

## Overview

Webhooks are a way to send and receive events from external services. Triggering tasks using webhooks allow you to add real-time, event driven functionality to your app.

A webhook handler is code that executes in response to an event. They can be endpoints in your framework's routing which can be triggered by an external service.

## Webhook guides

<CardGroup>
  <Card title="Next.js - triggering tasks using webhooks" icon="N" href="/docs/guides/frameworks/nextjs-webhooks">
    How to create a webhook handler in a Next.js app, and trigger a task from it.
  </Card>

  <Card title="Remix - triggering tasks using webhooks" icon="R" href="/docs/guides/frameworks/remix-webhooks">
    How to create a webhook handler in a Remix app, and trigger a task from it.
  </Card>

  <Card title="Stripe webhooks" icon="webhook" href="/docs/guides/examples/stripe-webhook">
    How to create a Stripe webhook handler and trigger a task when a 'checkout session completed'
    event is received.
  </Card>

  <Card title="Hookdeck webhooks" icon="webhook" href="/docs/guides/examples/hookdeck-webhook">
    Use Hookdeck to receive webhooks and forward them to Trigger.dev tasks with logging and replay
    capabilities.
  </Card>

  <Card title="Supabase database webhooks guide" icon="webhook" href="/docs/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>
</CardGroup>
