---
title: "SingleStore Search Tool"
source: https://docs.crewai.com/v1.15.8/en/tools/database-data/singlestoresearchtool
path: v1.15.8/en/tools/database-data/singlestoresearchtool
---

The `SingleStoreSearchTool` safely executes SELECT/SHOW queries on SingleStore with pooling.

# `SingleStoreSearchTool`

## Description

Execute read‑only queries (`SELECT`/`SHOW`) against SingleStore with connection pooling and input validation.

## Installation

```shell theme={null}
uv add crewai-tools[singlestore]
```

## Environment Variables

Variables like `SINGLESTOREDB_HOST`, `SINGLESTOREDB_USER`, `SINGLESTOREDB_PASSWORD`, etc., can be used, or `SINGLESTOREDB_URL` as a single DSN.

Generate the API key from the SingleStore dashboard, [docs here](https://docs.singlestore.com/cloud/reference/management-api/#generate-an-api-key).

## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SingleStoreSearchTool

tool = SingleStoreSearchTool(
    tables=["products"], 
    host="host", 
    user="user", 
    password="pass", 
    database="db",
)

agent = Agent(
    role="Analyst", 
    goal="Query SingleStore", 
    tools=[tool], 
    verbose=True,
)

task = Task(
    description="List 5 products", 
    expected_output="5 rows as JSON/text", 
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```
