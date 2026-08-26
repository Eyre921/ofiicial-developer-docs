---
title: "Writing tasks: Overview"
source: https://trigger.dev/docs/writing-tasks-introduction
path: docs/writing-tasks-introduction
---

Tasks are the core of Trigger.dev. They are long-running processes that are triggered by events.

Before digging deeper into the details of writing tasks, you should read the [fundamentals of tasks](/docs/tasks/overview) to understand what tasks are and how they work.

## Writing tasks

| Topic                                             | Description                                                                                         |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------------- |
| [Logging](/docs/logging)                          | View and send logs and traces from your tasks.                                                      |
| [Errors & retrying](/docs/errors-retrying)        | How to deal with errors and write reliable tasks.                                                   |
| [Wait](/docs/wait)                                | Wait for periods of time or for external events to occur before continuing.                         |
| [Concurrency & Queues](/docs/queue-concurrency)   | Configure what you want to happen when there is more than one run at a time.                        |
| [Realtime notifications](/docs/realtime/overview) | Send realtime notifications from your task that you can subscribe to from your backend or frontend. |
| [Versioning](/docs/versioning)                    | How versioning works.                                                                               |
| [Machines](/docs/machines)                        | Configure the CPU and RAM of the machine your task runs on                                          |
| [Idempotency](/docs/idempotency)                  | Protect against mutations happening twice.                                                          |
| [Replaying](/docs/replaying)                      | You can replay a single task or many at once with a new version of your code.                       |
| [Max duration](/docs/runs/max-duration)           | Set a maximum duration for your task to run.                                                        |
| [Tags](/docs/tags)                                | Tags allow you to easily filter runs in the dashboard and when using the SDK.                       |
| [Metadata](/docs/runs/metadata)                   | Attach a small amount of data to a run and update it as the run progresses.                         |
| [Usage](/docs/run-usage)                          | Get compute duration and cost from inside a run, or for a specific block of code.                   |
| [Context](/docs/context)                          | Access the context of the task run.                                                                 |
| [Bulk actions](/docs/bulk-actions)                | Run actions on many task runs at once.                                                              |
| [Priority](/docs/runs/priority)                   | Specify a priority when triggering a task.                                                          |
| [Hidden tasks](/docs/hidden-tasks)                | Create tasks that are not exported from your trigger files but can still be executed.               |

## Our library of examples, guides and projects

<CardGroup>
  <Card title="Walkthrough guides" icon="book" href="/docs/guides/introduction">
    Detailed guides for setting up Trigger.dev with popular frameworks and services, including
    Next.js, Remix, Supabase, Stripe and more.
  </Card>

  <Card title="Example tasks" icon="code" href="/docs/guides/introduction#example-tasks">
    Task code you can copy and paste to use in your own projects, including OpenAI, Vercel AI SDK,
    Deepgram, FFmpeg, Puppeteer, Stripe, Supabase and more.
  </Card>

  <Card title="Webhook guides" icon="code" href="/docs/guides/frameworks/webhooks-guides-overview">
    Learn how to trigger tasks from webhooks, including Next.js, Remix, Supabase and Stripe and
    more.
  </Card>

  <Card title="Example projects" icon="GitHub" href="/docs/guides/introduction#example-projects">
    Full-stack projects demonstrating how to use Trigger.dev. Fork them in GitHub as a starting
    point for your own projects.
  </Card>
</CardGroup>
