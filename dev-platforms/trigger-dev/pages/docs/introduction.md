---
title: "Welcome to the Trigger.dev docs"
source: https://trigger.dev/docs/introduction
path: docs/introduction
---

Find all the resources and guides you need to get started

<CardGroup>
  <Card title="Quick start" href="/quick-start">
    Get started with Trigger.dev and run your first task in 3 minutes
  </Card>

  <Card title="Guides, frameworks & examples" href="/guides/introduction#example-tasks">
    Browse our wide range of guides, frameworks and example projects
  </Card>

  <Card title="Building with AI" href="/building-with-ai">
    Learn how to build Trigger.dev projects using AI coding assistants
  </Card>

  <Card title="Video walkthrough" href="/video-walkthrough">
    Watch an end-to-end demo of Trigger.dev in 10 minutes
  </Card>
</CardGroup>

## What is Trigger.dev?

Trigger.dev is an open source background jobs framework that lets you write reliable workflows in plain async code. Run long-running AI tasks, handle complex background jobs, and build AI agents with built-in queuing, automatic retries, and real-time monitoring. No timeouts, elastic scaling, and zero infrastructure management required.

We provide everything you need to build and manage background tasks: a CLI and SDK for writing tasks in your existing codebase, support for both [regular](/docs/tasks/overview) and [scheduled](/docs/tasks/scheduled) tasks, full observability through our dashboard, and a [Realtime API](/docs/realtime) with [React hooks](/docs/realtime/react-hooks#realtime-hooks) for showing task status in your frontend. You can use [Trigger.dev Cloud](https://cloud.trigger.dev) or [self-host](/docs/self-hosting/overview) on your own infrastructure.

## Learn the concepts

<CardGroup>
  <Card title="Writing tasks" icon="wand-magic-sparkles" href="/tasks/overview">
    Tasks are the core of Trigger.dev. Learn what they are and how to write them.
  </Card>

  <Card title="Triggering tasks" icon="bullseye-pointer" href="/triggering">
    Learn how to trigger tasks from your codebase.
  </Card>

  <Card title="Runs" icon="person-running" href="/runs">
    Runs are the instances of tasks that are executed. Learn how they work.
  </Card>

  <Card title="API keys" icon="key" href="/apikeys">
    API keys are used to authenticate requests to the Trigger.dev API. Learn how to create and use
    them.
  </Card>
</CardGroup>

## Explore by feature

<CardGroup>
  <Card title="Scheduled tasks (cron)" icon="clock" href="/tasks/scheduled">
    Scheduled tasks are a type of task that is scheduled to run at a specific time.
  </Card>

  <Card title="Realtime API" icon="loader" href="/realtime">
    The Realtime API allows you to trigger tasks and get the status of runs.
  </Card>

  <Card title="React hooks" icon="react" href="/realtime/react-hooks">
    React hooks are a way to show task status in your frontend.
  </Card>

  <Card title="Waits" icon="calendar-clock" href="/wait">
    Waits are a way to wait for a task to finish before continuing.
  </Card>

  <Card title="Errors and retries" icon="message-exclamation" href="/errors-retrying">
    Learn how to handle errors and retries.
  </Card>

  <Card title="Concurrency & Queues" icon="line-height" href="/queue-concurrency">
    Configure what you want to happen when there is more than one run at a time.
  </Card>

  <Card title="Wait for token (human-in-the-loop)" icon="hand" href="/wait-for-token">
    Pause runs until a token is completed via an approval workflow.
  </Card>

  <Card title="Build extensions" icon="gear" href="/config/extensions/overview">
    Customize the build process or the resulting bundle and container image.
  </Card>
</CardGroup>

## Explore by build extension

| Extension             | What it does                                                 | Docs                                                                   |
| :-------------------- | :----------------------------------------------------------- | :--------------------------------------------------------------------- |
| prismaExtension       | Use Prisma with Trigger.dev                                  | [prismaExtension docs](/docs/config/extensions/prismaExtension)             |
| pythonExtension       | Execute Python scripts in Trigger.dev                        | [pythonExtension docs](/docs/config/extensions/pythonExtension)             |
| playwright            | Use Playwright with Trigger.dev                              | [playwright extension docs](/docs/config/extensions/playwright)             |
| puppeteer             | Use Puppeteer with Trigger.dev                               | [puppeteer extension docs](/docs/config/extensions/puppeteer)               |
| lightpanda            | Use Lightpanda with Trigger.dev                              | [lightpanda extension docs](/docs/config/extensions/lightpanda)             |
| ffmpeg                | Use FFmpeg with Trigger.dev                                  | [ffmpeg extension docs](/docs/config/extensions/ffmpeg)                     |
| aptGet                | Install system packages with aptGet                          | [aptGet extension docs](/docs/config/extensions/aptGet)                     |
| additionalFiles       | Copy additional files to the build directory                 | [additionalFiles docs](/docs/config/extensions/additionalFiles)             |
| additionalPackages    | Include additional packages in the build                     | [additionalPackages docs](/docs/config/extensions/additionalPackages)       |
| syncEnvVars           | Automatically sync environment variables to Trigger.dev      | [syncEnvVars docs](/docs/config/extensions/syncEnvVars)                     |
| esbuildPlugin         | Add existing or custom esbuild plugins to your build process | [esbuildPlugin docs](/docs/config/extensions/esbuildPlugin)                 |
| emitDecoratorMetadata | Support for the emitDecoratorMetadata TypeScript compiler    | [emitDecoratorMetadata docs](/docs/config/extensions/emitDecoratorMetadata) |
| audioWaveform         | Support for Audio Waveform in your project                   | [audioWaveform docs](/docs/config/extensions/audioWaveform)                 |

## Explore by example

<CardGroup>
  <Card title="FFmpeg" href="/guides/examples/ffmpeg-video-processing" />

  <Card title="Fal.ai" href="/guides/examples/fal-ai-image-to-cartoon" />

  <Card title="Puppeteer" href="/guides/examples/puppeteer" />

  <Card title="LibreOffice" href="/guides/examples/libreoffice-pdf-conversion" />

  <Card title="OpenAI" href="/guides/examples/open-ai-with-retrying" />

  <Card title="Browserbase" href="/guides/examples/scrape-hacker-news" />

  <Card title="Sentry" href="/guides/examples/sentry-error-tracking" />

  <Card title="Resend" href="/guides/examples/resend-email-sequence" />

  <Card title="Vercel AI SDK" href="/guides/examples/vercel-ai-sdk" />

  <Card title="Sharp" href="/guides/examples/sharp-image-processing" />

  <Card title="Deepgram" href="/guides/examples/deepgram-transcribe-audio" />

  <Card title="Supabase" href="/guides/examples/supabase-database-operations" />

  <Card title="DALL•E" href="/guides/examples/dall-e3-generate-image" />

  <Card title="Firecrawl" href="/guides/examples/firecrawl-url-crawl" />

  <Card title="Lightpanda" href="/guides/examples/lightpanda" />
</CardGroup>

## Getting help

We'd love to hear from you or give you a hand getting started. Here are some ways to get in touch with us.

<CardGroup>
  <Card title="Join our Discord server" icon="discord" href="https://discord.gg/kA47vcd8P6">
    Our Discord is the best place to get help with any questions about Trigger.dev.
  </Card>

  <Card
    title="Follow us on X (Twitter)"
    icon={
  <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 0 512 512">
    <path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z" />
  </svg>
}
    href="https://twitter.com/triggerdotdev"
  >
    Follow us to get the latest updates and news.
  </Card>

  <Card title="Schedule a call" icon="phone" href="https://cal.com/team/triggerdotdev/founders-call">
    Arrange a call with one of the founders to get help with any questions.
  </Card>

  <Card title="Give us a star on GitHub" icon="star" href="https://github.com/triggerdotdev/trigger.dev">
    Check us out our GitHub repo and give us a star if you like what we're doing.
  </Card>
</CardGroup>
