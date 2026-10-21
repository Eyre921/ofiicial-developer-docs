---
title: "Overview"
source: https://docs.crewai.com/v1.15.28/en/tools/ai-ml/overview
path: v1.15.28/en/tools/ai-ml/overview
---

Leverage AI services, generate images, process vision, and build intelligent systems

These tools integrate with AI and machine learning services to enhance your agents with advanced capabilities like image generation, vision processing, and intelligent code execution.

## **Available Tools**

> **[DALL-E Tool](/en/tools/ai-ml/dalletool)**
>
> Generate AI images using OpenAI's DALL-E model.

> **[Vision Tool](/en/tools/ai-ml/visiontool)**
>
> Process and analyze images with computer vision capabilities.

> **[AI Mind Tool](/en/tools/ai-ml/aimindtool)**
>
> Advanced AI reasoning and decision-making capabilities.

> **[LlamaIndex Tool](/en/tools/ai-ml/llamaindextool)**
>
> Build knowledge bases and retrieval systems with LlamaIndex.

> **[LangChain Tool](/en/tools/ai-ml/langchaintool)**
>
> Integrate with LangChain for complex AI workflows.

> **[RAG Tool](/en/tools/ai-ml/ragtool)**
>
> Implement Retrieval-Augmented Generation systems.

> **[Code Interpreter Tool](/en/tools/ai-ml/codeinterpretertool)**
>
> Execute Python code and perform data analysis.

## **Common Use Cases**

* **Content Generation**: Create images, text, and multimedia content
* **Data Analysis**: Execute code and analyze complex datasets
* **Knowledge Systems**: Build RAG systems and intelligent databases
* **Computer Vision**: Process and understand visual content
* **AI Safety**: Implement content moderation and safety checks

```python theme={null}
from crewai_tools import DallETool, VisionTool

# Create AI tools
image_generator = DallETool()
vision_processor = VisionTool()

# Add to your agent
agent = Agent(
    role="AI Specialist",
    tools=[image_generator, vision_processor],
    goal="Create and analyze content using AI capabilities"
)
```
