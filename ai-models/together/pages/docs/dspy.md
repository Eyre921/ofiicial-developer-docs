---
title: "DSPy"
source: https://docs.together.ai/docs/dspy
path: docs/dspy
---

Using DSPy with Together AI

DSPy is a framework for programming language models rather than relying on static prompts. It enables you to build modular AI systems with code instead of hand-crafted prompting, and it offers methods to automatically optimize these systems.

Features

* Programmatic approach to LLM interactions through Python
* Modular components for building complex AI pipelines
* Self-improvement algorithms that optimize prompts and weights
* Support for various applications from simple classifiers to RAG systems and agent loops

## Installing libraries

<CodeGroup>
  ```shell Shell theme={null}
  pip install -U dspy
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

Setup and connect DSPy to LLMs on Together AI

<CodeGroup>
  ```python Python theme={null}
  import dspy

  # Configure dspy with an LLM from Together AI
  lm = dspy.LM(
      "together_ai/togethercomputer/llama-2-70b-chat",
      api_key=os.environ.get("TOGETHER_API_KEY"),
      api_base="https://api.together.ai/v1",
  )

  # Now you can call the LLM directly as follows
  lm("Say this is a test!", temperature=0.7)  # => ['This is a test!']
  lm(
      messages=[{"role": "user", "content": "Say this is a test!"}]
  )  # => ['This is a test!']
  ```
</CodeGroup>

Now we can set up a DSPy module, like `dspy.ReAct` with a task-specific signature. For example, `question -> answer: float` tells the module to take a question and to produce a floating point number answer below.

<CodeGroup>
  ```python Python theme={null}
  # Configure dspy to use the LLM
  dspy.configure(lm=lm)


  # Gives the agent access to a python interpreter
  def evaluate_math(expression: str):
      return dspy.PythonInterpreter({}).execute(expression)


  # Gives the agent access to a wikipedia search tool
  def search_wikipedia(query: str):

      results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(
          query, k=3
      )
      return [x["text"] for x in results]


  # setup ReAct module with question and math answer signature
  react = dspy.ReAct(
      "question -> answer: float",
      tools=[evaluate_math, search_wikipedia],
  )

  pred = react(
      question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?"
  )

  print(pred.answer)
  ```
</CodeGroup>

## Next steps

<Info>
  ### DSPy - Together AI Notebook

  Learn more about building agents using DSPy with Together AI in this [notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/DSPy/DSPy_Agents.ipynb).
</Info>
