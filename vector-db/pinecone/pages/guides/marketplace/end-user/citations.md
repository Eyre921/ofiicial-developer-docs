---
title: "Understand answers"
source: https://docs.pinecone.io/guides/marketplace/end-user/citations
path: guides/marketplace/end-user/citations
---

Read citations, work with visual components, export and share answers, and give feedback in a Pinecone Marketplace knowledge application.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Every answer in a Pinecone Marketplace knowledge application is grounded in connected documents and includes citations. This page covers how to read citations, what visual components mean, how to export and share answers, and how to give feedback that helps the operator improve the application.

## Citations and sources

Citations let you verify an answer and read the original context.

### How citations look

Citations appear inline with the answer, usually as numbered references that link to specific source documents. The sources panel lists the cited documents in order.

### Opening a source

Click a citation or a source in the panel to open the document viewer. The viewer shows the full document scrolled to the cited section where possible, the document's title and metadata, and links to the original source if the operator has enabled them.

### When an answer has no citations

A knowledge application is built to ground every answer. If you see an answer without citations, that usually means the response was a meta-statement (such as a refusal or a clarifying question) rather than content from a document.

If you see what looks like a substantive answer with no citations, share that with the operator. See [Give feedback](#give-feedback).

### Trusting an answer

Citations are how you verify trust. A useful habit:

* For high-stakes questions, open at least one cited source.
* Confirm the source actually says what the answer claims.
* If the source contradicts the answer, give negative feedback so the operator can investigate.

## Visual components

Some answers are easier to read as a table, a timeline, or a map than as plain text. A knowledge application can render the following visual components when an answer fits a structured shape.

| Component         | When you see it                                              |
| ----------------- | ------------------------------------------------------------ |
| Comparison tables | Side-by-side comparisons of options, plans, or policies      |
| Content cards     | Browsable summaries of documents or items                    |
| Timelines         | Sequences of dated events                                    |
| Progress trackers | Step-by-step processes                                       |
| Coverage matrices | Two-dimensional lookups, such as benefits by plan and region |
| Geolocation maps  | Locations and venue context                                  |

### Interacting with components

* Most components are read-only views. Click rows, cards, or items to drill into the underlying source documents.
* Components include citations the same way text answers do.
* If a component does not fit on your screen, it will scroll horizontally where appropriate.

### Why an answer is sometimes a table and sometimes prose

The application picks the shape based on the question, the answer, and the components the operator has enabled. If the operator has not enabled tables, you will get prose even for a comparison question. If you would prefer a different shape for a recurring kind of question, [give feedback](#give-feedback).

## Export and share

You can save and share individual answers or whole conversations.

### Export to PDF

To save an answer or conversation as a PDF, open the answer or conversation, use the export action in the conversation header, choose **PDF**, and save the file. PDF exports include the questions, answers, citations, and any rendered components.

### Share to Slack

If the operator has enabled the Slack share action, open the answer, use the share action, pick a Slack channel or person, and optionally add a note. The shared message includes a summary, citations, and a link back to the answer in the application.

### Linking back to a conversation

The conversation URL is shareable with anyone who has access to the application. Sharing the URL takes the recipient to the same conversation when they open it.

### Privacy

When you share or export an answer, you are sharing the content as it appeared to you. The recipient still needs access to the application to follow citations or continue the conversation.

## Give feedback

Feedback is the most direct way to help the operator improve a knowledge application. Operators can see ratings and comments per answer.

### How to give feedback

After each answer, you can:

* Give a thumbs-up or thumbs-down rating.
* Add an optional comment explaining what was good or what was wrong.

Feedback is associated with the conversation and the version of the application you used.

### When to give feedback

* The answer is wrong or missing context: thumbs down with a comment.
* The application refused a question you think it should be able to answer: thumbs down with a comment that includes the question.
* The answer was exactly what you needed: thumbs up.
* The answer was useful but the format could be better (for example, a table would have been clearer): thumbs up with a comment.

### What happens with your feedback

Feedback shows up in the operator's analytics dashboard and event log. Operators use the patterns to add or rework content in connected sources, tighten or loosen scope and guardrails, adjust operating parameters, or decide whether to roll back a recent publish.

If the operator publishes a new version that addresses your feedback, ask the same question again. The application updates as it improves.
