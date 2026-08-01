---
title: "Composio Tool"
source: https://docs.crewai.com/v1.15.10/en/tools/automation/composiotool
path: v1.15.10/en/tools/automation/composiotool
---

Composio provides 250+ production-ready tools for AI agents with flexible authentication management.

# `ComposioToolSet`

## Description

Composio is an integration platform that allows you to connect your AI agents to 250+ tools. Key features include:

* **Enterprise-Grade Authentication**: Built-in support for OAuth, API Keys, JWT with automatic token refresh
* **Full Observability**: Detailed tool usage logs, execution timestamps, and more

## Installation

To incorporate Composio tools into your project, follow the instructions below:

```shell theme={null}
pip install composio composio-crewai
pip install crewai
```

After the installation is complete, set your Composio API key as `COMPOSIO_API_KEY`. Get your Composio API key from [here](https://platform.composio.dev)

## Example

The following example demonstrates how to initialize the tool and execute a github action:

1. Initialize Composio with CrewAI Provider

```python Code theme={null}
from composio_crewai import ComposioProvider
from composio import Composio
from crewai import Agent, Task, Crew

composio = Composio(provider=ComposioProvider())
```

2. Create a new Composio Session and retrieve the tools

<CodeGroup>
  ```python theme={null}
  session = composio.create(
      user_id="your-user-id",
      toolkits=["gmail", "github"] # optional, default is all toolkits
  )
  tools = session.tools()
  ```

  Read more about sessions and user management [here](https://docs.composio.dev/docs/configuring-sessions)
</CodeGroup>

3. Authenticating users manually

Composio automatically authenticates the users during the agent chat session. However, you can also authenticate the user manually by calling the `authorize` method.

```python Code theme={null}
connection_request = session.authorize("github")
print(f"Open this URL to authenticate: {connection_request.redirect_url}")
```

4. Define agent

```python Code theme={null}
crewai_agent = Agent(
    role="GitHub Agent",
    goal="You take action on GitHub using GitHub APIs",
    backstory="You are AI agent that is responsible for taking actions on GitHub on behalf of users using GitHub APIs",
    verbose=True,
    tools=tools,
    llm= # pass an llm
)
```

5. Execute task

```python Code theme={null}
task = Task(
    description="Star a repo composiohq/composio on GitHub",
    agent=crewai_agent,
    expected_output="Status of the operation",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

crew.kickoff()
```

* More detailed list of tools can be found [here](https://docs.composio.dev/toolkits)
