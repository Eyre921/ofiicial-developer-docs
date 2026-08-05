---
title: "Success evaluation"
source: https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/success-evaluation.md
path: docs/eleven-agents/customization/agent-analysis/success-evaluation
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Success evaluation

Success evaluation allows you to define custom goals and success metrics for your conversations. Each criterion is evaluated against the conversation transcript and returns a result of `success`, `failure`, or `unknown`, along with a detailed rationale.

## Overview

Success evaluation uses LLM-powered analysis to assess conversation quality against your specific business objectives. This enables systematic performance measurement and quality assurance across all customer interactions.

### How it works

Each evaluation criterion analyzes the conversation transcript using a custom prompt and returns:

* **Result**: `success`, `failure`, or `unknown`
* **Rationale**: Detailed explanation of why the result was chosen

### Types of evaluation criteria

#### Goal prompt criteria

**Goal prompt criteria** pass the conversation transcript along with a custom prompt to an LLM to verify if a specific goal was met. This is the most flexible type of evaluation and can be used for complex business logic.

**Examples:**

* Customer satisfaction assessment
* Issue resolution verification
* Compliance checking
* Custom business rule validation

## Configuration

#### Access agent settings

Navigate to your agent's dashboard and select the **Analysis** tab to configure evaluation criteria.

![Analysis settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/fee8bc444d5436c71eae3829b9ec8d5cdb6a57c4d4efe6483d7bfed2b066e438/assets/images/conversational-ai/analysis-settings.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260805%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260805T233318Z&X-Amz-Expires=604800&X-Amz-Signature=5a1c775949e507f7441a1dfe96243cf956c2477d87fec41b0cb9c0f07de604c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add evaluation criteria

Click **Add criteria** to create a new evaluation criterion.

Define your criterion with:

* **Identifier**: A unique name for the criterion (e.g., `user_was_not_upset`)
* **Description**: Detailed prompt describing what should be evaluated

![Setting up evaluation criteria](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0e1ad5eec745d5733701dcf8cbf4f413473f55a0b5f26add4faac540dbbd086a/assets/images/conversational-ai/evaluation.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260805%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260805T233318Z&X-Amz-Expires=604800&X-Amz-Signature=7324c7d168c4ccf036628741f91a0c6901de5da149bfc2b38b553386f8010cde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Evaluation criteria are limited to 30 per agent.

#### View results

After conversations complete, evaluation results appear in your conversation history dashboard. Each conversation shows the evaluation outcome and rationale for every configured criterion.

![Evaluation results in conversation history](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/657888630b51010fa6920275cfbb8f3dce51c0cbcfdb8ecf3d5d938f17a8186a/assets/images/conversational-ai/evaluation_result.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260805%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260805T233318Z&X-Amz-Expires=604800&X-Amz-Signature=6fccd221d5ad3086347c22569aacb1a46c01bbb5008b5342dca17a5e5b407895&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Best Practices

#### Writing effective evaluation prompts

* Be specific about what constitutes success vs. failure
* Include edge cases and examples in your prompt
* Use clear, measurable criteria when possible
* Test your prompts with various conversation scenarios

#### Common evaluation criteria

* **Customer satisfaction**: "Mark as successful if the customer expresses satisfaction or their
  issue was resolved" - **Goal completion**: "Mark as successful if the customer completed the
  requested action (booking, purchase, etc.)" - **Compliance**: "Mark as successful if the agent
  followed all required compliance procedures" - **Issue resolution**: "Mark as successful if the
  customer's technical issue was resolved during the call"

#### Handling ambiguous results

The `unknown` result is returned when the LLM cannot determine success or failure from the transcript. This often happens with:

* Incomplete conversations
* Ambiguous customer responses
* Missing information in the transcript

Monitor `unknown` results to identify areas where your criteria prompts may need refinement.

## Use Cases

#### Customer Support Quality

Measure issue resolution rates, customer satisfaction, and support quality metrics to improve
service delivery.

#### Sales Performance

Track goal achievement, objection handling, and conversion rates across sales conversations.

#### Compliance Monitoring

Ensure agents follow required procedures and capture necessary consent or disclosure
confirmations.

#### Training & Development

Identify coaching opportunities and measure improvement in agent performance over time.

## Troubleshooting

#### Evaluation criteria returning unexpected results

* Review your prompt for clarity and specificity
* Test with sample conversations to validate logic
* Consider edge cases in your evaluation criteria
* Check if the transcript contains sufficient information for evaluation

#### High frequency of 'unknown' results

* Ensure your prompts are specific about what information to look for - Consider if conversations
  contain enough context for evaluation - Review transcript quality and completeness - Adjust
  criteria to handle common edge cases

#### Performance considerations

* Each evaluation criterion adds processing time to conversation analysis
* Complex prompts may take longer to evaluate
* Consider the trade-off between comprehensive analysis and response time
* Monitor your usage to optimize for your specific needs

Success evaluation results are available through [Post-call
Webhooks](/docs/eleven-agents/workflows/post-call-webhooks) for integration with external systems
and analytics platforms.
