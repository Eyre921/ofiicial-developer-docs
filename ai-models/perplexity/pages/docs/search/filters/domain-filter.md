---
title: "Search Domain Filter"
source: https://docs.perplexity.ai/docs/search/filters/domain-filter
path: docs/search/filters/domain-filter
---

<Note>
  The `search_domain_filter` parameter allows you to limit search results to specific domains or exclude certain domains from search results. This supports domain-level filtering for precise content control.
</Note>

<Warning>
  You can add a maximum of 20 domains to the `search_domain_filter` list. The filter works in either allowlist mode (include only) or denylist mode (exclude), but not both simultaneously.
</Warning>

<Info>
  Domain filters allow you to specify which domains to include or exclude in search results. You can filter by specific domains, top-level domains (TLDs), or domain parts. You can specify up to 20 domains per request. Domains should be provided without the protocol (e.g., "nature.com" not "[https://nature.com](https://nature.com)").
</Info>

## Overview

The domain filter for the Search API allows you to control which sources appear in your search results by limiting them to specific domains or excluding certain domains. This is particularly useful when you need to:

* Focus research on authoritative or trusted sources
* Filter out specific domains from search results
* Search within specific publication networks or organizations
* Build domain-specific search applications
* Conduct competitive research within specific industry domains

The `search_domain_filter` parameter accepts an array of domain strings. The filter operates in two modes:

* **Allowlist mode**: Include only the specified domains (no `-` prefix)
* **Denylist mode**: Exclude the specified domains (use `-` prefix)

```bash theme={null}
# Allowlist: Only search these domains
"search_domain_filter": ["nature.com", "science.org", "cell.com"]

# Denylist: Exclude these domains
"search_domain_filter": ["-reddit.com", "-pinterest.com", "-quora.com"]
```

## Filtering Capabilities

Domain filters support flexible matching across different domain components:

### Root Domain Filtering

Specify a root domain to match all content from that domain and its subdomains:

```bash theme={null}
"search_domain_filter": ["wikipedia.org"]
```

This will match:

* `en.wikipedia.org`
* `fr.wikipedia.org`
* `de.wikipedia.org`
* Any other Wikipedia language subdomain

### Top-Level Domain (TLD) Filtering

Filter by top-level domain to target specific categories of sites:

```bash theme={null}
"search_domain_filter": [".gov"]
```

This will match all government domains:

* `nasa.gov`
* `cdc.gov`
* `irs.gov`
* Any other `.gov` domain

<Tip>
  TLD filtering is particularly useful for targeting specific types of organizations, such as `.gov` for government sites, `.edu` for educational institutions, or country-specific TLDs like `.uk` or `.ca`.
</Tip>

### Path Filtering

Add a path after a domain to limit (or exclude) results to one section of a site. The path is matched against the start of the URL's path segments:

```bash theme={null}
"search_domain_filter": ["nature.com/articles"]
```

This will match:

* `nature.com/articles`
* `nature.com/articles/d41586-024-001`
* the same path on any subdomain (e.g. `blog.nature.com/articles`)

It will **not** match:

* `nature.com/news`

Path filtering works in both allowlist and denylist mode. Prefix a path-qualified value with `-` to exclude a section of a site while still searching the rest of it:

```bash theme={null}
# Only this section
"search_domain_filter": ["reddit.com/r/MachineLearning"]

# Everything on the site except this section
"search_domain_filter": ["-reddit.com/r/all"]
```

<Note>
  Path filtering matches on path-segment boundaries, so `"example.com/docs"` matches `/docs` and `/docs/intro` but not `/documentation`. Query strings are allowed after the path boundary (`/docs?x=1` matches).
</Note>

### Domain Part Filtering

Any part of a domain can be used as a filter. The system will match domains containing that component.

## Examples

**1. Allowlist Specific Domains**

