---
title: "What is a token?"
source: https://docs.fireworks.ai/faq-new/models-inference/what-is-a-token
path: faq-new/models-inference/what-is-a-token
---

A token is the unit Fireworks uses to read, write, and bill model text. Learn how input, cached input, and generated tokens differ.

A token is the unit a model reads and writes. It is usually a piece of a word, not a whole word or a character.

Fireworks bills Serverless usage in three token counts:

* **Prompt tokens** are what you send.
* **Cached prompt tokens** are the part of that prompt Fireworks already computed. They cost less. The discount depends on the model.
* **Generated tokens** are what the model writes back.

The `usage` object on each response is the source of truth for those counts. Prices are on [Serverless pricing](/serverless/pricing). More words are in the [glossary](/getting-started/glossary).
