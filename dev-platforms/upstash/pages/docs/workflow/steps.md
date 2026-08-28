---
title: "Overview"
source: https://upstash.com/docs/workflow/steps
path: docs/workflow/steps
---

A workflow's **context** is an object provided by the route function.

The context object provides:
* **Workflow APIs** – functions for defining workflow steps.
* **Workflow Run Properties** – request payload, request headers, and other metadata.

<CodeGroup>
    ```typescript api/workflow/route.ts highlight={4-5}
    import { serve } from "@upstash/workflow/nextjs";

    export const { POST } = serve(
      // 👇 the workflow context
      async (context) => {
        // ...
      }
    );
    ```

    ```python main.py
    from fastapi import FastAPI
    from upstash_workflow.fastapi import Serve
    from upstash_workflow import AsyncWorkflowContext

    app = FastAPI()
    serve = Serve(app)

    @serve.post("/api/example")
    async def example(context: AsyncWorkflowContext[str]) -> None: ...

    ```
</CodeGroup>

## Context Object Properties

<ParamField path="requestPayload" type="object">
  The request payload passed to the workflow run via `trigger()` call.
</ParamField>

<ParamField path="headers" type="object">
  The request headers passed to the workflow run via `trigger()` call.
</ParamField>

<ParamField path="workflowRunId" type="string">
  The unique identifier of the current workflow run.
</ParamField>

<ParamField path="url" type="string">
  The public URL of the workflow endpoint.
</ParamField>

<ParamField path="failureUrl" type="string">
  The URL used for workflow failure callback.

  If a failure function is defined, this is the same as the workflow's `url`.
</ParamField>

<ParamField path="env" type="object">
  The environment variables available to the workflow.
</ParamField>

<ParamField path="qstashClient" type="object">
  The QStash client instance used by the workflow endpoint.
</ParamField>

<ParamField path="labels" type="string[]">
  The labels attached to the current workflow run, if set in [client.trigger](/docs/workflow/basics/client/trigger).
  Defaults to an empty array when no label was set.
</ParamField>

<ParamField path="label" type="string | undefined" deprecated>
  Deprecated. Use `labels` instead. When a run has multiple labels, this only
  returns the first one.
</ParamField>

## Context Object Functions

You can use the functions exposed by context object to define workflow steps.

* [context.run](/docs/workflow/basics/context/run)
* [context.sleep](/docs/workflow/basics/context/sleep)
* [context.sleepUntil](/docs/workflow/basics/context/sleepUntil)
* [context.waitForEvent](/docs/workflow/basics/context/waitForEvent)
* [context.createWebhook](/docs/workflow/basics/context/createWebhook)
* [context.waitForWebhook](/docs/workflow/basics/context/waitForWebhook)
* [context.notify](/docs/workflow/basics/context/notify)
* [context.invoke](/docs/workflow/basics/context/invoke)
* [context.call](/docs/workflow/basics/context/call)
* [context.cancel](/docs/workflow/basics/context/cancel)
* [context.api](/docs/workflow/basics/context/api)
