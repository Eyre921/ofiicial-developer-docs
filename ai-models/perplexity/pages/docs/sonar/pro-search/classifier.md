---
title: "Pro Search Classifier"
source: https://docs.perplexity.ai/docs/sonar/pro-search/classifier
path: docs/sonar/pro-search/classifier
---

Optimize cost and performance with automatic query classification between Pro Search and Fast Search modes

## Overview

The Pro Search Classifier is an intelligent system that automatically determines whether a query requires the advanced multi-step tool usage of Pro Search or can be effectively answered with standard Fast Search. This optimization helps you balance performance needs with cost efficiency.

<Info>
  Instead of manually choosing between `"pro"` and `"fast"` search types, you can use `"auto"` to let the classifier make the optimal decision for each query.
</Info>

## How It Works

When you set `search_type: "auto"`, the classifier analyzes your query across multiple dimensions:

<Steps>
  <Step title="Query Complexity Analysis">
    The classifier evaluates:

    * Number of sub-questions or aspects
    * Requirement for comparative analysis
    * Need for multi-step reasoning
    * Complexity of information synthesis required

    ```json theme={null}
    {
      "web_search_options": {
        "search_type": "auto"  // Let the classifier decide
      }
    }
    ```
  </Step>

  <Step title="Classification Decision">
    Based on the analysis, the classifier routes the query to either:

    * **Pro Search** for complex, multi-faceted queries requiring multi-step tool usage
    * **Fast Search** for straightforward information retrieval

    The decision is transparent in the response metadata.
  </Step>

  <Step title="Execution">
    The selected search mode processes your query:

    * **Pro Search**: Uses built-in tools (web\_search, fetch\_url\_content) automatically
    * **Fast Search**: Performs optimized single-pass search and synthesis

    You receive the same high-quality response format regardless of which mode is used.
  </Step>
</Steps>

## Classification Patterns

### Queries Classified as Pro Search

Complex queries that benefit from multi-step tool usage are automatically routed to Pro Search:

<AccordionGroup>
  <Accordion title="Multi-Part Questions">
    **Example Query:**
    "What are the differences between React, Vue, and Angular in terms of performance, learning curve, and ecosystem? Which one should I choose for a large enterprise application?"

    **Why Pro Search:**

    * Requires information about three different frameworks
    * Needs comparative analysis across multiple dimensions
    * Involves gathering expert opinions and recommendations
    * Benefits from synthesis of diverse sources

    **Tool Usage:**

    * Multiple web searches for each framework
    * URL fetching for benchmark data and official documentation
  </Accordion>

  <Accordion title="Research Synthesis">
    **Example Query:**
    "Summarize the latest peer-reviewed research on the effectiveness of intermittent fasting for weight loss and metabolic health. Include sample sizes and study limitations."

    **Why Pro Search:**

    * Requires finding multiple research papers
    * Needs access to full paper content, not just abstracts
    * Involves extracting specific data (sample sizes, limitations)
    * Requires synthesis across multiple studies

    **Tool Usage:**

    * Web search for recent peer-reviewed papers
    * `fetch_url_content` to read full papers
    * Information extraction and synthesis
  </Accordion>

  <Accordion title="Time-Sensitive Complex Analysis">
    **Example Query:**
    "Analyze the stock market impact of the Federal Reserve's most recent interest rate decision, including effects on different sectors and expert predictions for the next quarter."

    **Why Pro Search:**

    * Requires very recent information
    * Needs multi-source verification
    * Involves sector-by-sector analysis
    * Benefits from expert opinion gathering

    **Tool Usage:**

    * Multiple targeted web searches
    * URL fetching for financial analysis reports
    * Synthesis of diverse expert opinions
  </Accordion>
</AccordionGroup>

### Queries Classified as Fast Search

Straightforward queries that don't require multi-step reasoning are efficiently handled by Fast Search:

