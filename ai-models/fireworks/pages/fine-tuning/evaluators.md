---
title: "Evaluators"
source: https://docs.fireworks.ai/fine-tuning/evaluators
path: fine-tuning/evaluators
---

Understand the fundamentals of evaluators and reward functions in reinforcement fine-tuning

An evaluator (also called a reward function) is code that scores model outputs from 0.0 (worst) to 1.0 (best). During reinforcement fine-tuning, your evaluator guides the model toward better responses by providing feedback on its generated outputs.

## Why evaluators matter

Unlike supervised fine-tuning where you provide perfect examples, RFT uses evaluators to define what "good" means. This is powerful because:

* **No perfect data required** - Just prompts and a way to score outputs
* **Encourages exploration** - Models learn strategies, not just patterns
* **Noise tolerant** - Even noisy signals can improve model performance
* **Encodes domain expertise** - Complex rules and logic that are hard to demonstrate with examples

## Anatomy of an evaluator

Every evaluator has three core components:

### 1. Input data

The prompt and any ground truth data needed for evaluation:

```python theme={null}
{
  "messages": [
    {"role": "system", "content": "You are a math tutor."},
    {"role": "user", "content": "What is 15 * 23?"}
  ],
  "ground_truth": "345"  # Optional additional data
}
```

### 2. Model output

The assistant's response to evaluate:

```python theme={null}
{
  "role": "assistant",
  "content": "Let me calculate that step by step:\n15 * 23 = 345"
}
```

### 3. Scoring logic

Code that compares the output to your criteria:

```python theme={null}
def evaluate(model_output: str, ground_truth: str) -> float:
    # Extract answer from model's response
    predicted = extract_number(model_output)
    
    # Score it
    if predicted == int(ground_truth):
        return 1.0  # Perfect
    else:
        return 0.0  # Wrong
```

## Types of evaluators

### Rule-based evaluators

Check if outputs match specific patterns or rules:

* **Exact match** - Output exactly equals expected value
* **Contains** - Output includes required text
* **Regex** - Output matches a pattern
* **Format validation** - Output follows required structure (e.g., valid JSON)

<Tip>
  Start with rule-based evaluators. They're simple, fast, and surprisingly effective.
</Tip>

### Execution-based evaluators

Run code or commands to verify correctness:

* **Code execution** - Run generated code and check results
* **Test suites** - Pass generated code through unit tests
* **API calls** - Execute commands and verify outcomes
* **Simulations** - Run agents in environments and measure success

### LLM-as-judge evaluators

Use another model to evaluate quality:

* **Rubric scoring** - Judge outputs against criteria
* **Comparative ranking** - Compare multiple outputs
* **Natural language assessment** - Evaluate subjective qualities like helpfulness

## Scoring guidelines

Your evaluator should return a score between 0.0 and 1.0:

| Score range | Meaning | Example                     |
| ----------- | ------- | --------------------------- |
| 1.0         | Perfect | Exact correct answer        |
| 0.7-0.9     | Good    | Right approach, minor error |
| 0.4-0.6     | Partial | Some correct elements       |
| 0.1-0.3     | Poor    | Wrong but attempted         |
| 0.0         | Failure | Completely wrong            |

<Note>
  Binary scoring (0.0 or 1.0) works well for many tasks. Use gradual scoring when you can meaningfully distinguish between partial successes.
</Note>

## Best practices

<AccordionGroup>
  <Accordion title="Start simple, iterate">
    Begin with basic evaluation logic and refine over time:

    ```python theme={null}
    # Start here
    score = 1.0 if predicted == expected else 0.0

    # Then refine if needed
    score = calculate_similarity(predicted, expected)
    ```

    Start with the simplest scoring approach that captures your core requirements. You can always add sophistication later based on training results.
  </Accordion>

  <Accordion title="Make evaluators fast">
    Training generates many outputs to evaluate, so performance matters:

    * **Cache expensive computations**: Store results of repeated calculations
    * **Use timeouts for code execution**: Prevent hanging on infinite loops
    * **Batch API calls when possible**: Reduce network overhead
    * **Profile slow evaluators and optimize**: Identify and fix bottlenecks

    Aim for evaluations that complete in seconds, not minutes. Slow evaluators directly increase training time and cost.
  </Accordion>

  <Accordion title="Handle edge cases">
    Models will generate unexpected outputs, so build robust error handling:

    ```python theme={null}
    try:
        result = execute_code(model_output)
        score = check_result(result)
    except TimeoutError:
        score = 0.0  # Code ran too long
    except SyntaxError:
        score = 0.0  # Invalid code
    except Exception as e:
        score = 0.0  # Any other error
    ```

    Anticipate and gracefully handle malformed outputs, syntax errors, timeouts, and edge cases specific to your domain.
  </Accordion>

  <Accordion title="Avoid reward hacking">
    Models will exploit evaluation weaknesses, so design defensively:

    **Example: Length exploitation**

    If you score outputs by length, the model might generate verbose nonsense. Add constraints:

    ```python theme={null}
    # Bad: Model learns to write long outputs
    score = min(len(output) / 1000, 1.0)

    # Better: Require correctness AND reasonable length
    if is_correct(output):
        score = 1.0 if len(output) < 500 else 0.8
    else:
        score = 0.0
    ```

    **Example: Format over substance**

    If you only check JSON validity, the model might return valid but wrong JSON. Check content too:

    ```python theme={null}
    # Bad: Only checks format
    score = 1.0 if is_valid_json(output) else 0.0

    # Better: Check format AND content
    if is_valid_json(output):
        data = json.loads(output)
        score = evaluate_content(data)
    else:
        score = 0.0
    ```

    Always combine format checks with content validation to prevent models from gaming the system.
  </Accordion>
</AccordionGroup>

## Debugging evaluators

Test your evaluator before training. Look for:

* **Correct scoring** - Good outputs score high, bad outputs score low
* **Reasonable runtime** - Each evaluation completes in reasonable time
* **Clear feedback** - Evaluation reasons explain scores

<Tip>
  Run your evaluator on manually created good and bad examples first. If it doesn't score them correctly, fix the evaluator before training.
</Tip>

## Next steps

<CardGroup>
  <Card title="Connect environments" icon="code" href="/fine-tuning/connect-environments">
    Connect to your environment for single and multi-turn agents
  </Card>

  <Card title="Quickstart: Math solver" icon="calculator" href="/fine-tuning/quickstart-math">
    Follow a complete example building and using an evaluator
  </Card>
</CardGroup>
