---
title: "Agent workflows"
source: https://docs.together.ai/docs/workflows
path: docs/workflows
---

Orchestrating together multiple language model calls to solve complex tasks.

In order to solve complex tasks a single LLM call might not be enough. Here you'll see how to solve complex problems by orchestrating multiple language models.

The execution pattern of actions within an agent workflow is determined by its control flow. Various control flow types enable different capabilities:

## Sequential

Tasks execute one after another when later steps depend on earlier ones. For example, a SQL query can only run after being translated from natural language.

Learn more about [Sequential Workflows](/docs/sequential-agent-workflow)

## Parallel

Multiple tasks execute simultaneously. For instance, retrieving prices for multiple products at once rather than sequentially.

Learn more about [Parallel Workflows](/docs/parallel-workflows)

## Conditional (if statement)

The workflow branches based on evaluation results. An agent might analyze a company's earnings report before deciding to buy or sell its stock.

Learn more about [Conditional Workflows](/docs/conditional-workflows)

## Iterative (for loop)

A task repeats until a condition is met. For example, generating random numbers until finding a prime number.

Learn more about [Iterative Workflows](/docs/iterative-workflow)

When evaluating which workflow to use for a task consider tradeoffs between task complexity, latency, and cost. Workflows with parallel execution capabilities can dramatically reduce perceived latency, especially for tasks involving multiple independent operations like scraping several websites. Iterative workflows are great for optimizing for a given task until a termination condition is met but can be costly.
