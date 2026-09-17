---
title: "Vision Tool"
source: https://docs.crewai.com/v1.15.22/en/tools/ai-ml/visiontool
path: v1.15.22/en/tools/ai-ml/visiontool
---

The `VisionTool` is designed to extract text from images.

# `VisionTool`

## Description

This tool is used to extract text from images. When passed to the agent it will extract the text from the image and then use it to generate a response, report or any other output.
The URL or the PATH of the image should be passed to the Agent.

You can also ask a custom `query` about the image and pick a `complexity_level` that automatically selects the model best suited for the request:

| Complexity level   | Model           |
| :----------------- | :-------------- |
| `easy`             | `gpt-5.6-luna`  |
| `medium` (default) | `gpt-5.6-terra` |
| `hard`             | `gpt-5.6-sol`   |

When an explicit `llm` or `model` is provided to the tool, it takes precedence over the complexity-based model selection.

## Installation

Install the crewai\_tools package

```shell theme={null}
pip install 'crewai[tools]'
```

## Usage

In order to use the VisionTool, the OpenAI API key should be set in the environment variable `OPENAI_API_KEY`.

```python Code theme={null}
from crewai_tools import VisionTool

vision_tool = VisionTool()

@agent
def researcher(self) -> Agent:
    '''
    This agent uses the VisionTool to extract text from images.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[vision_tool]
    )
```

## Arguments

The VisionTool accepts the following arguments:

| Argument              | Type     | Description                                                                                                              |
| :-------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------- |
| **image\_path\_url**  | `string` | **Mandatory**. The path to the image file (or URL) from which text needs to be extracted.                                |
| **query**             | `string` | **Optional**. The question or instruction to ask the model about the image. Defaults to `"What's in this image?"`.       |
| **complexity\_level** | `string` | **Optional**. The complexity of the request, which selects the model: `easy`, `medium`, or `hard`. Defaults to `medium`. |