<AccordionGroup>
  <Accordion title="Simple Factual Questions">
    **Example Query:**
    "What is the capital of France?"

    **Why Fast Search:**

    * Single, well-established fact
    * No calculation or analysis needed
    * Information readily available in search snippets

    **Processing:**

    * Single web search
    * Direct answer from search results
    * No need for multi-step reasoning
  </Accordion>

  <Accordion title="Straightforward Information Retrieval">
    **Example Query:**
    "What are the main features of the iPhone 15 Pro?"

    **Why Fast Search:**

    * Single product inquiry
    * Information available in product descriptions
    * No comparative analysis required
    * No calculations needed

    **Processing:**

    * Search for product specifications
    * Extract and list features
    * Synthesize from search results
  </Accordion>

  <Accordion title="Single-Topic Queries">
    **Example Query:**
    "Explain what machine learning is."

    **Why Fast Search:**

    * Single concept definition
    * No multi-part analysis required
    * Standard information readily available

    **Processing:**

    * Search for machine learning explanations
    * Synthesize clear definition
    * Provide context from reliable sources
  </Accordion>

  <Accordion title="Basic Definitional Requests">
    **Example Query:**
    "What does API stand for and what is it used for?"

    **Why Fast Search:**

    * Simple definition request
    * No complex analysis needed
    * Information readily available

    **Processing:**

    * Quick search for API definition
    * Explain acronym and basic usage
    * Provide clear, concise answer
  </Accordion>
</AccordionGroup>

## Cost Implications

Understanding the cost difference helps you optimize your API usage:

<div>
  <div>
    <h4>Classified as Pro Search</h4>

    <ul>
      <li>Complex multi-part questions</li>
      <li>Requests requiring calculation or analysis</li>
      <li>Comparative research across sources</li>
      <li>Time-sensitive information needs</li>
    </ul>

    <div>
      <span>Uses Pro Search billing rates</span>
    </div>
  </div>

  <div>
    <h4>Classified as Fast Search</h4>

    <ul>
      <li>Simple factual questions</li>
      <li>Straightforward information retrieval</li>
      <li>Single-topic queries</li>
      <li>Basic definitional requests</li>
    </ul>

    <div>
      <span>Uses standard Sonar Pro billing rates</span>
    </div>
  </div>
</div>

### Pricing Comparison

**Pro Search Rates:**

* Input: \$3 per 1M tokens
* Output: \$15 per 1M tokens
* Request fees: \$14-\$22 per 1,000 requests (based on context size)

**Fast Search Rates:**

* Input: \$3 per 1M tokens
* Output: \$15 per 1M tokens
* Request fees: \$6-\$14 per 1,000 requests (based on context size - same as standard Sonar Pro)

<Tip>
  The automatic classifier helps you save money by using Pro Search only when its advanced capabilities are truly needed, while still ensuring complex queries get full multi-step tool usage.
</Tip>

## Usage Examples

