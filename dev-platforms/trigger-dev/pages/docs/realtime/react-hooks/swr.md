---
title: "SWR hooks"
source: https://trigger.dev/docs/realtime/react-hooks/swr
path: docs/realtime/react-hooks/swr
---

Fetch and cache data using SWR-based hooks

SWR hooks use the [swr](https://swr.vercel.app/) library to fetch data once and cache it. These hooks are useful when you need to fetch data without real-time updates.

<Note>
  While SWR can be configured to poll for updates, we recommend using our other [Realtime
  hooks](/docs/realtime/react-hooks/) for most use-cases due to rate-limits and the way the Trigger.dev
  API works.
</Note>

## useRun

The `useRun` hook allows you to fetch a run by its ID.

```tsx theme={"theme":"css-variables"}
"use client"; // This is needed for Next.js App Router or other RSC frameworks

import { useRun } from "@trigger.dev/react-hooks";

export function MyComponent({ runId }: { runId: string }) {
  const { run, error, isLoading } = useRun(runId);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>Run: {run.id}</div>;
}
```

The `run` object returned is the same as the [run object](/docs/management/runs/retrieve) returned by the Trigger.dev API. To correctly type the run's payload and output, you can provide the type of your task to the `useRun` hook:

```tsx theme={"theme":"css-variables"}
import { useRun } from "@trigger.dev/react-hooks";
import type { myTask } from "@/trigger/myTask";

export function MyComponent({ runId }: { runId: string }) {
  const { run, error, isLoading } = useRun<typeof myTask>(runId, {
    refreshInterval: 0, // Disable polling
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  // Now run.payload and run.output are correctly typed

  return <div>Run: {run.id}</div>;
}
```

## Common SWR options

You can pass the following options to the all SWR hooks:

<ParamField type="boolean">
  Revalidate the data when the window regains focus.
</ParamField>

<ParamField type="boolean">
  Revalidate the data when the browser regains a network connection.
</ParamField>

<ParamField type="number">
  Poll for updates at the specified interval (in milliseconds). Polling is not recommended for most
  use-cases. Use the Realtime hooks instead.
</ParamField>

## Common SWR return values

<ResponseField name="error" type="Error">
  An error object if an error occurred while fetching the data.
</ResponseField>

<ResponseField name="isLoading" type="boolean">
  A boolean indicating if the data is currently being fetched.
</ResponseField>

<ResponseField name="isValidating" type="boolean">
  A boolean indicating if the data is currently being revalidated.
</ResponseField>

<ResponseField name="isError" type="boolean">
  A boolean indicating if an error occurred while fetching the data.
</ResponseField>