This example limits search results to authoritative academic publishers:

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="IPCC AR6 synthesis report key findings",
      max_results=10,
      search_domain_filter=[
          "nature.com",
          "science.org",
          "cell.com"
      ]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "IPCC AR6 synthesis report key findings",
    max_results: 10,
    search_domain_filter: [
      "nature.com",
      "science.org",
      "cell.com"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "IPCC AR6 synthesis report key findings",
      "max_results": 10,
      "search_domain_filter": [
        "nature.com",
        "science.org",
        "cell.com"
      ]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "75c39a4e-a46c-4850-bf27-4c061186ece6",
    "results": [
      {
        "snippet": "",
        "title": "10 Big Findings from the 2023 IPCC Report on Climate Change",
        "url": "https://www.wri.org/insights/2023-ipcc-ar6-synthesis-report-climate-change-findings",
        "date": "2023-03-20",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "",
        "title": "AR6 Synthesis Report",
        "url": "https://www.ipcc.ch/report/ar6/syr/",
        "date": null,
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "[PDF] Climate Change 2023 Synthesis Report",
        "url": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_LongerReport.pdf",
        "date": null,
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "The Synthesis Report is based on the content of the three Working Groups Assessment Reports:* WGI – The Physical Science Basis, WGII – Impacts, Adaptation and Vulnerability, WGIII – Mitigation of Climate Change*, and the three Special Reports: *Global Warming of 1.5°C*, *Climate Change and Land*, *The Ocean and Cryosphere in a Changing Climate*.\n...\nThe SYR outline agreed at the 52^nd^ Panel Session of the IPCC consists of an introduction and three main sections arranged by timeframes.\nThe first section, ‘Current Status and Trends’, covers the historical and present period.\nThe second section, ‘Long-term Climate and Development Futures’, addresses projected futures up to 2100 and beyond.\nThe final section is ‘Near-term Responses in a Changing Climate’, considers current international policy timeframes, and the time interval between now and 2030-2040.\nThis structure, substantially different to what was adopted for AR5 SYR, enables a holistic framing that integrates across the Working Groups, better enabling the SYR to cover different aspects of climate change.",
        "title": "AR6 Synthesis Report: Climate Change 2023 — IPCC",
        "url": "https://www.ipcc.ch/report/sixth-assessment-report-cycle/",
        "date": null,
        "last_updated": "2026-05-12"
      },
      {
        "snippet": "",
        "title": "[PDF] IPCC_AR6_SYR_FullVolume.pdf",
        "url": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf",
        "date": null,
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "Summary for Policymakers",
        "url": "https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/",
        "date": null,
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "SYR Longer Report - Intergovernmental Panel on Climate Change",
        "url": "https://www.ipcc.ch/report/ar6/syr/longer-report/",
        "date": null,
        "last_updated": "2026-03-21"
      },
      {
        "snippet": "",
        "title": "IPCC Secretariat",
        "url": "https://www.ipcc.ch/site/assets/uploads/2023/03/Doc5_Adopted_AR6_SYR_Longer_Report.pdf",
        "date": null,
        "last_updated": "2024-02-26"
      },
      {
        "snippet": "",
        "title": "IPCC AR6 Working Group 1: Technical Summary",
        "url": "https://www.ipcc.ch/report/ar6/wg1/chapter/technical-summary/",
        "date": null,
        "last_updated": "2026-03-18"
      },
      {
        "snippet": "",
        "title": "IPCC_AR6_SYR_SPM.pdf",
        "url": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_SPM.pdf",
        "date": null,
        "last_updated": "2026-05-21"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**2. Tech News Sources**

Search across major technology news websites:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="enterprise AI adoption trends in financial services",
      max_results=10,
      search_domain_filter=[
          "techcrunch.com",
          "theverge.com",
          "arstechnica.com",
          "wired.com"
      ]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"Source: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "enterprise AI adoption trends in financial services",
    max_results: 10,
    search_domain_filter: [
      "techcrunch.com",
      "theverge.com",
      "arstechnica.com",
      "wired.com"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`Source: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "enterprise AI adoption trends in financial services",
      "max_results": 10,
      "search_domain_filter": [
        "techcrunch.com",
        "theverge.com",
        "arstechnica.com",
        "wired.com"
      ]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "3c32332e-256e-42f6-94c8-f9435d547e2a",
    "results": [
      {
        "snippet": "",
        "title": "The future of banking: How AI is reshaping the industry - PwC",
        "url": "https://www.pwc.com/us/en/industries/financial-services/library/how-ai-is-reshaping-banking.html",
        "date": "2025-10-16",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "### 1.\nMoving from pilot to scale as access expandsexEnterprise AI adoption grows\nWorker access to AI rose by 50% in 2025, and expectations for scale are high: the number of companies with ≥40% projects in production is set to double in six months.\n...\nAI is delivering on efficiency and productivity, and twice as many leaders as last year are reporting transformative impact.\nBut just 34% are truly reimagining the business.\n### 3.\nAI fluency over role redesignroAI workforce impact remains low\nThe AI skills gap is seen as the biggest barrier to integration, and education—not role or workflow redesign—was the No. 1 way companies adjusted their talent strategies due to AI.\n...\nSovereign AI is when a country—and companies within it—deploy AI under their own laws, infrastructure, and data.\nIt's not just about ownership.\nIt's about strategic independence.\n### 5.\nAI agents outpace their guardrailspaThe oncoming surge in agentic AI\nAgentic AI usage is poised to rise sharply in the next two years, but oversight is lagging: Only one in five companies has a mature model for governance of autonomous AI agents.\n### 6.\nPhysical AI's fast-growing footprint fGaining traction by 22 percentage points in two years\nMore than half of companies (58%) report at least limited use of physical AI today, and that figure is set to reach 80% in two years—with Asia Pacific leading in early implementation.\n### 7.\n...\nCompared to last year, more companies (42%) believe their strategy is highly prepared for AI adoption—but they feel less prepared in terms of infrastructure, data, risk, and talent.\n## What's top of mind when it comes to AI in the enterprise?itAs they turn the corner to scale, leaders are asking about ROI, safe and ethical practices, workforce readiness, and tactical, go-to-market moves.\n...\nDigital transformation with AI can yield a variety of benefits for businesses, from cost savings to service delivery.\nImproving productivity and efficiency top the list of benefits achieved from enterprise AI adoption so far, with two-thirds (66%) of organizations reporting gains.\nOther benefits organizations reported achieving include:\n- Enhancing insights and decision-making (53%)\n- Reducing costs (40%)\n- Enhancing client/customer relationships (38%)\n- Improving products/services and fostering innovation (20%)\n- Increasing revenue (20%)\nRevenue growth largely remains an aspiration, with 74% of organizations hoping to grow revenue through their AI initiatives in the future compared to just 20% that are already doing so.\n...\nOne-third (34%) of surveyed organizations are starting to use AI to deeply transform—creating new products and services or reinventing core processes or business models.\nAnother third (30%) are redesigning key processes around AI.\nThe remaining third (37%) are using AI at a more surface level, with little or no change to existing processes.\nWhile each are capturing productivity and efficiency gains, only the first group are truly reimagining their businesses rather than optimizing what already exists.\nAdditionally, different types of AI technologies yield different expectations for impact.\n**Generative AI (GenAI):** The areas of GenAI that leaders believe will have the most impactful effects on their industries are:\n- Search and knowledge management\n- Virtual assistants/chatbots\n- Content generation\n**Agentic AI:** While agentic AI is expected to have the highest impact in customer support, use cases for supply chain management, R&D, knowledge management, and cybersecurity are also seen as having high potential.\nThe enterprises we interviewed are already deploying autonomous AI agents across diverse functions:\n- A financial services company is building agentic workflows to automatically capture meeting actions from video conferences, draft communications to remind participants of their commitments, and track follow-through.\n- An air carrier is using AI agents to help customers complete the most common transactions, such as rebooking a flight or rerouting bags, freeing up time for human agents to address more complex matters.\n- A manufacturer is using AI agents to support new product development initiatives, leveraging AI to find the optimal balance between competing objectives such as cost and time-to-market.\n- In the public sector, AI agents are being used to cover workforce shortages, partnering with human workers to complete key processes.\n**Physical AI:** Physical AI applications span a wide range of industrial and commercial settings.\nCommon use cases for physical AI include:\n- collaborative robots (cobots) on assembly lines\n- Inspection drones with automated response capabilities\n- Robotic picking arms\n- Autonomous forklifts\nAdoption is especially advanced in manufacturing, logistics, and defense, where robotics, autonomous vehicles, and drones are already reshaping operations.\n...\nAccording to the leaders surveyed, insufficient worker skills are the biggest barrier to integrating AI into existing workflows.\nThese are the top ways organizations are adjusting AI talent strategy:\n- Educating the broader workforce to raise overall AI fluency (53%)\n- Designing and implementing upskilling and reskilling strategies (48%)\n- Assessing target talent acquisition levels and hiring specialized talent to drive AI initiatives (36%)\n- Redesigning career paths and career mobility strategies (33%)\n- Assessing changes to the anticipated supply and demand of skills (30%)\n- Providing performance-based incentives for leveraging AI (30%)\n- Combining or reimagining organizations based on new patterns resulting from AI usage (30%)\n- Measuring worker trust and engagement (30%)\n- Changing the balance between full-time, contract, and gig workers (19%)\n...\nTrends and insights about AI in the enterprise vary from sector to sector, company to company.\nGet a tailored snapshot of your industry to understand where AI is making the biggest impact in your industry.\n...\n### Financial ServicesuDownload",
        "title": "The State of AI in the Enterprise - 2026 AI report | Deloitte US",
        "url": "https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html",
        "date": null,
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "The banking industry stands at a critical inflection point.\nAs we advance through 2025, artificial intelligence has evolved from experimental technology to a strategic imperative reshaping how financial institutions operate, serve customers, and manage risk.\n...\nThe numbers tell a compelling story.\nAccording to McKinsey's latest Global Survey on AI, [78% of organizations now use AI in at least one business function](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work), up from 72% in early 2024 and 55% a year earlier.\nMeanwhile, the financial services industry invested an estimated [$35 billion in AI](https://www.statista.com/statistics/1446366/leading-banks-in-ai-adoption-worldwide/) in 2023, with banking accounting for approximately $21 billion.\nThis investment is expected to generate substantial returns, [with AI contributing $2 trillion](https://www.statista.com/topics/7083/artificial-intelligence-ai-in-finance/) to the global economy through innovative investment strategies, better customer insights, and improved operational efficiency.\n...\nBased on nCino's experience with over 2,700 customers, including community banks, credit unions, independent mortgage banks, and the largest financial entities globally, three key priorities are driving AI adoption in 2025 and beyond:\n#### 1.\nOperational Efficiency: AI Shifts from Broad Automation to Workflow-Level Impact\nIn 2025, banks are moving past generic automation goals.\nThe focus now is on applying AI to specific, high-friction workflows — especially in lending, onboarding, and document-heavy processes.\nEfficiency is no longer about reducing headcount.\nIt’s about speeding up what still takes too long.\n#### Targeted AI Replaces One-Size-Fits-All Automation\nInstead of general-purpose tools, banks are deploying AI tuned to their internal workflows.\nThese applications help teams move faster with fewer manual steps.\nExamples:\n- Parsing tax returns or balance sheets to pre-fill borrower profiles\n- Prioritizing credit files based on deal complexity or risk level\n- Drafting loan memos from financial and historical deal data\n#### Queue Optimization Becomes a Strategic Advantage\nCycle time is still a pain point — and AI is helping by automating file assignment, surfacing bottlenecks, and routing based on business value.\nExamples:\n- Auto-assigning stalled deals to available underwriters\n- Flagging missing documentation before an analyst starts a review\n- Dynamically re-prioritizing workloads as queues shift\n...\n#### 2.\nRisk Management: AI as Strategic Defense\nAI revolutionizes risk management by transforming how institutions identify, assess, and mitigate threats.\nKey applications include:\n- **Fraud Detection:** Real-time transaction pattern analysis identifies anomalies with unprecedented accuracy and speed.\n- **Credit Risk Assessment:** Machine learning models predict defaults by analyzing customer behavior and transaction patterns more accurately than traditional methods.\n- **Cybersecurity:** In 2023, financial services experienced over 20,000 cyberattacks resulting in $2.5 billion in losses.\nAI-powered security systems detect and respond to threats in real-time.\n...\nBy strengthening these risk management capabilities, banks can confidently offer personalized financial products and services, knowing they have robust safeguards in place to protect both the institution and individual customers from evolving threats.\n#### 3.\nCustomer Experience: Personalizing Services at Scale\n[77% of banking leaders say personalization leads to boosted customer retention](https://dovetail.com/ux/customer-experience-in-banking-trends/), with AI enabling the personalized experiences that drive customer satisfaction and loyalty.\nAI enables personalized service delivery, 24/7 customer support through chatbots, predictive analytics for proactive solutions, and streamlined digital experiences.\nDespite these impressive stats, only 26% of companies have developed the necessary set of capabilities to move beyond proofs of concept and generate tangible value, [according to new research by Boston Consulting Group (BCG)](https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value).\nSuccess requires strategic implementation focusing on four key factors:\n- **Risk-proportionate governance** that matches oversight intensity to actual risk levels, from low-risk internal automation requiring 1-2 day approvals to high-risk automated decisions demanding comprehensive review\n- **Accelerated implementation timelines** where leading institutions follow streamlined roadmaps from governance foundation through production deployment\n- **Human-in-the-loop design** that maintains human oversight as a core principle while capturing efficiency benefits\n- **Executive leadership engagement** that significantly reduces approval timeframes by providing necessary decision-making authority for rapid implementation.\nTogether, these strategic approaches enable banks to deploy AI solutions that can analyze customer data, predict needs, and deliver personalized experiences at the scale and speed required to compete in today's digital banking landscape.\n...\n75% of banks with over $100 billion in assets are expected to fully integrate AI strategies by 2025.\nEmerging trends include agentic AI for complex tasks, multimodal AI processing multiple data types, and federated learning for privacy-preserving collaboration.\nRegulatory evolution will bring more specific AI requirements focusing on algorithmic transparency, standardized risk frameworks, and enhanced consumer protection.\nTo fully embrace these opportunities, financial institutions must:\n- **Develop a Comprehensive AI Strategy:** Start with clear business objectives aligned with efficiency, risk management, or customer experience priorities.\n...\nThe AI transformation of banking is accelerating rapidly.\nThis growth will contribute $2 trillion to the global economy through innovative strategies and improved efficiency.\nFinancial institutions that embrace AI responsibly and rapidly – with proper governance, risk management, and customer focus – will thrive in the digital future.",
        "title": "AI Trends in Banking 2025 - nCino",
        "url": "https://www.ncino.com/blog/ai-accelerating-these-trends",
        "date": "2025-06-30",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "Top 10 trends in AI adoption for enterprises in 2025 - Glean",
        "url": "https://www.glean.com/perspectives/enterprise-insights-from-ai",
        "date": "2025-10-30",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "Discover how autonomous frontier technologies, like agentic AI, driverless vehicles, and humanoid robotics, are poised to transform the insurance industry.\nFive priorities for winning with GenAI in wealth and asset management\nWealth and asset managers have the opportunity to reimagine their business models and transform their operations with GenAI.",
        "title": "AI in financial services: adoption across sectors | EY - US",
        "url": "https://www.ey.com/en_us/ai-in-financial-services",
        "date": "2025-09-22",
        "last_updated": "2026-05-10"
      },
      {
        "snippet": "The 2026 survey identifies key AI trends being adopted by financial institutions around the world.\n...\nThis year’s results reveal the trends, challenges, and opportunities that define the state of AI in financial services in 2026.",
        "title": "State of AI in Financial Services Survey Report from NVIDIA.",
        "url": "https://www.nvidia.com/en-us/industries/finance/ai-financial-services-report/",
        "date": "2026-01-22",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "In financial services, AI is no longer a futuristic idea — it’s part of daily business.\nBy 2027, the sector is expected to spend nearly $100B on AI.\nBut this excitement is tempered by legacy systems, governance requirements, and hard-to-measure ROI.\nA new wave of startups is emerging to overcome these hurdles while preserving the control, compliance, and precision that financial institutions require.\n...\n## Broadly bullish, but ROI remains uncertain and hard to quantify\nFinancial institutions are excited about AI, but the ROI is hard to measure, and leaders expect clearer results:\n> *“There’s a healthy amount of skepticism around how much efficiency AI can truly deliver.\nThe potential productivity gains are real, but it’s my job to separate substance from noise to determine what will actually deliver impact.”\n*\n*— Jennifer Charters, EVP and CIO at Lincoln Financial*\nMost now view AI as a useful tool that can create leverage in targeted areas, but not a universal fix.\nSo, firms are increasingly selective in their approach and prioritizing companies that can show measurable ROI.\n## AI push is both top-down and bottom-up\nBoards and senior executives see peers touting AI initiatives at conferences and earnings calls, and public markets are rewarding firms that can show credible strategies.\nNo one wants to be left behind, so the top-down push toward AI has become as much about optics as efficiency.\nHowever, the push isn’t just top-down.\nEmployees want tools that reduce manual work, putting real pressure on procurement and IT teams to move quickly:\n> *“Front-line teams are pushing for automation to make their lives easier while leadership pushes for AI strategy.\nThe two forces have started to reinforce to drive real AI adoption.*”\n*— Dan Zinkin, former CIO Global Investment & Corporate Banking at J.P.\nMorgan & Head of AI and Data at InvestCloud*\nThe result is a rare alignment across the org chart — many want AI, even if for different reasons.\n## Main AI use cases today are productivity-oriented\n### Investment knowledge management\nFor investment and research teams, AI is chipping away at the hunt for information.\nAnalysts and portfolio managers typically spend hours gathering documents and parsing filings.\nStill, firms are now deploying internal search and summarization tools that surface relevant content — from research notes and client decks to compliance filings and meeting transcripts.\nPlatforms like Rogo, Metal, and Reflexivity make proprietary knowledge searchable in natural language rather than buried in disparate drives.\n### Developer efficiency\nAI is changing how developers write and maintain code, from boilerplate generation to code conversion and documentation.\nMore AI-suggested code now reaches production, which is particularly useful in financial services, where many systems still rely on Common Business-Oriented Language (COBOL) and mainframes maintained by a shrinking pool of experts.\nAs a result, modernization is slow and risky.\nSwimm* and CoreStory help teams understand the business logic of code inside legacy systems.\n### Customer service\nAI is speeding up customer support by giving Agents access to internal documents, past interactions, and policy information, replacing time-consuming searches through PDFs and emails.\nLeaders say these tools don’t replace humans but make service faster and more consistent.\nWonderful*, for example, uses Agents to power voice and text support and is seeing early success in financial services, while Glia* applies AI to automate and analyze customer interactions across banks and credit unions.\nJump is vertically focused on financial advisors and uses AI to manage client conversations across onboarding and ongoing relationship needs.\n## Agentic adoption is early but expanding\nComfort with AI Agents varies, but many firms are exploring them.\nSome, like BNY, are running dozens of agentic workflows in production:\n> *“We have over 100 agentic digital employees doing everything from enhancing code to validating payment instructions.\nThis AI workforce allows for a different level of collaboration and productivity.”\n...\n*— Julie Gerdeman, Global Head of Data and Analytics at BNY*\nSome firms are piloting Agents internally but avoiding client-facing use, while more conservative institutions are holding back altogether due to regulatory concerns and Agent unpredictability.\nCrewAI*, Relevance AI*, and Tavily* all enable the orchestration and deployment of AI Agents.\nDespite differing comfort levels, Agents are now seen as the next phase of enterprise AI, and even hesitant firms are laying the groundwork for future use.\n## Business units drive strategy while the central org enables\nAcross most institutions, AI strategy is business-led, centrally governed.\nBusiness units identify use cases and set priorities, while the central technology teams manage vendors, negotiate contracts, and ensure firmwide standards are met:\n> *“Ideas need sponsorship from the business unit.\nEvery AI use case requires a clear business owner who partners with the central tech team to drive execution and implementation.”*\n*— Ericson Chan, CIO at Zurich Insurance*\nThis structure creates a necessary balance.\nIt gives front-line teams the ability to move quickly while keeping AI aligned with enterprise risk frameworks.\n...\nThe human side of AI adoption can sometimes prove harder than the technical one.\nDespite AI’s potential to streamline work, many employees don’t trust the tools, creating cultural resistance:\n...\nLeaders are responding with internal training, documentation, and AI literacy initiatives designed to show the goal of enhancing, not eliminating, human work.\n...\nCounterintuitively, the pace of AI innovation has made some technology leaders cautious.\nFirms worry about adopting a solution, embedding it across the organization, only to realize it’s obsolete just months later.\nAs a result, teams are wary of tools that create vendor lock-in and are piloting more options to avoid becoming dependent on any single provider.\n...\nFinancial institutions still lack the pipes to unify data across different systems:\n...\nMany banks still keep large volumes of untagged or on-premise data, meaning only a small share is truly AI-ready.\nData cleanup is time-consuming, and rising data volumes make the problem worse, paving the way for improvements throughout the data organization.\n...\nMany leaders now view stronger data hygiene as the essential prerequisite for unlocking AI’s potential.\n...\nFinancial institutions operate under heavy regulatory scrutiny, and uncertainty around LLM behavior makes compliance teams uneasy.\nBecause these systems are inherently nondeterministic, they don’t align easily with workflows that require consistent, auditable results.\nMost firms still lack standardized frameworks to assess accuracy, trace model reasoning, or measure performance against regulatory expectations.\nFiddler* and Arize improve transparency and auditability across AI/ML models.\nCymphony helps companies monitor how employees use data and tools, enabling them to prevent internal security risks as they adopt AI.\nAnd tools like Harmony provide proactive, intelligent IT management with built-in compliance controls, helping firms maintain auditable workflows as they use AI.\nUntil clearer rules and stronger control mechanisms emerge, governance will continue to define the speed and scope of AI adoption.\nAs AI becomes embedded in financial services, the real opportunity belongs to companies that can deliver practical, governed, and measurable value to institutions.",
        "title": "AI in financial services is here: How firms are adopting and where ...",
        "url": "https://www.insightpartners.com/ideas/ai-in-financial-services/",
        "date": "2025-12-12",
        "last_updated": "2026-05-19"
      },
      {
        "snippet": "",
        "title": "How artificial intelligence is reshaping the financial services industry",
        "url": "https://www.ey.com/en_gr/insights/financial-services/how-artificial-intelligence-is-reshaping-the-financial-services-industry",
        "date": "2024-11-12",
        "last_updated": "2026-05-19"
      },
      {
        "snippet": "",
        "title": "Top AI Trends Transforming Financial Services for 2026 - Keyrus",
        "url": "https://keyrus.com/us/en/insights/top-ai-trends-transforming-financial-services-for-2026",
        "date": null,
        "last_updated": "2026-05-24"
      },
      {
        "snippet": "",
        "title": "[PDF] Artificial Intelligence in Financial Services",
        "url": "https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Financial_Services_2025.pdf",
        "date": null,
        "last_updated": "2026-05-17"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**3. Government and Educational Sources (TLD Filtering)**

Use top-level domain filtering to search across all government or educational institutions:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search all .gov and .edu domains
  response = client.search.create(
      query="climate change policy research",
      max_results=15,
      search_domain_filter=[
          ".gov",
          ".edu"
      ]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"Source: {result.url}")
      print("---")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search all .gov and .edu domains
  const response = await client.search.create({
    query: "climate change policy research",
    max_results: 15,
    search_domain_filter: [
      ".gov",
      ".edu"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`Source: ${result.url}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change policy research",
      "max_results": 15,
      "search_domain_filter": [
        ".gov",
        ".edu"
      ]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "79bfb4ae-dc85-4d01-899b-bf241b9e6bb9",
    "results": [
      {
        "snippet": "*Climate Policy* aims to make high-quality research accessible and relevant to academics, and also to policymakers and practitioners.\nOur objective is to provide a platform for new ideas, innovative approaches and research-based insights that can help advance an effective response to climate change in practice.\nTo do so, the journal particularly seeks to highlight the policy implications of emergent research and analysis.\nAs an interdisciplinary journal, *Climate Policy* encourages submissions from all academic fields, but with a requirement that papers are written in an accessible style.\n*Climate Policy* welcomes submissions across a broad range of areas, including:\n· Mitigation and adaptation (beyond a focus on climate impacts alone) to climate change, loss and damage, climate change laws, technologies and innovations, institutions and governance at different scales, and climate finance\n· Design of climate-relevant policies and policy packages, implementation and evaluation of their impact on the ground, especially ex-post empirical assessment.\n· International climate negotiations and related international processes relevant to global climate governance, including linkages to geopolitics, trade and finance\n· Linkages to broader processes of structural change and transformation at regional, national and local levels, including low-emissions and climate-resilient development, sectoral transitions, and just transitions.\n· Please also look at the more detailed substantive criteria for consideration by\n*Climate Policy*.\n...\nTo promote independent commentary and debate,\n*Climate Policy* publishes papers in the following formats, all of which are peer reviewed and eligible for open access (see more information here):\n· Research articles present the latest research on all aspects of climate change policy (7,000 words)\n· Synthesis articles review the state of knowledge in key areas of interest (8,000 words).\n· Policy Analysis articles put forward evidence-based objective analysis of particular policy approaches (5,000 words)\n· Viewpoint articles offer rigorous insights and commentary on contemporary climate debates, including from practitioners and policymakers (3,000 words)\n...\nProspective authors are welcome to send short summaries of their work to the Editorial office for an opinion on its suitability for\n*Climate Policy*.\nThe Editorial Office may be contacted at editor@climatepolicyjournal.org.",
        "title": "Climate Policy | Journal | Taylor & Francis Online",
        "url": "https://www.tandfonline.com/journals/tcpo20",
        "date": "2025-08-04",
        "last_updated": "2025-08-05"
      },
      {
        "snippet": "Brazil, UNESCO and the UN have joined forces to strengthen research to counter narratives that are delaying and derailing urgently needed climate action.",
        "title": "ClimateChange - the United Nations",
        "url": "https://www.un.org/en/climatechange",
        "date": "2026-04-07",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "EPA is taking action to address some of our nation’s largest sources of both climate- and health-harming pollution, such as the transportation, oil and natural gas, and power sectors.\nEPA will continue to update this information as we move forward with new regulatory actions.\n...\nThe American Innovation and Manufacturing (AIM) Act of 2020 directs EPA to address HFCs by providing new authorities to phase down the production and consumption of listed HFCs, manage these HFCs and their substitutes, and facilitate the transition to next-generation technologies that do not rely on HFCs.\nOn September 23, 2021, EPA issued a final rule establishing the HFC Allocation program that will phase down the U.S. production and consumption of HFCs by 85% from historic levels by 2036, as mandated by the AIM Act.\nA global phasedown of HFCs is expected to avoid up to 0.5°C of global warming by 2100.\nThe Emissions Reduction & Reclamation program to manage HFCs and substitutes was established in October 2024.\nThe Technology Transitions program issued its first rule putting in place restrictions on HFCs in over 40 subsectors in October 2023.\n...\nOn December 20, 2021, EPA finalized federal greenhouse gas emissions standards for passenger cars and light trucks for Model Years (MY) 2023 through 2026.\nThe final standards leverage advances in clean car technology to unlock $190 billion in net benefits to Americans, including reducing climate pollution, improving public health, and saving drivers money at the pump.\nThese standards are the strongest vehicle emissions standards ever established for the light-duty vehicle sector, and are based on sound science and grounded in a rigorous assessment of current and future technologies.\nThe updated standards will result in avoiding more than 3 billion tons of GHG emissions through 2050.\n...\nEPA is implementing CO~2~ emission standards for airplanes used in commercial aviation and for large business jets.\n...\nEPA is also responsible for implementing the Renewable Fuels Standard Program, a national policy that requires a certain volume of renewable fuel to replace petroleum-based transportation fuel.\n...\nIn May 2024, EPA published final carbon pollution standards for power plants that set carbon dioxide (CO~2~) limits for new gas-fired combustion turbines and CO~2~ emission guidelines for existing coal, oil and gas-fired steam generating units, securing important climate benefits and protecting public health.",
        "title": "Climate Change Regulatory Actions and Initiatives | US EPA",
        "url": "https://www.epa.gov/climate-change/climate-change-regulatory-actions-and-initiatives",
        "date": "2021-06-11",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "Addressing the urgent challenges of climate change requires a concerted, coordinated effort among governments at the sub-national, national, regional, and global levels.\nIt also demands technological innovation to and understanding mitigation policies based on the latest research.\nIn addition, these innovations and cooperative global initiatives* * must be economically feasible.\nAll of which means that today’s leaders in government, industry, and other fields must develop policies that effectively blend insights into the science, economics, and politics of climate change.\n*Climate Change Policy: Economics and Politics * is an online executive program developed by Harvard Kennedy School faculty to address these challenges.\nLed by Faculty Chair Robert Stavins, Director of the Harvard Environmental Economics Program and the Harvard Project on Climate Agreements, this five-day interactive program is designed for managers, analysts, and leaders both inside and outside governments.\nTogether with a global cohort, you will explore the latest research, analytical tools, and conceptual frameworks to better understand climate-related policies.",
        "title": "Climate Change Policy: Economics and Politics",
        "url": "https://www.hks.harvard.edu/educational-programs/executive-education/climate-change-policy-economics-and-politics",
        "date": null,
        "last_updated": "2026-05-09"
      },
      {
        "snippet": "",
        "title": "A review of the global climate change impacts, adaptation ... - PMC",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8978769/",
        "date": "2022-04-04",
        "last_updated": "2026-03-30"
      },
      {
        "snippet": "",
        "title": "Climate policy conflict in the U.S. states: a critical review and way ...",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8853238/",
        "date": "2022-02-16",
        "last_updated": "2026-03-18"
      },
      {
        "snippet": "",
        "title": "Environmental justice and climate change policies - PMC - NIH",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9391311/",
        "date": "2022-04-30",
        "last_updated": "2026-04-18"
      },
      {
        "snippet": "- Climatic Change\nClimatic Change is an international, interdisciplinary journal dedicated to the totality of the problem of climatic variability and change - its descriptions, causes, implications and interactions among these.\n- Climate Policy\nA leading international peer-reviewed academic journal, publishing on all aspects of climate change policy, including adaptation and mitigation, governance and negotiations, policy design, implementation and impact, and the full range of economic, social and political issues at stake in responding to climate change.\n- Environmental Research Letters\nCovers all areas of environmental science, providing a coherent and integrated approach including research articles, perspectives and review articles.\n- Nature\nWeekly international journal publishing peer-reviewed research in all fields of science and technology.\nNature also provides news and interpretation of topical and coming trends affecting science, scientists and the wider public.\n- WIREs Climate Change\nA forum to promote cross-disciplinary discussion of a global phenomenon with long-term societal implications, and and provides an important new encyclopedic reference for climate change scholarship and research.\n...\nThese books and many more are available at the Dag Hammarskjöld Library.\n...\nThis report analyzes international experience to identify effective pathways to coherent policy packages that harness synergies and manage tensions between climate mitigation and air-quality management.",
        "title": "Research Guides: Climate Change - A Global Issue: Books & Journals",
        "url": "https://research.un.org/en/climate-change/books",
        "date": "2014-08-19",
        "last_updated": "2026-03-28"
      },
      {
        "snippet": "## Why is it important?\niPolicymakers need to be informed about the state of the climate, how human activity is affecting it, and the possible future outcomes that we might experience.\nRigorous policymaking requires a robust scientific evidence base, which climate scientists can help to deliver.\n## What are we doing?haOur work helps to ensure that policymakers have access to up-to-date scientific evidence and expertise on the Earth’s climate system and how humans are impacting it.\nThis includes the latest understanding on: the level of greenhouse gases in the atmosphere; how this will affect global temperatures; what impacts are likely to occur in future (such as extreme weather and sea level rise); and the extent to which human-caused climate change is already making extreme weather more likely and intense.\n...\n### Policy briefing: Earth Systems Insights SThis policy briefing draws on work from six projects: ESM2025, ClimTip, TipESM, OptimESM, nextGEMS, and RESCUE, which\nall conduct policy-relevant climate change research using Earth Systems Models, in particular in relation to the Paris Agreement.\n...\nContact:\nJenny Bird\nCampaign Manager\nj.bird@imperial.ac.uk\n## Further resources",
        "title": "Climate science for policymakers - Imperial College London",
        "url": "https://www.imperial.ac.uk/grantham/policy/climate-science-for-policymakers/",
        "date": "2024-08-27",
        "last_updated": "2026-05-09"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**4. Wikipedia Across Languages (Subdomain Matching)**

Search across all Wikipedia language editions by specifying the root domain:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Matches en.wikipedia.org, fr.wikipedia.org, de.wikipedia.org, etc.
  response = client.search.create(
      query="quantum mechanics fundamentals",
      max_results=10,
      search_domain_filter=["wikipedia.org"]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print("---")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Matches en.wikipedia.org, fr.wikipedia.org, de.wikipedia.org, etc.
  const response = await client.search.create({
    query: "quantum mechanics fundamentals",
    max_results: 10,
    search_domain_filter: ["wikipedia.org"]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "quantum mechanics fundamentals",
      "max_results": 10,
      "search_domain_filter": ["wikipedia.org"]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "dd3d8ff9-e837-4413-9628-80a1c8dba4f6",
    "results": [
      {
        "snippet": "",
        "title": "Quantum mechanics - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Quantum_mechanics",
        "date": "2001-11-14",
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "Quantum mechanics is the field of physics that explains how extremely small objects simultaneously have the characteristics of both particles (tiny pieces of matter) and waves (a disturbance or variation that transfers energy).\nPhysicists call this the “wave-particle duality.”\nThe particle portion of the wave-particle duality involves how objects can be described as “quanta.”\nA quanta is the smallest discrete unit (such as a particle) of a natural phenomenon in a system where the units are in a bound state.\nFor example, a quanta of electromagnetic radiation, or light, is a photon.\nA bound state is one where the particles are trapped.\nOne example of a bound state is the electrons, neutrons, and protons that are in an atom.\nTo be “quantized” means the particles in a bound state can only have discrete values for properties such as energy or momentum.\nFor example, an electron in an atom can only have very specific energy levels.\nThis is different from our world of macroscopic particles, where these properties can be any value in a range.\nA baseball can have essentially any energy as it is thrown, travels through the air, gradually slows down, then stops.\nAt the same time, tiny quantized particles such as electrons can also be described as waves.\nLike a wave in the ocean in our macroscopic world – the world we can see with our eyes -- waves in the quantum world are constantly shifting.\nIn quantum mechanics, scientists talk about a particle’s “wave function.”\nThis is a mathematical representation used to describe the probability that a particle exists at a certain location at a certain time with a certain momentum.\nThe world of quantum mechanics is very different from how we usually see our macroscopic world, which is controlled by what physicists call classical mechanics.\n...\n- Many subatomic particles, including the proton, have angular momentum, which is often referred to as “spin.”\nMedical experts use this property in MRI imaging devices.\n- Smartphones contain billions of transistors that work based on the wave nature of electrons, which scientists understand through quantum mechanics.\n- Quantum computers and quantum networks are new applications of quantum mechanics that use the quantized nature of particles to store and transfer information.",
        "title": "DOE Explains...Quantum Mechanics - Department of Energy",
        "url": "https://www.energy.gov/science/doe-explainsquantum-mechanics",
        "date": "2026-05-14",
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "",
        "title": "Introduction to quantum mechanics - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Introduction_to_quantum_mechanics",
        "date": "2005-09-29",
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "",
        "title": "The Basics of Quantum Mechanics",
        "url": "https://thequantumlaend.de/basic-tutorial/",
        "date": null,
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "## Quantum mechanics explores the fundamental nature of matter and energy at the smallest scales.\nKey concepts include quantised particles and probabilistic wave functions, as governed by the Schrödinger equation.\nNotable principles of quantum mechanics, such as wave-particle duality and the uncertainty principle, challenge classical physics.\nQuantum phenomena like tunnelling and entanglement enable groundbreaking technologies, including quantum computing and cryptography.\nThe origins of quantum theory can be traced back to pivotal contributions by Max Planck, Albert Einstein, and others.\n...\nQuantum physics, the branch of science that investigates the behaviour of matter and energy at the smallest scales, introduces a groundbreaking framework where classical mechanics no longer apply.\nAt the core of this field lies the concept of quantisation, where particles such as electrons are described by discrete packets referred to as quanta.\nThese quantum objects are governed by probabilistic wave functions and the Schrödinger equation, allowing them to exist in multiple states simultaneously—an idea recognised as superposition.\nOne of the intriguing phenomena in quantum physics is quantum tunnelling, where particles pass through potential barriers that would be insurmountable in classical physics.\n...\nQuantum decoherence describes the process by which a quantum system loses its superposition state due to interaction with its environment, shifting it to a classical state.\nThis phenomenon is a significant challenge in the development of quantum computing, where maintaining coherence is essential for performing calculations that far exceed the capabilities of classical computers.\nQuantum teleportation, another fascinating concept, involves the transfer of quantum information between particles over distance, leveraging the phenomenon of entanglement.\n...\nThese collective efforts culminated in the formulation of quantum mechanics, a probabilistic framework that profoundly altered our understanding of particle behaviour and interactions at the microscopic level.\n...\nOne of the most intriguing aspects of quantum mechanics is wave-particle duality, which posits that particles such as electrons exhibit both wave-like and particle-like properties.\nThis concept challenges the classical physics paradigm by demonstrating that particles can exhibit wave characteristics, such as interference patterns, a phenomenon traditionally attributed solely to waves.\n...\nSuperposition and entanglement are cornerstones of quantum mechanics.\nThey present phenomena that defy classical intuition and underpin the field’s most revolutionary advancements.\nIn quantum physics, superposition refers to the ability of quantum particles to exist in multiple states simultaneously.\nThis property is pivotal in quantum computing, where quantum bits, or qubits, harness superposition to perform complex computations in parallel, leading to exponential speedups in solving certain problems compared to classical computers.\nQuantum entanglement, another fundamental concept, occurs when particles become interconnected in such a way that the state of one particle instantly influences the state of another, regardless of the distance separating them.\nThis phenomenon, known as quantum entanglement, is instrumental in the development of quantum communication and quantum information processing.\n...\nThe Schrödinger Equation stands as a cornerstone in quantum mechanics, offering a profound mathematical framework for understanding the dynamic behaviour of quantum systems.\n...\nAt the heart of the Schrödinger Equation is the concept of the wave function.\n...\nThe Uncertainty Principle, a cornerstone of quantum mechanics formulated by Werner Heisenberg, delineates the fundamental limitations in simultaneously measuring certain pairs of complementary properties, such as a particle’s position and momentum, with arbitrary precision.\nThis principle underscores the quantum uncertainty inherent in particle dynamics, challenging the classical physics notion that such properties can be measured with exactitude.\nHeisenberg’s principle asserts that the more precisely one knows a particle’s position, the less precisely one can know its momentum, and vice versa.\n...\nConsequently, any attempt to measure one property with high precision inevitably disturbs the other, introducing an intrinsic quantum uncertainty.\nAt its core, the Uncertainty Principle fundamentally alters our understanding of predictability and measurability at the quantum level.\nIt implies that there is a limit to the precision with which we can simultaneously know a particle’s position and momentum.\nThis limit is not due to experimental imperfections but a fundamental property of nature itself, rooted in the principles of quantum mechanics.\n...\nQuantum physics fundamentally challenges classical conceptions of reality by introducing phenomena such as superposition, wave-particle duality, and probabilistic behaviour.",
        "title": "Exploring the key concepts of quantum mechanics",
        "url": "https://www.innovationnewsnetwork.com/exploring-the-key-concepts-of-quantum-mechanics/51254/",
        "date": "2024-10-14",
        "last_updated": "2026-02-18"
      },
      {
        "snippet": "Quantum mechanics was developed in just two years, 1925 and 1926 (see here if you want to know why).\nThere were initially two versions, one formulated by Werner Heisenberg and one by Erwin Schrödinger.\n...\nDe Broglie figured that\nwhat goes for light might go for matter too: perhaps tiny\nbuilding blocks of matter, such as electrons, might also suffer from this\n*wave particle duality*.\n...\nOrdinary waves, such as those that can travel down a piece of\nstring, can be described mathematically.\nYou can formulate a\n*wave\nequation*, which describes how a particular wave\nchanges over space and time.\nA solution to that equation is a *wave\nfunction*, which describes the shape of the wave at every point in\ntime.\n...\nA solution to Schrödinger's equation is called a\n*wave\nfunction*.\nIt tells you things about the *quantum system* you\nare considering.\n...\nAs an example, imagine a single particle moving around in a closed box.\nSolving the wave equation which\ndescribes this system, you get the corresponding wave function.\nOne\nthing the wave function doesn't tell you is where exactly the particle\nwill be at each point in time of its journey.\n...\nWhat the wave function does give you is a number (generally a\n*complex number*) for each\npoint *x* in the box at each point *t* in time of the particle's journey.\nIn\n1926 the physicist Max Born came up with an interpretation of this\nnumber: after a slight modification, it gives you the probability of\nfinding the particle at the point *x* at time *t*.\nWhy\na probability?\nBecause unlike an ordinary billiard ball, which obeys the\nclassical laws of physics, our particle doesn't have a clearly defined trajectory that leads it to a particular point.\nWhen we open the box and look, we *will*\nfind it at one particular point, but there's no way of predicting in\nadvance which one it is.\nAll we have are probabilities.\nThat's the\nfirst strange prediction of the theory: the world, at bottom, is not\nas certain as our everyday experience of billiard balls has us\nbelieve.\nA second strange prediction follows straight on from the first.\nIf we don't open the box and spot the particle in a particular location, then where is it?\nThe answer is that it's in all the places we could have potentially seen it in at once.\n...\nSuppose you have found a wave function that is a solution to Schrödinger's\nequation and describes our particle being in some location in the box.\nNow there might be another wave function\nwhich is also a solution to the same equation, but describes the\nparticle being in another part of the box.\nAnd here's the thing: if\nyou add these two different wave functions, the sum is also a\nsolution!\nSo, if the particle being in one place is a solution and the\nparticle being in another place is a solution, then the particle being in the first place and the second place is also a solution.\nIn this sense, the particle can\nbe said to be in several places at once.\nIt's called\n*quantum\nsuperposition* (and it's the inspiration for Schrödinger's famous thought experiment involving a cat).\n...\nAs we have seen, it's impossible to\npredict where\nour particle in the box is going be when we measure\nit.\nThe same goes for any other thing you might want to measure about the particle, for example its momentum: all you can do is work out the probability that the momentum takes each of several possible values.\nTo work out from the wave function what those possible values of position and momentum are, you need mathematical objects called\n*operators*.\n...\nWhen we have performed the measurement, say of position, the particle is most\ndefinitely in a single place.\nThis means that its wave function has\nchanged (collapsed) to a wave function describing a particle that is\ndefinitely in one particular place with 100% certainty.\n...\nIf you were to measure momentum and position simultaneously, and get certain answers for both, then the two eigenstates corresponding to position and momentum would have to be the same.\nIt's a mathematical fact, however, that the eigenstates of these two operators never do coincide.\nJust as 3+2 will never make 27, so don't the mathematical operators corresponding to position and momentum behave in a way that would allow them to have coinciding eigenstates.\nTherefore, position and momentum can never be measured simultaneously with arbitrary accuracy.\n(For those familiar with some of the technicalities, the eigenstates cannot be the same because the operators don't commute.)\nAs we know from experience, superposition disappears when we look\nat a particle.\nNobody has ever directly seen a single particle in several places at once.\n...\nAnother thing that comes straight out of the maths of Schrödinger's equation is\nHeisenberg's famous\n*uncertainty principle*.\nThe principle says that\nyou can never, ever measure both the position and the momentum of\na quantum object, like our particle in a box, with arbitrary precision.\nThe\nmore precise you are about the one, the less you can say about the\nother.\nThis isn't because your measurement tools aren't good enough —\nit's a fact of nature.\n...\nPosition and momentum aren't the only\n*observables* that\ncan't be measured simultaneously with arbitrary accuracy.\nTime and\nenergy are another pair: the more precise you are about the time span\nsomething happens in the less precise you can be about the energy of\nthat something and vice versa.\nFor this reason, particles can acquire\nenergy from out of nowhere for very brief moments of time, something\nthat's impossible in ordinary life — it's called *quantum\n...\nAnd here's another quantum strangeness arising from the wave\nfunction:\n*entanglement*.\nA wave function can also describe a\nsystem of many particles.\nSometimes it is impossible to decompose the\nwave function into components that correspond to the individual\nparticles.\nWhen that happens, the particles become inextricably\nlinked, even if they move far away from each other.\nWhen something happens to one of the entangled particles, a corresponding thing happens to its distant partner, a phenomenon Einstein described as \"spooky action at a distance\".",
        "title": "Introduction to Quantum Mechanics",
        "url": "https://plus.maths.org/content/ridiculously-brief-introduction-quantum-mechanics",
        "date": "2025-01-01",
        "last_updated": "2026-02-28"
      },
      {
        "snippet": "",
        "title": "Quantum Physics Full Course | Quantum Mechanics Course",
        "url": "https://www.youtube.com/watch?v=hyctIDPRSqY",
        "date": "2021-10-21",
        "last_updated": "2026-03-26"
      },
      {
        "snippet": "In this chapter we summarize the main elements of non-relativistic quantum mechanics.\nWe will do so through a list of postulates and principles that can be followed for the\napplication of the quantum mechanical formalism to specific problems.\n...\n1.1.1 First Postulate\nAt a given time t, the physical state of a system is described by a ket |ψ (t)⟩(using\n…\nd3x ϕ∗(x) χ (x) ,\n(1.2)\nwhere ∗stands for complex conjugation.\nSecond, to the ket |r⟩is associated a Dirac\ndistribution\n|r⟩⇐⇒δ (x −r) ,\n(1.3)\nsuch that\n⟨r | ψ (t)⟩\n=\n�∞\n−∞\nd3x δ (x −r) ψ (x, t)\n≡\nψ (r, t)\n(1.4)\n1\n…\n...\n.\n(1.5)\n1.1.2 Second Postulate\nFor every measurable physical quantity A corresponds an operator ˆA, and this operator\n…\n(1.7)\nwith ˆA† the adjoint of ˆA and, by definition, (|ψ⟩)† = ⟨ψ|.\n1.1.3 Third Postulate\nThe outcome of the measurement of a physical quantity A must be an eigenvalue of the\ncorresponding observable ˆA.\n…\n...\n1.1.4 Fourth Postulate\nThe ket, say |ψ (t)⟩, specifying the state of a system is assumed normalized to unity.\nThat is,\n⟨ψ (t) | ψ (t)⟩= 1.\n(1.10)\n…\n...\ndefinitions, we can state the fourth postulate of quantum mechanics as follows:\nIn measuring the physical quantity A on a system in the state |ψ⟩, the probability of\nobtaining the (possibly degenerate) eigenvalue “a” of the corresponding observable is\nP (a) =\ngn\n�\n…\n...\nThis postulate\nsimply ensures that the new ket (or wave function) describing the system after a mea-\nsurement is suitably normalized to unity.\n...\nAlthough it is possible to give a “derivation” of the Schrödinger equation, it is sufficient\nfor our purposes to introduce it as the sixth, and last, postulate of quantum mechanics:\nThe time evolution of the state vector of a system is dictated by the Schrödinger equa-\ntion\niℏd\ndt |ψ (t)⟩= ˆH (t) |ψ (t)⟩,\n(1.52)\nwhere ˆH (t) is the Hamiltonian of the system, i.e., the observable associated with the\nenergy of the system.\nIn most cases, we will be dealing with a time-independent Hamiltonian that has so-\ncalled stationary states whose norms do not change as a function of time (see below).\n...\nA few principles need to be added to the previous postulates in order to use the formalism\nof quantum mechanics to make predictions on experiments, and to ensure that it is\n...\n1.2.1 The Principle of Superposition\nWe already know that the state of a quantum mechanical system is entirely contained\nwithin a ket, say, ϕ1, which can be a function of time.\nIt may be the case, however,\nthat several different states ϕj, with j = 1, 2, . . . , n, are available for the system.\nThe\nPrinciple of Superposition then states that\nIf several states are available for a quantum mechanical system, then it can also be in\nany possible linear combinations of them.\nIn mathematical terms this means that the most general form for the state ψ of the\nsystem is given by\nψ =\nn\n�\nj=1\ncj |ϕj⟩\n(1.60)\nwhere cj = ⟨ϕj | ψ⟩are complex coefficients.\n...\nThe superposition of states is responsible for the presence of interference (and coherence)\nin quantum mechanical systems.\nThis experimental fact can be understood if one accepts\n...\nThis was\nfirst made explicit by Bohr when he enunciated his Principle of Complementarity,\nwhich can be stated as follows1\nIt is not possible to describe physical observables simultaneously and completely in terms\nof particles and waves.\nWhat this principle implies is that attempts to acquire knowledge on the state of a\nsystem (e.g., the path a particle takes) cannot be accomplished without disturbing it\nand changing its state.\nIn other word, the interference that would be detected for the\nundisturbed system (i.e., the wave-like behaviour) will be affected by the act of acquiring\ninformation on its state.\n...\nAlthough the picture of the microscopic world provided by quantum mechanics is often\ncompletely at odds with what we would expect on large scales with classical mechanics, it\nmust be that the two realms are consistent with one another and come to an agreement\n...\nImportantly, predictions made with quantum mechanics\nmust agree with those of classical mechanics in conditions where the applicability of the\nlatter is warranted.\nThis requirement is formulated through Bohr’s Correspondence\nPrinciple\nQuantum mechanical physical quantities should tend to the classical mechanical coun-\nterparts in the macroscopic limit.\nMathematically, the macroscopic limit is reached when the Planck constant h is negli-\ngible compared to the action of the system2.\nIn such cases, quantum mechanical effects\nand phenomena have no consequence on the behaviour of the system.\n...\nWe therefore find the fundamental result that the action of the momentum operator in\nthe position basis {|r⟩} is represented by\nˆp ⇒−iℏ∇.",
        "title": "[PDF] 1 Fundamentals of Quantum Mechanics",
        "url": "https://physics.uwo.ca/~mhoude2/courses/PDF%20files/physics9203/Ch1-Fundamentals.pdf",
        "date": null,
        "last_updated": "2026-04-12"
      },
      {
        "snippet": "1st Edition\n# Quantum Mechanics Fundamentals\nBy Kurt Gottfried Copyright 1974\n528 Pages\nby CRC Press\n...\nThis book contains discussions of radiation theory, quantum statistics and the many-body problem, and more advanced topics in collision theory.\nIt is intended as a text for a first-year graduate quantum mechanics course.",
        "title": "Quantum Mechanics: Fundamentals",
        "url": "https://www.routledge.com/Quantum-Mechanics-Fundamentals/Gottfried/p/book/9780201406337",
        "date": null,
        "last_updated": "2024-08-02"
      },
      {
        "snippet": "",
        "title": "[PDF] Fundamentals of Quantum Mechanics",
        "url": "http://iht.knu.ua/Kolezhuk/SelChapPhys/Tang.pdf",
        "date": null,
        "last_updated": "2026-04-22"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**5. Filter to a Section of a Site**

Restrict results to a specific path on a domain — useful for documentation sites, subreddits, blogs, or news sections:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Only results under nature.com/articles
  response = client.search.create(
      query="CRISPR base editing clinical results",
      max_results=10,
      search_domain_filter=["nature.com/articles"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Only results under nature.com/articles
  const response = await client.search.create({
    query: "CRISPR base editing clinical results",
    max_results: 10,
    search_domain_filter: ["nature.com/articles"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "CRISPR base editing clinical results",
      "max_results": 10,
      "search_domain_filter": ["nature.com/articles"]
    }' | jq
  ```
</CodeGroup>

**6. Denylist Specific Domains**

This example shows how to exclude specific domains from search results by prefixing the domain name with a minus sign (`-`):

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Exclude social media and Q&A sites from search results
  response = client.search.create(
      query="renewable energy capacity additions and grid storage breakthroughs",
      max_results=10,
      search_domain_filter=[
          "-pinterest.com",
          "-reddit.com",
          "-quora.com"
      ]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Exclude social media and Q&A sites from search results
  const response = await client.search.create({
    query: "renewable energy capacity additions and grid storage breakthroughs",
    max_results: 10,
    search_domain_filter: [
      "-pinterest.com",
      "-reddit.com",
      "-quora.com"
    ]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "renewable energy capacity additions and grid storage breakthroughs",
      "max_results": 10,
      "search_domain_filter": [
        "-pinterest.com",
        "-reddit.com",
        "-quora.com"
      ]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "5764c1f5-c71d-4e0f-94cb-d02f7c2f1af8",
    "results": [
      {
        "snippet": "U.S. power plant developers and operators plan to add 86 gigawatts (GW) of new utility-scale electric generating capacity to the U.S. power grid in 2026 in our latest Preliminary Monthly Electric Generator Inventory report, a record if realized.\nSolar power makes up 51% of the planned 2026 capacity additions, followed by battery storage at 28% and wind at 14%.\nIn 2025, 53 GW of new capacity was added to the grid, the largest capacity installation in a single year since 2002.\nSolar.\nWe expect 2026 to be another big year for solar additions, similar to the record utility-scale solar capacity added to the U.S. grid in 2024 (30.8 GW) and in 2025 (27.2 GW).\nDevelopers plan to add 43.4 GW of new utility-scale solar capacity in 2026, a 60% increase in capacity additions from last year if realized.\nMore than half of the new utility-scale solar capacity is planned for four states: Texas (40%), Arizona (6%), California (6%), and Michigan (5%).\nA new project, Tehuacana Creek 1 Solar and BESS, adding 837 megawatts (MW) in Texas, is the largest solar photovoltaic project expected to come online in 2026; it will also offer an additional 418 MW in battery energy storage capacity.\nBattery storage.\nDevelopers plan to add 24 GW of utility-scale battery storage to the grid this year, compared with a record 15 GW added in 2025.\nU.S. battery storage capacity has grown exponentially over the last five years with more than 40 GW added to the grid during this period.\nProjects in three states make up the bulk of planned battery storage capacity in 2026, accounting for about 80% of the new U.S. battery storage capacity: 53%, or 12.9 GW, in Texas; 14%, or 3.4 GW, in California; and 13%, or 3.2 GW, in Arizona.\nThree of the four largest battery storage projects scheduled to come online in 2026 are in Texas:\nWind.\nAnnual U.S. wind capacity additions have slowed, following record additions of more than 14 GW in both 2020 and 2021.\nBut wind capacity addition could rise in 2026 with 11.8 GW planned to be added to the grid, more than double the capacity added last year.\nNew Mexico, Texas, Illinois, and Wyoming combined will account for almost 60% of 2026 wind capacity additions.\nTwo large offshore wind plants, the 800-MW Vineyard Wind 1 in Massachusetts and the 715-MW Revolution Wind in Rhode Island, which the companies now plan to bring online in 2026 after delays.\nThe 3,650-MW SunZia Wind project in New Mexico is also expected to start commercial operations this year and will be the largest onshore wind project in the United States.",
        "title": "New U.S. electric generating capacity expected to reach a record high in ...",
        "url": "https://www.eia.gov/todayinenergy/detail.php?id=67205",
        "date": "2026-05-21",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "[PDF] Progress in Grid Energy Storage",
        "url": "https://www.energy.gov/sites/prod/files/Presentation%20to%20the%20EAC%20-%20Progress%20in%20Grid%20Energy%20Storage%20-%20Imre%20Gyuk.pdf",
        "date": null,
        "last_updated": "2026-03-11"
      },
      {
        "snippet": "We expect 63 gigawatts (GW) of new utility-scale electric-generating capacity to be added to the U.S. power grid in 2025 in our latest Preliminary Monthly Electric Generator Inventory report.\nThis amount represents an almost 30% increase from 2024 when 48.6 GW of capacity was installed, the largest capacity installation in a single year since 2002.\nTogether, solar and battery storage account for 81% of the expected total capacity additions, with solar making up over 50% of the increase.\nSolar.\nIn 2024, generators added a record 30 GW of utility-scale solar to the U.S. grid, accounting for 61% of capacity additions last year.\nWe expect this trend will continue in 2025, with 32.5 GW of new utility-scale solar capacity to be added.\nTexas (11.6 GW) and California (2.9 GW) will account for almost half of the new utility-scale solar capacity addition in 2025.\nWe expect five other states (Indiana, Arizona, Michigan, Florida, and New York) each to account for more than 1 GW of added solar capacity in 2025 and collectively account for 7.8 GW of planned solar capacity additions.\nBattery storage.\nIn 2025, capacity growth from battery storage could set a record as we expect 18.2 GW of utility-scale battery storage to be added to the grid.\nU.S. battery storage already achieved record growth in 2024 when power providers added 10.3 GW of new battery storage capacity.\nThis growth highlights the importance of battery storage when used with renewable energy, helping to balance supply and demand and improve grid stability.\n...\nWind.\nIn 2025, we expect 7.7 GW of wind capacity to be added to the U.S. grid.\nLast year, only 5.1 GW was added, the smallest wind capacity addition since 2014.\nTexas, Wyoming, and Massachusetts will account for almost half of 2025 wind capacity additions.\nTwo large offshore wind plants are expected to come online this year: the 800-megawatt (MW) Vineyard Wind 1 in Massachusetts and the 715-MW Revolution Wind in Rhode Island.",
        "title": "Solar, battery storage to lead new U.S. generating capacity additions ...",
        "url": "https://www.eia.gov/todayinenergy/detail.php?id=64586",
        "date": "2026-05-14",
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "# US$ 1.2 trillion in battery storage investments needed to support global renewable buildoutt\nGrid-forming battery technology emerges as critical solution for US$5 trillion global renewable energy integration\n...\nInvestments of US$1.2 trillion in battery energy storage systems (BESS) will be required to support the installation of over 5,900 GW (Gigawatt) of new wind and solar capacity globally through 2034, according to Wood Mackenzie.\nThe deployment of grid-forming technology (GFM) needs to accelerate over the next decade to facilitate the projected $5 trillion global expansion of renewable energy.\nUnlike traditional grid-following systems that simply respond to grid conditions, grid-forming battery energy storage systems can actively create and maintain grid stability.\nThis capability becomes essential as renewable energy becomes the dominant source of power generation globally.\n“Grid-forming battery energy storage systems represent a critical breakthrough for renewable energy integration,” said Robert Liew, research director at Wood Mackenzie.\n“As global power demand is projected to surge 55% by 2034, with variable renewable energy comprising over 80% of new capacity additions, GFM BESS provides the technological bridge between renewable abundance and grid stability requirements.”\n...\nAccording to a recent Wood Mackenzie report, the global power sector faces a capacity gap of 1,400 GW for additional battery energy storage installations utilising GFM for grid stability between 2024 to 2034.\n...\nWhile grid-forming capabilities add an estimated 15% to overall system costs largely due to upgraded inverters, controls, and software, these cost hurdles are becoming more manageable as average battery energy storage prices have declined between 10% and 40% across global markets in the past year, according to Wood Mackenzie.\n...\nWith global electricity demand forecast to grow at a compound annual rate of 3% through 2040, according to Wood Mackenzie, grid-forming batteries are emerging as a practical replacement for conventional synchronous generators.\nTheir ability to provide voltage and frequency stability is positioning them as a foundational technology for high-renewable power systems.\n“We’re seeing a convergence of key factors, declining battery costs, stronger clean energy targets, supportive policy developments, and proven pilot projects, that are accelerating the adoption of grid-forming technology,” said Liew.\n“With global battery capacity expected to triple by 2035, grid-forming capabilities will likely become a baseline requirement for new storage deployments.\nThis will be essential not only for grid reliability, but also for unlocking the full value of renewable energy investments at scale.”",
        "title": "US$ 1.2 trillion in battery storage investments needed to support ...",
        "url": "https://www.woodmac.com/press-releases/bess-opportunity/",
        "date": "2025-07-02",
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "According to data from the Federal Energy Regulatory Commission, renewable energy sources will account for 99% of all new electricity generating capacity added to the American grid in 2026, marking what industry experts describe as a fundamental restructuring of the nation’s power infrastructure.\nThis near-total dominance of clean energy in new capacity additions represents a dramatic acceleration from previous years and signals that the transition away from fossil fuel generation has moved beyond policy aspirations into market reality.\nSlashdot reported that solar power alone will contribute 76.9 gigawatts of new capacity, while wind energy will add another 15.2 gigawatts, with battery storage systems providing an additional 33.8 gigawatts to support grid stability.\n...\nNatural gas, which once represented the bridge fuel to a cleaner energy future, will account for merely 1% of new capacity additions this year, with a paltry 1.1 gigawatts of new plants coming online.\n...\nThe shift toward renewable dominance stems primarily from fundamental economics rather than regulatory mandates.\nSolar panel costs have plummeted approximately 90% since 2010, while wind turbine efficiency has improved dramatically through technological advances in blade design and tower height.\nBattery storage costs have followed a similar trajectory, dropping roughly 80% over the past decade, making it economically viable to pair intermittent renewable sources with storage systems that can dispatch power when the sun isn’t shining or wind isn’t blowing.\n...\nThe rapid expansion of variable renewable energy sources has forced grid operators to fundamentally rethink how they manage electricity supply and demand.\n...\nBattery storage systems have emerged as the critical technology enabling this transition.\nThe 33.8 gigawatts of storage capacity being added in 2026 will provide grid operators with unprecedented flexibility to absorb excess renewable generation during periods of high production and release that stored energy during peak demand periods.\n...\nIndustry analysts project that renewable energy’s dominance of new capacity additions will continue and likely intensify in coming years.\n...\nThe United States is in the midst of the most significant transformation of its electricity infrastructure since the original grid buildout in the early twentieth century, and renewable energy has emerged as the dominant force shaping that transformation.",
        "title": "How Renewable Energy Seized 99% of New Capacity ...",
        "url": "https://www.webpronews.com/americas-grid-transformation-how-renewable-energy-seized-99-of-new-capacity-additions-in-2026/",
        "date": "2026-02-02",
        "last_updated": "2026-02-24"
      },
      {
        "snippet": "New Delhi: Global investment of $1.2 trillion will be required in\nbattery energy storage systems\n(BESS) over the next decade to support the addition of 5,900 gigawatts (GW) of new wind and solar capacity worldwide, energy consultancy Wood Mackenzie said in its latest analysis.\nThe report forecasts a 55 per cent increase in\nglobal power demand by 2034\n, with more than 80 per cent of new capacity additions expected to come from variable renewable energy sources.\n'Grid-forming battery energy storage systems represent a critical breakthrough for\nrenewable energy integration\n,' Robert Liew, Research Director at Wood Mackenzie, said.\n'As global power demand is projected to surge 55 per cent by 2034, with variable renewable energy comprising over 80 per cent of new capacity additions, GFM BESS provides the technological bridge between renewable abundance and\ngrid stability requirements\n.'\nGrid-forming battery systems differ from traditional grid-following systems by actively supporting voltage and frequency stability, which is essential as the share of intermittent renewable sources increases.\nAccording to the report, the power sector faces a 1,400 GW capacity gap for\ngrid-forming battery storage\ninstallations between 2024 and 2034. This shortfall highlights the need for large-scale deployment of storage systems to ensure grid reliability.\n...\nWhile grid-forming capabilities add about 15 per cent to system costs, primarily due to advanced inverters and software, battery prices have declined by 10–40 per cent across global markets over the past year. The report said this has improved the economic feasibility of such installations.\nHybrid utility-scale solar and battery storage systems are already cost-competitive with onshore wind, and projections suggest that battery systems will undercut coal and gas power generation costs in several non-US markets by 2040.\n...\n'Increasing\nclean energy targets\n, policy developments, and proven pilot projects are accelerating the adoption of grid-forming technology,' Liew added. 'With global battery capacity expected to triple by 2035, grid-forming capabilities will likely become a baseline requirement for new storage deployments.'",
        "title": "$1.2 trillion needed for grid-forming battery storage to support global renewable push: Report",
        "url": "https://energy.economictimes.indiatimes.com/news/renewable/1-2-trillion-needed-for-grid-forming-battery-storage-to-support-global-renewable-push-report/122195907",
        "date": "2025-07-02",
        "last_updated": "2025-07-02"
      },
      {
        "snippet": "# $1.2 trillion needed for grid-forming battery storage to support global renewable push: Report\n...\nNew Delhi: Global investment of $1.2 trillion will be required in battery energy storage systems (BESS) over the next decade to support the addition of 5,900 gigawatts (GW) of new wind and solar capacity worldwide, energy consultancy Wood Mackenzie said in its latest analysis.\n...\n“Grid-forming battery energy storage systems represent a critical breakthrough for renewable energy integration,” Robert Liew, Research Director at Wood Mackenzie, said.\n“As global power demand is projected to surge 55 per cent by 2034, with variable renewable energy comprising over 80 per cent of new capacity additions, GFM BESS provides the technological bridge between renewable abundance and grid stability requirements.”\nGrid-forming battery systems differ from traditional grid-following systems by actively supporting voltage and frequency stability, which is essential as the share of intermittent renewable sources increases.\nAccording to the report, the power sector faces a 1,400 GW capacity gap for grid-forming battery storage installations between 2024 and 2034.\nThis shortfall highlights the need for large-scale deployment of storage systems to ensure grid reliability.\n...\n“With global battery capacity expected to triple by 2035, grid-forming capabilities will likely become a baseline requirement for new storage deployments.”",
        "title": "$1.2 trillion needed for grid-forming battery storage to support global renewable push: Report - ET EnergyWorld",
        "url": "https://energy.economictimes.indiatimes.com/amp/news/renewable/1-2-trillion-needed-for-grid-forming-battery-storage-to-support-global-renewable-push-report/122195907",
        "date": "2025-07-02",
        "last_updated": "2025-07-11"
      },
      {
        "snippet": "The United States is experiencing an unprecedented acceleration in utility-scale battery storage deployment, a critical development that immediately enhances the power grid’s ability to manage intermittent renewable energy.\nThis surge means that wind and solar power can be reliably dispatched when needed, effectively turning variable generation into firm capacity.\nThe most significant indicator of this shift is the projected installation of **74 gigawatts (GW)** of new storage capacity between 2024 and 2028.\n...\nThis rapid deployment is a direct result of two converging forces: supportive federal policy and clear market demand.\nThe federal Investment Tax Credit (ITC) for standalone storage has made these projects financially viable on their own, decoupling them from solar farms.\n...\nThink of grid batteries like a shock absorber for the power system: they instantly absorb excess power when generation is high and release it just as quickly when demand spikes, smoothing out the volatility inherent in renewable sources.\n...\n- **Projected Capacity Addition** → 74 GW.\nThe expected new utility-scale storage capacity to be installed in the US between 2024 and 2028.\n- **Operational Capacity (July 2024)** → 20.7 GW.\nThe total utility-scale battery storage capacity already operating on the US grid as of mid-2024.\n- **Record Quarterly Addition** → 3,806 MW.\nThe amount of new utility-scale storage capacity added in the US during the record-setting third quarter of 2024.\n...\nThe next critical indicator will be the pace of long-duration energy storage (LDES) projects moving from pilot to final investment decision.\nWhile current batteries handle four to eight hours of storage, the long-term stability of a deeply decarbonized grid requires solutions that can store power for days or weeks.\nWatch for major finance announcements for non-lithium technologies like iron-air or compressed air storage, which will signal the next phase of grid resilience.\n**The US grid is rapidly transforming, with battery storage now a primary, bankable asset for securing a reliable, high-renewable power system.**",
        "title": "US Grid Battery Storage Boom Secures Massive Renewable Energy ...",
        "url": "https://news.sustainability-directory.com/energy/us-grid-battery-storage-boom-secures-massive-renewable-energy-future/",
        "date": "2025-12-01",
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "The US power sector is planning a record 86 gigawatts (GW) of new electric generating capacity additions for 2026, signaling a fundamental shift in resource procurement where variable renewables and storage are now the dominant development focus for the grid.\nThis means the grid is rapidly evolving to rely on intermittent sources that require immediate co-location with storage to provide reliable power.\nThe single most important data point is that solar power alone accounts for 51% of all planned 2026 capacity additions, followed by battery storage at 28%.\n...\nThis massive planned build is caused by the sustained economic advantage of solar photovoltaic technology combined with the rapidly falling cost and increasing duration of battery storage, making them the cheapest and fastest-to-deploy options for adding net new power.\nThe core dynamic is that solar provides cheap energy when the sun shines, and batteries provide the necessary “firming” capacity → the ability to dispatch power when needed → to make that solar reliable for the grid.\nThink of grid batteries like a water tower for electricity: they capture the excess solar energy during the day and release it during evening peak demand, directly replacing the need for traditional gas or coal plants to ramp up.\n...\n- **Total Planned Capacity** → 86 gigawatts (GW) – The total planned addition of new utility-scale electric generating capacity for 2026\n...\n**The US energy system is now fundamentally structured around deploying solar power paired with battery storage as the primary engine for all new electricity capacity.**",
        "title": "Record US Power Build Signals Solar and Storage Grid Dominance",
        "url": "https://news.sustainability-directory.com/energy/record-us-power-build-signals-solar-and-storage-grid-dominance/",
        "date": "2026-03-18",
        "last_updated": "2026-05-09"
      },
      {
        "snippet": "The U.S. utility-scale battery storage market is experiencing a massive, policy-driven surge, setting a record for new capacity additions.\nThis development fundamentally changes the power grid’s operational dynamics, shifting it to a system where intermittent solar and wind can be stored and dispatched on demand, thereby enhancing reliability.\nThe scale of this transition is underscored by the forecast of **74 gigawatts** of new storage capacity expected to be installed between 2024 and 2028.\n...\nThis explosive growth is a direct cause-and-effect outcome of state-level clean energy mandates and the falling cost of battery technology.\nStates like California and Texas have set aggressive procurement targets, creating a clear, stable demand signal for investors.\nThis market shift has turned batteries into a “non-wires alternative,” meaning they can solve grid congestion and reliability issues more cheaply and quickly than building new power lines or fossil fuel plants.\nThink of grid batteries like a water tower for electricity: they store excess power when supply is high, such as midday solar, and release it instantly when demand peaks, smoothing out the variability of renewables and providing essential grid services like frequency response.\n...\n- **Projected New Capacity** → 74 GW (Gigawatts).\nThe total utility-scale battery storage capacity forecast to be installed across the U.S. between 2024 and 2028, showing the massive scale of the near-term market.\n- **Operational Capacity** → 20.7 GW (Gigawatts).\nThe approximate utility-scale battery storage capacity operational in the U.S. as of Q3 2024.\n- **Record Quarter** → 3,806 MW (Megawatts).\nThe record amount of new utility-scale storage capacity added to the U.S. grid in the third quarter of 2024.\n...\nThe next thing to watch is the continued commercialization of long-duration energy storage technologies, which can store power for 8 to 100 hours.\nThis will show if the grid can move beyond daily solar-shifting to multi-day resilience, which is the final technical hurdle for a truly decarbonized, 24/7 clean power system.\n**Grid-scale batteries are no longer a niche technology; they are the core infrastructure enabling the next phase of the clean energy transition.**",
        "title": "US Grid Battery Storage Deployment Surges, Enabling Massive ...",
        "url": "https://news.sustainability-directory.com/energy/us-grid-battery-storage-deployment-surges-enabling-massive-renewable-growth/",
        "date": "2026-01-06",
        "last_updated": "2026-05-19"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**7. Combining Domain Filter with Other Filters**

Domain filters work seamlessly with other search parameters for precise control:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine domain filter with date and language filters
  response = client.search.create(
      query="quantum computing hardware breakthroughs",
      max_results=20,
      search_domain_filter=[
          "nature.com",
          "science.org",
          "arxiv.org"
      ],
      search_recency_filter="month",
      search_language_filter=["en"]
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine domain filter with date and language filters
  const response = await client.search.create({
    query: "quantum computing hardware breakthroughs",
    max_results: 20,
    search_domain_filter: [
      "nature.com",
      "science.org",
      "arxiv.org"
    ],
    search_recency_filter: "month",
    search_language_filter: ["en"]
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "quantum computing hardware breakthroughs",
      "max_results": 20,
      "search_domain_filter": [
        "nature.com",
        "science.org",
        "arxiv.org"
      ],
      "search_recency_filter": "month",
      "search_language_filter": ["en"]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "2e8b1795-66a6-4cb5-978e-e21db62d3907",
    "results": [
      {
        "snippet": "- U.S. National Science Foundation funding drives breakthroughs that are enabling new quantum technologies while providing specialized training and education for American scientists and engineers.\n...\nThis combination of superposition and entanglement enables quantum computers to perform numerous calculations in parallel, dramatically increasing computing power and making them potentially capable of solving problems that are far too complex for classical computers.\n...\nIts full potential depends on a connected ecosystem of quantum computers to perform calculations, quantum networks to transmit information, and quantum sensors that capture precise details from their surroundings.\n...\nQuantum computing is in an experimental stage and requires highly specialized equipment, extremely cold temperatures and extraordinary precision.\nDespite remarkable progress, qubit-based computing is fragile and prone to errors, making it difficult to scale systems to hundreds or thousands of qubits while maintaining reliable performance.\nIn addition, developing algorithms that can fully harness quantum hardware and integrating quantum and classical systems adds another layer of complexity.\nYet, NSF-funded research is steadily overcoming these obstacles by advancing error correction, developing new qubit technologies and training next-generation quantum scientists and engineers — bringing the promise of practical quantum computing closer to reality.\n...\nNSF has been at the center of quantum computing breakthroughs for decades.\nIn the mid-1980s, NSF-funded researchers demonstrated that quantum tunneling, previously seen only in subatomic particles, could occur in a superconducting electrical circuit visible to the naked eye.\nThis showed that circuits could behave as quantum objects, opening the door to engineered quantum computers and later earning the 2025 Nobel Prize in physics.\nAbout a decade later, NSF-supported researchers advanced the field again by creating the first Bose-Einstein condensate, a state of matter where thousands of atoms act as a single \"superatom.\"\nThis breakthrough made it possible to study quantum phenomena on a macroscopic scale, unlocking new ways to understand quantum behavior and earning the 2001 Nobel Prize in physics.\nIn the early 2000s, NSF helped launch research into topological materials, whose unique properties can help keep quantum information intact.\nThis work was a key step in the ongoing work to create materials-based quantum computers, including Microsoft's Majorana-1 chip that debuted in 2025.\nNSF researchers are chipping away at long-standing challenges in quantum computing, like error correction and scalability.\nIn 2025, research groups at two NSF Physics Frontiers Centers made significant strides: One group created a new system that can detect and remove errors below a key performance threshold, a sign that practical error correction may finally be within reach.\nAnother group created a record-setting array of 6,100 neutral-atom qubits held in a grid by lasers.\nThey even moved these atoms across the grid while maintaining superposition, a key capability that makes neutral-atom systems especially promising for efficient error correction.\nTogether, these advances bring practical, powerful quantum computers closer to reality.\n...\nToday, NSF continues to drive the field forward through a range of programs.\nThe NSF Quantum Leap Challenge Institutes, established in 2020, fund large, collaborative projects to develop the essential components and functional pieces needed for reliable, scalable quantum computers, while training the next generation of quantum scientists and engineers.\nThe NSF National Quantum Virtual Laboratory is designing prototypes of future quantum infrastructure to give researchers across the country access to cutting-edge quantum hardware, software and algorithms, making it easier to test ideas and turn discoveries into technology.\nNSF boosts early-stage innovation through America's Seed Fund, supporting startups that are building everything from new qubit technologies to software and hardware subsystems.\nAt the same time, NSF fosters partnerships across universities, government labs, and industry to push forward hybrid classical-quantum systems, improve error correction, and explore emerging applications in artificial intelligence, cryptography, biotechnology and beyond.\nFrom theory to application, NSF's continued investments are enabling new methods, hardware and software with unparalleled capabilities.\nThese breakthroughs are laying the groundwork for a future where quantum computers can help us seize enormous opportunities — revolutionizing scientific discoveries, fortifying national security and strengthening economic competitiveness.\n...\nThis center develops key technologies for creating the first error-corrected local and global quantum networks, enabling nationwide access to quantum computing.",
        "title": "Quantum computing: Expanding what's possible",
        "url": "https://www.nsf.gov/science-matters/quantum-computing-expanding-whats-possible",
        "date": "2026-01-21",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "While quantum computing might seem like technology for the distant future, the breakthroughs from the collaboration between Fermilab’s Superconducting Quantum Materials and Systems (SQMS) Center, the National Institute of Standards and Technology (NIST), and several other government, university, and industrial partners, could reshape industries and daily life in the near future.\n...\nScientists from NIST’s Communications Technology Laboratory (CTL) and the Physical Measurement Laboratory (PML) are leading the SQMS Center’s Nanofabrication Taskforce, a joint effort aimed at enhancing the performance of superconducting quantum bits (qubits) — the building blocks of quantum computers.\n...\nUnder his guidance, the team has pioneered breakthroughs in qubit fabrication techniques, such as encapsulating the surface of qubits made from the chemical element niobium, a superconducting metal, to reduce material losses and extend qubit coherence times significantly.\n...\nThe taskforce is tackling one of the biggest challenges in quantum computing: improving qubit coherence.\nLonger coherence times mean qubits can maintain their quantum states longer, leading to more powerful and reliable quantum computers.\n...\n### Key Technical Breakthroughs\nRecent innovations by the SQMS Nanofabrication Taskforce have led to a systematic improvement in qubit coherence, with the best-performing qubits now reaching coherence times of up to 0.6 milliseconds, a significant leap for superconducting quantum technology.\nThis achievement is driven by optimized qubit designs and enhanced readout resonators, which improve qubit stability and coherence.\nAdditionally, researchers have tackled qubit loss mechanisms by encapsulating niobium surfaces with gold or tantalum to prevent the formation of lossy niobium oxide, a major source of decoherence.\nEfforts are also underway to explore alternative materials for Josephson junctions, addressing losses caused by aluminum oxide tunnel barriers, while recognizing that other material interfaces and sapphire substrates currently limit coherence times to approximately 1 millisecond.\nTo push the boundaries of performance even further, the taskforce is investigating new superconducting materials, while also refining Josephson tunnel junction fabrication techniques.\nIn addition to the advancements in materials, nanofabrication process optimizations, such as reducing processing steps and developing sidewall capping techniques, are enhancing the reliability and scalability of quantum hardware, paving the way for next-generation quantum computing.\n...\nThe breakthroughs from the SQMS Nanofabrication Taskforce bring quantum research closer to the ultimate goal: building scalable, fault-tolerant quantum computers.\nBy tackling the fundamental challenges of qubit fabrication and coherence, NIST scientists from CTL and PML help to ensure the U.S. remains a leader in this transformative field.",
        "title": "Quantum Breakthroughs: NIST & SQMS Lead the Way",
        "url": "https://www.nist.gov/news-events/news/2025/04/quantum-breakthroughs-nist-sqms-lead-way",
        "date": "2025-04-04",
        "last_updated": "2026-03-09"
      },
      {
        "snippet": "IBM delivers the most performant and reliable quantum hardware, backed by industry-leading production processes.\nQuantum devices (<100q)\n60\nSince 2016\nQuantum computers (>100q)\n30+\nSince 2022\nAvailable qubits\n2300+\nCircuits ran\n3.9T+\nAvailability (% uptime)\n97%\nOur qubits are made using state-of-the-art 300mm semiconductor chip fabrication technologies.\nBy putting semi-automated tooling to work in new ways, we are accelerating our development cycles.\nTo date, we have cut the time needed to build each new processor by at least half, while enabling multiple designs to be researched and explored in parallel.\n...\nFrom multi-layer wiring to tunable couplers, we’ve fine-tuned our signal delivery and packaging techniques to ensure qubit control scales with processor complexity.\nWe are also developing a new low-loss wiring layer to enable the distant qubit connections required for our qLDPC error-correcting code.\nWe are pioneering inter-module communication with l-couplers, enabling computation across chips, modules, and systems.\nThese microwave cables extend processing power in multi-QPU systems and soon fault-tolerant architectures.\nBuilding systems that can run billions of gates requires modular components that create a single cryogenic environment.\nFrom componentized fridge design to flex wiring, we continue to drive scalability and affordability.\nWe are also developing cryogenic CMOS control electronics, reducing system complexity and improving reliability.\n...\nThe cryostat demo offers a detailed look inside an IBM quantum computing system.\nOur quantum processors need to be very cold—about a hundredth of a degree above absolute zero.\nThis complex array of components creates the required ultra-cold environment.\nFrom top to bottom:\nA tightly-sealed plate protects the flexible input wiring as it passes into the ultra-high vacuum fridge\nThis device provides initial cooling, down to temperatures of 4 kelvin.\nThat’s -452.47° Fahrenheit, or -269.15° Celsius.\nFlexible printed circuit boards carry microwave signals into and out of this ultra-cold environment in an inexpensive, low-crosstalk manner.\nThese low-noise amplifiers take the weak readout signals from the qubits and make them large enough that they are not swamped by the electronic noise from the room temperature world outside the fridge.\nThese cables send signals to and from qubits, like a coaxial line for a cable television.\nThe superconducting lines are zero-loss, meaning they can transmit information without losing energy.\nElectromagnetic signals like those from your phone create noise in a quantum system.\nThis shield protects our systems from the interference of this kind of radiation.\nIt’s particularly effective at the ultra-low temperatures in which we operate.\nQuantum-limited amplifiers (QLAs) boost the faint readout signals that come from sensitive quantum processors while adding the minimum amount of noise allowed by the laws of quantum mechanics.\nIBM Quantum Heron is a 156-qubit processor designed for performance and the basis of our plan to scale quantum computers.\nHeron contains the qubit and gate technology that forms the foundation of our development roadmap.\nAt 127 qubits, the Eagle processor features breakthrough packaging technologies for enhanced qubit control and scalability.\nWith 133 or 156 fixed-frequency qubits and tunable couplers, the Heron family of processors is our highest-performing yet and the core of our System Two architecture.\nThe next evolution of our chip architecture, Nighthawk features 120 qubits on a square lattice, with four-degree connectivity to scale workload complexity.\nWith 133 or 156 fixed-frequency qubits and tunable couplers, the Heron family of processors is our highest-performing yet and the core of our System Two architecture.\nIBM Quantum System Two is the cornerstone of quantum-centric supercomputing.\nIts flexible design allows multiple QPUs to be linked in a data center environment.\nThese systems combine scalable cryogenic infrastructure and classical runtime servers with modular qubit control electronics to facilitate hybrid architectures.\nIBM Quantum partners are doing real science with quantum.\nOur new reference architecture shows how to bring those capabilities to any HPC research center.",
        "title": "IBM Quantum Computing | Hardware and roadmap",
        "url": "https://www.ibm.com/quantum/hardware",
        "date": null,
        "last_updated": "2026-05-23"
      },
      {
        "snippet": "",
        "title": "10 quantum computing milestones | Network World",
        "url": "https://www.networkworld.com/article/3618098/10-quantum-computing-milestones-of-2024.html",
        "date": "2024-12-16",
        "last_updated": "2026-05-24"
      },
      {
        "snippet": "Quantum computing just crossed a threshold nobody saw coming.\nFrom Amazon’s first superconducting chip Ocelot, to IBM’s modular Quantum System Two, and Microsoft’s Majorana One prototype redefining stability itself—2025 has become the year quantum hardware finally starts looking like real, scalable computing.\nIn this video, you’ll discover nine groundbreaking developments that are reshaping how scientists, engineers, and entire industries think about computation.\nLearn how circuit knitting lets small chips solve massive problems, how Google’s Willow processor achieved unheard-of stability, and how quantum spin echoes are unlocking molecular secrets classical computers can’t touch.\nThese milestones aren’t just academic—they’re the foundation of the next technological revolution.\nCloud giants, research labs, and startups are proving that quantum computing is shifting from laboratory demos to practical tools for chemistry, finance, and materials science.\nThe race isn’t about qubit counts anymore—it’s about reliability, scalability, and who can make the quantum future actually usable.\n...\nBut in 2025, they quietly took a significant\n{ts:46} step that puts them in the same competitive conversation as IBM and Google in an entirely different arena.\n{ts:54} Quantum computing AWS introduced a superconducting quantum chip called Ocelot, marking Amazon's first\n{ts:62} proprietary quantum processor.\nFor years, Amazon's quantum platform called Bracket allowed scientists and\n{ts:69} researchers to run experiments on hardware manufactured by other companies like ion, Reetti, and Xanadu.\nNow they\n{ts:77} have their own processor sitting inside their research labs.\n...\nBut what genuinely matters\n{ts:90} here is that a major cloud computing provider is now building physical quantum hardware instead of just renting\n{ts:96} access to someone else's technology.\n...\nQuantum chips available\n{ts:138} today are genuinely powerful for specific tasks, but they're not huge by the standards needed for solving the\n...\nInstead of waiting patiently for a thousand cubit machines\n{ts:165} to be developed over the next decade, researchers started using something called circuit knitting.\nIt sounds\n...\n{ts:177} intelligently cut it into smaller, manageable pieces, run those pieces simultaneously on multiple separate\n{ts:183} quantum chips, and then let classical computers stitch all the results together mathematically.\nIn 2025, this\n{ts:190} approach stopped being purely theoretical research and turned into real practical tools that scientists can\n{ts:196} actually use.\nPlatforms like KisKit, CIRC, and AWS Bracket now support circuit knitting natively in their\n{ts:202} software.\nEarly demonstrations successfully showed that molecular energy calculations that used to be\n{ts:208} completely too large for a single quantum chip can now run distributed across multiple devices.\nIt's definitely\n{ts:215} slower than running everything on one massive processor would be, but it works reliably.\nMore importantly, it helps\n{ts:222} researchers test real quantum algorithms on actual hardware today rather than waiting potentially years for\n{ts:228} significantly larger processors to arrive from manufacturers.\n...\nIn 2025, Google pushed its 105 cubit Willow processor through extensive longduration\n{ts:258} repeated stress tests to determine if it could maintain stability under demanding conditions.\n...\n{ts:282} The chip successfully held quantum coherence through extended sequences of operations and thousands of experimental\n{ts:289} cycles without collapsing.\nThis represents genuinely important progress because early quantum processors often\n{ts:296} lost accuracy catastrophically when computational tasks became complicated or lengthy.\nWith Willow, researchers\n{ts:303} successfully ran quantum simulations for physics experiments and tested quantum machine learning models without the chip\n{ts:311} falling apart mid-run and losing all data.\n...\nWillow's test results demonstrated that superconducting cubits can handle real\n{ts:336} repeated work, which represents a critical step toward more reliable quantum hardware.\n...\n{ts:356} Quantum system 2 is a full modular setup featuring multiple cryogenic refrigerators, specialized racks for\n{ts:363} quantum chips, fast classical control servers, and networking infrastructure built into one integrated platform.\n...\nIn late 2024 and\n...\n{ts:462} It represents one of the first serious attempts to transform quantum hardware into something that operates like an\n{ts:469} actual computing cluster, not a single experimental device that requires constant babysitting by PhD physicists.\n{ts:477} Noise represents the biggest enemy of quantum hardware performance.\n...\nIBM's Heron processor was engineered\n{ts:490} specifically to solve exactly that challenge.\nIt contains 133 superconducting cubits and the key\n{ts:496} distinguishing feature is something called tunable couplers.\nThese couplers precisely control which cubits\n{ts:502} communicate with each other and when they remain isolated and quiet.\nEarly testing demonstrated Heron can deliver\n{ts:509} roughly three to five times better performance than IBM's previous generation processors because the\n{ts:515} quantum signals are dramatically cleaner.\nLess cross talk directly translates to fewer errors during\n{ts:521} execution of complex algorithms.\nHeron is also specifically designed for modular systems so multiple processors\n...\n{ts:556} Instead of building progressively larger chips following the same superconducting architecture everyone else uses,\n{ts:563} Microsoft is pursuing a fundamentally different approach.\nTheir Majorana 1 chip is based on topological cubits\n{ts:570} which use exotic quantum states that are theoretically more stable than ordinary cubits.\nThe underlying idea is that\n{ts:578} these cubits are naturally protected from certain types of noise because of the mathematical way quantum information\n{ts:584} is stored in the system.\nThe major one device is a small prototype, not a huge processor, but the architecture matters\n{ts:592} enormously for the future.\n...\nMicrosoft's approach aims to dramatically shrink that gap.\nMajorana 1\n{ts:620} will not replace existing quantum platforms overnight, but it demonstrates a viable path towards stable cubits that\n{ts:626} hold their quantum state considerably longer, which remains one of the biggest technical challenges in quantum\n{ts:632} computing.\n...\nIn 2025, researchers demonstrated a\n{ts:646} new technique using quantum manybody nuclear spin echoes functioning as a kind of molecular ruler.\nThe idea is to\n{ts:654} measure the precise geometry of molecules with extremely high accuracy.\nClassical methods including spectroscopy\n{ts:661} and electron microscopy can struggle with certain molecular structures because the signals overlap or the\n{ts:667} sample size is too small.\nQuantum spin echoes can probe interactions inside a molecule in ways classical sensors\n{ts:675} physically cannot.\nThis doesn't mean quantum computers replace chemistry laboratories, but it expands\n{ts:681} dramatically what scientists can measure.\n...\nIt's a quiet breakthrough that doesn't generate mainstream\n{ts:693} headlines, but it shows that quantum technology is not limited to computing tasks.",
        "title": "9 NEW Quantum Computing Breakthroughs That Redefine What’s Possible!",
        "url": "https://www.youtube.com/watch?v=hA8plV8m9Gg",
        "date": "2025-11-15",
        "last_updated": "2025-11-17"
      },
      {
        "snippet": "",
        "title": "Breakthroughs in Quantum Computing - Wevolver",
        "url": "https://www.wevolver.com/article/breakthroughs-in-quantum-computing",
        "date": "2024-08-19",
        "last_updated": "2026-05-25"
      },
      {
        "snippet": "",
        "title": "Top 15 New Quantum Computing Breakthroughs That Will Change Everything",
        "url": "https://www.youtube.com/watch?v=8JRJxsvJdRs",
        "date": "2026-03-16",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "Top quantum breakthroughs of 2025 | Network World",
        "url": "https://www.networkworld.com/article/4088709/top-quantum-breakthroughs-of-2025.html",
        "date": "2025-11-13",
        "last_updated": "2026-05-15"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

## Parameter Reference

### `search_domain_filter`

* **Type**: Array of strings
* **Format**:
  * Domain names without protocol, optionally with a path (e.g., "example.com" or "example.com/blog")
  * Prefix with `-` for denylisting (e.g., "-reddit.com" or "-reddit.com/r/all")
* **Description**: Filters search results to include or exclude content from specified domains
* **Optional**: Yes
* **Maximum**: 20 domains per request
* **Modes**:
  * Allowlist mode: Include only specified domains (no `-` prefix)
  * Denylist mode: Exclude specified domains (use `-` prefix)
* **Example**:
  * Allowlist: `"search_domain_filter": ["nature.com", "science.org", "arxiv.org/abs"]`
  * Denylist: `"search_domain_filter": ["-reddit.com", "-pinterest.com", "-quora.com/topic"]`

## Domain Format Guidelines

**Correct Domain Formats:**

* `"nature.com"` - Root domain (matches nature.com and all subdomains)
* `"blog.example.com"` - Specific subdomain
* `"nature.com/articles"` - Domain + path prefix (matches that section and its subpaths)
* `"arxiv.org"` - Root domain (matches all subdomains)
* `".gov"` - Top-level domain (matches all .gov sites)
* `".edu"` - Top-level domain (matches all .edu sites)
* `".uk"` - Country-code TLD (matches all .uk sites)
* `"wikipedia.org"` - Matches en.wikipedia.org, fr.wikipedia.org, etc.
* `"-reddit.com"` - Exclude entire domain and all subdomains
* `"-pinterest.com"` - Exclude entire domain and all subdomains
* `"-.gov"` - Exclude all .gov domains

**Incorrect Domain Formats:**

* ❌ `"https://nature.com"` - Don't include protocol
* ❌ `"www.nature.com"` - Avoid www prefix (use root domain)

## Best Practices

### Domain Selection Strategy

* **Use Root Domains for Broad Coverage**: Specify root domains (e.g., "wikipedia.org") to match all subdomains automatically, including different language versions and regional sites.
* **Use TLDs for Categorical Filtering**: Target specific organization types with TLD filters like `.gov` for government, `.edu` for education, or `.org` for non-profits.
* **Be Specific When Needed**: Choose specific domains that are directly relevant to your search query to ensure high-quality results.
* **Quality Over Quantity**: Using fewer, highly relevant domains often produces better results than maximizing the 20-domain limit.
* **Consider Domain Authority**: Prioritize authoritative sources in your field for more reliable information.
* **Choose Your Mode**: Use either allowlist mode (include only) OR denylist mode (exclude), but not both in the same request. Denylisting is useful when you want broad search coverage but need to exclude specific low-quality or irrelevant sources.

### Locale and Regional Targeting

While domain filters don't directly filter by user location, you can target specific locales using:

* **Country-code TLDs**: Use filters like `.uk`, `.ca`, `.de`, `.jp` to target country-specific domains
* **Subdomain matching**: Specify regional subdomains when available (e.g., "uk.domain.com")
* **Combined approach**: Mix country TLDs with specific trusted domains for precise regional filtering

<Tip>
  For international research, combine TLD filtering with the `search_language_filter` parameter to refine results by both location and language.
</Tip>

### Domain Selection

* **Use Trusted Sources**: Select a specific set of trusted sources you want to search within (e.g., academic research, official documentation).
* **Leverage TLD Filtering**: When researching topics that span many sites of the same type, use TLD filters to cast a wider net (e.g., `.gov` for policy research).
* **Focus on Quality**: Choose authoritative domains that consistently provide reliable information relevant to your queries.

### Client-Side Validation

Validate domain formats on the client side before sending requests:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_domain(domain):
      """Validate domain format including TLD filters."""
      # TLD filter (e.g., .gov, .edu)
      if domain.startswith('.'):
          tld_pattern = r'^\.[a-zA-Z]{2,}$'
          return bool(re.match(tld_pattern, domain))
      
      # Standard domain validation pattern
      pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
      return bool(re.match(pattern, domain))

  def validate_domain_filter(domains):
      """Validate domain filter array."""
      if len(domains) > 20:
          raise ValueError("Maximum 20 domains allowed")

      for domain in domains:
          if not validate_domain(domain):
              raise ValueError(f"Invalid domain format: {domain}")

      return True

  # Usage examples
  try:
      # Mix of regular domains and TLD filters
      domains = ["nature.com", "science.org", ".gov", ".edu"]
      validate_domain_filter(domains)

      response = client.search.create(
          query="CRISPR gene editing clinical trial outcomes for sickle cell disease",
          search_domain_filter=domains
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript Typescript theme={null}
  function validateDomain(domain: string): boolean {
    // TLD filter (e.g., .gov, .edu)
    if (domain.startsWith('.')) {
      const tldPattern = /^\.[a-zA-Z]{2,}$/;
      return tldPattern.test(domain);
    }
    
    // Standard domain validation pattern
    const pattern = /^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
    return pattern.test(domain);
  }

  function validateDomainFilter(domains: string[]): void {
    if (domains.length > 20) {
      throw new Error("Maximum 20 domains allowed");
    }

    for (const domain of domains) {
      if (!validateDomain(domain)) {
        throw new Error(`Invalid domain format: ${domain}`);
      }
    }
  }

  // Usage examples
  try {
    // Mix of regular domains and TLD filters
    const domains = ["nature.com", "science.org", ".gov", ".edu"];
    validateDomainFilter(domains);

    const response = await client.search.create({
      query: "CRISPR gene editing clinical trial outcomes for sickle cell disease",
      search_domain_filter: domains
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "7bd7e5d8-68c3-433d-b78e-50fea0df5f61",
    "results": [
      {
        "snippet": "Today, the U.S. Food and Drug Administration approved two milestone treatments, Casgevy and Lyfgenia, representing the first cell-based gene therapies for the treatment of sickle cell disease (SCD) in patients 12 years and older.\nAdditionally, one of these therapies, Casgevy, is the first FDA-approved treatment to utilize a type of novel genome editing technology, signaling an innovative advancement in the field of gene therapy.\n...\nCasgevy, a cell-based gene therapy, is approved for the treatment of sickle cell disease in patients 12 years of age and older with recurrent vaso-occlusive crises.\nCasgevy is the first FDA-approved therapy utilizing CRISPR/Cas9, a type of genome editing technology.\nPatients’ hematopoietic (blood) stem cells are modified by genome editing using CRISPR/Cas9 technology.\n...\n**Data Supporting Casgevy**\nThe safety and effectiveness of Casgevy were evaluated in an ongoing single-arm, multi-center trial in adult and adolescent patients with SCD.\nPatients had a history of at least two protocol-defined severe VOCs during each of the two years prior to screening.\nThe primary efficacy outcome was freedom from severe VOC episodes for at least 12 consecutive months during the 24-month follow-up period.\nA total of 44 patients were treated with Casgevy.\nOf the 31 patients with sufficient follow-up time to be evaluable, 29 (93.5%) achieved this outcome.\nAll treated patients achieved successful engraftment with no patients experiencing graft failure or graft rejection.\nThe most common side effects were low levels of platelets and white blood cells, mouth sores, nausea, musculoskeletal pain, abdominal pain, vomiting, febrile neutropenia (fever and low white blood cell count), headache and itching.\n**Data Supporting Lyfgenia**\nThe safety and effectiveness of Lyfgenia is based on the analysis of data from a single-arm, 24-month multicenter study in patients with sickle cell disease and history of VOEs between the ages of 12- and 50- years old.\nEffectiveness was evaluated based on complete resolution of VOEs (VOE-CR) between 6 and 18 months after infusion with Lyfgenia.\nTwenty-eight (88%) of 32 patients achieved VOE-CR during this time period.\nThe most common side effects included stomatitis (mouth sores of the lips, mouth, and throat), low levels of platelets, white blood cells, and red blood cells, and febrile neutropenia (fever and low white blood cell count), consistent with chemotherapy and underlying disease.\nHematologic malignancy (blood cancer) has occurred in patients treated with Lyfgenia.\nA black box warning is included in the label for Lyfgenia with information regarding this risk.\nPatients receiving this product should have lifelong monitoring for these malignancies.\nBoth the Casgevy and Lyfgenia applications received Priority Review, Orphan Drug, Fast Track and Regenerative Medicine Advanced Therapy designations.",
        "title": "FDA Approves First Gene Therapies to Treat Patients with Sickle ...",
        "url": "https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapies-treat-patients-sickle-cell-disease",
        "date": "2023-12-08",
        "last_updated": "2026-05-23"
      },
      {
        "snippet": "",
        "title": "CRISPR Clinical Trials: A 2024 Update - Innovative Genomics Institute",
        "url": "https://innovativegenomics.org/news/crispr-clinical-trials-2024/",
        "date": "2024-03-13",
        "last_updated": "2025-07-16"
      },
      {
        "snippet": "",
        "title": "CRISPR/Cas9 in the treatment of sickle cell disease (SCD) and its ...",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11444630/",
        "date": "2024-08-14",
        "last_updated": "2026-03-26"
      },
      {
        "snippet": "",
        "title": "CRISPR/Cas9 gene editing for curing sickle cell disease - PMC",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8049447/",
        "date": "2021-01-10",
        "last_updated": "2026-03-29"
      },
      {
        "snippet": "",
        "title": "Sickle Cell Gene Therapy Using CRISPR - Synthego",
        "url": "https://www.synthego.com/crispr-sickle-cell-disease/",
        "date": "2025-08-05",
        "last_updated": "2026-05-16"
      },
      {
        "snippet": "# Gene Editing Therapy Shows Success Against Severe Sickle Cell Disease\nNearly all patients have achieved a functional cure\n## Media Contact\n...\nNew results from a clinical trial show promising outcomes for a gene-edited treatment for severe sickle cell disease, a genetic blood disorder with few curative options.\nConducted as part of the multicenter RUBY Trial, researchers published their latest findings in the New England Journal of Medicine.\nRemarkably, 27 out of 28 patients did not have any painful sickle cell crises after treatment, achieving what physicians call a \"functional cure.\"\nIn the trial, patients were treated with an experimental one-time gene editing cell therapy – Renizgamglogene autogedtemcel (reni-cel) – that modifies a patient’s own blood-forming stem cells to correct the mutation responsible for sickle cell disease.\nThe novel therapy increases levels of fetal hemoglobin – which prevents red blood cells from forming into sickle-shaped cells – and improves overall hemoglobin levels, reducing complications from the disease.\n“We have seen that a benefit of this CRISPR/Cas12a gene-editing technology is that there is no rejection, so it's different from traditional bone marrow transplants, which is standard treatment for sickle cell patients currently,” says Rabi Hanna, M.D., lead author and chair of the Pediatric Hematology – Oncology & Blood and Bone Marrow Transplant Division at Cleveland Clinic Children’s.\n“Our aim has been to achieve a functional cure to help prevent any future damage caused by sickle cell disease, and these latest results are compelling.”\n...\nThe results showed that most patients saw key blood cells recover within a month after treatment and by six months, average total hemoglobin levels rose to 13.8 g/dL, up from 9.8 g/dL before treatment – a level closer to what is seen in people without sickle cell disease.\nThe average level of fetal hemoglobin (HbF) was 48.1%, and these levels remained stable over time.",
        "title": "Gene Editing Therapy Shows Success Against Severe ...",
        "url": "https://newsroom.clevelandclinic.org/2026/04/01/gene-editing-therapy-shows-success-against-severe-sickle-cell-disease",
        "date": "2026-04-01",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "Researchers Publish Final Results of Key Clinical Trial for Gene Therapy for Sickle Cell Disease\n...\nIn a landmark study, an international consortium led by researchers at Children’s Hospital of Philadelphia (CHOP) published the final results of a key clinical trial of the gene therapy CASGEVY (exagamglogene autotemcel) for the treatment of sickle cell disease in patients 12 years and older with recurrent vaso-occlusive crises (VOCs).\nThe study found that 96.7% of patients in the study did not have any vaso-occlusive crises (VOCs) – a blockage that results in lack of oxygen and painful episodes – for at least one year, and 100% were able to remain hospitalization-free for the same length of time.\nThe findings, published today in the *New England Journal of Medicine*, provide the complete details of the critical clinical trial that led to the FDA approval of CASGEVY™ for the treatment of sickle cell disease in December 2023.\n...\nResearchers have been studying the use of gene therapy and CRISPR technology to edit portions of DNA in people with inherited or genetic disorders, like sickle cell disease.\nIn the case of sickle cell disease, the CASGEVY process edits DNA within the patient’s own cells and enables the patient to produce a different form of hemoglobin in their red blood cells.\nClinical trials at CHOP and other sites have shown that successful gene editing can prevent cells from developing the distinctive crescent shape apparent in sickle cell disease and have eliminated pain episodes in almost all patients.\nCASGEVY was the first FDA-approved therapy developed with CRISPR technology.\n“In this clinical trial, sickle cell patients who were having significant issues with their disease began to see their problems resolve within months and improve their quality of life significantly,” said senior study author Stephan A. Grupp, MD, PhD, Section Chief of the Cellular Therapy and Transplant Section, Inaugural Director of the Susan S. and Stephen P. Kelly Center for Cancer Immunotherapy, and Medical Director of the Cell and Gene Therapy Laboratory at CHOP.\nGrupp was also one of the principal investigators in the clinical trials that led to the approval of CASGEVY and the leader of the study’s steering committee.\nThe researchers conducted the CLIMB SCD-121 trial, a phase 3, single-arm, open-label study of exa-cel in patients between 12 and 35 years old with sickle cell disease and at least two severe VOCs in each of the two years before screening.\nThe key primary endpoint of the study was a proportion of patients without severe VOCs for at least 12 consecutive months, with a secondary endpoint of patients who were free from inpatient hospitalization for severe VOCs for at least 12 consecutive months.\nA total of 44 patients received exa-cel with a median follow up of 19.3 months.\nIn a total of 30 patients with sufficient follow-up data to be evaluated, 29 (96.7%) were free of VOCs for at least 12 consecutive months.\nThis information is an update for the US Prescribing Information for CASGEVY, which includes an evaluation of 31 patients resulting in a response rate of 93.5%.\nThe safety of treatment was comparable to treatment with hematopoietic and progenitor stem cells, and no malignancies were reported as a result of treatment.\n...\nAdditionally, the results of a clinical trial on the efficacy of exa-cel for the treatment of β-thalassemia were also published today in the *New England Journal of Medicine*.\nThe preliminary results of the trial led to the FDA approval of CASGEVY for transfusion-dependent β-thalassemia in January 2024.\n...\n215-590-3025\n...\n267-426-0762",
        "title": "Researchers Publish Final Results of Key Clinical Trial for Gene ...",
        "url": "https://www.chop.edu/news/researchers-publish-final-results-key-clinical-trial-gene-therapy-sickle-cell-disease",
        "date": "2024-04-24",
        "last_updated": "2026-05-11"
      },
      {
        "snippet": "",
        "title": "Other Gene Editing...",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12599223/",
        "date": "2025-11-06",
        "last_updated": "2026-04-20"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Performance Considerations

* **Result Availability**: Narrowing to specific domains may reduce the number of available results. Be prepared to handle cases where fewer results are returned than requested.
* **Domain Coverage**: Ensure the domains you specify actually contain content relevant to your query. Overly restrictive filters may return zero results.
* **Combination Effects**: Domain filters combined with other restrictive filters (date, language) can significantly reduce result counts.

<Tip>
  For best results, combine domain filtering with other filters like `search_recency_filter` or `search_language_filter` to narrow down your search to highly relevant, timely content from your target sources. Use TLD filters like `.gov` or `.edu` when you need broad coverage across an entire category of authoritative sites.
</Tip>
