---
title: "Code tools"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/code-tools.md
path: docs/eleven-agents/customization/tools/code-tools
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Code tools

**Code tools** let your agent run custom JavaScript in a sandboxed server-side environment, without you having to stand up and host your own webhook endpoint. Write the logic once in the built-in code editor, and ElevenLabs executes it whenever the agent calls the tool.

This is an enterprise-only feature.

## Overview

A code tool is a JavaScript function that runs when the agent calls it. You write the whole function body, so the tool can do as much or as little as the task requires:

* **Custom calculations**: apply pricing rules, unit conversions, scoring logic, or date math using only the tool-call parameters. No network access required.
* **Calling external APIs**: `fetch` from allowlisted domains, with workspace secrets and auth connections injected into the function's context.
* **Combining multiple sources**: call two or three APIs and merge, compare, or reconcile their results before returning a single answer.
* **Conditional branching**: run different logic depending on the tool-call parameters, without needing a separate tool per branch.
* **Reshaping data**: return exactly the structure you want the agent to see, rather than a raw upstream response.

For a single external API call with no custom logic, [webhook tools](/docs/eleven-agents/customization/tools/webhook-tools) are usually simpler to set up. To
trigger actions in a user's browser or app, use [client tools](/docs/eleven-agents/customization/tools/client-tools) instead.

## How it works

Your code is a JavaScript module that exports a single default async function. The function receives a `ctx` object and returns the tool's result:

```javascript
export default async (ctx) => {
  // ctx.args.<paramName> — the parameters the agent passed to this tool call
  const { city } = ctx.args;

  return { message: `Hello from ${city}!` };
};
```

