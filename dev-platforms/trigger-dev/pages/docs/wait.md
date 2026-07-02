---
title: "Wait: Overview"
source: https://trigger.dev/docs/wait
path: docs/wait
---

During your run you can wait for a period of time or for something to happen.

Waiting allows you to write complex tasks as a set of async code, without having to schedule another task or poll for changes.

In the Trigger.dev Cloud we automatically pause execution of tasks when they are waiting for
longer than a few seconds.

When triggering and waiting for subtasks, the parent is checkpointed and while waiting does not count towards compute usage. When waiting for a time period (`wait.for` or `wait.until`), if the wait is longer than 5 seconds we checkpoint and it does not count towards compute usage.

| Function                                                              | What it does                                       |
| :-------------------------------------------------------------------- | :------------------------------------------------- |
| [wait.for()](/docs/wait-for)                                               | Waits for a specific period of time, e.g. 1 day.   |
| [wait.until()](/docs/wait-until)                                           | Waits until the provided `Date`.                   |
| [wait.forToken()](/docs/wait-for-token)                                    | Pauses runs until a token is completed.            |
| [inputStream.wait()](/docs/tasks/streams#wait--suspend-until-data-arrives) | Pauses runs until data arrives on an input stream. |
