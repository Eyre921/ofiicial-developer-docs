---
title: "Run hybrid search on separate indexes"
source: https://docs.pinecone.io/guides/search/hybrid-search/separate-indexes
path: guides/search/hybrid-search/separate-indexes
---

Store dense and sparse vectors in two Pinecone indexes linked by ID, query each, and merge the results client-side with reciprocal rank fusion.

Store dense and sparse vectors in two separate Pinecone indexes linked by a shared record ID, query each index, and merge the results client-side (for example, with [reciprocal rank fusion](/guides/search/reciprocal-rank-fusion)). This is the Vectors API separate-index hybrid pattern. It is more flexible than a single index (it supports sparse-only queries, integrated embedding, and per-index reranking) but requires managing two indexes.

## Set up and search

To perform hybrid search with separate indexes, follow these steps:

<Steps>
  <Step title="Create the indexes">
    [Create one index for dense vectors](/guides/index-data/create-an-index#create-an-index-for-dense-vectors) and [another for sparse vectors](/guides/index-data/create-an-index#create-an-index-for-sparse-vectors), either with integrated embedding or for vectors created with external models.

    For example, the following code creates indexes with integrated embedding models.

    ```python Python theme={null}
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    dense_index_name = "dense-for-hybrid-py"
    sparse_index_name = "sparse-for-hybrid-py"

    if not pc.has_index(dense_index_name):
        pc.create_index_for_model(
            name=dense_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "chunk_text"}
            }
        )

    if not pc.has_index(sparse_index_name):
        pc.create_index_for_model(
            name=sparse_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"pinecone-sparse-english-v0",
                "field_map":{"text": "chunk_text"}
            }
        )
    ```
  </Step>

  <Step title="Upsert dense and sparse vectors">
    [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors) and [upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors) into their respective indexes.

    Make sure to establish a linkage between the dense and sparse vectors so you can merge and deduplicate search results later. For example, the following uses `_id` as the linkage, but you can use any other custom field as well. Because the indexes are integrated with embedding models, you provide the source texts and Pinecone converts them to vectors automatically.

    ```python Python [expandable] theme={null}
    # Define the records
    records = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python theme={null}
    # Target both indexes
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    dense_index = pc.Index(host="INDEX_HOST")
    sparse_index = pc.Index(host="INDEX_HOST")

    # Upsert the records
    # The `chunk_text` fields are converted to dense and sparse vectors
    dense_index.upsert_records("example-namespace", records)
    sparse_index.upsert_records("example-namespace", records)
    ```
  </Step>

  <Step title="Search by dense vectors">
    Perform a [semantic search](/guides/search/semantic-search) against the index that stores dense vectors.

    For example, the following code searches that index for 40 records most semantically related to the query "Q3 2024 us economic data". Because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a dense vector automatically.

    ```python Python theme={null}
    query = "Q3 2024 us economic data"

    dense_results = dense_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(dense_results)
    ```

    ```python Response [expandable] theme={null}
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 0.8629686832427979,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec36',
                          '_score': 0.8573639988899231,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec6',
                          '_score': 0.8535352945327759,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 0.8336166739463806,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec48',
                          '_score': 0.8328524827957153,
                          'fields': {'chunk_text': 'Wage growth outpaced inflation '
                                                   'for the first time in years, '
                                                   'signaling improved purchasing '
                                                   'power in 2024.'}},
                         {'_id': 'vec55',
                          '_score': 0.8322604298591614,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec45',
                          '_score': 0.8309446573257446,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec72',
                          '_score': 0.8275909423828125,
                          'fields': {'chunk_text': 'In early 2024, global GDP '
                                                   'growth slowed, driven by '
                                                   'weaker exports in Asia and '
                                                   'Europe.'}},
                         {'_id': 'vec29',
                          '_score': 0.8270887136459351,
                          'fields': {'chunk_text': 'Growth vs. value investing '
                                                   'strategies in 2024.'}},
                         {'_id': 'vec46',
                          '_score': 0.8263787627220154,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec79',
                          '_score': 0.8258304595947266,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec87',
                          '_score': 0.8257324695587158,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec40',
                          '_score': 0.8253997564315796,
                          'fields': {'chunk_text': 'Labor market trends show a '
                                                   'declining participation rate '
                                                   'despite record low '
                                                   'unemployment in 2024.'}},
                         {'_id': 'vec37',
                          '_score': 0.8235862255096436,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec58',
                          '_score': 0.8233317136764526,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec47',
                          '_score': 0.8231339454650879,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec41',
                          '_score': 0.8187897801399231,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec56',
                          '_score': 0.8155254125595093,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}},
                         {'_id': 'vec63',
                          '_score': 0.8136948347091675,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec52',
                          '_score': 0.8129132390022278,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec23',
                          '_score': 0.8126378655433655,
                          'fields': {'chunk_text': 'Top SPAC mergers in the '
                                                   'technology sector for 2024.'}},
                         {'_id': 'vec62',
                          '_score': 0.8116977214813232,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec64',
                          '_score': 0.8109902739524841,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec54',
                          '_score': 0.8092231154441833,
                          'fields': {'chunk_text': 'The global tourism sector '
                                                   'showed signs of recovery in '
                                                   'late 2024 after years of '
                                                   'pandemic-related setbacks.'}},
                         {'_id': 'vec96',
                          '_score': 0.8075559735298157,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec49',
                          '_score': 0.8062589764595032,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec7',
                          '_score': 0.8034461140632629,
                          'fields': {'chunk_text': 'The CPI index rose by 6% in '
                                                   'July 2024, raising concerns '
                                                   'about purchasing power.'}},
                         {'_id': 'vec84',
                          '_score': 0.8027160167694092,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec13',
                          '_score': 0.8010239601135254,
                          'fields': {'chunk_text': 'Credit card APRs reached an '
                                                   'all-time high of 22.8% in '
                                                   '2024.'}},
                         {'_id': 'vec53',
                          '_score': 0.8007135391235352,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec60',
                          '_score': 0.7980866432189941,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec91',
                          '_score': 0.7980680465698242,
                          'fields': {'chunk_text': 'The impact of ESG investing on '
                                                   'corporate strategies has been '
                                                   'a major focus in 2024.'}},
                         {'_id': 'vec68',
                          '_score': 0.797269880771637,
                          'fields': {'chunk_text': 'Cybersecurity spending reached '
                                                   'new highs in 2024, reflecting '
                                                   'the growing threat of digital '
                                                   'attacks on infrastructure.'}},
                         {'_id': 'vec59',
                          '_score': 0.795337438583374,
                          'fields': {'chunk_text': 'The adoption of digital '
                                                   'currencies by central banks '
                                                   'increased in 2024, reshaping '
                                                   'monetary policy frameworks.'}},
                         {'_id': 'vec39',
                          '_score': 0.793889045715332,
                          'fields': {'chunk_text': 'The rise in energy prices '
                                                   'significantly impacted '
                                                   'inflation trends during the '
                                                   'first half of 2024.'}},
                         {'_id': 'vec66',
                          '_score': 0.7919396162033081,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec57',
                          '_score': 0.7917722463607788,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec75',
                          '_score': 0.7907494306564331,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec51',
                          '_score': 0.790622889995575,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec89',
                          '_score': 0.7899052500724792,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}}]},
     'usage': {'embed_total_tokens': 12, 'read_units': 1}}
    ```
  </Step>

  <Step title="Search by sparse vectors">
    Perform a [sparse-vector search](/guides/search/lexical-search) against the index that stores sparse vectors.

    For example, the following code searches that index for 40 records that most exactly match the words in the query. Again, because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a sparse vector automatically.

    ```python Python theme={null}
    sparse_results = sparse_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(sparse_results)
    ```

    ```python Response [expandable] theme={null}
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 7.0625,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec46',
                          '_score': 7.041015625,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec36',
                          '_score': 6.96875,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 6.9609375,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec49',
                          '_score': 6.65625,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec63',
                          '_score': 6.4765625,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec92',
                          '_score': 5.72265625,
                          'fields': {'chunk_text': 'Income inequality widened in '
                                                   '2024 despite strong economic '
                                                   'growth in developed nations.'}},
                         {'_id': 'vec52',
                          '_score': 5.599609375,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec89',
                          '_score': 4.0078125,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}},
                         {'_id': 'vec62',
                          '_score': 3.99609375,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec57',
                          '_score': 3.93359375,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec69',
                          '_score': 3.8984375,
                          'fields': {'chunk_text': 'The agricultural sector faced '
                                                   'challenges in 2024 due to '
                                                   'extreme weather and rising '
                                                   'input costs.'}},
                         {'_id': 'vec37',
                          '_score': 3.89453125,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec60',
                          '_score': 3.822265625,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec51',
                          '_score': 3.783203125,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec55',
                          '_score': 3.765625,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec70',
                          '_score': 3.76171875,
                          'fields': {'chunk_text': 'Consumer spending patterns '
                                                   'shifted in 2024, with a '
                                                   'greater focus on experiences '
                                                   'over goods.'}},
                         {'_id': 'vec90',
                          '_score': 3.70703125,
                          'fields': {'chunk_text': 'The surge in e-commerce in '
                                                   '2024 was facilitated by '
                                                   'advancements in logistics '
                                                   'technology.'}},
                         {'_id': 'vec87',
                          '_score': 3.69140625,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec78',
                          '_score': 3.673828125,
                          'fields': {'chunk_text': 'Consumer sentiment surveys in '
                                                   '2024 reflected optimism '
                                                   'despite high interest rates.'}},
                         {'_id': 'vec82',
                          '_score': 3.66015625,
                          'fields': {'chunk_text': 'Renewable energy subsidies in '
                                                   '2024 reduced the global '
                                                   'reliance on fossil fuels.'}},
                         {'_id': 'vec53',
                          '_score': 3.642578125,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec94',
                          '_score': 3.625,
                          'fields': {'chunk_text': 'Cyberattacks targeting '
                                                   'financial institutions in 2024 '
                                                   'led to record cybersecurity '
                                                   'spending.'}},
                         {'_id': 'vec45',
                          '_score': 3.607421875,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec47',
                          '_score': 3.576171875,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec84',
                          '_score': 3.5703125,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec41',
                          '_score': 3.5546875,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec65',
                          '_score': 3.537109375,
                          'fields': {'chunk_text': 'The global shipping industry '
                                                   'experienced declining freight '
                                                   'rates in 2024 due to '
                                                   'overcapacity and reduced '
                                                   'demand.'}},
                         {'_id': 'vec96',
                          '_score': 3.53125,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec86',
                          '_score': 3.52734375,
                          'fields': {'chunk_text': 'Digital transformation '
                                                   'initiatives in 2024 drove '
                                                   'productivity gains in the '
                                                   'services sector.'}},
                         {'_id': 'vec95',
                          '_score': 3.5234375,
                          'fields': {'chunk_text': 'Automation in agriculture in '
                                                   '2024 increased yields but '
                                                   'displaced rural workers.'}},
                         {'_id': 'vec64',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec79',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec66',
                          '_score': 3.48046875,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec6',
                          '_score': 3.4765625,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec58',
                          '_score': 3.39453125,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec80',
                          '_score': 3.390625,
                          'fields': {'chunk_text': 'Technological innovation in '
                                                   'the fintech sector disrupted '
                                                   'traditional banking in 2024.'}},
                         {'_id': 'vec75',
                          '_score': 3.37109375,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec67',
                          '_score': 3.357421875,
                          'fields': {'chunk_text': 'Renewable energy projects '
                                                   'accounted for a record share '
                                                   'of global infrastructure '
                                                   'investment in 2024.'}},
                         {'_id': 'vec56',
                          '_score': 3.341796875,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}}]},
     'usage': {'embed_total_tokens': 9, 'read_units': 1}}
    ```
  </Step>

  <Step title="Merge and deduplicate the results">
    Merge the 40 dense and 40 sparse results and deduplicate them based on the field you used to link sparse and dense vectors.

    For example, the following code merges and deduplicates the results based on the `_id` field, resulting in 52 unique results.

    ```python Python theme={null}
    def merge_chunks(h1, h2):
        """Get the unique hits from two search results and return them as single array of {'_id', 'chunk_text'} dicts, printing each dict on a new line."""
        # Deduplicate by _id
        deduped_hits = {hit['_id']: hit for hit in h1['result']['hits'] + h2['result']['hits']}.values()
        # Sort by _score descending
        sorted_hits = sorted(deduped_hits, key=lambda x: x['_score'], reverse=True)
        # Transform to format for reranking
        result = [{'_id': hit['_id'], 'chunk_text': hit['fields']['chunk_text']} for hit in sorted_hits]
        return result

    merged_results = merge_chunks(sparse_results, dense_results)

    print('[\n   ' + ',\n   '.join(str(obj) for obj in merged_results) + '\n]')
    ```

    ```console Response [expandable] theme={null}
    [
       {'_id': 'vec92', 'chunk_text': 'Income inequality widened in 2024 despite strong economic growth in developed nations.'},
       {'_id': 'vec69', 'chunk_text': 'The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs.'},
       {'_id': 'vec70', 'chunk_text': 'Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods.'},
       {'_id': 'vec90', 'chunk_text': 'The surge in e-commerce in 2024 was facilitated by advancements in logistics technology.'},
       {'_id': 'vec78', 'chunk_text': 'Consumer sentiment surveys in 2024 reflected optimism despite high interest rates.'},
       {'_id': 'vec82', 'chunk_text': 'Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels.'},
       {'_id': 'vec94', 'chunk_text': 'Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending.'},
       {'_id': 'vec65', 'chunk_text': 'The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand.'},
       {'_id': 'vec86', 'chunk_text': 'Digital transformation initiatives in 2024 drove productivity gains in the services sector.'},
       {'_id': 'vec95', 'chunk_text': 'Automation in agriculture in 2024 increased yields but displaced rural workers.'},
       {'_id': 'vec80', 'chunk_text': 'Technological innovation in the fintech sector disrupted traditional banking in 2024.'},
       {'_id': 'vec67', 'chunk_text': 'Renewable energy projects accounted for a record share of global infrastructure investment in 2024.'},
       {'_id': 'vec35', 'chunk_text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
       {'_id': 'vec36', 'chunk_text': 'Unemployment is expected to hit 2.5% in Q3 of 2024.'},
       {'_id': 'vec6', 'chunk_text': 'Unemployment hit a record low of 3.7% in Q4 of 2024.'},
       {'_id': 'vec42', 'chunk_text': 'Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.'},
       {'_id': 'vec48', 'chunk_text': 'Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.'},
       {'_id': 'vec55', 'chunk_text': 'Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows.'},
       {'_id': 'vec45', 'chunk_text': 'Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations.'},
       {'_id': 'vec72', 'chunk_text': 'In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.'},
       {'_id': 'vec29', 'chunk_text': 'Growth vs. value investing strategies in 2024.'},
       {'_id': 'vec46', 'chunk_text': 'Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.'},
       {'_id': 'vec79', 'chunk_text': 'The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains.'},
       {'_id': 'vec87', 'chunk_text': "The U.S. labor market's resilience in 2024 defied predictions of a severe recession."},
       {'_id': 'vec40', 'chunk_text': 'Labor market trends show a declining participation rate despite record low unemployment in 2024.'},
       {'_id': 'vec37', 'chunk_text': 'In Q3 2025 unemployment for the prior year was revised to 2.2%'},
       {'_id': 'vec58', 'chunk_text': 'Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies.'},
       {'_id': 'vec47', 'chunk_text': 'The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand.'},
       {'_id': 'vec41', 'chunk_text': 'Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand.'},
       {'_id': 'vec56', 'chunk_text': 'Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession.'},
       {'_id': 'vec63', 'chunk_text': 'Population aging emerged as a critical economic issue in 2024, especially in advanced economies.'},
       {'_id': 'vec52', 'chunk_text': 'Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change.'},
       {'_id': 'vec23', 'chunk_text': 'Top SPAC mergers in the technology sector for 2024.'},
       {'_id': 'vec62', 'chunk_text': 'Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities.'},
       {'_id': 'vec64', 'chunk_text': 'Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials.'},
       {'_id': 'vec54', 'chunk_text': 'The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks.'},
       {'_id': 'vec96', 'chunk_text': 'New trade agreements signed 2022 will make an impact in 2024'},
       {'_id': 'vec49', 'chunk_text': "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports."},
       {'_id': 'vec7', 'chunk_text': 'The CPI index rose by 6% in July 2024, raising concerns about purchasing power.'},
       {'_id': 'vec84', 'chunk_text': "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets."},
       {'_id': 'vec13', 'chunk_text': 'Credit card APRs reached an all-time high of 22.8% in 2024.'},
       {'_id': 'vec53', 'chunk_text': 'Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization.'},
       {'_id': 'vec60', 'chunk_text': 'Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness.'},
       {'_id': 'vec91', 'chunk_text': 'The impact of ESG investing on corporate strategies has been a major focus in 2024.'},
       {'_id': 'vec68', 'chunk_text': 'Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure.'},
       {'_id': 'vec59', 'chunk_text': 'The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks.'},
       {'_id': 'vec39', 'chunk_text': 'The rise in energy prices significantly impacted inflation trends during the first half of 2024.'},
       {'_id': 'vec66', 'chunk_text': 'Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship.'},
       {'_id': 'vec57', 'chunk_text': 'Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth.'},
       {'_id': 'vec75', 'chunk_text': 'The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024.'},
       {'_id': 'vec51', 'chunk_text': 'The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth.'},
       {'_id': 'vec89', 'chunk_text': 'Venture capital investments in 2024 leaned heavily toward AI and automation startups.'}
    ]
    ```
  </Step>

  <Step title="Rerank the results">
    Use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank the merged and deduplicated results based on a unified relevance score and then return a smaller set of the most highly relevant results.

    For example, the following code sends the 52 unique results from the last step to the `bge-reranker-v2-m3` reranking model and returns the top 10 most relevant results.

    ```python Python theme={null}
    result = pc.inference.rerank(
        model="bge-reranker-v2-m3",
        query=query,
        documents=merged_results,
        rank_fields=["chunk_text"],
        top_n=10,
        return_documents=True,
        parameters={
            "truncate": "END"
        }
    )

    print("Query", query)
    print('-----')
    for row in result.data:
        print(f"{row['document']['_id']} - {round(row['score'], 2)} - {row['document']['chunk_text']}")
    ```

    ```console Response [expandable] theme={null}
    Query Q3 2024 us economic data
    -----
    vec36 - 0.84 - Unemployment is expected to hit 2.5% in Q3 of 2024.
    vec35 - 0.76 - Unemployment hit at 2.4% in Q3 of 2024.
    vec48 - 0.33 - Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.
    vec37 - 0.25 - In Q3 2025 unemployment for the prior year was revised to 2.2%
    vec42 - 0.21 - Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.
    vec87 - 0.2 - The U.S. labor market's resilience in 2024 defied predictions of a severe recession.
    vec63 - 0.08 - Population aging emerged as a critical economic issue in 2024, especially in advanced economies.
    vec92 - 0.08 - Income inequality widened in 2024 despite strong economic growth in developed nations.
    vec72 - 0.07 - In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.
    vec46 - 0.06 - Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.
    ```
  </Step>
</Steps>
