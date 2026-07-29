---
title: "OCR Tool"
source: https://docs.crewai.com/v1.15.8/en/tools/file-document/ocrtool
path: v1.15.8/en/tools/file-document/ocrtool
---

The `OCRTool` extracts text from local images or image URLs using an LLM with vision.

# `OCRTool`

## Description

Extract text from images (local path or URL). Uses a vision‑capable LLM via CrewAI’s LLM interface.

## Installation

No extra install beyond `crewai-tools`. Ensure your selected LLM supports vision.

## Parameters

### Run Parameters

* `image_path_url` (str, required): Local image path or HTTP(S) URL.

## Examples

### Direct usage

```python Code theme={null}
from crewai_tools import OCRTool

print(OCRTool().run(image_path_url="/tmp/receipt.png"))
```

### With an agent

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import OCRTool

ocr = OCRTool()

agent = Agent(
    role="OCR", 
    goal="Extract text", 
    tools=[ocr],
)

task = Task(
    description="Extract text from https://example.com/invoice.jpg", 
    expected_output="All detected text in plain text",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

## Notes

* Ensure the selected LLM supports image inputs.
* For large images, consider downscaling to reduce token usage.
* You can pass a specific LLM instance to the tool (e.g., `LLM(model="gpt-4o")`) if needed, matching the README guidance.

## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import OCRTool

tool = OCRTool()

agent = Agent(
    role="OCR Specialist",
    goal="Extract text from images",
    backstory="Vision‑enabled analyst",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Extract text from https://example.com/receipt.png",
    expected_output="All detected text in plain text",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```
