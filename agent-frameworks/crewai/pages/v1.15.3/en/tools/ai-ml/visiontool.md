---
title: "Vision Tool"
source: https://docs.crewai.com/v1.15.3/en/tools/ai-ml/visiontool
path: v1.15.3/en/tools/ai-ml/visiontool
---

The `VisionTool` is designed to extract text from images.

# `VisionTool`

## Description

This tool is used to extract text from images. When passed to the agent it will extract the text from the image and then use it to generate a response, report or any other output.
The URL or the PATH of the image should be passed to the Agent.

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

The VisionTool requires the following arguments:

| Argument             | Type     | Description                                                                      |
| :------------------- | :------- | :------------------------------------------------------------------------------- |
| **image\_path\_url** | `string` | **Mandatory**. The path to the image file from which text needs to be extracted. |