The value you return becomes the tool's result. It's passed back to the agent, shown in the conversation transcript, and can be used for [dynamic variable assignment](/docs/eleven-agents/customization/tools/webhook-tools#tool-configuration).

### The `ctx` object

`ctx` is your entry point to everything the tool can access at call time. The parameters the agent provides always arrive in `ctx.args`; secrets, config values, and auth connections are optional, and appear only if you map them in the tool's **Context object** section.

| Property               | Description                                                                                                                                                                                                                                                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ctx.args`             | The tool-call parameters the agent provided.                                                                                                                                                                                                                                                                                                             |
| `ctx.config`           | Plain string variables you've mapped into this tool's context.                                                                                                                                                                                                                                                                                           |
| `ctx.secrets`          | Workspace secrets you've mapped into this tool's context for use in request headers. The raw secret is never exposed to your code; injection happens on egress and exclusively in the headers.                                                                                                                                                           |
| `ctx.auth_connections` | References to configured [auth connections](/docs/eleven-agents/customization/tools/webhook-tools#supported-authentication-methods) you've mapped into this tool's context, for use in the `X-With-Auth-Connection` request header. The underlying credential is never exposed to your code; injection happens on egress and exclusively in the headers. |

Only `ctx.args` is visible to the agent when it calls the tool. Secrets, config values, and auth
connections are never revealed to the agent.

#### Configuring parameters

Parameters are the values the agent supplies when it calls the tool, and they arrive in `ctx.args`. Define them in the **Parameters** section of the tool configuration form, or in the code editor under the **Params** tab, in the **Define Params** sub-tab. Each parameter takes a data type, an identifier, and a description that the agent uses to determine the correct value from the conversation. Your code reads that value under the identifier, such as `ctx.args.appointment_datetime` below.

![Defining a code tool parameter](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d492e864ae15f3a355251faae3b719544e1ab56b703c02740b51be6c6769ccf7/assets/images/conversational-ai/code-tool-parameters.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T200739Z&X-Amz-Expires=604800&X-Amz-Signature=4618f9c99d54460fe745a076730fbcadae71ad29a8a4d61ebea1b03be6ac8f25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Configuring the context object

Add secrets, config values, and auth connections in the tool's **Context object** section. Each entry takes a type and a name. The panel shows the exact accessor for each entry, such as `ctx.secrets.DEMO_KEY` below.

![Mapping a workspace secret into a code tool's context object](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ad58ee53f3591f447b108191aff760f1134350911933b968b06798fa6d42f438/assets/images/conversational-ai/code-tool-context-object.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260906T200739Z&X-Amz-Expires=604800&X-Amz-Signature=8239df0a28091f4e24bcb31df5a30163f2984ca9395184c9bb692392294463f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Network access

Code running in the sandbox can only reach domains your workspace has explicitly allowed. Add the domains your code needs to call in your workspace's **General Settings**, under **Code tool allowed domains**. A request to any other domain fails.

Editing the **Code tool allowed domains** list requires Workspace admin permissions.

### Execution limits

* **Timeout**: each run must complete within the tool's configured response timeout, from 1 up to 30 seconds.
* **No external packages**: code tools currently run without npm dependencies.

### Testing your code

Before saving, use **Run** in the code editor to execute your code with sample parameter values:

* **Params** — set test values for each parameter your tool defines.
* **Output** — see the returned result, or the error if execution failed.
* **Logs** — see anything written with `console.log`, `console.warn`, or `console.error`, plus build and execution timing.

## Guide

In this guide, we'll create a code tool that converts a temperature and returns a friendly, formatted string:

#### Create a new code tool

On the **Agent** section of your agent settings page, choose **Add Tool**. Select **Code** as the Tool Type, then set a name and description:

| Field       | Value                                                 |
| ----------- | ----------------------------------------------------- |
| Name        | convert\_temperature                                  |
| Description | Converts a temperature between Celsius and Fahrenheit |

#### Define the parameters

Add two parameters so the LLM knows what to provide:

| Data Type | Identifier | Required | Description                              |
| --------- | ---------- | -------- | ---------------------------------------- |
| number    | value      | true     | The temperature value to convert         |
| string    | from\_unit | true     | The unit to convert from: `"C"` or `"F"` |

#### Write the code

Open the code editor and replace the default source with:

```javascript
export default async (ctx) => {
  const { value, from_unit } = ctx.args;

  if (from_unit === "C") {
    const fahrenheit = (value * 9) / 5 + 32;
    return { result: `${value}°C is ${fahrenheit.toFixed(1)}°F` };
  }

  const celsius = ((value - 32) * 5) / 9;
  return { result: `${value}°F is ${celsius.toFixed(1)}°C` };
};
```

Use **Run** with a few sample values (e.g. `value: 100, from_unit: "C"`) to confirm the output before saving.

#### Orchestration

Update your agent's system prompt so it knows when to reach for the tool:

```plaintext System prompt
When the user asks to convert a temperature, call convert_temperature with the
value and its unit ("C" or "F"), and read back the result naturally.
```

#### Testing

Start a conversation and try:

> *What's 100 degrees Celsius in Fahrenheit?*

The agent should call the tool and read back the converted value.

### Authentication examples

**Calling an API with a secret**

```javascript
export default async (ctx) => {
  const { order_id } = ctx.args;

  const response = await fetch(`https://api.example.com/orders/${order_id}`, {
    headers: {
      Authorization: `Bearer ${ctx.secrets.EXAMPLE_API_KEY}`,
    },
  });

  if (!response.ok) {
    throw new Error(`Upstream error: ${response.status}`);
  }

  return await response.json();
};
```

Map `EXAMPLE_API_KEY` to a workspace secret in the tool's **Context object** section, then add `api.example.com` to **Code tool allowed domains** so the request is allowed to egress. The value you reference is a placeholder: the real secret is substituted into the header on egress, and is never visible to your code.

**Calling an API with an OAuth auth connection**

```javascript
export default async (ctx) => {
  const { customer_id } = ctx.args;

  const response = await fetch(`https://api.example.com/customers/${customer_id}`, {
    headers: {
      "X-With-Auth-Connection": ctx.authConnections.EXAMPLE_CRM,
    },
  });

  if (!response.ok) {
    throw new Error(`Upstream error: ${response.status}`);
  }

  return await response.json();
};
```

Map `EXAMPLE_CRM` to a configured [auth connection](/docs/eleven-agents/customization/tools/webhook-tools#supported-authentication-methods) in the tool's **Context object** section. The value you reference is a placeholder: the real credential is substituted into the header on egress, and is never visible to your code.

## Best practices

#### Name tools intuitively, with detailed descriptions

If you find the assistant does not make calls to the correct tools, you may need to update your tool names and descriptions so the assistant more clearly understands when it should select each tool. Avoid using abbreviations or acronyms to shorten tool and argument names.

You can also include detailed descriptions for when a tool should be called. For complex tools, you should include descriptions for each of the arguments to help the assistant know what it needs to ask the user to collect that argument.

#### Name tool parameters intuitively, with detailed descriptions

Use clear and descriptive names for tool parameters. If applicable, specify the expected format for a parameter in the description (e.g., YYYY-mm-dd or dd/mm/yy for a date).

#### Consider providing additional information about how and when to call tools in your assistant's&#xA;system prompt

Providing clear instructions in your system prompt can significantly improve the assistant's tool calling accuracy. For example, guide the assistant with instructions like the following:

```plaintext
Use `check_order_status` when the user inquires about the status of their order, such as 'Where is my order?' or 'Has my order shipped yet?'.
```

Provide context for complex scenarios. For example:

```plaintext
Before scheduling a meeting with `schedule_meeting`, check the user's calendar for availability using check_availability to avoid conflicts.
```

#### LLM selection

When using tools, we recommend picking high intelligence models like GPT 5.2, Gemini-2.5-Flash, or
Claude Sonnet 4.5 and avoiding Gemini-2.0-Flash.

It's important to note that the choice of LLM matters to the success of function calls. Some LLMs can struggle with extracting the relevant parameters from the conversation.
