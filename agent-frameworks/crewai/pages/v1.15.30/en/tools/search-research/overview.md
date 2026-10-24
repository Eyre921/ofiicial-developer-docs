---
title: "Overview"
source: https://docs.crewai.com/v1.15.30/en/tools/search-research/overview
path: v1.15.30/en/tools/search-research/overview
---

Perform web searches, find repositories, and research information across the internet

These tools enable your agents to search the web, research topics, and find information across various platforms including search engines, GitHub, and YouTube.

## **Available Tools**

> **[Serper Dev Tool](/en/tools/search-research/serperdevtool)**
>
> Google search API integration for comprehensive web search capabilities.

> **[Brave Search Tool](/en/tools/search-research/bravesearchtool)**
>
> Privacy-focused search with Brave's independent search index.

> **[Exa Search Tool](/en/tools/search-research/exasearchtool)**
>
> AI-powered search for finding specific and relevant content.

> **[LinkUp Search Tool](/en/tools/search-research/linkupsearchtool)**
>
> Real-time web search with fresh content indexing.

> **[GitHub Search Tool](/en/tools/search-research/githubsearchtool)**
>
> Search GitHub repositories, code, issues, and documentation.

> **[Website Search Tool](/en/tools/search-research/websitesearchtool)**
>
> Search within specific websites and domains.

> **[Code Docs Search Tool](/en/tools/search-research/codedocssearchtool)**
>
> Search through code documentation and technical resources.

> **[YouTube Channel Search](/en/tools/search-research/youtubechannelsearchtool)**
>
> Search YouTube channels for specific content and creators.

> **[YouTube Video Search](/en/tools/search-research/youtubevideosearchtool)**
>
> Find and analyze YouTube videos by topic, keyword, or criteria.

> **[Tavily Search Tool](/en/tools/search-research/tavilysearchtool)**
>
> Comprehensive web search using Tavily's AI-powered search API.

> **[Tavily Extractor Tool](/en/tools/search-research/tavilyextractortool)**
>
> Extract structured content from web pages using the Tavily API.

> **[Tavily Research Tool](/en/tools/search-research/tavilyresearchtool)**
>
> Run multi-step research tasks and get cited reports using the Tavily Research API.

> **[Tavily Get Research Tool](/en/tools/search-research/tavilygetresearchtool)**
>
> Retrieve the status and results of an existing Tavily research task.

> **[Arxiv Paper Tool](/en/tools/search-research/arxivpapertool)**
>
> Search arXiv and optionally download PDFs.

> **[SerpApi Google Search](/en/tools/search-research/serpapi-googlesearchtool)**
>
> Google search via SerpApi with structured results.

> **[SerpApi Google Shopping](/en/tools/search-research/serpapi-googleshoppingtool)**
>
> Google Shopping queries via SerpApi.

## **Common Use Cases**

* **Market Research**: Search for industry trends and competitor analysis
* **Content Discovery**: Find relevant articles, videos, and resources
* **Code Research**: Search repositories and documentation for solutions
* **Lead Generation**: Research companies and individuals
* **Academic Research**: Find scholarly articles and technical papers

```python theme={null}
from crewai_tools import (
    GitHubSearchTool,
    SerperDevTool,
    TavilyExtractorTool,
    TavilyGetResearchTool,
    TavilyResearchTool,
    TavilySearchTool,
    YoutubeVideoSearchTool,
)

# Create research tools
web_search = SerperDevTool()
code_search = GitHubSearchTool()
video_research = YoutubeVideoSearchTool()
tavily_search = TavilySearchTool()
content_extractor = TavilyExtractorTool()
tavily_research = TavilyResearchTool()
tavily_get_research = TavilyGetResearchTool()

# Add to your agent
agent = Agent(
    role="Research Analyst",
    tools=[
        web_search,
        code_search,
        video_research,
        tavily_search,
        content_extractor,
        tavily_research,
        tavily_get_research,
    ],
    goal="Gather comprehensive information on any topic"
)
```
