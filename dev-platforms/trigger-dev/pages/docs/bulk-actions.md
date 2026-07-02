---
title: "Bulk actions"
source: https://trigger.dev/docs/bulk-actions
path: docs/bulk-actions
---

Perform actions like replay and cancel on multiple runs at once.

Bulk actions allow you to perform replaying and canceling on multiple runs at once. This is especially useful when you need to retry a batch of failed runs with a new version of your code, or when you need to cancel multiple in-progress runs.

<video />

## How to create a new bulk action

<Icon icon="circle-1" /> Open the bulk action panel from the top right of the runs page

<img alt="Access bulk actions" />

<Icon icon="circle-2" /> Filter the runs table to show the runs you want to bulk action

<Icon icon="circle-3" /> Alternatively, you can select individual runs

<Icon icon="circle-4" /> Choose the runs you want to bulk action

<Icon icon="circle-5" /> Name your bulk action (optional)

<Icon icon="circle-6" /> Choose the action you want to perform, replay or cancel

<Icon icon="circle-7" /> Click the "Replay" or "Cancel" button and confirm in the dialog

<img alt="Access bulk actions" />

<Icon icon="circle-8" /> You'll now view the bulk action processing from the bulk action page

<Icon icon="circle-9" /> You can replay or view the runs from this page

<img alt="Access bulk actions" />

<Note>
  You can only cancel runs that are in states that allow cancellation (like QUEUED or EXECUTING).
  Runs that are already completed, failed, or in other final states by the time the bulk action process gets to them, cannot be canceled.
</Note>
