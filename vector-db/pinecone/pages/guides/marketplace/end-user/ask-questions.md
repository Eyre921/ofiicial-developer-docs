---
title: "Ask questions"
source: https://docs.pinecone.io/guides/marketplace/end-user/ask-questions
path: guides/marketplace/end-user/ask-questions
---

Tips for end users on asking clear, specific questions in a Pinecone Marketplace knowledge application, using follow-ups, and handling clarifications.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

A knowledge application answers questions in plain language, grounded in the documents an operator has connected. The way you ask affects how useful the answer is.

## How to ask

* **Be specific.** "What is the parental leave policy in California?" beats "tell me about leave."
* **Include the context that matters.** Region, plan, role, product line, and dates often change the answer.
* **Use follow-ups.** Once you get an answer, ask the next question naturally; the application carries context across turns.

## Suggested follow-ups

After each answer, the application may suggest related questions. Use them to drill down without retyping context.

## When the application asks you a question back

If a question is ambiguous or missing context, the application asks you to clarify. Pick the option you meant or provide the missing detail. The application uses your clarification for the rest of the conversation.

## When the application says it does not know

A knowledge application is built to be honest about its scope. Common refusals:

* **Out of scope**: the application does not have content that addresses your question. The refusal will list what the application can help with.
* **Blocked**: the application has been configured not to engage with the request.

If you think the application should be able to answer but is refusing, share that feedback with the operator. See [Give feedback](/guides/marketplace/end-user/citations#give-feedback).

## What about completely new conversations?

Starting a new conversation resets context. Use a new conversation when you are switching topics so the application does not carry over slot values from a different question.
