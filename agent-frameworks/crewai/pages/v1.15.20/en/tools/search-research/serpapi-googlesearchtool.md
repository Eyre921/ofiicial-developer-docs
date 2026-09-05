---
title: "SerpApi Google Search Tool"
source: https://docs.crewai.com/v1.15.20/en/tools/search-research/serpapi-googlesearchtool
path: v1.15.20/en/tools/search-research/serpapi-googlesearchtool
---

The `SerpApiGoogleSearchTool` performs Google searches using the SerpApi service.

# `SerpApiGoogleSearchTool`

## Description

Use the `SerpApiGoogleSearchTool` to run Google searches with SerpApi and retrieve structured results. Requires a SerpApi API key.

## Installation

```shell theme={null}
uv add crewai-tools[serpapi]
```

## Environment Variables

* `SERPAPI_API_KEY` (required): API key for SerpApi. Create one at [https://serpapi.com/](https://serpapi.com/) (free tier available).

## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SerpApiGoogleSearchTool

tool = SerpApiGoogleSearchTool()

agent = Agent(
    role="Researcher",
    goal="Answer questions using Google search",
    backstory="Search specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search for the latest CrewAI releases",
    expected_output="A concise list of relevant results with titles and links",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

## Notes

* Set `SERPAPI_API_KEY` in the environment. Create a key at [https://serpapi.com/](https://serpapi.com/)
* See also Google Shopping via SerpApi: `/en/tools/search-research/serpapi-googleshoppingtool`

## Parameters

### Run Parameters

* `search_query` (str, required): The Google query.
* `location` (str, optional): Geographic location parameter.

## Notes

* This tool wraps SerpApi and returns structured search results.
