---
title: "CrewAI"
source: https://docs.together.ai/docs/crewai
path: docs/crewai
---

Using CrewAI with Together

CrewAI is an open source production-grade framework for orchestrating AI agent systems. It enables multiple AI agents to collaborate effectively by assuming roles and working toward shared goals. The framework supports both simple automations and complex applications that require coordinated agent behavior.

## Installing Libraries

<CodeGroup>
  ```shell Shell theme={null}
  uv pip install crewai
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

<CodeGroup>
  ```python Python theme={null}
  import os
  from crewai import LLM, Task, Agent, Crew

  llm = LLM(
      model="together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo",
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.ai/v1",
  )

  research_agent = Agent(
      llm=llm,
      role="Research Analyst",
      goal="Find and summarize information about specific topics",
      backstory="You are an experienced researcher with attention to detail",
      verbose=True,  # Enable logging for debugging
  )

  research_task = Task(
      description="Conduct a thorough research about AI Agents.",
      expected_output="A list with 10 bullet points of the most relevant information about AI Agents",
      agent=research_agent,
  )

  # Execute the crew
  crew = Crew(
      agents=[research_agent],
      tasks=[research_task],
      verbose=True,
  )

  result = crew.kickoff()

  # Accessing the task output
  task_output = research_task.output

  print(task_output)
  ```
</CodeGroup>

## Example Output

```
[2025-03-09 16:20:14][🚀 CREW 'CREW' STARTED, 42A4F700-E955-4794-B6F3-6EA6EF279E93]: 2025-03-09 16:20:14.069394

[2025-03-09 16:20:14][📋 TASK STARTED: CONDUCT A THOROUGH RESEARCH ABOUT AI AGENTS.]: 2025-03-09 16:20:14.085335

[2025-03-09 16:20:14][🤖 AGENT 'RESEARCH ANALYST' STARTED TASK]: 2025-03-09 16:20:14.096438
# Agent: Research Analyst
## Task: Conduct a thorough research about AI Agents.

[2025-03-09 16:20:14][🤖 LLM CALL STARTED]: 2025-03-09 16:20:14.096671

[2025-03-09 16:20:18][✅ LLM CALL COMPLETED]: 2025-03-09 16:20:18.993612

# Agent: Research Analyst
## Final Answer:
* AI Agents are computer programs that use artificial intelligence (AI) to perform tasks that typically require human intelligence, such as reasoning, problem-solving, and decision-making. They can be used in a variety of applications, including virtual assistants, customer service chatbots, and autonomous vehicles.
* There are several types of AI Agents, including simple reflex agents, model-based reflex agents, goal-based agents, and utility-based agents. Each type of agent has its own strengths and weaknesses, and is suited to specific tasks and environments.
* AI Agents can be classified into two main categories: narrow or weak AI, and general or strong AI. Narrow AI is designed to perform a specific task, while general AI is designed to perform any intellectual task that a human can.
* AI Agents use a variety of techniques to make decisions and take actions, including machine learning, deep learning, and natural language processing. They can also use sensors and other data sources to perceive their environment and make decisions based on that information.
* One of the key benefits of AI Agents is their ability to automate repetitive and mundane tasks, freeing up human workers to focus on more complex and creative tasks. They can also provide 24/7 customer support and help to improve customer engagement and experience.
* AI Agents can be used in a variety of industries, including healthcare, finance, and transportation. For example, AI-powered chatbots can be used to help patients schedule appointments and access medical records, while AI-powered virtual assistants can be used to help drivers navigate roads and avoid traffic.
* Despite their many benefits, AI Agents also have some limitations and challenges. For example, they can be biased if they are trained on biased data, and they can struggle to understand the nuances of human language and behavior.
* AI Agents can be used to improve decision-making and problem-solving in a variety of contexts. For example, they can be used to analyze large datasets and identify patterns and trends, and they can be used to simulate different scenarios and predict outcomes.
* The development and use of AI Agents raises important ethical and social questions, such as the potential impact on employment and the need for transparency and accountability in AI decision-making. It is essential to consider these questions and develop guidelines and regulations for the development and use of AI Agents.
* The future of AI Agents is likely to involve the development of more advanced and sophisticated agents that can learn and adapt in complex and dynamic environments. This may involve the use of techniques such as reinforcement learning and transfer learning, and the development of more human-like AI Agents that can understand and respond to human emotions and needs.


[2025-03-09 16:20:19][✅ AGENT 'RESEARCH ANALYST' COMPLETED TASK]: 2025-03-09 16:20:19.012674

[2025-03-09 16:20:19][✅ TASK COMPLETED: CONDUCT A THOROUGH RESEARCH ABOUT AI AGENTS.]: 2025-03-09 16:20:19.012784

[2025-03-09 16:20:19][✅ CREW 'CREW' COMPLETED, 42A4F700-E955-4794-B6F3-6EA6EF279E93]: 2025-03-09 16:20:19.027344
```
