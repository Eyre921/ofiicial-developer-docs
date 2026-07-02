---
title: "Use annotation queues"
source: https://docs.langchain.com/langsmith/annotation-queues
path: langsmith/annotation-queues
---

*Annotation queues* give human reviewers a focused workflow for attaching feedback to specific [runs](/langsmith/observability-concepts#runs). While you can always annotate [traces](/langsmith/observability-concepts#traces) inline, annotation queues let you group runs together, prescribe rubrics, and track reviewer progress.

<Info>
  You can also manage annotation queues and feedback configs programmatically with the SDK. Refer to [Manage feedback & annotation queues programmatically](/langsmith/annotation-queues-sdk).
</Info>

LangSmith supports two queue styles:

* [**Single-run annotation queues**](#single-run-annotation-queues) present one run at a time and let reviewers submit any rubric feedback you configure. Single-run queues also support [assertions](/langsmith/assertions) to capture acceptance criteria for offline evaluation.
* [**Pairwise annotation queues (PAQs)**](#pairwise-annotation-queues) present two runs side-by-side so reviewers can quickly decide which output is better (or if they are equivalent) against the rubric items you define.

<Tip>
  For a demonstration of using annotation queues, watch the [Getting started with annotation queues](#video-guide) video guide.
</Tip>

## Single-run annotation queues

Single-run queues present one run at a time and let reviewers submit any rubric feedback you configure. They can be created directly from the **Annotation queues** section in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-annotation-queues).

### Create a single-run queue

1. Navigate to **Annotation Queues** in the left navigation.
2. Click **+ Annotation Queue** in the top-left corner.

   <img alt="Create Annotation Queue form with Basic Details, Annotation Rubric, and Feedback sections." />

#### Basic details

1. Fill in the **Name** and **Description** of the queue.
2. Optionally assign a **default dataset** to streamline exporting reviewed runs into a dataset in your LangSmith [workspace](/langsmith/administration-overview#workspaces).

#### Annotation rubric

1. Draft some high-level **Instructions** for your annotators, which will be shown in the sidebar on every run.
2. Click **+ Add a feedback rubric** to add feedback keys to your annotation queue. Annotators will be presented with these feedback keys on each run.
3. Add a description for each, as well as a short description of each category, if the feedback is categorical.

   <img alt="Annotation queue rubric form with instructions and desired feedback entered." />

   For example, with the descriptions in the previous screenshot, reviewers will see the **Annotation Rubric** details in the right-hand pane of the UI.

   <img alt="The rendered rubric for reviewers from the example instructions." />

#### Collaborator settings

Set a number of reviewers or the maximum time you want to reserve the item to a collaborator. When there are multiple annotators for a run, you can choose to have the run stay in the queue until all reviewers have marked it as **Done**. The settings are as follows:

* **All workspace members review each run**: When enabled, a run remains in the queue until every [workspace](/langsmith/administration-overview#workspaces) member has marked their review as **Done**.

* **Enable reservations on runs**: Reserving a run locks it for your review for a set amount of time. While a run is reserved, other reviewers can view it but cannot add feedback or notes. Reservations are disabled if all workspace members review each run.

  If a reviewer has viewed a run and then leaves the run without marking it **Done**, the reservation will expire after the specified **Reservation length**. The run is then released back into the queue and can be reserved by another reviewer.

  <Note>
    Clicking **Requeue** for a run's annotation will only move the current run to the end of the current user's queue; it won't affect the queue order of any other user. It will also release the reservation that the current user has on that run.
  </Note>

* **Number of reviewers per run**: This determines the number of reviewers that must mark a run as **Done** for it to be removed from the queue.

  * Reviewers cannot view the feedback left by other reviewers.
  * Comments on runs are visible to all reviewers.

  <Note>
    The **Number of reviewers per run** setting is hidden when **Use assigned reviewers** is enabled (see below).
  </Note>

* **Use assigned reviewers**: Enable this toggle to use specific workspace members instead of a count-based threshold. When enabled:

  * A multi-select user picker appears so you can choose specific workspace members as assigned reviewers.
  * A run is marked **Completed** only when every assigned reviewer has submitted their review. Queue items progress through three states: **Needs Review** → **Needs Others' Review** → **Completed**.
  * Non-assigned workspace members can still annotate runs, but their submissions do not count toward completion.
  * Any workspace member can edit the assigned reviewers list in the queue settings.

  <Note>
    When you add a new assigned reviewer to a queue that already has completed items, those items do not revert to pending. If you remove an assigned reviewer, any items they had not yet reviewed recalculate their completion status.
  </Note>

Because of these settings, the number of runs visible to each reviewer can differ from the total queue size.

### Edit a queue's settings

1. Open the **Edit Annotation Queue** panel for the annotation queue you want to edit. You can access this panel in two ways:

   * In the **Annotation queues** list, click the **Actions**  icon <Icon icon="dots-vertical" /> at the right of the queue's row. Select <Icon icon="pencil" /> **Edit** from the dropdown.
   * In the annotation queue view, click the **Settings** icon <Icon icon="settings" /> in the top-right corner.

2. In the **Edit Annotation Queue** panel, modify any of the settings you configured during queue creation and click **Save**.

### Assign runs to a single-run queue

There are several ways to populate a single-run queue with work items:

* **From the Details view**: Click **Add to Annotation Queue** in the top-right corner of any trace. You can add any intermediate [run](/langsmith/observability-concepts#runs), but not the root span.

  <img alt="Trace view with the Add to Annotation Queue button highlighted at the top of the screen." />

* **From the runs table**: Select multiple runs, then click **Add to Annotation Queue** at the bottom of the page.

  <img alt="View of the runs table with runs selected. Add to Annotation Queue button at the bottom of the page." />

* **Automation rules**: [Set up a rule](/langsmith/rules) to automatically assign runs that match a filter (for example, errors or low user scores) into a queue.

* **Datasets & experiments**: Select one or more [experiments](/langsmith/evaluation-concepts#experiment) within a dataset and click **<Icon icon="pencil" /> Annotate**. Choose an existing queue or create a new one, then confirm the (single-run) queue option.

  <img alt="Selected experiments with the Annotate button at the bottom of the page." />

### Review a single-run queue

1. Navigate to the **Annotation Queues** section through the left-hand navigation bar.

   The queue list includes an **Assigned Reviewers** column showing which reviewers are assigned to each queue. To see only queues assigned to you, click the **Assigned to me** filter at the top of the list.

2. Click on the queue you want to review. This will take you to a focused, cyclical view of the runs in the queue that require review. A left side panel shows the status of each run (**Needs Review**, **Needs Others' Review**, **Completed**).

3. Add **Reviewer Notes**, score [**Feedback**](/langsmith/observability-concepts#feedback) criteria, or mark the run as reviewed. To build a dataset, edit the run's input and output to create a corrected reference example and click **Add to Dataset**. Click **Delete** to remove the run from the queue for all users, regardless of any current reservations or queue settings.

   Instead of crafting a corrected reference output by hand, you can [write assertions](/langsmith/assertions) directly in the review side panel and save them as the example's expected output.

   <Tip>
     The keyboard shortcuts that are next to each option can help streamline the review process.
   </Tip>

## Pairwise annotation queues

Pairwise annotation queues (PAQs) present two runs side-by-side so reviewers can quickly decide which output is better (or if they are equivalent) against the rubric items you define. They are designed for fast A/B comparisons between two experiments (often a baseline vs. a candidate model) and must be created from the **Datasets & Experiments** pages.

### Create a pairwise queue

1. Navigate to **Datasets & Experiments**, open a dataset, and select **exactly two experiments** you want to compare.

2. Click **Annotate**. In the popover, choose **Add to Pairwise Annotation Queue**. (The button is disabled until exactly two experiments are selected.)

   <img alt="Popover showing the &#x22;Add to Pairwise Annotation Queue&#x22; card highlighted after two experiments are selected." />

3. Decide whether to send the experiments to an existing pairwise queue or create a new one.

4. Provide the queue details:
   * **Basic details** (name and description)
   * **Instructions & rubrics** tailored to pairwise scoring
   * **Collaborator settings** (reviewer count, reservations, reservation length)

5. Submit the form to create the queue. LangSmith immediately pairs runs from the two experiments and populates the queue.

Key differences for PAQs:

* **Experiments**: You must provide two experiment sessions up front. LangSmith automatically pairs their runs in chronological order and populates the queue during creation.
* **Rubric**: Pairwise rubric items only require a feedback key and (optionally) a description. Annotators decide whether Run A, Run B, or both are better for each rubric item.
* **Dataset**: Pairwise queues do not use a default dataset, because comparisons span two experiments.
* **Reservations & reviewers**: The same collaborator controls apply. Reservations help prevent two people from judging the same comparison simultaneously.

### Add more comparisons to a pairwise queue

If you need to add more comparisons later, return to **Datasets & Experiments**, select the two experiments again, and choose **Add to Pairwise Annotation Queue** to append new pairs.

Selecting two experiments and creating a PAQ automatically pairs the runs. When augmenting an existing PAQ, LangSmith preserves historical comparisons and appends new pairs to the queue.

### Review a pairwise queue

1. From **Annotation queues**, select the pairwise queue you want to review.
2. Each queue item displays Run A on the left and Run B on the right, along with your rubric.
3. For every rubric item:
   * Choose **A is better**, **B is better**, or **Equal**. The UI records binary feedback on both runs behind the scenes.
   * Use hotkeys `A`, `B`, or `E` to lock in your choice.
4. Once you finish all rubric items, press **Done** (or `Enter` on the final rubric item) to advance to the next comparison.
5. Optional actions:
   * Leave comments tied to either run.
   * Requeue the comparison if you need to revisit it later.
   * Open the Details view for deeper debugging.

Reservations, reviewer thresholds, and comments behave identically to those in single-run queues, enabling teams to use different queue types without modifying their existing workflow.

<img alt="Pairwise review screen showing runs side-by-side with the feedback pane containing A/B/Equal buttons and keyboard shortcuts." />

<Check>
  Consider routing runs that already have user feedback (e.g., thumbs-down) into a single-run queue for triage and a pairwise queue for head-to-head comparisons against a stronger baseline. This helps you identify regressions quickly. To learn more about how to capture user feedback from your LLM application, follow the guide on [attaching user feedback](/langsmith/attach-user-feedback).
</Check>

## Video guide

<iframe title="YouTube video player" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/annotation-queues.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
