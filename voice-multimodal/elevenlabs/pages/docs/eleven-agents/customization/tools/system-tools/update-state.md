---
title: "Update state"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/update-state.md
path: docs/eleven-agents/customization/tools/system-tools/update-state
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update state

## Overview

The **Update state** tool lets your agent set one or more [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) while a conversation is in progress. Like other [system tools](/docs/eleven-agents/customization/tools/system-tools), it only changes the internal state of the conversation — it never calls an external API or a client-side function.

Use it to record information as a call unfolds, for example flagging that a conversation should be escalated, storing a value the user provided, or computing a value derived from other dynamic variables.

## Functionality

* **Multiple updates per call**: A single tool call can assign up to 10 dynamic variables at once.
* **Expression-based values**: Each value is the result of an expression, which can combine constants, existing dynamic variables, values the LLM extracts from the conversation, and operators.
* **LLM extraction only when needed**: The tool only asks the LLM to extract parameters for the updates that require it. Updates built entirely from constants and/or existing dynamic variables don't add any parameters to the function call.
* **Immediate availability**: Once the tool runs, the updated dynamic variables are available to the rest of the conversation — later prompts, other tool calls, and overrides can all reference them, the same way as any other dynamic variable.

## How it works

Each state update assigns the result of an expression to a dynamic variable:

```text
variable_name = expression
```

An expression is one of the following types, and expressions can be nested inside each other to build more complex logic:

| Type                | Description                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| Constant            | A fixed string, number, boolean, or null value.                                                        |
| Dynamic variable    | The current value of another dynamic variable.                                                         |
| LLM-extracted value | A value the LLM infers from the conversation, matching a type you define (string, number, or boolean). |
| Logical operator    | `and`, `or`, or a conditional (`if` / `then` / `else`) expression combining other expressions.         |
| Comparison operator | `=`, `≠`, `>`, `<`, `≥`, `≤`, comparing two expressions.                                               |
| Arithmetic operator | `+`, `-`, `×`, `÷`, combining two numeric (or, for `+`, string) expressions.                           |

For example, the following state update sets `should_escalate` to `true` if the LLM judges the user is frustrated, or if a `retry_count` dynamic variable is already greater than 3:

```text
should_escalate = (llm: "User sounds frustrated with the conversation") OR (retry_count > 3)
```

If a state update fails to evaluate — for example, a division by zero — the tool call returns an
error and none of the updates in that call are applied.

## Configuration

### Step 1: Add the tool

Navigate to your agent's configuration page. In the **Tools** section, click **Add tool** and choose **Update state**.

### Step 2: Define state updates

For each state update, provide:

* **Variable name**: The dynamic variable to assign.
* **Expression**: The value to assign, built from the value and operator types described above. Values can be nested to build more complex expressions.

You can define up to 10 state updates for a single tool.

### Step 3: Configure the description (optional)

You can provide a custom description to guide the LLM on when to call the tool. If left blank, a default description optimized for this tool is used.

## Use cases

* **Escalation flags**: Set a dynamic variable (for example `should_escalate`) that a downstream system or business rule checks, as shown in the [Genesys integration guide](/docs/eleven-agents/customization/integrations/genesys#configure-escalation).
* **Recording extracted information**: Store a value the user provided (an order number, a preference, a chosen department) as a dynamic variable for use later in the conversation.
* **Derived values**: Compute a value from other dynamic variables, such as incrementing a counter or combining two variables into one.

**Purpose**: Let the agent update one or more dynamic variables based on the conversation, without calling an external API.

**Trigger conditions**: The LLM should call this tool when:

* The conversation provides information that should be recorded (e.g. an escalation flag, a chosen option, a value the user provided)
* A configured state update depends on a value the LLM must judge or extract from the conversation

**Parameters**:

The function's parameters depend on how the tool is configured. Each configured state update that uses an LLM-extracted value adds one property to the schema, named after that update's dynamic variable and typed as `string`, `number`, or `boolean`. State updates built only from constants or other dynamic variables don't add any parameters.

**Function call format**:

```json
{
  "type": "function",
  "function": {
    "name": "update_state",
    "arguments": "{\"should_escalate\": true}"
  }
}
```

**Implementation**: The agent evaluates every configured expression using the extracted parameters plus the conversation's current dynamic variables, then assigns the results to the corresponding dynamic variables. No external request is made.

## FAQ

#### Does this tool make any external calls?

No. Like all system tools, Update state only modifies the internal state of the conversation. It
doesn't call an external API or a client-side function.

#### Does calling this tool always require the LLM to extract parameters?

No. The tool only asks the LLM to extract a parameter for state updates whose expression
includes an LLM-extracted value. If every configured update is built from constants and/or
existing dynamic variables, the function call takes no parameters.

#### Where can I use the dynamic variables this tool sets?

Anywhere you can use a dynamic variable: system prompts, first messages, tool parameters and
headers, and overrides. See [Dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) for details.

#### Can I configure this tool through the API?

Update state is currently configurable through the agent dashboard. API and SDK support isn't
available yet.