### Using Automatic Classification

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()
  # Let the classifier decide
  response = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": "Compare the energy efficiency (kWh/100mi and MPGe) of the Tesla Model 3, Chevrolet Bolt, and Nissan Leaf using EPA data."
          }
      ],
      stream=True,
      web_search_options={
          "search_type": "auto"  # Automatic classification
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript Typescript SDK theme={null}
  import { Perplexity } from '@perplexity-ai/sdk';

  const client = new Perplexity();

  // Let the classifier decide
  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Compare the energy efficiency (kWh/100mi and MPGe) of the Tesla Model 3, Chevrolet Bolt, and Nissan Leaf using EPA data.'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'auto'  // Automatic classification
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/v1/sonar \
    --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Compare the energy efficiency (kWh/100mi and MPGe) of the Tesla Model 3, Chevrolet Bolt, and Nissan Leaf using EPA data."
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "auto"
      }
    }' --no-buffer
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "cab71ad3-867d-4139-997e-c36ce805351b",
    "results": [
      {
        "snippet": "The following table compares official EPA ratings for fuel economy (in miles per gallon gasoline equivalent, mpg-e or MPGe, for plug-in electric vehicles) for series production all-electric passenger vehicles rated by the EPA for model years 2015, 2016, 2017, and 2023 versus the model year\n2016 vehicles that were rated the most efficient by the EPA with plug-in hybrid drivetrains (Chevrolet Volt – second generation), gasoline-electric hybrid drivetrains (Toyota Prius Eco - fourth generation), and the average new vehicle for that model year, which has a fuel economy of 25 mpg~‑US~ (9.4 L/100 km; 30 mpg~‑imp~).\nEPA rating data are taken from manufacturer testing of their own vehicles using a series of tests specified by federal law.\n...\nReal-world EV efficiency can also be expressed in miles per kilowatt-hour (mi/kWh), which converts EPA MPGe values into direct electrical energy consumption, allowing cross-comparison between electric and gasoline vehicles.\n...\n|Vehicle|Model year|EPA rated fuel economy|EPA rated fuel economy|EPA rated fuel economy|Notes| | |\n...\n|Toyota Prius HEV|2023|57 mpg|57 mpg|56 mpg|(9)| | |\n|Hyundai Ioniq 6 Long Range RWD w/ 18-inch wheels|2023|140 mpg‑e 24.1 kWh/100 mi; 15.0 kWh/100 km|153 mpg‑e 22.0 kWh/100 mi; 13.7 kWh/100 km|127 mpg‑e 26.5 kWh/100 mi; 16.5 kWh/100 km|(1)| | |\n...\n|Tesla Model Y AWD|2023|123 mpg‑e 27.4 kWh/100 mi; 17.0 kWh/100 km|129 mpg‑e 26.1 kWh/100 mi; 16.2 kWh/100 km|116 mpg‑e 29.1 kWh/100 mi; 18.1 kWh/100 km|(1)| | |\n|Tesla Model 3 Standard Range|2020|141 mpg‑e 23.9 kWh/100 mi; 14.9 kWh/100 km|148 mpg‑e 22.8 kWh/100 mi; 14.2 kWh/100 km|132 mpg‑e 25.5 kWh/100 mi; 15.9 kWh/100 km|(1)| | |\n...\n|Tesla Model 3 Long Range AWD|2020|121 mpg‑e 27.9 kWh/100 mi; 17.3 kWh/100 km|124 mpg‑e 27.2 kWh/100 mi; 16.9 kWh/100 km|116 mpg‑e 29.1 kWh/100 mi; 18.1 kWh/100 km|(1)| | |\n|Chevrolet Bolt EV|2017|119 mpg‑e 28.3 kWh/100 mi; 17.6 kWh/100 km|121 mpg‑e 27.9 kWh/100 mi; 17.3 kWh/100 km|110 mpg‑e 30.6 kWh/100 mi; 19.0 kWh/100 km| | | |\n...\n|Nissan Leaf (24 kW-h)|2013/14/15/16|114 mpg‑e 29.6 kWh/100 mi; 18.4 kWh/100 km|126 mpg‑e 26.8 kWh/100 mi; 16.6 kWh/100 km|101 mpg‑e 33.4 kWh/100 mi; 20.7 kWh/100 km|(1) (6)| | |\n...\n|Nissan Leaf (30 kW-h)|2016|112 mpg‑e 30.1 kWh/100 mi; 18.7 kWh/100 km|124 mpg‑e 27.2 kWh/100 mi; 16.9 kWh/100 km|101 mpg‑e 33.4 kWh/100 mi; 20.7 kWh/100 km|(1)| | |",
        "title": "Electric car EPA fuel economy - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Electric_car_EPA_fuel_economy",
        "date": "2015-04-30",
        "last_updated": "2026-05-05"
      },
      {
        "snippet": "Instead of focusing on battery size or total range, we look at **energy consumption (kWh per 100 miles)** and **MPGe**, the EPA’s miles-per-gallon equivalent metric.\n...\n**Methodology**: Recurrent's Most Efficient EVs of 2026 were determined based on combined efficiency in kWh/100miles as reported to the EPA.\n...\n## 3.\nTesla Model 3\n**Efficiency:** 25 kWh/100 miles\n**MPGe:** 134.8\n**Body style:** Compact sedan\n...\n## 5.\nTesla Model Y\n**Efficiency:** 26 kWh/100 miles\n**MPGe:** 129.6\n**Body style:** Compact crossover SUV\n...\n## 6.\nNissan LEAF\n**Efficiency:** 28 kWh/100 miles\n**MPGe:** 120.4\n**Body style:** Compact crossover (redesigned)",
        "title": "2026 Most Efficient EV by Size According to Testing - Recurrent",
        "url": "https://www.recurrentauto.com/research/most-efficient-ev",
        "date": "2026-03-02",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "|EPA MPG MPGe:Miles per Gallon Equivalent 1 gallon of gasoline=33.7 kWh About All-Electric Cars|Electricity Combined MPG:111 MPGe City MPG:123 Highway MPG:99 30 kWh/100 miles|",
        "title": "Find and Compare Cars",
        "url": "https://www.fueleconomy.gov/feg/noframes/48400.shtml",
        "date": "2023-01-01",
        "last_updated": "2024-10-03"
      },
      {
        "snippet": "MPGe is a unit of measure used by the Environmental Protection Agency (EPA) to represent EV fuel economy in a common unit with gas-powered vehicles, where 33.7 kilowatt-hours of electricity are equal to the energy contained in one gallon of gasoline.\nAmong those 17 models, there were a total of 37 unique configurations that achieved 100 MPGe or higher.\nThe Tesla Model 3 in rear-wheel drive configuration achieved the highest rating for MY 2022 with 132 MPGe.\n||\n|--|\n|||\n|Tesla Model 3|132|\n|Lucid Air|131|\n|Tesla Model Y|129|\n|Chevrolet Bolt EV|120|\n|Hyundai Kona Electric|120|\n|Tesla Model S|120|\n|Kia EV6|117|\n|Chevrolet Bolt EUV|115|\n|Hyundai Ioniq 5|114|\n|Kia Niro Electric|112|\n|Nissan Leaf|111|\n|MINI Cooper SE|110|\n|BMW i4 Gran Coupe|109|\n|Polestar 2|107|\n|Volkswagen ID.4|107|\n|Ford Mustang Mach-E|103|\n|Tesla Model X|102|\n...\n**Source: **U.S. Department of Energy and U.S. Environmental Protection Agency’s Fuel Economy Website, Compare Electric Vehicles Side-by-Side.\nData accessed August 24, 2022.",
        "title": "FOTW #1257, September 26, 2022: Seventeen EV Models Achieved ...",
        "url": "https://www.energy.gov/eere/vehicles/articles/fotw-1257-september-26-2022-seventeen-ev-models-achieved-epa-combined-rating",
        "date": "2022-09-26",
        "last_updated": "2025-10-09"
      },
      {
        "snippet": "Nevertheless, the efficiency and range varies a lot from EV to EV.\nTo help you choose which electric car is more suitable for you, I made the table below with EPA efficiency and range figures – for different driving scenarios (city, highway and mixed/combined).\nElectric car range and efficiency (EPA)\n|Electric car\n|City\nrange\n|Combined\nrange\n|Highway\nrange\n|City\nefficiency\n|Combined\nefficiency\n|Highway\nefficiency\n|2019 Tesla Model 3 Long Range (RWD)\n|340 miles\n547 km\n|325 miles\n523 km\n|307 miles\n494 km\n|24,8 kWh/100 miles\n15,4 kWh/100 km\n|25,9 kWh/100 miles\n16,1 kWh/100 km\n|27,4 kWh/100 miles\n17 kWh/100 km\n|2019 Tesla Model 3 Long Range (AWD)\n|320 miles\n515 km\n|310 miles\n499 km\n|297 miles\n478 km\n|28,1 kWh/100 miles\n17,5 kWh/100 km\n|29,1 kWh/100 miles\n18,1 kWh/100 km\n|30,1 kWh/100 miles\n18,7 kWh/100 km\n|2019 Tesla Model 3 Standard Range Plus\n|253 miles\n407 km\n|240 miles\n386 km\n|224 miles\n361 km\n|24,1 kWh/100 miles\n15 kWh/100 km\n|25,3 kWh/100 miles\n15,7 kWh/100 km\n|27,2 kWh/100 miles\n16,9 kWh/100 km\n|2019 Tesla Model S Long Range\n|382 miles\n614 km\n|370 miles\n595 km\n|356 miles\n573 km\n|29,3 kWh/100 miles\n18,2 kWh/100 km\n|30,4 kWh/100 miles\n18,9 kWh/100 km\n|31,5 kWh/100 miles\n19,6 kWh/100 km\n|2019 Tesla Model X Long Range\n...\n22,5 kWh/100 km\n...\n|2017-2019 Chevrolet Bolt EV\n|255 miles\n411 km\n|238 miles\n383 km\n|217 miles\n350 km\n|26,3 kWh/100 miles\n16,4 kWh/100 km\n|28,3 kWh/100 miles\n17,6 kWh/100 km\n|30,6 kWh/100 miles\n19 kWh/100 km\n|2020 Chevrolet Bolt EV\n|279 miles\n449 km\n|259 miles\n417 km\n|237 miles\n381 km\n|26,5 kWh/100 miles\n16,5 kWh/100 km\n|28,6 kWh/100 miles\n17,7 kWh/100 km\n|31,2 kWh/100 miles\n19,4 kWh/100 km",
        "title": "Electric car range and efficiency (EPA) - 🔋PushEVs",
        "url": "https://pushevs.com/electric-car-range-efficiency-epa/",
        "date": null,
        "last_updated": "2024-02-21"
      },
      {
        "snippet": "An efficient EV is simply a car that uses fewer kilowatt-hours of electricity to go the same distance.\n...\n53–140 MPGe\nEPA spread\nModel‑year 2024 EVs range from about 53 to 140 miles‑per‑gallon‑equivalent, nearly a 3x difference in efficiency.\n1.5–4.2 mi/kWh\nEnergy use\nOn the same test cycle, some EVs travel less than 1.5 miles per kWh while the best creep above 4 miles per kWh.\n...\nMPGe, or **miles per gallon equivalent**, is the EPA’s attempt to put EVs in gas‑car language.\nOne “gallon” of gasoline is treated as 33.7 kWh of energy.\nIf an EV uses 25 kWh to travel 100 miles, the math works out to roughly 135 MPGe.\n...\nElectricity is billed in **kilowatt‑hours** (kWh).\nSo the most honest unit is simply: how many kWh do you burn to go 100 miles?\n- **kWh/100 mi**: lower is better (like L/100 km)\n- **mi/kWh**: higher is better (like MPG)\nExample: a car that uses 25 kWh/100 mi delivers 4.0 mi/kWh.\nAt $0.15/kWh, those 100 miles cost about $3.75.\n...\nTake the EPA’s kWh/100‑mile number, divide by 100, and multiply by your home rate.\n...\nThat’s why EPA ratings show 2024 EVs spanning roughly 53–140 MPGe while gasoline cars live between 9–57 MPG for the same model year.\n...\nRecent EPA data and independent testing put a handful of EVs at the sharp end of the efficiency spear, especially in sedan form.\n### Sample of highly efficient EVs on sale (2024–2025)\nRepresentative trims; always confirm the exact configuration’s window sticker, as wheels, motors, and options change the numbers.\n|Model & year|Type|Energy use (kWh/100 mi)*|Approx. mi/kWh|EPA combined MPGe*|Notable trait|\n|--|--|--|--|--|--|\n|Lucid Air Pure (2025 RWD)|Sedan|≈23–24|≈4.2–4.3|High 130s–140s|Luxury sedan that somehow drinks like a subcompact.|\n|Hyundai Ioniq 6 SE (2024–2025 RWD)|Sedan|≈24–25|≈4.0–4.2|Around 140|Super‑slippery aero and efficient 800‑V platform.|\n|Tesla Model 3 Long Range RWD (2025)|Sedan|≈25|≈4.0|Low‑to‑mid 130s|The efficiency benchmark among mass‑market sedans.|\n|Tesla Model Y Long Range RWD (2025)|SUV|≈27–28|≈3.6–3.7|Mid‑120s|Roomier crossover form factor, small aero penalty.|\n|Lexus RZ 300e (2024–2025)|SUV|≈27|≈3.7|Mid‑120s|Luxury compact SUV that surprised everyone with its frugality.|\n|Kia EV6 / Hyundai Kona Electric / Kia Niro EV (2024–2025 RWD)|Crossovers|≈28–29|≈3.4–3.6|High teens/low 120s|The efficient heartland of the EV market.|\n|GMC Hummer EV Pickup/SUV|Truck/SUV|≈70+|≈1.4–1.5|Under 50|Off‑the‑charts consumption; think of it as a rolling coal plant with a conscience.|\n...\n### Sedans & hatchbacks\n- **Typical energy use:** ~24–30 kWh/100 mi\n- **Examples:** Hyundai Ioniq 6, Tesla Model 3, Lucid Air, Chevy Bolt (used)\n...\n#### 1.\nStart with kWh/100 mi, not just range\nRange is a product of pack size; kWh/100 mi is the diet.\n...\n#### 2.\nNormalize for body style and mission\nCompare sedans to sedans, crossovers to crossovers, trucks to trucks.\n...\nWhen you compare electric cars, focus less on the billboard range number and more on **kWh per 100 miles, body style, and real battery health**.\n- Use kWh/100 miles (or mi/kWh) as your primary yardstick; MPGe is just the translation into gas‑car language.",
        "title": "Electric Car Efficiency Comparison: 2025 Buyer's Guide - Recharged",
        "url": "https://recharged.com/articles/electric-car-efficiency-comparison-guide",
        "date": "2025-11-17",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "With an EPA-rated efficiency of 111 MPGe, it’s middle-of-the-road in efficiency, far below the Tesla but way above the 2021 Ford Mustang Mach-E GT’s 84 MPGe.\n...\nRecent figures from the U.S. Environmental Protection Agency (EPA) show that the 2021 Tesla Model 3 Standard Range Plus RWD stands at the top of the efficiency range, boasting a combined 142 MPGe—the electrical equivalent of a gallon of fuel.\n...\nEV testing and analysis firm Recurrent crunched the numbers on a set of 99 cars—half Tesla Model 3s and half Nissan Leafs—and their 500,000 data points of efficiency metrics were logged between November 2021 and March 2022.\nUsing an EPA figure-based mile per kWh (mi/kWh) measurement as opposed to MPGe, the Tesla range was calculated from 3.33 to 4.17 mi/kWh, and the Nissan Leaf was 2.94 to 3.45 mi/kWh.\nTherefore, even bargain standard Model 3s will achieve greater road efficiency than the best Leaf.\nHowever, the EPA ratings weren’t what was measured when real-world driving conditions were considered.\nOver the four-month timeframe, Recurrent revealed the median observed efficiency for each vehicle as the Tesla Model 3 having 3.39 mi/kWh and the Nissan Leaf having 3.71 mi/kWh.",
        "title": "Is the Nissan Leaf More Efficient Than the Tesla Model 3? Here's What 1 Study Found",
        "url": "https://www.motorbiscuit.com/nissan-leaf-more-efficient-tesla-model-3-what-study-found/",
        "date": "2022-08-11",
        "last_updated": "2025-06-25"
      },
      {
        "snippet": "Compare USA EV efficiency by kWh/100 mi and MPGe, with EPA and charging metrics across all models and trims.\nUpdated monthly (2026).",
        "title": "Most Efficient EVs in the USA (kWh/100 mi) - BEV Database",
        "url": "https://bev-database.com/cars-list-usa/most-efficient-electric-cars",
        "date": "2026-02-28",
        "last_updated": "2026-02-28"
      },
      {
        "snippet": ",\nModel Year 2022 EVs Achieving EPA Combined Rating of 100 MPGe or more,\nMake and Model,Highest MPGe For Base Model\nTesla Model 3,132\nLucid Air,131\nTesla Model Y,129\nChevrolet Bolt EV,120\nHyundai Kona Electric,120\nTesla Model S,120\nKia EV6,117\nChevrolet Bolt EUV,115\nHyundai Ioniq 5,114\nKia Niro Electric,112\nNissan Leaf,111\nMINI Cooper SE,110\nBMW i4 Gran Coupe,109\nPolestar 2,107\nVolkswagen ID.4,107\nFord Mustang Mach-E,103\nTesla Model X,102\n,\n...\nEVs include only all-electric vehicles.,\n...\nOnly the base model names are shown and only the highest MPGe values are shown for each model name.\nSome models listed have configurations that fall below 100 MPGe.,\n...\n,\n\"Source: U.S. Department of Energy and U.S. Environmental Protection Agency’s Fuel Economy Website, Compare Electric Vehicles Side-by-Side.\nData accessed August 24, 2022.\",\n,\n,\nhttps://www.fueleconomy.gov/feg/evSelect.jsp,",
        "title": "FOTW_1257_web.xlsx",
        "url": "https://www.energy.gov/sites/default/files/2022-09/FOTW_1257_web.xlsx",
        "date": null,
        "last_updated": "2025-03-28"
      },
      {
        "snippet": ",\nModel Year 2022 EVs Achieving EPA Combined Rating of 100 MPGe or more,\nMake and Model,Highest MPGe For Base Model\nTesla Model 3,132\nLucid Air,131\nTesla Model Y,129\nChevrolet Bolt EV,120\nHyundai Kona Electric,120\nTesla Model S,120\nKia EV6,117\nChevrolet Bolt EUV,115\nHyundai Ioniq 5,114\nKia Niro Electric,112\nNissan Leaf,111\nMINI Cooper SE,110\nBMW i4 Gran Coupe,109\nPolestar 2,107\nVolkswagen ID.4,107\nFord Mustang Mach-E,103\nTesla Model X,102\n,\n...\nEVs include only all-electric vehicles.,\n...\nOnly the base model names are shown and only the highest MPGe values are shown for each model name.\nSome models listed have configurations that fall below 100 MPGe.,\n...\n,\n\"Source: U.S. Department of Energy and U.S. Environmental Protection Agency’s Fuel Economy Website, Compare Electric Vehicles Side-by-Side.\nData accessed August 24, 2022.\",\n,\n,\nhttps://www.fueleconomy.gov/feg/evSelect.jsp,",
        "title": "[XLS] FOTW #1257 - Energy.gov",
        "url": "https://www.energy.gov/documents/fotw1257webxlsx",
        "date": null,
        "last_updated": "2026-03-05"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Manual Override

You can still manually specify the search type when you know what you need:

<Tabs>
  <Tab title="Force Pro Search">
    Use when you know you need multi-step tool usage:

    ```python theme={null}
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Your complex query"}],
        stream=True,
        web_search_options={
            "search_type": "pro"  # Force Pro Search
        }
    )
    ```

    **Use cases for manual Pro:**

    * You know the query needs multi-step reasoning
    * Previous auto-classification was Fast but you need deeper analysis
    * Critical queries where you want maximum capability
  </Tab>

  <Tab title="Force Fast Search">
    Use when you want to optimize for speed and cost:

    ```python theme={null}
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Your simple query"}],
        stream=True,
        web_search_options={
            "search_type": "fast"  # Force Fast Search (or omit - fast is default)
        }
    )
    ```

    **Use cases for manual Fast:**

    * Simple queries where Pro Search would be overkill
    * Cost-sensitive applications
    * When response speed is critical
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Default to automatic classification">
    For most applications, use `search_type: "auto"` and let the classifier optimize:

    ```python theme={null}
    web_search_options={"search_type": "auto"}
    ```

    This ensures the right tool for each query while optimizing costs.
  </Step>

  <Step title="Monitor classification patterns">
    Track which queries get classified as Pro vs Fast to understand your usage patterns:

    * Review queries that consistently use Pro Search
    * Identify opportunities to rephrase queries for Fast Search when appropriate
    * Understand which user questions require advanced capabilities

    This helps optimize your application's query design.
  </Step>

  <Step title="Use manual override strategically">
    Override the classifier only when:

    * You have specific performance requirements
    * Testing and comparing Pro vs Fast results
    * Building features with known complexity levels

    **Example:**

    ```python theme={null}
    # Known complex analysis - force Pro
    if query_requires_calculations(user_query):
        search_type = "pro"
    else:
        search_type = "auto"
    ```
  </Step>

  <Step title="Design queries effectively">
    Structure queries to help the classifier make optimal decisions:

    **Less optimal:**
    "Tell me about electric cars"

    **Better:**
    "What is the average range of electric vehicles?" (Fast Search appropriate)

    **Or:**
    "Compare the total cost of ownership over 5 years for Tesla Model 3, Chevrolet Bolt, and Nissan Leaf, including depreciation, electricity costs, and maintenance" (Pro Search appropriate)

    Clear, specific queries enable better classification.
  </Step>
</Steps>

## Classification Transparency

You can verify the classification decision in the response metadata:

```json theme={null}
{
  "id": "12345",
  "model": "sonar-pro",
  "search_metadata": {
    "search_type_used": "pro",  // or "fast"
    "classification_reason": "Multi-part comparative analysis with calculations"
  },
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 150,
    "total_tokens": 175
  }
}
```

<Info>
  This transparency helps you understand why queries were classified a certain way and optimize future queries.
</Info>

## When to Use Each Mode

<CardGroup>
  <Card title="Auto (Recommended)" icon="wand">
    **Best for:** Most applications

    Let the classifier optimize for you. Balances cost and capability automatically based on query complexity.
  </Card>

  <Card title="Manual Pro" icon="brain">
    **Best for:** Known complex tasks

    Use when you're certain multi-step tool usage is needed: calculations, multi-source synthesis, deep analysis.
  </Card>

  <Card title="Manual Fast" icon="bolt">
    **Best for:** Simple retrieval

    Use for straightforward facts, definitions, or when optimizing for speed and cost with simple queries.
  </Card>
</CardGroup>

## Common Questions

<AccordionGroup>
  <Accordion title="How accurate is the classifier?">
    The classifier is highly accurate, trained on thousands of query patterns. It errs on the side of using Pro Search when there's any ambiguity, ensuring you don't lose capability.

    However, if you notice consistent mis-classifications:

    * Rephrase queries to be more specific
    * Use manual override for those query types
    * Consider your use case's specific needs
  </Accordion>

  <Accordion title="Can I see which mode was used?">
    Yes, the response includes metadata showing:

    * Which search type was used
    * Why the classification was made (when using auto)
    * Cost breakdown by search type

    This helps you understand and optimize your usage patterns.
  </Accordion>

  <Accordion title="Does automatic classification add latency?">
    No. Classification happens in milliseconds before query processing begins and does not meaningfully impact response time. The classifier is optimized for real-time decision making.
  </Accordion>

  <Accordion title="What if I disagree with the classification?">
    You can always use manual override:

    ```python theme={null}
    web_search_options={"search_type": "pro"}  # Force your preference
    ```

    If you consistently disagree with classifications, consider:

    * Making queries more specific
    * Using manual override for those query types
    * Reviewing whether your use case needs consistent Pro or Fast mode
  </Accordion>
</AccordionGroup>

## Related Resources

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/docs/sonar/pro-search/quickstart">
    Get started with Pro Search basics
  </Card>

  <Card title="Built-in Tool Capabilities" icon="tool" href="/docs/sonar/pro-search/tools">
    Learn about Pro Search's built-in tools and capabilities
  </Card>

  <Card title="Pricing Guide" icon="currency-dollar" href="/docs/getting-started/pricing">
    Understand pricing for Pro and Fast Search
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/sonar-post">
    Complete API documentation
  </Card>
</CardGroup>
