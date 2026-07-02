---
title: "People Search"
source: https://docs.perplexity.ai/docs/search/filters/people-search
path: docs/search/filters/people-search
---

<Note>
  The `search_type` parameter switches the Search API between general web search and specialized search modes. Set `search_type="people"` to invoke People Search and retrieve professional information about individuals such as names, job titles, and companies.
</Note>

## Overview

People Search lets you query Perplexity's index for professionals, employees, and public figures. Use it when your application needs to:

* Look up a specific person's professional background
* Find employees at a company by role or title
* Identify professionals in a particular field or location
* Research leadership teams or organizational structures

Pass `search_type="people"` on a standard Search API request to route the query through the People Search backend. All other Search API parameters (e.g., `max_results`, `max_tokens_per_page`) continue to apply.

## Request Example

The example below finds engineering leadership at a specific company.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="Stripe VP of Engineering",
      search_type="people",
      max_results=10
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
      query: "Stripe VP of Engineering",
      search_type: "people",
      max_results: 10
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
      "query": "Stripe VP of Engineering",
      "search_type": "people",
      "max_results": 10
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "719f1f3c-d01b-4430-8ee4-cd9c1b836083",
    "results": [
      {
        "snippet": "We are a brand new team, working quickly to accelerate Stripes engineering productivity by effectively deploying LLM agents and tools to automate large swaths of the engineering workflow.\nWe’re a cross-continent team, spanning North America and Europe, filled with high agency engineers with strong product perspectives.\n...\nWe are looking for a hands-on Manager who can effectively lead and guide a team high agency engineers to move quickly on a rapidly growing tech space.\nThey will help set the product direction in a field with a nearly endless possible solution space.\nFolks passionate about great products, user experience and with a strong opinion about how engineers do good work will excel in this role.\nPrior experience with deploying AI developer tools isn’t necessary, but is interesting.\nYou will:\n- Lead a senior, cross-continent team of engineers to move rapidly to deploy and exploit the latest in AI devtools.\n- Deliver compelling user and product experiences for internal users.\n- Work across the company to redefine how software engineers at Stripe work.\n- Keep up with an incredibly fast paced technology environment.\n- Dig deep into the data on how engineers use AI tools to seek out every bit of benefit, and help Stripe accelerate.\n...\n### Minimum requirements\n- 2+ years managing high performing engineering teams, and at least 5+ years of experience as a software engineer.\n- Proven success in recruiting and building great teams.\n- A repeated history of delivering great, innovative product experiences - either for internal or external users.\n- Effective cross-functional collaboration, with the ability to think rigorously, communicate clearly, and make or coordinate difficult decisions and trade-offs.\n- Thrives with high autonomy and responsibility in an ambiguous environment.\n- Ability to foster a healthy, inclusive, challenging, and supportive work environment.\n### Preferred qualifications\n- Experience Tech leading, mentoring and managing a team that shipped products to engineers.\n- Experience building tools and products, ideally for technical audiences - either as internal or external customers.\n- Deep curiosity and opinionation about the use of AI in software engineering.\n- Strong written and verbal communication skills for various audiences, including leadership, users, and company-wide.\nThis role is available either in an office or a remote location (35+ miles or 56+ km from a Stripe office).\n...\nA remote location is defined as being 35 miles (56 kilometers) or more from one of our offices.\n...\nThe annual US base salary range for this role is $214,600 - $321,800.\nFor sales roles, the range provided is the role’s On Target Earnings (\"OTE\") range, meaning that the range includes both the sales commissions/sales bonuses target and annual base salary for the role.\nThis salary range may be inclusive of several career levels at Stripe and will be narrowed during the interview process based on a number of factors, including the candidate’s experience, qualifications, and location.\nApplicants interested in this role and who are not located in the US may request the annual salary range for their location during the interview process.\nAdditional benefits for this role may include: equity, company bonus or sales commissions/bonuses; 401(k) plan; medical, dental, and vision benefits; and wellness stipends.\nOffice locations\nSeattle, or South San Francisco HQ\nRemote locations\nRemote in United States\nTeam\nInfrastructure & Corporate Tech\nJob type\nFull time",
        "title": "Engineering Manager, Developer Productivity AI",
        "url": "https://stripe.com/jobs/listing/engineering-manager-developer-productivity-ai/7736943",
        "date": null,
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "# Head of Engineering, Identity Graph\n•San Francisco / Remote\n**Job type**\nFull-time\n**Role**\nEngineering, Backend\n**Experience**\n11+ years\n**Visa**\nWill sponsor\n**Skills**\nJava\n...\nWe’re looking for an experienced engineering leader to lead our technical strategy in building a graph of identities and inferences that enriches Stripe’s product portfolio by knowing our users deeply and enhances the user experience that enables users to establish trust, accelerate globalization, and open up new market opportunities quickly with just a few lines of code.\nYou’ll manage and grow a strong team of backend and machine learning developers, build relationships with customers and other teams at Stripe, and work on something trajectory altering for Stripe.\n...\nYou will:\nWork with engineers, product, and design to build new customer-facing APIs and products, while maintaining the quality and improving the experience of existing products\nWork with marketing and developer relations teams to explain our products by preparing demos for user-facing events\nCoordinate with other teams at Stripe, both on the problem domain of how payment systems really work and on our shared infrastructure\nEmpower the engineering team to achieve a high level of technical productivity and quality\nManage an excellent team of engineers, helping to develop their careers with stretch projects and excellent feedback\nRecruit a diverse team of engineers that are amongst the best in the industry, from outreach to closing\nContribute to engineering-wide initiatives as part of the engineering management team\nWe’re looking for someone who has:\nExperience working in large graph-based systems\nDomain expertise in the fraud and/or financial risk space\nAn excitement for collaborating with teammates across engineering, operations, and data science\nThe ability to thrive with a high level of autonomy and responsibility\nExperience managing engineering teams with a strong record of shipping\nStrong recruiting skills, with a track record of hiring new team members who are extremely effective over the long term",
        "title": "Head of Engineering, Identity Graph at Stripe",
        "url": "https://www.ycombinator.com/companies/stripe/jobs/yaLKuLq-head-of-engineering-identity-graph",
        "date": "2021-10-07",
        "last_updated": "2026-05-25"
      },
      {
        "snippet": "# Stripe poaches Google’s Vice President of Engineering\nSilicon Valley-based startup Stripe has reportedly hired Google’s Vice President of Engineering as the head of its own engineering department, with news having first been reported by\n*Axios*.\nWith Stripe looking to continue its expansion, Singleton has been brought in largely due to his experience in both leadership roles and innovative product development.\n...\nIn his current position at Google, Singleton has been playing a leading role within the company’s Android Wear and Google Fit teams, becoming renowned as one of the key figures behind Google’s smartwatch products.\nHe has largely specialised in engineering since he joined Google in May 2006, having initially been appointed as a Software Engineer for the company.\n*Axios* also revealed that Singleton will now relocate to San Francisco for his new role with Stripe, with Engineering talent currently in high demand in the Silicon Valley area.",
        "title": "Stripe poaches Google's Vice President of Engineering",
        "url": "https://businesschief.com/leadership-and-strategy/stripe-poaches-googles-vice-president-engineering-1",
        "date": "2020-05-19",
        "last_updated": "2025-07-03"
      },
      {
        "snippet": "Ryan Liu is an accomplished technology leader with extensive experience in engineering management, having served as Vice President of Engineering at Stripe from January 2017 to February 2024.\nIn this role, Ryan successfully oversaw the engineering organization by driving strategic initiatives, fostering innovation, and ensuring infrastructure scalability.\nPreviously, Ryan held key positions at Stripe, including Head of Engineering and Director of Engineering, focusing on aligning engineering efforts with company objectives and enhancing collaboration across teams.",
        "title": "Ryan Liu - VP Of Engineering at Stripe",
        "url": "https://theorg.com/org/stripe/org-chart/ryan-liu",
        "date": "2025-10-07",
        "last_updated": "2025-12-30"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

## Query Tips

For best results, include identifying details in the query:

| Approach            | Example query                              |
| ------------------- | ------------------------------------------ |
| **Name + company**  | "Find John Smith who works at Google"      |
| **Role + company**  | "Head of Design at Figma"                  |
| **Role + location** | "Marketing directors in San Francisco"     |
| **Role + field**    | "Machine learning researchers at Stanford" |

<Tip>
  For agentic workflows that need the model to autonomously decide when to look up people, use the [`people_search` tool](/docs/agent-api/tools/people-search) with the Agent API instead. To wire People Search into a third-party agent SDK, see [Use as an agent tool](#use-as-an-agent-tool) below.
</Tip>

## Use as an agent tool

People Search can be exposed to a third-party agent SDK as a `people_search` function tool — useful when you want the model to autonomously decide when to look up individuals. The plumbing below mirrors the [`web_search` Agent SDK integrations](/docs/search/agent-sdks/anthropic); wire `people_search` into the same tool-call loop alongside or in place of `web_search`.

### Tool description

Keep the description verbatim — its wording is what produces good, focused queries and prevents the model from picking People Search for general-knowledge questions.

<CodeGroup>
  ```python Python theme={null}
  PEOPLE_SEARCH_TOOL_DESCRIPTION = """\
  Searches LinkedIn for individual profiles and employee data. Returns profile information including names, job titles, companies, and LinkedIn profile URLs. Results are exclusively from LinkedIn. Use this tool ONLY when the user specifically wants LinkedIn profiles, individual employee lookups, or data that only LinkedIn would have (e.g., listing employees at a company by location, finding someone's career history). For general questions about executives, leadership teams, or public figures, prefer search_web instead as it returns richer curated results.

  Best practices:
  - Include the person's name and/or company for targeted results.
  - Add job title or role keywords to narrow results.
  - Use both abbreviations AND full titles for better coverage (e.g., query for both "CTO" and "Chief Technology Officer").
  - Use multiple distinct query variations for broader coverage, varying by role, department, company name, or location.
  - Use up to five queries for complex requests.

  Examples:
    - ["John Smith software engineer Google"]
    - ["CTO Stripe", "Chief Technology Officer Stripe"]
    - ["Perplexity AI engineer SF", "Perplexity product manager", "Perplexity AI designer San Francisco"]
    - ["machine learning researcher Stanford"]"""

  PEOPLE_QUERIES_PARAM_DESCRIPTION = (
      "An array of keyword-based people search queries. Each query should "
      "include names, titles, or companies."
  )
  ```

  ```typescript Typescript theme={null}
  const PEOPLE_SEARCH_TOOL_DESCRIPTION = `Searches LinkedIn for individual profiles and employee data. Returns profile information including names, job titles, companies, and LinkedIn profile URLs. Results are exclusively from LinkedIn. Use this tool ONLY when the user specifically wants LinkedIn profiles, individual employee lookups, or data that only LinkedIn would have (e.g., listing employees at a company by location, finding someone's career history). For general questions about executives, leadership teams, or public figures, prefer search_web instead as it returns richer curated results.

  Best practices:
  - Include the person's name and/or company for targeted results.
  - Add job title or role keywords to narrow results.
  - Use both abbreviations AND full titles for better coverage (e.g., query for both "CTO" and "Chief Technology Officer").
  - Use multiple distinct query variations for broader coverage, varying by role, department, company name, or location.
  - Use up to five queries for complex requests.

  Examples:
    - ["John Smith software engineer Google"]
    - ["CTO Stripe", "Chief Technology Officer Stripe"]
    - ["Perplexity AI engineer SF", "Perplexity product manager", "Perplexity AI designer San Francisco"]
    - ["machine learning researcher Stanford"]`;

  const PEOPLE_QUERIES_PARAM_DESCRIPTION =
    "An array of keyword-based people search queries. Each query should " +
    "include names, titles, or companies.";
  ```
</CodeGroup>

### Tool registration

The tool registration shape varies per SDK. The schema allows up to five queries (vs. three for `web_search`).

<Tabs>
  <Tab title="Anthropic">
    <CodeGroup>
      ```python Python theme={null}
      PEOPLE_SEARCH_TOOL = {
          "name": "people_search",
          "description": PEOPLE_SEARCH_TOOL_DESCRIPTION,
          "input_schema": {
              "type": "object",
              "properties": {
                  "queries": {
                      "type": "array",
                      "description": PEOPLE_QUERIES_PARAM_DESCRIPTION,
                      "items": {"type": "string"},
                      "minItems": 1,
                      "maxItems": 5,
                  },
              },
              "required": ["queries"],
          },
      }
      ```

      ```typescript Typescript theme={null}
      const PEOPLE_SEARCH_TOOL = {
        name: "people_search",
        description: PEOPLE_SEARCH_TOOL_DESCRIPTION,
        input_schema: {
          type: "object" as const,
          properties: {
            queries: {
              type: "array" as const,
              description: PEOPLE_QUERIES_PARAM_DESCRIPTION,
              items: { type: "string" as const },
              minItems: 1,
              maxItems: 5,
            },
          },
          required: ["queries"],
        },
      };
      ```
    </CodeGroup>
  </Tab>

  <Tab title="OpenAI">
    <CodeGroup>
      ```python Python theme={null}
      PEOPLE_SEARCH_TOOL = {
          "type": "function",
          "name": "people_search",
          "description": PEOPLE_SEARCH_TOOL_DESCRIPTION,
          "strict": True,
          "parameters": {
              "type": "object",
              "additionalProperties": False,
              "properties": {
                  "queries": {
                      "type": "array",
                      "description": PEOPLE_QUERIES_PARAM_DESCRIPTION,
                      "items": {"type": "string"},
                  },
              },
              "required": ["queries"],
          },
      }
      ```

      ```typescript Typescript theme={null}
      const PEOPLE_SEARCH_TOOL = {
        type: "function" as const,
        name: "people_search",
        description: PEOPLE_SEARCH_TOOL_DESCRIPTION,
        strict: true,
        parameters: {
          type: "object" as const,
          additionalProperties: false,
          properties: {
            queries: {
              type: "array" as const,
              description: PEOPLE_QUERIES_PARAM_DESCRIPTION,
              items: { type: "string" as const },
            },
          },
          required: ["queries"],
        },
      };
      ```
    </CodeGroup>

    <Warning>
      **Strict mode constraints.** When `strict: true`, the JSON Schema must set `additionalProperties: false` and list every property in `required`. OpenAI rejects `maxItems`/`minItems` in strict mode — enforce the five-query cap through the description and truncate defensively in your handler.
    </Warning>
  </Tab>

  <Tab title="Gemini">
    <CodeGroup>
      ```python Python theme={null}
      from google.genai import types

      PEOPLE_SEARCH_FUNCTION = types.FunctionDeclaration(
          name="people_search",
          description=PEOPLE_SEARCH_TOOL_DESCRIPTION,
          parameters_json_schema={
              "type": "object",
              "properties": {
                  "queries": {
                      "type": "array",
                      "description": PEOPLE_QUERIES_PARAM_DESCRIPTION,
                      "items": {"type": "string"},
                      "minItems": 1,
                      "maxItems": 5,
                  },
              },
              "required": ["queries"],
          },
      )

      PEOPLE_SEARCH_TOOL = types.Tool(function_declarations=[PEOPLE_SEARCH_FUNCTION])
      ```

      ```typescript Typescript theme={null}
      import type { FunctionDeclaration, Tool } from "@google/genai";

      const PEOPLE_SEARCH_FUNCTION: FunctionDeclaration = {
        name: "people_search",
        description: PEOPLE_SEARCH_TOOL_DESCRIPTION,
        parametersJsonSchema: {
          type: "object",
          properties: {
            queries: {
              type: "array",
              description: PEOPLE_QUERIES_PARAM_DESCRIPTION,
              items: { type: "string" },
              minItems: 1,
              maxItems: 5,
            },
          },
          required: ["queries"],
        },
      };

      const PEOPLE_SEARCH_TOOL: Tool = {
        functionDeclarations: [PEOPLE_SEARCH_FUNCTION],
      };
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Handler

The handler is identical across SDKs — call Search API with `search_type="people"`:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  perplexity = Perplexity()

  def run_people_search(queries: list[str]) -> str:
      """Call Perplexity People Search and format the results for the model."""
      response = perplexity.search.create(
          query=queries, search_type="people", max_results=10
      )

      lines = []
      for result in response.results:
          snippet = (result.snippet or "").strip().replace("\n", " ")
          if len(snippet) > 400:
              snippet = snippet[:400] + "…"
          lines.append(f"- {result.title}\n  {result.url}\n  {snippet}")
      return "\n\n".join(lines) if lines else "No results."
  ```

  ```typescript Typescript theme={null}
  import Perplexity from "@perplexity-ai/perplexity_ai";

  const perplexity = new Perplexity();

  async function runPeopleSearch(queries: string[]): Promise<string> {
    const response = await perplexity.search.create({
      query: queries,
      search_type: "people",
      max_results: 10,
    });

    const lines = response.results.map((r) => {
      const snippet = (r.snippet ?? "").trim().replace(/\n/g, " ");
      const trimmed = snippet.length > 400 ? `${snippet.slice(0, 400)}…` : snippet;
      return `- ${r.title}\n  ${r.url}\n  ${trimmed}`;
    });
    return lines.length ? lines.join("\n\n") : "No results.";
  }
  ```
</CodeGroup>

### Tool-call loop

The tool-call loop is identical to the `web_search` pattern in each SDK's guide. Wire `people_search` into the same loop, either alongside `web_search` or on its own, and dispatch on the tool name when handling tool calls.

<CardGroup>
  <Card title="Anthropic SDK" icon="code" href="/docs/search/agent-sdks/anthropic">
    Messages API tool-use loop.
  </Card>

  <Card title="OpenAI SDK" icon="code" href="/docs/search/agent-sdks/openai">
    Responses API tool-call loop.
  </Card>

  <Card title="Gemini SDK" icon="code" href="/docs/search/agent-sdks/gemini">
    `google-genai` SDK function calling.
  </Card>
</CardGroup>
