---
title: "Search Filters"
source: https://docs.perplexity.ai/docs/sonar/filters
path: docs/sonar/filters
---

Control and customize Sonar API search results with filters

Control which websites appear in search results, filter by date and location, target specific languages, and fine-tune search behavior using Sonar API filters.

## Domain Filters

Control which websites are included or excluded from search results using `search_domain_filter`. Supports both domain-level and URL-level filtering.

**Key parameters:**

* `search_domain_filter`: Array of domains or URLs (max 20)
* **Allowlist mode**: Include only specified domains (no prefix)
* **Denylist mode**: Exclude domains (prefix with `-`)

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Allowlist: Only search specific domains
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Explain how LIGO detects gravitational waves and summarize the GW150914 binary black hole merger detection."}],
    search_domain_filter=["nasa.gov", "wikipedia.org", "space.com"]
)

# Denylist: Exclude specific domains
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Explain the dominant grid-scale battery storage chemistries (lithium-ion, vanadium flow, sodium-ion): operating principle, typical use case, and cost dimensions."}],
    search_domain_filter=["-reddit.com", "-pinterest.com"]
)
```

<AccordionGroup>
  <Accordion title="Response — Explain how LIGO detects gravitational waves and summarize the GW150914 binary black ho...">
    ```json theme={null}
    {
      "id": "f5e40c51-a377-4599-bde4-851660e90515",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "LIGO has detected gravitational waves by using exquisitely sensitive laser interferometers, and its first major success was the observation of GW150914, a merger of two stellar-mass black holes. Here’s a concise explanation of both parts.\n\n---\n\n## 1. How LIGO detects gravitational waves\n\n### Basic idea: measure tiny changes in length\n\nA passing gravitational wave stretches space in one direction and squeezes it in the perpendicular direction. LIGO measures this as a tiny change in the relative lengths of two perpendicular arms using **laser interferometry**.\n\n**Core setup (Michelson interferometer):**\n\n- A very stable laser produces a beam of light.\n- A **beam splitter** divides the beam into two equal parts that travel down two **perpendicular 4 km arms**.\n- At the end of each arm, a highly polished, extremely isolated **test mass (mirror)** reflects the light back.\n- The returning beams recombine at the beam splitter and are sent to a **photodetector**.\n\nBecause the arms are tuned so that the two beams are normally **out of phase**, they destructively interfere and the detector sees almost *no light* (“dark fringe”).\n\n### What a gravitational wave does\n\nWhen a gravitational wave passes:\n\n- One arm is stretched while the other is squeezed; the roles then oscillate as the wave passes.\n- This changes the distance the light travels in each arm by about **10⁻¹⁸ m** (roughly ten‑thousandth the width of a proton for a 4 km arm).\n- That tiny difference makes the two light beams **no longer perfectly out of phase**.\n- The recombined light intensity **flickers** at the photodetector.\n\nLIGO’s computers continuously monitor this intensity:\n\n- The signal is a time-varying pattern of light intensity.\n- Data analysis looks for specific oscillatory patterns (“chirps”) predicted by **general relativity** for systems like orbiting and merging black holes or neutron stars.\n\n### Key technologies that make this possible\n\n- **Long arms and optical cavities**: Light bounces back and forth ~300 times between mirrors in each arm, effectively increasing the path length to hundreds of km, amplifying the effect of a given strain.\n- **Ultra-stable laser**: Single, well-defined wavelength so the “ruler” doesn’t change (otherwise the interference pattern would be meaningless).\n- **Vibration isolation**: Test mass mirrors are suspended in multi-stage pendulum systems and isolated from ground vibrations, seismic noise, and thermal noise, so they “feel” almost like they’re floating in space.\n- **Two detectors**: Twin observatories (Hanford, WA and Livingston, LA) separated by ~3000 km. A true gravitational-wave signal:\n  - Arrives at both with a time delay up to ~10 ms.\n  - Shows a consistent pattern in both instruments.\n  - This helps distinguish real astrophysical signals from local noise or glitches.\n\n---\n\n## 2. The GW150914 binary black hole merger\n\n**Event name:** GW150914  \n**Date of detection:** 2015-09-14, at 09:50:45 UTC  \n**Published/announced:** February 2016  \n\nThis was **the first direct detection of gravitational waves** and the **first direct observation of a binary black hole merger**.\n\n### What LIGO observed\n\n- A short signal, lasting about **0.2 seconds** in the LIGO band.\n- The frequency and amplitude increased over time in a characteristic **“chirp”**:\n  - Frequency swept from ~35 Hz up to ~150 Hz (and beyond) as the black holes spiraled together and merged.\n- The signal was observed in **both** LIGO detectors (Hanford and Livingston) with a time delay of about **7 ms**, consistent with a wavefront crossing Earth at the speed of light.\n\n### What produced the waves\n\nBy matching the observed waveform with general-relativistic models:\n\n- The source was identified as a **binary black hole system**:\n  - One black hole: ~36 solar masses\n  - The other: ~29 solar masses\n- They orbited each other at relativistic speeds and, in the last few orbits:\n  - Reached **fraction-of-light-speed** orbital velocities.\n  - Produced rapidly increasing gravitational waves as they spiraled inward.\n\nAt the moment of merger:\n\n- They formed a single black hole of about **62 solar masses**.\n- The mass difference (~3 solar masses) was converted almost entirely into **gravitational-wave energy**, according to \\(E = mc^2\\).\n- Peak power output was briefly greater than the combined luminosity of all the stars in the observable universe, but carried away as gravitational waves.\n\n### Distance and scale\n\n- The source was located about **1.3 billion light-years** away.\n- By the time the waves reached Earth, the strain in spacetime they produced at LIGO was about:\n  - **h ~ 10⁻²¹**, corresponding to:\n  - A change in a 4 km arm length of about **4 × 10⁻¹⁸ m**.\n- That’s roughly **10,000 times smaller than an atomic nucleus**.\n\n### Why GW150914 was historic\n\n- **First direct detection** of gravitational waves, confirming a major prediction of Einstein’s general relativity from 1916.\n- **First direct evidence** that:\n  - Stellar-mass black hole binaries exist.\n  - They can merge within the age of the universe.\n- Demonstrated that gravitational-wave astronomy is feasible, opening an entirely new way to observe the universe, complementary to telescopes that detect light (electromagnetic waves).\n\nIf you’d like, I can also summarize how the waveform carries information about the black holes’ masses and spins, or how data analysis separates such a tiny signal from noise.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779391555,
      "model": "sonar-pro",
      "citations": [
        "https://news.mit.edu/2016/ligo-first-detection-gravitational-waves-0211",
        "https://www.ligo.caltech.edu/page/ligo-technology",
        "https://www.nasa.gov/universe/nsfs-ligo-has-detected-gravitational-waves/",
        "https://www.youtube.com/watch?v=o7D8h_53jOM",
        "https://www.youtube.com/watch?v=XJ-lgnkovMc",
        "https://www.ligo.caltech.edu/page/what-are-gw",
        "https://www.ligo.caltech.edu/video/ligo20171016v8",
        "https://en.wikipedia.org/wiki/LIGO",
        "https://pressbooks.howardcc.edu/jrip1/chapter/ligo-analysis-direct-detection-of-gravitational-waves/"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "Scientists make first direct detection of gravitational waves | MIT News",
          "url": "https://news.mit.edu/2016/ligo-first-detection-gravitational-waves-0211",
          "date": "2016-02-11",
          "last_updated": "2026-05-16",
          "snippet": "Now LIGO has made the first direct observation of gravitational waves with an instrument on Earth. The researchers detected the gravitational ...",
          "source": "web"
        },
        {
          "title": "LIGO Technology | LIGO Lab | Caltech",
          "url": "https://www.ligo.caltech.edu/page/ligo-technology",
          "date": null,
          "last_updated": "2026-05-18",
          "snippet": "LIGO detects gravitational waves by generating a laser beam, splitting it in half, and sending each half down an arm of the interferometer. Inside each arm ...",
          "source": "web"
        },
        {
          "title": "NSF's LIGO Has Detected Gravitational Waves - NASA",
          "url": "https://www.nasa.gov/universe/nsfs-ligo-has-detected-gravitational-waves/",
          "date": "2016-02-11",
          "last_updated": "2026-05-15",
          "snippet": "LIGO is sensitive to gravitational waves within the range of 10 to 1,000 cycles per second (10 to 1,000 Hz). A space-based system would be able ...",
          "source": "web"
        },
        {
          "title": "How LIGO Detects Gravitational Waves - YouTube",
          "url": "https://www.youtube.com/watch?v=o7D8h_53jOM",
          "date": "2022-04-04",
          "last_updated": "2026-05-18",
          "snippet": "Share your videos with friends, family, and the world.",
          "source": "web"
        },
        {
          "title": "Laser Interferometer Gravitational-Wave Observatory (LIGO) Explained",
          "url": "https://www.youtube.com/watch?v=XJ-lgnkovMc",
          "date": "2025-02-14",
          "last_updated": "2026-03-31",
          "snippet": "Jonathan Richardson, an experimental physicist at UC Riverside who works on gravitational wave detection, explains what gravitational waves ...",
          "source": "web"
        },
        {
          "title": "What are Gravitational Waves? | LIGO Lab | Caltech",
          "url": "https://www.ligo.caltech.edu/page/what-are-gw",
          "date": null,
          "last_updated": "2026-05-19",
          "snippet": "In fact, by the time gravitational waves from LIGO's first detection reached us, the amount of space-time wobbling they generated was 10,000 times smaller than ...",
          "source": "web"
        },
        {
          "title": "Video | Ripples of Gravity, Flashes of Light | LIGO Lab | Caltech",
          "url": "https://www.ligo.caltech.edu/video/ligo20171016v8",
          "date": "2017-10-16",
          "last_updated": "2026-04-15",
          "snippet": "On Aug. 17, 2017, the Laser Interferometer Gravitational-wave Observatory (LIGO) and Virgo detected, for the first time, gravitational waves ...",
          "source": "web"
        },
        {
          "title": "LIGO - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/LIGO",
          "date": "2002-09-06",
          "last_updated": "2026-05-18",
          "snippet": "The Laser Interferometer Gravitational-Wave Observatory (LIGO) is a large-scale physics experiment and observatory designed to detect cosmic gravitational ...",
          "source": "web"
        },
        {
          "title": "LIGO Analysis: Direct Detection of Gravitational Waves",
          "url": "https://pressbooks.howardcc.edu/jrip1/chapter/ligo-analysis-direct-detection-of-gravitational-waves/",
          "date": "2018-05-03",
          "last_updated": "2026-03-04",
          "snippet": "The LIGO team used a Michelson interferometer, in which a laser beam is split into two identical beams at a 90-degree angle. Each beam travels through a 2.5- ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1206,
        "cost": {
          "input_tokens_cost": 6e-05,
          "output_tokens_cost": 0.01809,
          "total_cost": 0.02415,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 21,
        "total_tokens": 1227,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — Explain the dominant grid-scale battery storage chemistries (lithium-ion, vanadium flow...">
    ```json theme={null}
    {
      "id": "8de4a06d-4fef-4236-a1dd-36496785d4e5",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "Here’s a concise overview of the **dominant grid-scale battery storage chemistries**—**lithium-ion, vanadium flow, and sodium-ion**—focused on **how they work, where they’re used, and what drives their cost**.\n\n## 1) Lithium-ion (Li-ion)\n**Operating principle**\n- Stores energy by moving **lithium ions** between a **cathode** and **anode** through an electrolyte during charge/discharge.\n- Common grid variants include **LFP (lithium iron phosphate)** and **NMC/NCA** types.\n- In grid storage, it’s favored for its **high power density**, **high round-trip efficiency**, and fast response.\n\n**Typical use case**\n- Best for **short-duration storage**: typically **1–4 hours**.\n- Used for:\n  - frequency regulation\n  - peak shaving\n  - renewable smoothing\n  - short backup / bridging power\n- It currently **dominates grid-scale BESS deployments**.\n\n**Cost dimensions**\n- **Capex:** often lower upfront than many alternatives at small-to-medium durations, but strongly dependent on commodity prices.\n- **Duration penalty:** cost rises as you extend storage time because you need more cells/capacity.\n- **Lifecycle cost:** impacted by **degradation**, thermal management, and replacements over time.\n- **Supply chain cost:** exposed to **lithium**, and sometimes **nickel/cobalt** (less so for LFP), plus manufacturing scale and recycling economics.\n- **Operational cost:** relatively efficient, but cooling and system controls add overhead.\n\n## 2) Vanadium redox flow batteries (VRFBs)\n**Operating principle**\n- Energy is stored in **liquid electrolytes** containing vanadium ions in different oxidation states.\n- The electrolyte is kept in **external tanks** and pumped through a **cell stack** where redox reactions occur.\n- Because **power and energy are decoupled**, you scale:\n  - **power** by enlarging the stack\n  - **energy** by enlarging the tanks\n\n**Typical use case**\n- Best for **long-duration, stationary storage**, typically **4–12+ hours**.\n- Good for:\n  - renewable shifting\n  - microgrids\n  - industrial/grid backup\n  - applications needing lots of daily cycling and long calendar life\n- Particularly attractive where **cycle life and safety** matter more than compactness.\n\n**Cost dimensions**\n- **Capex:** usually higher upfront than Li-ion for short durations because of pumps, tanks, membranes, and the electrolyte.\n- **Duration advantage:** economics improve as storage duration increases, since energy capacity is mainly tank size, not more battery stacks.\n- **Material cost:** heavily affected by **vanadium electrolyte price**, which can be a major cost swing factor.\n- **Lifecycle cost:** often favorable because of **long service life** and less degradation-sensitive operation.\n- **Opex:** pumps and balance-of-plant add parasitic loads and maintenance costs.\n\n## 3) Sodium-ion (Na-ion)\n**Operating principle**\n- Works similarly to Li-ion, but uses **sodium ions** instead of lithium ions.\n- During charge/discharge, sodium ions move between the electrodes through an electrolyte.\n- Designed to use more abundant and lower-cost materials than Li-ion.\n\n**Typical use case**\n- Emerging option for **grid storage** and some stationary applications.\n- Often positioned for:\n  - cost-sensitive storage\n  - moderate-duration storage\n  - deployments where **resource availability** and supply-chain security matter\n- Not yet as mature or widespread as Li-ion.\n\n**Cost dimensions**\n- **Capex potential:** promising because **sodium is abundant** and generally cheaper than lithium.\n- **Materials advantage:** can reduce reliance on constrained or expensive battery minerals.\n- **Energy density tradeoff:** typically lower energy density than Li-ion, which can affect system footprint and packaging costs.\n- **Maturity cost:** current systems may still be pricier than expected at scale because manufacturing is less mature and supply chains are still developing.\n- **Lifecycle:** still being validated at scale; durability and bankability are key economic questions.\n\n---\n\n## Quick comparison\n\n| Chemistry | Main advantage | Main limitation | Best-fit duration | Main cost driver |\n|---|---|---|---|---|\n| **Lithium-ion** | High efficiency, mature, compact | Degradation, material price volatility, shorter duration economics | 1–4 h | Cells/materials, replacements, cooling |\n| **Vanadium flow** | Long life, scalable energy capacity, safe | Higher upfront complexity and footprint | 4–12+ h | Vanadium electrolyte, tanks, stack/BOP |\n| **Sodium-ion** | Lower-cost, abundant materials, supply-chain security | Lower maturity, lower energy density | Short to moderate duration | Manufacturing scale, performance validation |\n\n## Bottom line\n- **Li-ion** is the current default for grid batteries because it’s the most mature and commercially deployed.\n- **Vanadium flow** is attractive for **longer-duration storage** where lifetime and scalability matter.\n- **Sodium-ion** is a strong **cost-and-supply-chain alternative** that could grow if manufacturing scale and performance improve.\n\nIf you want, I can also turn this into a **one-page executive summary** or a **side-by-side table with typical round-trip efficiency, lifespan, and footprint**.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779391762,
      "model": "sonar-pro",
      "citations": [
        "https://www.batterypowertips.com/what-battery-chemistries-are-used-in-grid-scale-energy-storage-faq/",
        "https://energyanalytics.org/the-battery-storage-delusion/",
        "https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202516590",
        "https://en.wikipedia.org/wiki/Grid_energy_storage",
        "https://www.fortunebusinessinsights.com/industry-reports/grid-scale-battery-market-101304",
        "https://eticaag.com/best-battery-types-for-energy-storage-guide/"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "What battery chemistries are used in grid-scale energy storage?",
          "url": "https://www.batterypowertips.com/what-battery-chemistries-are-used-in-grid-scale-energy-storage-faq/",
          "date": "2022-06-05",
          "last_updated": "2026-04-14",
          "snippet": "Li-ion batteries currently dominate the grid-scale BESSs needed to support FTM installations (Figure 1). In the longer term, that is not expected to be ...",
          "source": "web"
        },
        {
          "title": "The Battery Storage Delusion: Utility-Scale Batteries Are No Silver ...",
          "url": "https://energyanalytics.org/the-battery-storage-delusion/",
          "date": "2025-12-03",
          "last_updated": "2026-05-15",
          "snippet": "Most lithium-ion batteries—currently the dominant chemistry for utility-scale systems—last for 10 to 13 years and degrade by 3% to 7% annually.",
          "source": "web"
        },
        {
          "title": "Batteries for Grid‐Scale Energy Storage Applications - Zhang - 2025",
          "url": "https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202516590",
          "date": "2025-09-17",
          "last_updated": null,
          "snippet": "For grid-scale applications, battery performance requirements differ from those of portable electronics or electric vehicles. Key metrics ...",
          "source": "web"
        },
        {
          "title": "Grid energy storage - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Grid_energy_storage",
          "date": "2005-03-25",
          "last_updated": "2026-05-05",
          "snippet": "As of 2023 , the largest form of grid storage is pumped-storage hydroelectricity, with utility-scale batteries and behind-the-meter batteries coming second and ...",
          "source": "web"
        },
        {
          "title": "Grid Scale Battery Market Size, Share | Growth Report [2034]",
          "url": "https://www.fortunebusinessinsights.com/industry-reports/grid-scale-battery-market-101304",
          "date": null,
          "last_updated": "2026-05-19",
          "snippet": "Which is the dominating battery chemistry segment in the market? The lithium-ion segment is anticipated to dominate the market during the forecast period.",
          "source": "web"
        },
        {
          "title": "Battery Chemistries for Energy Storage Systems: Safety ... - EticaAG",
          "url": "https://eticaag.com/best-battery-types-for-energy-storage-guide/",
          "date": "2025-02-18",
          "last_updated": "2026-05-09",
          "snippet": "Lithium-ion batteries are the dominant choice for modern Battery Energy Storage ... grid storage, renewable energy integration, and large-scale ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1125,
        "cost": {
          "input_tokens_cost": 0.00011,
          "output_tokens_cost": 0.01688,
          "total_cost": 0.02298,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 36,
        "total_tokens": 1161,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Warning>
  You can add a maximum of 20 domains or URLs. Use either allowlist OR denylist mode, not both simultaneously.
</Warning>

## Date & Time Filters

Filter search results by publication date, last updated date, or recency using date range parameters.

**Key parameters:**

* `search_after_date_filter`: Filter by publication date (format: `%m/%d/%Y`)
* `search_before_date_filter`: Filter by publication date (format: `%m/%d/%Y`)
* `last_updated_after_filter`: Filter by last updated date
* `last_updated_before_filter`: Filter by last updated date
* `search_recency_filter`: Predefined periods (`"hour"`, `"day"`, `"week"`, `"month"`, `"year"`)

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Publication date range
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Summarize current trends in enterprise software adoption from major technology industry analysis publications."}],
    search_after_date_filter="3/1/2025",
    search_before_date_filter="3/5/2025"
)

# Last updated date range
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Explain how OpenAI's API documentation is organized: Models, API reference, and Cookbook sections."}],
    last_updated_after_filter="3/1/2025",
    last_updated_before_filter="3/5/2025"
)

# Recency filter for real-time results (breaking news or live events)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What economic indicators do investors most commonly watch (CPI, jobs report, FOMC decisions), and why?"}],
    search_recency_filter="hour"
)

# Recency filter (convenient relative dates)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What are the major categories of machine learning, and what are the most common applications of each?"}],
    search_recency_filter="week"
)
```

<AccordionGroup>
  <Accordion title="Response — Summarize current trends in enterprise software adoption from major technology industry...">
    ```json theme={null}
    {
      "id": "1f0b28de-6c93-4dcc-b509-c191e53ec625",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "Enterprise software adoption is being shaped by three dominant forces: near-universal **cloud and SaaS**, rapid but uneven **AI (especially generative AI) integration**, and a shift from tool experimentation to **measurable business impact and ROI**.[1][3][5]\n\nKey current trends from major industry analyses (Gartner, McKinsey, Deloitte, SVB, etc.):\n\n1. **Cloud- and SaaS‑first is now the default, moving toward strategic hybrid**  \n   - Around **94% of enterprises use cloud services**, and about **67% of enterprise infrastructure is cloud‑based**, signaling that cloud is no longer a differentiator but table stakes for enterprise software adoption.[1]  \n   - As AI workloads grow, organizations are shifting from “cloud‑first” to **strategic hybrid** architectures—using cloud for elasticity, on‑prem for consistency and cost control, and edge for low‑latency use cases.[5]  \n   - This is driving adoption of **cloud‑native ERP, CRM, collaboration and digital workplace platforms**, with cloud ERP and collaboration tools among the fastest-growing categories.[1]\n\n2. **AI and generative AI are embedded everywhere—and buyers now demand ROI, not pilots**  \n   - Major analyses describe a pivot from “What can we do with AI?” to “How do we get **impact** from AI?”[5] Enterprises are moving from endless proofs of concept to **production deployments** tied to clear business cases (productivity, revenue growth, cost reduction).[5]  \n   - **GenAI adoption** is accelerating in software development, IT service management, and knowledge work, but many organizations still lack the **training, governance and integration** needed for consistent value and ROI.[2]  \n   - Venture and product trends show AI is no longer optional: **AI-native enterprise software** is attracting the majority of new investment. In 2025, **65% of US enterprise software VC funding went to AI startups**, and AI capability is a core expectation in new enterprise platforms.[3]  \n   - Deloitte notes only **11%** of organizations have agentic (AI agent) systems in full production, despite many pilots, highlighting a gap between experimentation and scalable adoption.[5]\n\n3. **Digital transformation is mainstream; adoption is driven by process optimization and agility**  \n   - Around **65% of organizations increased digital transformation investments** post‑2020.[1]  \n   - Enterprises adopt new software primarily to **optimize processes (68%)**, **improve employee performance (63%)**, **increase agility (59%)**, and **reduce costs (51%)**, according to surveys cited by PwC and others.[1]  \n   - Communication/collaboration platforms, **digital workplace** suites, **ERP**, and **CRM** systems are widely deployed to support hybrid/remote work and modern operating models.[1]\n\n4. **Digital workplace, collaboration, and “enterprise OS” platforms continue to consolidate**  \n   - The global **team collaboration software** market is projected to reach about **$40B by 2028**, with strong double‑digit growth.[1]  \n   - Roughly **60% of organizations** have a formal **digital workplace strategy**, often centered on integrated suites (productivity, communication, content, and workflows) rather than point tools.[1]  \n   - This is pushing adoption of platforms that act as a **hub**—integrating messaging, meetings, knowledge, workflows, and increasingly AI assistants—rather than stand‑alone apps.\n\n5. **User adoption, skills, and change management are now recognized as critical bottlenecks**  \n   - More than **40% of businesses** cite **lack of user adoption** as the biggest barrier to realizing value from new enterprise software.[1]  \n   - Around **70% of employees** are reported to lack necessary digital skills, while only **30%** of organizations have formal digital training programs.[1]  \n   - In response, enterprises are increasing use of **e‑learning and blended learning** (used by about **73%** of organizations) and **microlearning** (used by ~**58%**) to support ongoing adoption.[1]  \n   - Despite this, over **40% of IT leaders don’t measure user satisfaction** with software adoption—suggesting a growing focus area for mature organizations.[1]\n\n6. **Architectures are becoming modular, composable, and API‑first**  \n   - Analyst and consulting reports emphasize a move toward **modular, composable architectures** and **API‑first** design for enterprise systems, enabling faster change and easier integration across SaaS and legacy landscapes.[5][9]  \n   - Composable, API‑based approaches are forecast to account for a substantial share of new enterprise applications in the next few years, supporting faster experimentation with AI services and microservices‑based backends.[9]  \n   - This trend supports “AI-native” organizations, where AI models, data services, and business capabilities can be recomposed rapidly around new use cases.[5]\n\n7. **Cost, security, and governance are reshaping enterprise AI/software strategies**  \n   - Enterprises are encountering **AI infrastructure and inference cost shocks**—some see monthly AI bills in the tens of millions, prompting a reevaluation of infrastructure and model choices.[5]  \n   - Deloitte and other analysts describe an **“AI infrastructure reckoning”**, with organizations optimizing model size, deployment patterns, and using hybrid/cloud/edge combinations to balance performance and cost.[5]  \n   - At the same time, AI introduces new **security and compliance** concerns: organizations must secure data, models, applications, and infrastructure while also using AI to enhance cyber defense capabilities.[5]  \n   - This is leading to adoption of **governance frameworks, model risk management, and AI observability tools** as standard parts of the enterprise software stack.\n\n8. **Market dynamics: AI‑native vendors, M&A, and platform consolidation**  \n   - The enterprise software market remains robust, with strong growth tied to **Industry 4.0, digitization, robotics, and connected devices** driving demand for advanced software in manufacturing and operations.[7]  \n   - There are now **hundreds of enterprise software unicorns**, with more than **75 new enterprise AI unicorns** emerging in the past year according to SVB data, illustrating sustained investor belief in AI‑centric enterprise software models.[3]  \n   - About **46% of enterprise software M&A deals** involved a US VC‑backed buyer, often using acquisitions to acquire **AI capabilities and talent** and to become more “AI‑native.”[3]  \n   - This M&A and investment activity accelerates **feature convergence and platform consolidation**, where leading vendors incorporate adjacent capabilities (analytics, automation, AI assistants) rather than ceding them to niche tools.\n\n9. **Human‑AI collaboration and operating model changes accompany software adoption**  \n   - Deloitte’s research finds that **only 1% of IT leaders** report no major operating‑model changes; most are restructuring around **human‑agent teams**, modular architectures, and continuous evolution.[5]  \n   - Successful adopters focus on **business problems first**, involve end users in solution design, and treat change as continuous rather than periodic.[5]  \n   - This shifts enterprise software buying criteria: organizations increasingly evaluate vendors on **ability to support ongoing change**, embedded governance, AI‑readiness, and end‑user experience—not just feature lists.\n\n10. **Persistent gap between technology capability and organizational readiness**  \n    - Major publications converge on a pattern: technology (especially AI and cloud) is advancing faster than **organizational readiness** in data, governance, skills, and process redesign.[2][5]  \n    - Generative AI tools are broadly available, but **engagement and sustained usage are inconsistent** without proper integration into workflows and clear accountability for outcomes.[2]  \n    - Organizations that succeed tend to have **high‑quality, well‑structured data**, repeatable workflows, and strong cross‑functional governance, enabling measurable productivity and revenue impact from new software.[2]\n\nIf you share your specific context (industry, size, or region), I can narrow this down to the trends and adoption patterns most relevant to your environment and point to the most pertinent analyst angles (e.g., CIO priorities vs. VC/market-structure views).",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896019,
      "model": "sonar-pro",
      "citations": [
        "https://lemonlearning.com/blog/infographic-enterprise-software-key-figures",
        "https://www.alpha-sense.com/resources/reports/enterprise-software-assessing-ai-adoption-trends/",
        "https://www.svb.com/trends-insights/reports/state-of-enterprise-software/",
        "https://kms-technology.com/blog/enterprise-software-trends/",
        "https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html",
        "https://www.bain.com/insights/six-trends-shaping-the-future-of-enterprise-technology/",
        "https://www.grandviewresearch.com/industry-analysis/enterprise-software-market",
        "https://www.bacancytechnology.com/blog/enterprise-software-trends",
        "https://www.integrate.io/blog/data-integration-adoption-rates-enterprises/"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "Enterprise Software: Key Figures for 2026 - Lemon Learning",
          "url": "https://lemonlearning.com/blog/infographic-enterprise-software-key-figures",
          "date": "2021-10-25",
          "last_updated": "2026-05-26",
          "snippet": "CRM: The CRM market is projected to grow to $128 billion by 2028, driven by increasing demand for AI-driven customer engagement (Fortune Business Insights).",
          "source": "web"
        },
        {
          "title": "Enterprise Software: Assessing AI Adoption Trends - AlphaSense",
          "url": "https://www.alpha-sense.com/resources/reports/enterprise-software-assessing-ai-adoption-trends/",
          "date": "2025-04-24",
          "last_updated": "2026-03-28",
          "snippet": "This report examines where genAI is driving real, positive business outcomes and what separates successful enterprise-scale efforts from those that stall.",
          "source": "web"
        },
        {
          "title": "Enterprise Software Report 2026: AI & VC trends - Silicon Valley Bank",
          "url": "https://www.svb.com/trends-insights/reports/state-of-enterprise-software/",
          "date": null,
          "last_updated": "2026-05-25",
          "snippet": "356 US VC-backed enterprise software unicorns now exist. More than 75 new unicorns have entered the stable since 2025, as record capital has poured in targeting ...",
          "source": "web"
        },
        {
          "title": "Key Trends Shaping The Future of Enterprise Software Development",
          "url": "https://kms-technology.com/blog/enterprise-software-trends/",
          "date": "2025-12-12",
          "last_updated": null,
          "snippet": "New trends like machine learning, generative AI, distributed systems, and CI/CD will transform how enterprise applications function. As ...",
          "source": "web"
        },
        {
          "title": "Tech Trends 2026 | Deloitte Insights",
          "url": "https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html",
          "date": "2025-12-10",
          "last_updated": "2026-05-24",
          "snippet": "As technology innovation and adoption accelerate, five trends reveal how successful organizations are moving from experimentation to impact.",
          "source": "web"
        },
        {
          "title": "Six Trends Shaping the Future of Enterprise Technology",
          "url": "https://www.bain.com/insights/six-trends-shaping-the-future-of-enterprise-technology/",
          "date": "2022-08-04",
          "last_updated": "2026-05-25",
          "snippet": "No sooner has cloud computing become mainstream than questions arise about new trends and buzzwords such as web3, the metaverse, hyperautomation, and quantum ...",
          "source": "web"
        },
        {
          "title": "Enterprise Software Market Size | Industry Report, 2033",
          "url": "https://www.grandviewresearch.com/industry-analysis/enterprise-software-market",
          "date": null,
          "last_updated": "2026-05-10",
          "snippet": "Key industry trends such as Industry 4.0, digitization, modern manufacturing, robotics, and the rise of connected devices are driving the demand for advanced ...",
          "source": "web"
        },
        {
          "title": "Top 10 Enterprise Software Trends to Catch Up in 2026",
          "url": "https://www.bacancytechnology.com/blog/enterprise-software-trends",
          "date": "2026-01-01",
          "last_updated": "2026-05-27",
          "snippet": "Emerging trends like Artificial Intelligence (AI), Machine Learning (ML), and Robotic Process Automation (RPA) are becoming more and more popular.",
          "source": "web"
        },
        {
          "title": "Data Integration Adoption Rates in Enterprises – 45 Statistics Every ...",
          "url": "https://www.integrate.io/blog/data-integration-adoption-rates-enterprises/",
          "date": "2026-01-10",
          "last_updated": "2026-05-27",
          "snippet": "Composable architecture adoption reaches 30% of new applications by 2027. McKinsey predicts modular, API-first approaches will reshape ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1727,
        "cost": {
          "input_tokens_cost": 5e-05,
          "output_tokens_cost": 0.02591,
          "total_cost": 0.03196,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 17,
        "total_tokens": 1744,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — Explain how OpenAI's API documentation is organized: Models, API reference, and Cookboo...">
    ```json theme={null}
    {
      "id": "6ba86d34-0390-4db2-9667-f94751e4fcfc",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "OpenAI’s API documentation is organized into three complementary pieces: **Models**, **API reference**, and the **Cookbook**. Each serves a different purpose:\n\n- **Models**: *What* you can call  \n- **API reference**: *How* to call it, parameter‑by‑parameter  \n- **Cookbook**: *Practical examples* and “recipes” for real tasks  \n\n---\n\n### 1. Models section – what’s available and when to use it\n\nThe **Models** part of the docs focuses on the **available model families**, their capabilities, and typical use cases.[6]\n\nYou’ll generally find:\n\n- **Model catalog**  \n  - Lists major models (for text, chat, images, audio, embeddings, etc.).  \n  - Notes capabilities like reasoning, multimodality, speed, and context length.[6]\n\n- **Use‑case guidance**  \n  - Which models are recommended for:  \n    - chat/assistants  \n    - structured outputs / tools  \n    - code  \n    - embeddings / search  \n    - image or audio tasks  \n\n- **Limits and behavior**  \n  - Context window, rate limits, and any model‑specific constraints.[6]\n\nYou use the Models section to **choose the right model name** (e.g., for the `model` field in your API call) and understand trade‑offs (price, speed, quality).\n\n---\n\n### 2. API reference – how to call the API\n\nThe **API reference** is the **technical contract** for every endpoint.[6] It explains *exactly* how to talk to the service.\n\nTypical structure:\n\n- **Endpoints grouped by functionality**  \n  For example (names/structure can change over time, but conceptually):  \n  - Chat / Assistants (multi‑turn conversations, tools)  \n  - Completions / text generation  \n  - Images (generate, edit, variations)  \n  - Audio (speech‑to‑text, text‑to‑speech)  \n  - Embeddings  \n  - Files / fine‑tuning / vector stores, etc.[6]\n\n- **Per‑endpoint details**  \n  For each endpoint, the reference includes:  \n  - HTTP method and path (e.g., `POST /v1/...`)  \n  - **Required and optional parameters**, with types and descriptions  \n  - Example **request and response** bodies in JSON  \n  - Error formats and status codes[3][6]\n\n- **Language‑specific examples**  \n  - Code snippets for curl, Python, JavaScript, and other SDKs (e.g., showing headers, auth, and JSON payload).[6]\n\nDevelopers mainly use this section when they:\n\n- Implement or debug calls in code  \n- Need exact parameter names, types, or defaults (e.g., `temperature`, `top_p`, `max_tokens`, `tools`)  \n- Want to see canonical examples of a specific endpoint’s usage[3]\n\n---\n\n### 3. Cookbook – concrete, end‑to‑end “recipes”\n\nThe **OpenAI Cookbook** is a collection of **worked examples** and **how‑to guides** for common tasks using the API.[4][5]\n\nKey characteristics:\n\n- **Task‑oriented “recipes”**  \n  Examples include:  \n  - building a Q&A chatbot over your documents  \n  - using embeddings for search or recommendation  \n  - creating function/tool calling flows  \n  - content moderation pipelines  \n  - structured JSON output, RAG workflows, etc.[4][5]\n\n- **Executable code**  \n  - Mostly Python and JavaScript notebooks/scripts.  \n  - Shows complete flows: data prep → API call(s) → post‑processing → basic app logic.[4]\n\n- **Concept explanations tied to code**  \n  - Explains *why* certain parameters are chosen, how to handle rate limiting, batching, streaming, etc., in the context of real applications.[4][5]\n\nThe Cookbook is what you reach for when the question is, “How do I **build X** with the API?” rather than “What does this parameter do?”\n\n---\n\n### How they fit together in practice\n\nWhen building with OpenAI’s API you typically:\n\n1. **Start with Models**  \n   - Pick the **model** that fits your task and constraints (capabilities, cost, speed).[6]\n\n2. **Use the API reference**  \n   - Implement the call(s) for the chosen endpoint.  \n   - Look up request format, parameters, and responses in detail.[3][6]\n\n3. **Consult the Cookbook**  \n   - Copy or adapt a **recipe** that matches your use case (e.g., RAG chatbot, summarization pipeline).[4][5]\n\nSo: **Models** answer “what can I use?”, the **API reference** answers “how do I call it exactly?”, and the **Cookbook** answers “how do I put this together into a working solution?”.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896014,
      "model": "sonar-pro",
      "citations": [
        "https://www.youtube.com/watch?v=9ZyHckE3iIo",
        "https://ai.google.dev/api",
        "https://www.youtube.com/watch?v=hLTOPHDCytM",
        "https://github.com/openai/openai-cookbook",
        "https://developers.openai.com/cookbook",
        "https://developers.openai.com/api/docs",
        "https://kwfoundation.org/wp-content/uploads/2025/10/OpenAI_API_Cookbook.pdf",
        "https://leanpub.com/openaiapicookbook"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "OpenAI API Masterclass: Platform, Models & API Explained (Part 1/5)",
          "url": "https://www.youtube.com/watch?v=9ZyHckE3iIo",
          "date": "2024-10-27",
          "last_updated": "2026-03-19",
          "snippet": "OpenAI API Masterclass: GPT-4, ChatGPT, Assistants API, DALL-E, Whisper | Complete Platform Tutorial for Beginners A Complete Beginner's ...",
          "source": "web"
        },
        {
          "title": "Gemini API reference | Google AI for Developers",
          "url": "https://ai.google.dev/api",
          "date": null,
          "last_updated": "2026-05-26",
          "snippet": "This API reference describes the standard, streaming, and real-time APIs you can use to interact with the Gemini models. You can use the REST APIs in any ...",
          "source": "web"
        },
        {
          "title": "The Definitive Guide to Reading OpenAI APIs & How to ... - YouTube",
          "url": "https://www.youtube.com/watch?v=hLTOPHDCytM",
          "date": "2023-05-02",
          "last_updated": "2026-02-23",
          "snippet": "In this video, you're going to learn how to read Open AI's API docs and connect this to apps such as Bubble. READ OUR FULL NO-CODE TOOL ...",
          "source": "web"
        },
        {
          "title": "Examples and guides for using the OpenAI API · GitHub",
          "url": "https://github.com/openai/openai-cookbook",
          "date": "2022-03-11",
          "last_updated": "2026-02-27",
          "snippet": "Example code and guides for accomplishing common tasks with the OpenAI API. To run these examples, you'll need an OpenAI account and associated API key.",
          "source": "web"
        },
        {
          "title": "Cookbook - OpenAI Developers",
          "url": "https://developers.openai.com/cookbook",
          "date": "2020-08-19",
          "last_updated": "2026-05-27",
          "snippet": "Recipes to help you build with OpenAI models ... OpenAI Developers · Home · API · Docs. Guides and concepts for the OpenAI API · API reference.",
          "source": "web"
        },
        {
          "title": "OpenAI API Platform Documentation",
          "url": "https://developers.openai.com/api/docs",
          "date": null,
          "last_updated": "2026-05-27",
          "snippet": "Explore guides, API docs, and examples for the OpenAI API.",
          "source": "web"
        },
        {
          "title": "[PDF] OpenAI API Cookbook | KW Foundation",
          "url": "https://kwfoundation.org/wp-content/uploads/2025/10/OpenAI_API_Cookbook.pdf",
          "date": null,
          "last_updated": null,
          "snippet": "As we learned in the Running a completion request in the OpenAI Playground recipe, ChatGPT and its. GPT models are built on a transformer architecture, which ...",
          "source": "web"
        },
        {
          "title": "OpenAI API Cookbook [Leanpub PDF/iPad/Kindle]",
          "url": "https://leanpub.com/openaiapicookbook",
          "date": "2024-12-23",
          "last_updated": "2025-02-02",
          "snippet": "You'll begin with the OpenAI API fundamentals, covering setup, authentication, and key parameters, and quickly progress to the different elements of the OpenAI ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1014,
        "cost": {
          "input_tokens_cost": 6e-05,
          "output_tokens_cost": 0.01521,
          "total_cost": 0.02127,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 21,
        "total_tokens": 1035,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — What economic indicators do investors most commonly watch (CPI, jobs report, FOMC decis...">
    ```json theme={null}
    {
      "id": "9f2708a6-75ed-427a-86a1-8bc5b097a7cc",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "Investors tend to focus on a relatively small set of economic indicators that have the biggest, most direct impact on markets. The ones you mentioned—CPI, jobs report, and FOMC decisions—are at the top of that list, but they’re part of a broader core group.\n\nBelow are the most commonly watched indicators, what they measure, and why markets care.\n\n---\n\n## 1. Jobs Report (Nonfarm Payrolls / Labor Market Data)\n\n**What it is:**  \nThe U.S. Jobs Report (Nonfarm Payrolls) is released monthly by the Bureau of Labor Statistics. It includes:\n- Jobs added/lost (nonfarm payrolls)\n- Unemployment rate\n- Labor force participation\n- Average hourly earnings (wage growth)\n\n**Why investors watch it:**\n- **Growth signal:** Strong job gains usually mean businesses are hiring, production is rising, and consumers have income to spend—supporting corporate revenues and profits.\n- **Consumer spending:** Employment drives household income, which drives ~70% of U.S. GDP through consumption.\n- **Policy implications:** A very strong labor market (especially with fast wage growth) can increase inflation pressure and push the Federal Reserve toward tighter policy (higher interest rates). Weak labor data can have the opposite effect.\n\n**Market impact:**\n- **Stocks:** Strong jobs + controlled wages → bullish for many sectors. Weak jobs → can hurt cyclical stocks but sometimes helps rate‑sensitive stocks if it implies easier Fed policy.\n- **Bonds:** Strong jobs/wages → higher yields (lower bond prices) as markets anticipate rate hikes. Weak jobs → lower yields.\n- **Dollar:** Strong jobs → often a stronger U.S. dollar (on expectations of higher rates).\n\n---\n\n## 2. Inflation Data (Especially CPI, PCE, and PPI)\n\n### Consumer Price Index (CPI)\n\n**What it is:**  \nMonthly measure of the average price change of a basket of consumer goods and services (food, housing, transportation, medical care, etc.).\n\n**Why investors watch it:**\n- **Purchasing power:** Rising CPI means inflation is eroding the value of money.\n- **Interest rates:** High or rising inflation pressures central banks to raise rates; low inflation allows easier policy.\n- **Profit margins:** Higher input costs can squeeze corporate margins if firms can’t pass on price increases.\n\n**Market impact:**\n- **Bonds:** Very sensitive. Higher inflation → higher yields, lower bond prices.\n- **Equities:** High inflation can hurt valuations (higher discount rates) and pressure growth stocks. Some sectors (energy, materials, certain financials) may benefit.\n- **Asset allocation:** Sustained high inflation can make inflation‑linked securities (TIPS), real assets (real estate, commodities), and certain equities more attractive relative to nominal bonds.\n\n### Personal Consumption Expenditures (PCE) Price Index\n\n**What it is:**  \nA broader measure of consumer prices from the BEA, and the **Fed’s preferred inflation gauge**.\n\n**Why investors watch it:**\n- It’s what the Fed targets when it talks about its 2% inflation goal, so it’s key for **monetary policy expectations**.\n\n### Producer Price Index (PPI)\n\n**What it is:**  \nMeasures price changes received by domestic producers (wholesale level).\n\n**Why investors watch it:**\n- **Leading signal:** Rising producer prices often show up later in consumer prices (CPI), providing an early hint of inflation trends and margin pressures.\n\n---\n\n## 3. Federal Reserve / FOMC Decisions\n\n**What they are:**\n- **Federal funds rate decisions** (target range)\n- **FOMC statements and minutes**\n- **Press conferences and forward guidance** (what the Fed hints it will do next)\n\n**Why investors watch them:**\n- **Cost of capital:** Policy rates influence borrowing costs for consumers and companies, mortgage rates, corporate bonds, etc.\n- **Valuation anchor:** Interest rates are central to discounting future cash flows, which affects stock and bond valuations.\n- **Risk appetite:** Easier policy (low rates, quantitative easing) tends to boost risk assets; tighter policy often pressures them.\n\n**Market impact:**\n- **Stocks:** Lower rates → generally bullish, especially for growth/tech and highly leveraged firms. Higher rates → can hurt valuations and rate‑sensitive sectors.\n- **Bonds:** Direct effect on short‑term yields and expectations for the entire yield curve.\n- **Currencies:** Higher relative U.S. rates often support a stronger dollar, affecting global capital flows and commodity prices.\n\n---\n\n## 4. Gross Domestic Product (GDP)\n\n**What it is:**  \nTotal value of goods and services produced in a country. Reported quarterly (with estimates and revisions).\n\n**Why investors watch it:**\n- **Big‑picture growth:** It’s the broadest measure of economic activity—whether the economy is expanding or contracting.\n- **Corporate earnings backdrop:** Strong GDP growth supports higher revenues and profits; weak or negative growth suggests weaker earnings and possible recessions.\n- **Cycle positioning:** Helps investors gauge where we are in the business cycle (expansion, slowdown, recession, recovery).\n\n**Market impact:**\n- Stronger‑than‑expected GDP → can lift stocks but may also push bond yields up if it raises expectations of higher rates.\n- Weak GDP → can pressure equities but support bonds; if very weak, can trigger fear of recession.\n\n---\n\n## 5. Other Key Indicators Many Investors Track\n\n### a) Purchasing Managers’ Index (PMI / ISM Manufacturing & Services)\n\n**What it is:**  \nSurvey-based index of business conditions (new orders, production, employment, inventories, supplier deliveries).  \n- Above 50 = expansion  \n- Below 50 = contraction\n\n**Why investors watch it:**\n- **Leading indicator:** PMIs often turn before GDP and earnings, giving an early signal of accelerations or slowdowns.\n- **Sector insight:** Manufacturing and services PMIs show which parts of the economy are strengthening or weakening.\n\n**Market impact:**\n- Rising PMIs above 50 often support cyclical stocks and risk appetite; falling PMIs below 50 can trigger risk‑off shifts.\n\n### b) Consumer Confidence / Consumer Sentiment\n\n**What it is:**  \nSurveys of how optimistic/pessimistic consumers are about the economy and their own finances.\n\n**Why investors watch it:**\n- **Spending indicator:** Confident consumers are more likely to spend, supporting retail sales and corporate earnings.\n\n**Market impact:**\n- Rising confidence often aligns with rising equity markets and stronger consumer‑facing sectors; persistent declines can warn of weaker consumption.\n\n### c) Retail Sales\n\n**What it is:**  \nMonthly report of consumer spending at retail stores and online.\n\n**Why investors watch it:**\n- Direct read on consumer demand, which is central to GDP and corporate revenue.\n\n**Market impact:**\n- Strong retail sales → positive for consumer discretionary and broader equities; weak sales → negative signal for growth.\n\n### d) Housing Data (Housing Starts, Building Permits, Home Sales)\n\n**Why investors watch it:**\n- **Leading indicator:** Construction drives employment and demand for materials; housing is also sensitive to interest rates.\n- Weak housing can signal tighter credit or consumer stress; strong housing suggests confidence and easier financial conditions.\n\n### e) Durable Goods Orders / Industrial Production\n\n**Why investors watch them:**\n- Measure business investment and manufacturing activity, especially for big‑ticket items.\n- Rising orders and production → sign of corporate confidence and capex; falling numbers can warn of slowdown.\n\n---\n\n## How Investors Use These Indicators in Practice\n\n1. **Macro direction:**  \n   - Are we in expansion, slowdown, or recession risk?  \n   - Jobs + PMIs + retail sales + GDP → answer this.\n\n2. **Inflation and interest rate expectations:**  \n   - CPI/PCE + wage growth + PPI → inform where inflation is headed.  \n   - That, plus Fed communications → shape bond yields and discount rates.\n\n3. **Positioning portfolios:**\n   - **Strong growth, moderate inflation:** Favor cyclicals (industrials, consumer discretionary, financials), possibly reduce long-duration bonds.\n   - **High inflation, rising rates:** Emphasize value sectors, shorter-duration bonds, TIPS, and sometimes commodities.\n   - **Weak growth, easing policy:** Tilt to quality growth, defensives (utilities, staples, healthcare), and longer-duration bonds.\n\n---\n\nIf you’d like, tell me what you invest in (e.g., stock ETFs, individual stocks, bonds, options, crypto), and I can narrow this down to the 3–5 indicators that matter most for *your* strategy and how to practically track and act on them.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779391864,
      "model": "sonar-pro",
      "citations": [
        "https://sheltonfunds.com/what-are-the-most-important-economic-indicators-to-watch/",
        "https://getbaraka.com/learn/economic-indicators-guide-to-informed-investing",
        "https://www.finra.org/investors/insights/key-economic-indicators-every-investor-should-know",
        "https://russellinvestments.com/ca/resources/financial-professionals/economic-indicators-dashboard",
        "https://www.youtube.com/watch?v=DEVRzIjAJCE",
        "https://www.financialsense.com/blog/21384/us-economic-boom-or-bust-indicators-every-investor-needs-watch"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "What Economic Indicators To Watch | Shelton Funds",
          "url": "https://sheltonfunds.com/what-are-the-most-important-economic-indicators-to-watch/",
          "date": "2025-08-01",
          "last_updated": "2025-11-03",
          "snippet": "What Are The Most Important Economic Indicators To Watch? · 1. The U.S. Jobs Report (Nonfarm Payrolls) · 2. Consumer Price Index (CPI) · 3. Gross ...",
          "source": "web"
        },
        {
          "title": "Economic Indicators: Guide to Informed Investing",
          "url": "https://getbaraka.com/learn/economic-indicators-guide-to-informed-investing",
          "date": "2026-01-22",
          "last_updated": "2026-01-28",
          "snippet": "Detailed Analysis of Top Economic Indicators · Gross Domestic Product (GDP) · Unemployment Rate · Consumer Price Index (CPI) · Producer Price Index (PPI).",
          "source": "web"
        },
        {
          "title": "Key Economic Indicators Every Investor Should Know | FINRA.org",
          "url": "https://www.finra.org/investors/insights/key-economic-indicators-every-investor-should-know",
          "date": "2024-12-10",
          "last_updated": "2026-05-20",
          "snippet": "Key Economic Indicators Every Investor Should Know · Real Gross Domestic Product (GDP) · Labor Market Data · Inflation Reports · Consumer Confidence ...",
          "source": "web"
        },
        {
          "title": "Economic Indicators Dashboard | Russell Investments",
          "url": "https://russellinvestments.com/ca/resources/financial-professionals/economic-indicators-dashboard",
          "date": null,
          "last_updated": "2026-03-24",
          "snippet": "To help you talk to your clients, we've identified a few key economic and market indicators to help assess the current economic health and trend. As of: 3/31/ ...",
          "source": "web"
        },
        {
          "title": "How Economic Indicators in India and the US Affect Your Investments",
          "url": "https://www.youtube.com/watch?v=DEVRzIjAJCE",
          "date": "2025-11-19",
          "last_updated": "2025-12-02",
          "snippet": "... data – and understanding both India and the US helps you move with them. To know more about investing in US stocks, ETFs and Mutual Funds ...",
          "source": "web"
        },
        {
          "title": "US Economic Boom or Bust? Indicators Every Investor Needs to Watch",
          "url": "https://www.financialsense.com/blog/21384/us-economic-boom-or-bust-indicators-every-investor-needs-watch",
          "date": "2025-08-28",
          "last_updated": null,
          "snippet": "Among the most widely followed are retail sales, industrial production, and the Services ISM Index. Retail sales directly measure consumer ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1815,
        "cost": {
          "input_tokens_cost": 7e-05,
          "output_tokens_cost": 0.02722,
          "total_cost": 0.0333,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 24,
        "total_tokens": 1839,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — What are the major categories of machine learning, and what are the most common applica...">
    ```json theme={null}
    {
      "id": "f737c85e-f293-4758-8852-3d0a523c2f92",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "The major categories of machine learning are **supervised**, **unsupervised**, **reinforcement**, and (less central but increasingly important) **semi‑supervised** and **self‑supervised** learning.[1][3][8] Each is defined by how it uses data and feedback, and each maps to characteristic application areas.\n\n---\n\n## 1. Supervised learning\n\n**Idea:** Learn a mapping from inputs to known outputs using **labeled data** (each example has an input and the correct target).[1][2][3]\n\n**Typical tasks**\n\n- **Classification** (predict a category: spam vs non‑spam, disease vs no disease)[2][3]  \n- **Regression** (predict a continuous value: price, temperature, demand)[2][3]  \n- **Forecasting / time‑series prediction** (future sales, load, weather, etc.)[3]\n\n**Common applications**\n\n- **Image, speech, and text processing**:  \n  - Image classification (e.g., recognizing objects, medical imaging diagnosis)[1][2]  \n  - Speech recognition (converting audio to text)[2]  \n  - Sentiment analysis and topic classification in text (reviews, social media)[2]\n- **Predictive analytics & forecasting**:  \n  - Sales forecasting, demand prediction, churn prediction, stock or price prediction[2][3]  \n  - Weather and event forecasting (e.g., tornado prediction)[1][3]\n- **Risk assessment & fraud detection**:  \n  - Credit scoring, default risk prediction[2]  \n  - Transaction fraud detection and anomaly scoring with labeled fraud cases[1][2]\n- **Recommendation & personalization** (when treated as supervised prediction of click/engagement):  \n  - Product, movie, or content recommendations based on past user behavior[2]\n- **Healthcare and diagnostics**:  \n  - Disease diagnosis from symptoms, lab values, or images[1][2]  \n  - Outcome prediction (e.g., risk of readmission)\n- **Automation & control** (when targets are available):  \n  - Quality inspection from images in manufacturing[2]  \n  - Some autonomous driving components (lane detection, object detection, sign recognition)[1][2]\n\n---\n\n## 2. Unsupervised learning\n\n**Idea:** Discover **patterns or structure** in **unlabeled data** (no explicit targets).[2][3][8]\n\nMain families include **clustering**, **dimensionality reduction**, and **association rule learning**.[2][3]\n\n**Common applications**\n\n- **Clustering / segmentation**[2][3]  \n  - Customer segmentation (group customers by behavior for marketing)  \n  - Image or document clustering (organizing data into similar groups)  \n  - Biological data clustering (e.g., gene expression patterns)\n- **Anomaly / outlier detection**  \n  - Detect unusual network traffic, equipment sensor readings, or financial transactions[2]  \n  - Industrial fault detection\n- **Dimensionality reduction & visualization**  \n  - Reduce high‑dimensional data for visualization or as preprocessing (PCA, etc.)[2][3]  \n  - Feature compression before supervised models or for noise reduction\n- **Association rule mining**  \n  - Market basket analysis (which products are frequently bought together)[2]  \n  - Recommendation support and cross‑selling (e.g., “customers who bought X also bought Y”)\n- **Data exploration & preprocessing**  \n  - Discover latent structure to guide further analysis or model building[2]  \n\nUnsupervised learning is often used upstream of other ML methods, e.g., to cluster data, then train supervised models per cluster.[2][3]\n\n---\n\n## 3. Reinforcement learning (RL)\n\n**Idea:** An **agent** learns to make sequential decisions by interacting with an environment, receiving **rewards or penalties** and improving its policy to maximize cumulative reward over time.[3][4][8]\n\nUnlike supervised learning, there are no labeled “correct actions”; feedback is through rewards.[3][4]\n\n**Common applications**\n\n- **Game playing and strategy**  \n  - Agents that learn to play board games or video games at or beyond human level[4]  \n  - Multi‑agent strategies and simulations\n- **Robotics and control**  \n  - Robot navigation, manipulation, and path planning[4]  \n  - Drones, warehouse robots, and industrial automation where robots learn control policies\n- **Autonomous driving & decision making**  \n  - High‑level driving policies (lane changes, merging, planning maneuvers)[1][4]  \n  - Traffic signal control and route optimization\n- **Recommender systems (sequential)**  \n  - Adaptive recommendation policies that consider long‑term user engagement or retention (RL bandits and full RL)  \n- **Operations research & resource allocation**  \n  - Dynamic pricing, inventory control, and allocation problems where actions influence future states and rewards\n\nRL is used when decisions affect future states and we optimize for long‑term, not just immediate, outcomes.[4]\n\n---\n\n## 4. Semi‑supervised learning\n\n**Idea:** Combine a **small amount of labeled data** with a **large amount of unlabeled data** to improve performance, especially when labeling is expensive.[1][2][3][8]\n\nFor example, the model may first find clusters in unlabeled data and then use the few labeled examples to label clusters.[1][2]\n\n**Common applications**\n\n- **Image and video classification**  \n  - Large image or video collections where only a small subset is labeled[1][2]  \n- **Natural language tasks**  \n  - Text classification or information extraction where annotation is costly  \n- **Medical and scientific data**  \n  - Domains where labels require expert annotation (radiology, pathology, etc.)\n- **Web‑scale applications**  \n  - User behavior logs with a few labeled outcomes and many unlabeled events\n\nSemi‑supervised learning is particularly common in large‑scale industrial settings where unlabeled data is abundant but labels are sparse.[1][2][3]\n\n---\n\n## 5. Self‑supervised learning (often grouped with unsupervised)\n\n**Idea:** Create **supervision from the data itself** by defining a “pretext” task (e.g., predict missing parts of input, next token in text) and train on massive unlabeled datasets.[1][8][9] Labels are generated automatically from the data.\n\nIt is often considered a subcategory of unsupervised or a separate fifth category alongside the others.[1][8][9]\n\n**Common applications**\n\n- **Representation learning for images and video**  \n  - Learn general visual features by predicting missing patches or rotations, then fine‑tune on downstream tasks (classification, detection)\n- **Large language models (LLMs)**  \n  - Train models to predict the next word/token given previous text, enabling capabilities in generation, question answering, and summarization[1]\n- **Audio and speech**  \n  - Learn representations by predicting masked segments in audio signals\n- **Pretraining for downstream supervised tasks**  \n  - Use self‑supervised pretraining on large unlabeled corpora, then fine‑tune with smaller labeled datasets in any domain\n\n---\n\n### Quick mapping: category → typical applications\n\n| Category                    | Core idea                          | Typical applications |\n|----------------------------|------------------------------------|----------------------|\n| **Supervised**             | Learn from labeled input–output pairs | Classification, regression, forecasting, fraud detection, diagnosis, recommendations, image/speech recognition[1][2][3] |\n| **Unsupervised**           | Find structure in unlabeled data      | Clustering, segmentation, anomaly detection, dimensionality reduction, association rules, exploration[2][3] |\n| **Reinforcement**          | Learn by trial‑and‑error with rewards | Robotics, games, autonomous control, sequential recommendations, resource allocation[3][4] |\n| **Semi‑supervised**        | Small labeled + large unlabeled data  | Image/text classification with few labels, medical/scientific data, web‑scale tasks[1][2][3] |\n| **Self‑supervised**        | Labels generated from the data itself | Pretraining for LLMs, vision/audio representations, large‑scale foundation models[1][8][9] |\n\nIf you’d like, I can follow up with:  \n- concrete algorithm examples per category (e.g., Random Forest, k‑Means, Q‑learning), or  \n- guidance on which type to use for a specific problem you have in mind.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896021,
      "model": "sonar-pro",
      "citations": [
        "https://www.ibm.com/think/topics/machine-learning-types",
        "https://www.geeksforgeeks.org/machine-learning/types-of-machine-learning/",
        "https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html",
        "https://help.pecan.ai/en/articles/6549972-three-types-of-machine-learning",
        "https://www.netcomlearning.com/blog/types-of-machine-learning",
        "https://www.youtube.com/watch?v=HI5muXcNngQ",
        "https://www.coursera.org/articles/types-of-machine-learning",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://lumenalta.com/insights/5-types-of-machine-learning"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "Types of Machine Learning | IBM",
          "url": "https://www.ibm.com/think/topics/machine-learning-types",
          "date": "2023-12-20",
          "last_updated": "2026-03-31",
          "snippet": "Machine learning algorithms fall into five broad categories: supervised learning, unsupervised learning, semi-supervised learning, self-supervised and ...",
          "source": "web"
        },
        {
          "title": "Types of Machine Learning - GeeksforGeeks",
          "url": "https://www.geeksforgeeks.org/machine-learning/types-of-machine-learning/",
          "date": "2026-01-19",
          "last_updated": "2026-05-19",
          "snippet": "Types of Machine Learning · 1. Supervised Machine Learning · 2. Unsupervised Machine Learning · 3. Reinforcement Learning. Reinforcement ...",
          "source": "web"
        },
        {
          "title": "A guide to the types of machine learning algorithms | SAS UK",
          "url": "https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html",
          "date": "2023-03-27",
          "last_updated": "2026-05-14",
          "snippet": "There are four types of machine learning algorithms: supervised, semi-supervised, unsupervised and reinforcement.",
          "source": "web"
        },
        {
          "title": "Three types of machine learning - Pecan Help Center",
          "url": "https://help.pecan.ai/en/articles/6549972-three-types-of-machine-learning",
          "date": null,
          "last_updated": "2025-09-03",
          "snippet": "Machine learning can be divided into three paradigms: supervised learning, unsupervised learning, and reinforcement learning.",
          "source": "web"
        },
        {
          "title": "Types of Machine Learning: Supervised, Unsupervised & More",
          "url": "https://www.netcomlearning.com/blog/types-of-machine-learning",
          "date": "2026-03-20",
          "last_updated": null,
          "snippet": "The four primary machine learning types are supervised learning, unsupervised learning, semi-supervised learning, and reinforcement learning. Q.",
          "source": "web"
        },
        {
          "title": "Types of Machine Learning Models - YouTube",
          "url": "https://www.youtube.com/watch?v=HI5muXcNngQ",
          "date": "2025-03-26",
          "last_updated": "2026-03-26",
          "snippet": "Types of Machine Learning Models | How Machine Learning Models REALLY Work | ML Models | Edureka · Comments. 10. Add a comment... 51:31. Go to ...",
          "source": "web"
        },
        {
          "title": "3 Types of Machine Learning You Should Know | Coursera",
          "url": "https://www.coursera.org/articles/types-of-machine-learning",
          "date": "2025-12-31",
          "last_updated": "2026-05-18",
          "snippet": "While machine learning models can learn through various methods, the most common types include supervised, unsupervised, and reinforcement ...",
          "source": "web"
        },
        {
          "title": "Machine learning - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Machine_learning",
          "date": "2003-05-25",
          "last_updated": "2026-05-22",
          "snippet": "4.1 Supervised learning · 4.2 Unsupervised learning. 4.2.1 Dimensionality reduction · 4.3 Semi-supervised learning · 4.4 Reinforcement learning · 4.5 Other types.",
          "source": "web"
        },
        {
          "title": "5 types of machine learning - Lumenalta",
          "url": "https://lumenalta.com/insights/5-types-of-machine-learning",
          "date": "2024-12-10",
          "last_updated": "2026-05-12",
          "snippet": "The 5 types of machine learning are supervised, unsupervised, semi-supervised, self-supervised, and reinforcement learning.",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1769,
        "cost": {
          "input_tokens_cost": 6e-05,
          "output_tokens_cost": 0.02653,
          "total_cost": 0.03259,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 20,
        "total_tokens": 1789,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Info>
  Date filters must use `%m/%d/%Y` format (e.g., `"3/1/2025"`). `search_recency_filter` cannot be combined with other date filters. Use `hour` for real-time data such as breaking news or live events.
</Info>

## Location Filters

Customize search results based on geographic location using `user_location` within `web_search_options`.

**Key parameters:**

* `country`: Two-letter ISO 3166 country code (required with coordinates)
* `region`: State, province, or administrative division
* `city`: City name
* `latitude`: Latitude coordinate (-90 to 90)
* `longitude`: Longitude coordinate (-180 to 180)

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Full location specification (recommended)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Explain what a Yelp business listing contains and how Yelp ranks local search results."}],
    web_search_options={
        "user_location": {
            "country": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    }
)

# Country code only
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Summarize how the Financial Times and The Economist differ in their approach to covering global business news."}],
    web_search_options={
        "user_location": {
            "country": "US"
        }
    }
)
```

<AccordionGroup>
  <Accordion title="Response — Explain what a Yelp business listing contains and how Yelp ranks local search results.">
    ```json theme={null}
    {
      "id": "b0ef8be4-c355-485e-bd7f-684fbe021b03",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "A Yelp business listing is a free business page that includes core contact details, location, hours, categories, photos, descriptions, and customer reviews, and once claimed it can expose additional business-management features.[3][5][1] Yelp’s local search results are driven by the user’s search terms, the business category or keyword relevance, and the geographic area or city tied to the listing; Yelp also states that submitted business additions are reviewed by moderators before appearing in search results.[3][7]\n\nA Yelp business listing commonly contains:\n- **Business name, address, and phone number (NAP)**, plus a website link.[1]\n- **Hours of operation** and, where applicable, phone or store hours.[1]\n- **Categories** that describe what the business does.[1]\n- **Photos/images** showing the location, products, services, interior, or exterior.[1]\n- **Owner/manager information**, a **history** section, and **specialties** or service descriptions.[1]\n- **Reviews and ratings**, which are a major reason users visit Yelp.[1]\n- Access to additional features after claiming the page, which Yelp says can total **20+ features** for promotion and reputation management.[3]\n\nHow Yelp ranks or surfaces local results:\n- Yelp says businesses can be found in **organic search results** when users search by **categories, keywords, business name, service area, or city**.[3]\n- BrightLocal notes that when Yelp finds a match from a search, it may return either the listing or a list with the **most likely match at the top**.[2]\n- Yelp Support says new business additions must be **evaluated by moderators** before they appear in search results, and that process usually takes **two days or less**.[7]\n\nWhat the available sources do *not* fully specify is a detailed ranking formula such as how much weight Yelp gives to review count, review quality, proximity, or paid advertising. From the sources here, the safest explanation is that Yelp’s local visibility is primarily based on **query relevance, location relevance, and listing completeness/verification**, with moderation applied before newly added businesses appear.[3][2][7]\n\n",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896017,
      "model": "sonar-pro",
      "citations": [
        "https://www.advicelocal.com/blog/yelp-business-listings/",
        "https://www.brightlocal.com/learn/how-to-add-or-claim-a-yelp-business-listing/",
        "https://business.yelp.com/products/business-page/",
        "https://www.youtube.com/watch?v=4DGpKPCyd6M",
        "https://business.yelp.com",
        "https://business.yelp.com/resources/videos/how-to-add-or-claim-your-yelp-business-page/?domain=local-business",
        "https://www.yelp-support.com/article/How-do-I-add-a-business-to-Yelp?l=en_US",
        "https://nowspeed.com/blog/yelp-guide/"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "Everything You Need to Know About Yelp Business Listings",
          "url": "https://www.advicelocal.com/blog/yelp-business-listings/",
          "date": "2019-04-23",
          "last_updated": "2026-04-30",
          "snippet": "Learn how to claim or create a business listing on Yelp. Additonally, dig into Yelp's other features such as the Yelp Q&A and activity dashboard.",
          "source": "web"
        },
        {
          "title": "How to Add or Claim a Yelp Business Listing - BrightLocal",
          "url": "https://www.brightlocal.com/learn/how-to-add-or-claim-a-yelp-business-listing/",
          "date": "2022-01-06",
          "last_updated": "2026-05-25",
          "snippet": "Read on to learn how you can easily add your business to Yelp, as well as to learn how to claim or verify an existing listing.",
          "source": "web"
        },
        {
          "title": "Why Claim Your Business Page on Yelp",
          "url": "https://business.yelp.com/products/business-page/",
          "date": "2026-05-12",
          "last_updated": "2026-05-27",
          "snippet": "Claiming your page gives you access to 20+ features that help you promote your services and build your reputation. Verify my free listing. Benefits of claiming ...",
          "source": "web"
        },
        {
          "title": "How to Access and Update your Yelp Listing - YouTube",
          "url": "https://www.youtube.com/watch?v=4DGpKPCyd6M",
          "date": "2024-07-17",
          "last_updated": "2025-08-09",
          "snippet": "... content and how to answer yelp reviews. I even show how to change the name of your business if it is incorrect. Referenced Video Links: Yelp ...",
          "source": "web"
        },
        {
          "title": "Yelp for Business: Free and paid advertising solutions",
          "url": "https://business.yelp.com",
          "date": "2026-05-26",
          "last_updated": "2026-05-26",
          "snippet": "It's free to be on Yelp. Simply search for your business below. Can't find it? Add your business name, and we'll help you claim your Yelp Page.",
          "source": "web"
        },
        {
          "title": "How to add or claim your Yelp Business Page I Watch Video",
          "url": "https://business.yelp.com/resources/videos/how-to-add-or-claim-your-yelp-business-page/?domain=local-business",
          "date": "2024-10-30",
          "last_updated": "2026-02-28",
          "snippet": "The first step in marketing your business on Yelp is adding or claiming your free Yelp Business Page. This video will walk you through the easy process.",
          "source": "web"
        },
        {
          "title": "How do I add a business to Yelp? | Support Center",
          "url": "https://www.yelp-support.com/article/How-do-I-add-a-business-to-Yelp?l=en_US",
          "date": "2004-01-01",
          "last_updated": "2026-02-25",
          "snippet": "Any business additions must first be evaluated by our moderators before they appear in search results. This process typically takes two days or less.",
          "source": "web"
        },
        {
          "title": "Should You Have A Listing For Your Business? A Yelp Guide.",
          "url": "https://nowspeed.com/blog/yelp-guide/",
          "date": "2024-09-12",
          "last_updated": "2026-05-24",
          "snippet": "Tip #1: Claim your business listing. Yelp users can add your business, and you can't block Yelp from listing your business, so it's best to claim it right away ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 443,
        "cost": {
          "input_tokens_cost": 5e-05,
          "output_tokens_cost": 0.00664,
          "total_cost": 0.0127,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 17,
        "total_tokens": 460,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — Summarize how the Financial Times and The Economist differ in their approach to coverin...">
    ```json theme={null}
    {
      "id": "9ad25773-905c-4f22-b3d1-e202753c126d",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "The **Financial Times** focuses on timely, data‑rich reporting and market-relevant analysis for practitioners, while **The Economist** offers weekly, highly opinionated, thematic essays that interpret global business within a broad political and social context.[1][3][5]\n\nKey differences in their approach to global business coverage:\n\n1. **Format and frequency**\n\n- **Financial Times (FT)**  \n  - **Daily newspaper** (plus live digital updates), designed to provide *real‑time* coverage of markets, deals, corporate moves, and policy developments.[1][3]  \n  - Emphasizes being a running log of what is happening now: market moves, earnings, M&A, regulatory changes, etc.[1][3]\n\n- **The Economist**  \n  - **Weekly magazine**, not a daily news source.[1][3]  \n  - Assumes readers already know the basic news and focuses on *explaining significance, causes, and consequences* with more distance from the daily news cycle.[1][3]\n\n2. **Core editorial style**\n\n- **FT**  \n  - Written in a relatively **straight news** style, closer to a traditional newspaper like the Wall Street Journal: concise articles, heavy use of data, clear separation of news and opinion.[1]  \n  - Reputation for being **“very concise”**, “rarely misstated facts,” and intellectually demanding, assuming readers are already literate in finance, economics, and markets.[1]  \n  - Opinion exists (e.g., Martin Wolf), but is structurally separated from the news pages.[2]\n\n- **The Economist**  \n  - Uses a **distinctive, unified editorial voice**, with unsigned articles that read more like essays than news reports.  \n  - Frequently described as **“strongly opinionated”** journalism, taking clear lines on economic and political questions rather than just describing events.[2]  \n  - Articles synthesize reporting from many places into narrative arguments: “here’s what this trend means and what should be done,” rather than “here’s what happened yesterday.”[2]\n\n3. **News vs. analysis emphasis**\n\n- **FT**  \n  - **News-led**: “extensive news, comment and data analysis for the global business community.”[3]  \n  - Primary value is *speed + depth*: timely coverage for professionals who need up‑to‑date information for decisions (investors, executives, policymakers).[1][3]  \n  - Analysis and commentary are present but usually tied tightly to specific events, markets, or companies (e.g., central bank decisions, earnings, bond markets).[1]\n\n- **The Economist**  \n  - **Analysis-led**: weekly issues scan many countries and sectors but focus on *interpretation*—what trends mean globally and ideologically.[1][3]  \n  - Often steps back to connect business news to broader themes: democracy, regulation, technology, demography, environment, etc.[1][3]  \n  - Less about “yesterday’s stock move,” more about “the long‑term direction of capitalism, trade, or regulation.”\n\n4. **Audience and assumed knowledge**\n\n- **FT**  \n  - Aimed squarely at the **global business and financial community** (investors, bankers, corporate executives, policymakers).[3]  \n  - Assumes substantial prior knowledge of **finance, accounting, economics, politics, and legal frameworks**, and does not spend much space re‑explaining basics.[1]  \n  - Coverage is very useful *transactionally* (e.g., for market participants).\n\n- **The Economist**  \n  - Aimed at a **broader elite readership**: professionals, policymakers, academics, and general readers with strong interest in global affairs.  \n  - Still assumes an educated reader, but covers a wider array of topics—science, society, culture—alongside business and economics.[3]  \n  - Provides context that can help non‑specialists understand complex business and economic issues, but in a conceptual, not “how to trade this” way.\n\n5. **Geographic and ideological orientation**\n\n- **FT**  \n  - Historically **London‑based** with a strong **European and global markets** focus.[1][5]  \n  - Editorial stance centered on **economic liberalism**—supportive of free trade and free markets—but day‑to‑day reporting strives for neutrality and tends to be more skeptical and nuanced on US coverage than many US outlets.[2][5]\n\n- **The Economist**  \n  - Also UK‑based but explicitly **internationalist**, covering “so many different countries in each issue.”[1]  \n  - Openly advocates a **market‑friendly, socially liberal, globalist** worldview, and its coverage frames business news within that ideological lens.[2]  \n\n6. **Use-case for a reader interested in global business**\n\n- Use **Financial Times** if you want:\n  - Up‑to‑the‑minute **global business and financial news**.  \n  - Detailed coverage of markets, deals, corporate results, and policy moves.  \n  - Concise, fact‑driven articles to inform investment or business decisions.[1][3]\n\n- Use **The Economist** if you want:\n  - Weekly, **big‑picture analysis** of global business trends.  \n  - Strongly argued pieces that connect business to politics, society, and long‑term structural forces.[2][3]  \n  - A coherent worldview and interpretive framework rather than continuous news flow.[2]\n\nIn short: the FT is a **daily global business newspaper** optimized for speed and precision in reporting, while The Economist is a **weekly analytical magazine** that uses business news as raw material for broader, explicitly opinionated essays about the global economy and world affairs.[1][2][3][5]",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896032,
      "model": "sonar-pro",
      "citations": [
        "https://www.wallstreetoasis.com/forum/investment-banking/wsj-vs-economist-vs-ft-vs-businessweek",
        "https://news.ycombinator.com/item?id=33799353",
        "https://libguides.marist.edu/c.php?g=87335&p=563019",
        "https://voices.media/the-primacy-of-personality-led-newsletters-at-the-economist-and-financial-times/",
        "https://en.wikipedia.org/wiki/Financial_Times"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "WSJ vs. Economist vs. FT vs. Businessweek - Wall Street Oasis",
          "url": "https://www.wallstreetoasis.com/forum/investment-banking/wsj-vs-economist-vs-ft-vs-businessweek",
          "date": "2013-07-26",
          "last_updated": "2025-07-24",
          "snippet": "The FT is a paper that is written in a style similar to the WSJ with real time updates and coverage of economics, business, politics, and among ...",
          "source": "web"
        },
        {
          "title": "Ask HN: Alternatives to The Economist? - Hacker News",
          "url": "https://news.ycombinator.com/item?id=33799353",
          "date": "2022-11-30",
          "last_updated": "2026-03-06",
          "snippet": "It's the same market-based, socially progressive, pragmatic international strongly opinionated journalism it's always been.",
          "source": "web"
        },
        {
          "title": "Newspapers: Business and Economic News - LibGuides",
          "url": "https://libguides.marist.edu/c.php?g=87335&p=563019",
          "date": "2026-05-11",
          "last_updated": "2026-03-19",
          "snippet": "Provides extensive news, comment and data analysis for the global business community. Financial Times Online. Provides extensive news, comment ...",
          "source": "web"
        },
        {
          "title": "How The Economist and Financial Times manage personality-driven ...",
          "url": "https://voices.media/the-primacy-of-personality-led-newsletters-at-the-economist-and-financial-times/",
          "date": "2025-09-02",
          "last_updated": null,
          "snippet": "So even when a newspaper or magazine tries its very hardest to be objective, that news has to be delivered with a certain voice or personality.",
          "source": "web"
        },
        {
          "title": "Financial Times - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Financial_Times",
          "date": "2002-10-25",
          "last_updated": "2026-05-22",
          "snippet": "The editorial stance of the Financial Times centres on economic liberalism, particularly advocacy of free trade and free markets. Since its founding, it has ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1188,
        "cost": {
          "input_tokens_cost": 6e-05,
          "output_tokens_cost": 0.01782,
          "total_cost": 0.02388,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 21,
        "total_tokens": 1209,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Tip>
  For best accuracy, provide as many location fields as possible. City and region significantly improve location precision.
</Tip>

## Language Filter

Filter search results by language using ISO 639-1 language codes.

**Key parameters:**

* `search_language_filter`: Array of 2-letter language codes (max 10)

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Single language
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Explain how a transformer language model is trained: pretraining objective, supervised fine-tuning, and RLHF."}],
    search_language_filter=["en"]
)

# Multiple languages
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Explain how mortgage interest rates are set, including the role of the 10-year US Treasury yield and lender spreads."}],
    search_language_filter=["en", "fr", "de"]
)
```

<AccordionGroup>
  <Accordion title="Response — Explain how a transformer language model is trained: pretraining objective, supervised ...">
    ```json theme={null}
    {
      "id": "2df1cfe5-1231-443b-9f27-d1ef4530da8e",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "A transformer language model is typically trained in three main stages: **unsupervised pretraining** with a language-modeling objective, **supervised fine‑tuning** on curated labeled data, and **RLHF (Reinforcement Learning from Human Feedback)** to better align behavior with human preferences.\n\n---\n\n## 1. Pretraining Objective (Unsupervised / Self‑Supervised)\n\n**Goal:** Learn general language representations and world knowledge from massive unlabeled text.\n\n### Core idea\n\nYou start with a randomly initialized transformer (decoder-only like GPT, or encoder(-decoder) like BERT) and train it on raw text using a **self‑supervised objective**—no human labels beyond the text itself.\n\nTwo canonical objectives:\n\n1. **Autoregressive language modeling (GPT‑style)**  \n   The model learns to predict the next token given previous tokens.  \n   Formally, given a token sequence \\(u_1, \\dots, u_n\\), maximize:\n   \\[\n   \\sum_i \\log P(u_i \\mid u_{i-k}, \\dots, u_{i-1}; \\Theta)\n   \\]\n   where \\(k\\) is the context window and \\(\\Theta\\) are model parameters.[2]  \n   This is implemented with a **Transformer decoder**: masked self‑attention so each position attends only to earlier tokens, then a softmax over the vocabulary to predict the next token.[2][4]\n\n2. **Masked language modeling (BERT‑style)**  \n   Some input tokens are replaced with a special [MASK] token (or corrupted), and the model predicts the original tokens from both left and right context.[3]  \n   This allows learning **bidirectional** representations, instead of strictly left‑to‑right prediction.[3]\n\nAdditional pretraining objectives (especially for BERT-like models):\n\n- **Next Sentence Prediction (NSP):** Predict whether sentence B follows sentence A in the original text.[3]  \n- Variants (e.g., sentence order prediction) or combined objectives, but modern practice often de-emphasizes NSP because it sometimes hurts performance.[1][3]\n\n### Why pretraining?\n\n- Uses huge unlabeled corpora to learn rich **language and world knowledge**.[1][2]  \n- Produces a **task-agnostic** model that can be adapted to many downstream tasks.[1][2][3]  \n- Reduces labeled data requirements and improves generalization.[1][2]\n\nThe result is a **base language model checkpoint** that is not yet aligned but is broadly capable at modeling text.\n\n---\n\n## 2. Supervised Fine‑Tuning (Instruction / Task Tuning)\n\n**Goal:** Specialize the pretrained model to follow instructions and perform specific tasks using labeled data.\n\n### Basic supervised fine‑tuning\n\nYou now have a pretrained transformer. You adapt it on a **labeled dataset** where each example includes an input (prompt) and an output (target), and you train it with standard supervised learning.\n\n- Classical setting (e.g., GPT‑1 paper):  \n  Given labeled pairs \\((x, y)\\), you pass \\(x\\) through the pretrained model, take one (or more) hidden states (e.g., the final token), feed them into an added linear layer, and train to predict the label \\(y\\), maximizing:\n  \\[\n  \\sum_{(x,y)} \\log P(y \\mid x_1, \\dots, x_m)\n  \\][2]\n\n- For generation-style fine‑tuning (instruction-tuned LLMs):  \n  You treat the **prompt + target answer** as a single sequence and train with **teacher forcing**: the model’s objective is to maximize the likelihood of each target token given the prompt and previous target tokens (i.e., next-token prediction, but only on the answer region).  \n  This is still just **cross‑entropy loss** between the model’s predicted distribution and the reference output tokens.\n\nIn both cases:\n\n- You usually **start from the pretrained parameters** and **update all or most weights** on this supervised objective.[1][2][3]  \n- Sometimes you also keep a small language modeling term as an auxiliary objective during fine‑tuning to improve generalization.[2]\n\n### Instruction tuning vs task-specific fine‑tuning\n\n- Traditional: fine‑tune separate models for tasks like classification, QA, NLI, etc., often with task-specific heads.[2][3]  \n- Modern LLMs: fine‑tune on a **mixture of instruction‑following examples** across many tasks (e.g., “Summarize…”, “Translate…”, “Write code that…”) so the model learns the general pattern “read an instruction, produce an appropriate completion” using natural language as the interface.\n\nThe result is a **supervised fine‑tuned (SFT) model** that can follow instructions and perform tasks, but may still:\n- Over-imitate biases in the data,\n- Produce unsafe or unhelpful responses,\n- Optimize for likelihood of training text, not human preference.\n\n---\n\n## 3. RLHF (Reinforcement Learning from Human Feedback)\n\n**Goal:** Further align the model’s behavior with *human preferences* (helpfulness, harmlessness, honesty, style) rather than pure likelihood of text.\n\nRLHF is typically a **three‑step process** built on top of the SFT model:\n\n### Step 1: Supervised Fine‑Tuning (already done)\n\n- The SFT model is used as the starting policy for RLHF.  \n- It already responds somewhat sensibly to prompts.\n\n### Step 2: Train a Reward Model (RM) from Human Preferences\n\nYou collect **preference data**:\n\n1. Show human labelers a prompt and several candidate responses from the SFT model (e.g., 2–4 alternatives).\n2. Ask them to **rank or pick the better response** based on guidelines (safety, helpfulness, factuality, etc.).\n3. You get data of the form: for the *same* prompt, response A is preferred over response B.\n\nYou then train a **reward model**:\n\n- Input: prompt + response.  \n- Output: scalar reward \\(r_\\phi(\\text{prompt}, \\text{response})\\).  \n- Training objective: make the reward model assign a higher score to human‑preferred responses than to rejected ones, usually with a **pairwise logistic loss**.\n\nThis converts human judgments into a differentiable reward function approximated by a neural network.\n\n### Step 3: RL Optimization of the Policy Model\n\nNow you treat the language model as a **policy** in an RL setup:\n\n- State: the prompt and the partial response generated so far.\n- Action: the next token.\n- Episode: generating a full response to a prompt.\n- Reward: the reward model’s scalar score for the completed response (possibly plus other penalties, like length penalties or rule violations).\n\nYou perform RL (commonly **PPO – Proximal Policy Optimization**) to:\n\n- Maximize expected reward from the reward model,\n- While adding a **KL-divergence penalty** to keep the updated policy close to the original SFT model (to avoid severe degradation or mode collapse).\n\nConceptually:\n\n1. Sample prompts.\n2. Generate responses with the current policy model.\n3. Score each response using the reward model.\n4. Use PPO to update the policy parameters toward higher‑reward behavior, with a KL penalty to the SFT policy.\n\nThe effect:\n\n- The model shifts away from merely “what text is likely” towards “what text humans *prefer* given these instructions and safety guidelines.”\n- It typically becomes more:\n  - **Helpful** (better answers, more on-topic),\n  - **Harmless** (less toxic/unsafe content),\n  - **Honest** (more likely to express uncertainty, follow instructions about constraints).\n\n---\n\n## Putting It All Together\n\nIn modern LLM training, the pipeline is roughly:\n\n1. **Pretraining:**  \n   - Objective: next-token prediction (autoregressive LM) or masked LM on massive unlabeled text.  \n   - Outcome: general-purpose language model with broad knowledge but no task specialization or alignment.\n\n2. **Supervised Fine‑Tuning (SFT / Instruction Tuning):**  \n   - Objective: cross‑entropy on curated prompt–response pairs, often multi‑task instructions.  \n   - Outcome: instruction-following model that imitates provided examples.\n\n3. **RLHF:**  \n   - Objective: maximize reward from a human‑trained reward model under an RL algorithm (e.g., PPO) with a KL constraint to SFT.  \n   - Outcome: aligned assistant model that better matches human preferences for helpfulness, safety, and style.\n\nIf you want, I can also sketch the math for the RLHF update (with PPO and KL penalty) or walk through a concrete example prompt and show how each stage would handle it differently.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896038,
      "model": "sonar-pro",
      "citations": [
        "https://taoyds.github.io/assets/courses/COMP3361-lec11.pdf",
        "https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf",
        "https://aclanthology.org/N19-1423.pdf",
        "https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html",
        "https://etc.cuit.columbia.edu/news/basics-language-modeling-transformers-gpt",
        "https://www.lesswrong.com/posts/8F4dXYriqbsom46x5/pretraining-language-models-with-human-preferences",
        "https://mbrenndoerfer.com/writing/gpt-1-generative-pretraining-language-understanding"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "[PDF] Lecture 11: Pre-training and large language models (LLMs)",
          "url": "https://taoyds.github.io/assets/courses/COMP3361-lec11.pdf",
          "date": null,
          "last_updated": "2025-03-06",
          "snippet": "(Devlin et al, 2019): BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. • Two new pre-training objectives: • Masked language ...",
          "source": "web"
        },
        {
          "title": "[PDF] Improving Language Understanding by Generative Pre-Training",
          "url": "https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf",
          "date": null,
          "last_updated": "2026-05-25",
          "snippet": "First, we use a language modeling objective on the unlabeled data to learn the initial parameters of a neural network model. Subsequently, we adapt these ...",
          "source": "web"
        },
        {
          "title": "[PDF] BERT: Pre-training of Deep Bidirectional Transformers for Language ...",
          "url": "https://aclanthology.org/N19-1423.pdf",
          "date": null,
          "last_updated": "2026-05-16",
          "snippet": "The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked. Page 2 ...",
          "source": "web"
        },
        {
          "title": "11.9. Large-Scale Pretraining with Transformers",
          "url": "https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html",
          "date": null,
          "last_updated": "2026-03-05",
          "snippet": "Using language modeling as the training objective, the GPT (generative pre-training) model chooses a Transformer decoder as its backbone (Radford et al., 2018).",
          "source": "web"
        },
        {
          "title": "The Basics of Language Modeling with Transformers: GPT",
          "url": "https://etc.cuit.columbia.edu/news/basics-language-modeling-transformers-gpt",
          "date": "2021-11-14",
          "last_updated": "2025-07-19",
          "snippet": "It achieved great success in its time by pre-training the model in an unsupervised way on a large corpus, and then fine tuning the model for ...",
          "source": "web"
        },
        {
          "title": "Pretraining Language Models with Human Preferences - LessWrong",
          "url": "https://www.lesswrong.com/posts/8F4dXYriqbsom46x5/pretraining-language-models-with-human-preferences",
          "date": "2023-02-21",
          "last_updated": "2026-05-21",
          "snippet": "There are other objectives we can use that train a model to imitate only certain aspects of the training data while avoiding others. Consider a ...",
          "source": "web"
        },
        {
          "title": "GPT-1: The Origin of Generative Pre-Training for Language ...",
          "url": "https://mbrenndoerfer.com/writing/gpt-1-generative-pretraining-language-understanding",
          "date": "2025-07-20",
          "last_updated": "2025-12-23",
          "snippet": "Explore the GPT-1 architecture, pre-training objective, fine-tuning approach, and transfer learning results that established the foundation ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1848,
        "cost": {
          "input_tokens_cost": 7e-05,
          "output_tokens_cost": 0.02772,
          "total_cost": 0.03379,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 24,
        "total_tokens": 1872,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — Explain how mortgage interest rates are set, including the role of the 10-year US Treas...">
    ```json theme={null}
    {
      "id": "dae6ef2c-852a-400d-b703-75f9c52a5041",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "Mortgage interest rates are set in two main layers: first, markets determine a **baseline level** using benchmarks like the **10‑year U.S. Treasury yield** and mortgage‑backed securities (MBS); then, individual lenders add **spreads and loan‑/borrower‑specific adjustments** to arrive at the actual rate you pay.[3][4][6]\n\nBelow is how the pieces fit together.\n\n---\n\n## 1. Market benchmark: 10‑year Treasury & MBS\n\nMost U.S. **30‑year fixed mortgage rates tend to move closely with the 10‑year U.S. Treasury yield**.[1][3][4][6]\n\n- 30‑year mortgages are long‑term loans, but they rarely last 30 full years because people move, sell, or refinance; statistically, their *average life* is closer to 7–10 years.[4]  \n- Because of that, lenders and investors use the **10‑year Treasury note** as a practical benchmark for pricing 30‑year mortgages.[4]\n\nAccording to Fannie Mae and other industry sources, **mortgage rates are determined by adding a spread to the 10‑year Treasury note**.[4][6] Bankrate notes that **mortgage rates typically move in lockstep with 10‑year Treasury yields**: when the yield rises, mortgage rates rise to maintain lender spreads, and vice versa.[3]\n\nTwo key market instruments matter:\n\n- **10‑year Treasury notes (T‑notes)**  \n  - These are low‑risk U.S. government bonds.  \n  - Their yields reflect **expectations for future short‑term rates, inflation, and growth**, shaped by Federal Reserve policy, economic data, and geopolitical risk.[1][3][4]  \n  - When investors seek safety (e.g., in uncertainty), they buy more Treasuries, pushing prices up and **yields down**, which typically pulls **mortgage rates down** as well.[3]\n\n- **Mortgage‑backed securities (MBS)**  \n  - Lenders often sell mortgages into MBS, which are bought by investors.[3][4]  \n  - When **MBS prices rise**, the yield investors demand on MBS falls, which supports **lower mortgage rates**; when MBS prices fall, mortgage rates tend to rise.[3]  \n  - Lenders “usually add a margin to the MBS rate to come up with the rate they charge for a mortgage loan.”[3]\n\nIn practice, lenders watch both **10‑year Treasury yields and MBS pricing** to set their base mortgage pricing each day.[3][4]\n\n---\n\n## 2. The “spread” over the 10‑year Treasury\n\nThe difference between the **30‑year fixed mortgage rate** and the **10‑year Treasury yield** is called the **spread**.[3][4][6]\n\n- Bankrate notes this spread is **usually about 2 percentage points** (e.g., 10‑year yield 4% → mortgage around 6%).[3]  \n- During stressed periods (like late in the pandemic), the spread widened to about **3 percentage points**, reflecting higher risk and market dislocation.[3]\n\nThe Federal Savings Bank and Fannie Mae break this spread into components:[4][6]\n\n### a) Secondary spread (MBS vs. 10‑year Treasury)\n\n- This is the difference between **MBS yields** and **10‑year Treasury yields**.[4]  \n- It exists because MBS are **riskier than Treasuries**:  \n  - **Prepayment risk**: borrowers can refinance or sell early, shortening or changing the cash flows.  \n  - **Credit risk**: borrowers can default, even on agency‑guaranteed loans there are guaranty structures and costs.[4]  \n- Investors demand a **higher yield** on MBS than on near‑risk‑free Treasuries, so MBS rates are above the 10‑year Treasury yield.[4]\n\n### b) Primary‑secondary spread (borrower rate vs. MBS)\n\n- This is the gap between the **rate offered to the borrower** and the **MBS yield**.[4]  \n- It includes:  \n  - **Origination costs** (staff, underwriting, overhead)  \n  - **Servicing fees** (collecting payments, managing escrow)  \n  - **Guaranty fees** (Fannie Mae, Freddie Mac, or FHA/VA/Ginnie Mae charges)  \n  - **Lender profit margin**[4]  \n\nCombined, these two pieces create the **overall mortgage‑Treasury spread**:\n\n\\[\n\\text{Borrower Rate} \\approx \\text{10‑yr Treasury Yield} + \\text{Secondary Spread} + \\text{Primary–Secondary Spread}\n\\]\n\nWhen market conditions change—credit stress, Fed buying/selling of MBS, investor appetite—the **spread can widen or narrow** even if the 10‑year yield is unchanged.[3][4]\n\n- For example, the Fed’s large‑scale **purchase of MBS during the pandemic** narrowed spreads and contributed to **record‑low mortgage rates**.[3]  \n- Later, as that support pulled back and volatility rose, spreads widened, so mortgage rates were higher relative to Treasuries.[3][4]\n\n---\n\n## 3. Role of the Federal Reserve and the economy\n\nThe **Fed does not directly set mortgage rates**.[3] Instead, it influences them through:\n\n- **Short‑term interest rate policy (federal funds rate)**, which shapes expectations for future rates and thus Treasury yields.[4]  \n- **Balance sheet policies (buying or selling Treasuries and MBS)**, which affect both Treasury yields and MBS prices/spreads.[3][4]  \n- Broader impacts on inflation and growth, which influence investor demand for bonds and risk assets.[2][3][4]\n\nMacro factors that move **Treasury yields and MBS spreads**—and therefore mortgage rates—include:[2][3][4]\n\n- Inflation and inflation expectations  \n- Overall economic growth and unemployment  \n- Risk sentiment and geopolitical events  \n- Government policy and regulation of the housing/finance system\n\n---\n\n## 4. How lenders set *your* specific rate\n\nOnce the **market baseline** is set (10‑year yield + market spread), individual lenders layer on **loan‑ and borrower‑specific adjustments**.\n\nExperian, the CFPB, and banks identify key factors:[1][2][5][7]\n\n- **Credit score and credit history**  \n  - Higher scores → lower perceived default risk → **lower rate**.[1][5][7]  \n  - Lower scores or recent derogatories → higher rate.\n\n- **Debt‑to‑income ratio (DTI) and income stability**  \n  - Lower DTI and stable income reduce risk, helping qualify for **better pricing**.[1][2][5][7]\n\n- **Loan‑to‑value (LTV) ratio / down payment**  \n  - Bigger down payment → lower LTV → less loss risk for lender → **lower rate**.[2][5][7]  \n  - High‑LTV or cash‑out refinances often carry rate add‑ons.\n\n- **Loan amount and type**  \n  - Jumbo vs. conforming, fixed vs. adjustable, conventional vs. FHA/VA/USDA all carry different capital, liquidity, and guarantee costs, which show up in your rate.[1][2][5][7]  \n  - Adjustable‑rate mortgages usually start lower because the rate can reset later to market levels.[1][5]\n\n- **Term length**  \n  - **Shorter terms (10–15 years)** generally have **lower rates** than 30‑year terms because the lender’s money is at risk for a shorter period.[1][5]\n\n- **Property and program details**  \n  - Investment property or 2–4 unit vs. primary residence  \n  - Manufactured housing, condos, or certain property types may have pricing add‑ons.\n\n- **Points and fees**  \n  - You can often pay **discount points** up front to reduce the interest rate; conversely, choosing lower closing costs may mean accepting a higher rate.[1][5]\n\nDifferent lenders also have different **overhead structures, risk appetites, and profit targets**, so **rates vary by lender even on the same day for the same borrower**.[2][5] This is why rate shopping is typically recommended.[2]\n\n---\n\n## 5. Putting it all together with a simple example\n\nConceptually, for a 30‑year fixed mortgage on a given day:\n\n1. **Market sets baseline**  \n   - 10‑year Treasury yield: 4.0%  \n   - MBS vs. Treasury secondary spread: +0.7%  \n   → MBS yield: 4.7%\n\n2. **Primary‑secondary and lender margin**  \n   - Servicing + guaranty fees + overhead + profit: +1.3%  \n   → Typical **par mortgage rate quote**: ~6.0% (a 2.0% spread over the 10‑year yield)[3][4][6]\n\n3. **Loan/borrower adjustments**  \n   - Strong borrower, 20% down, owner‑occupied, 740+ FICO: small or no add‑ons → ~6.0%  \n   - Riskier profile (lower credit score, high LTV, investment property): several add‑ons → 6.5–7.0%+\n\nThis illustrates how **the 10‑year Treasury yield anchors the level of mortgage rates**, while **spreads and loan‑specific pricing** explain why your actual rate may be higher or lower than that benchmark.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896043,
      "model": "sonar-pro",
      "citations": [
        "https://www.experian.com/blogs/ask-experian/how-mortgage-interest-works/",
        "https://www.leaderbank.com/blog/how-do-mortgage-interest-rates-work",
        "https://www.bankrate.com/mortgages/how-interest-rates-are-set/",
        "https://www.thefederalsavingsbank.com/Blog/how-are-mortgage-rates-determined/",
        "https://www.bankatfirst.com/personal/discover/flourish/how-banks-determine-mortgage-rates.html",
        "https://www.fanniemae.com/research-and-insights/publications/housing-insights/rate-30-year-mortgage",
        "https://www.consumerfinance.gov/about-us/blog/7-factors-determine-your-mortgage-interest-rate/",
        "https://www.freddiemac.com/pmms"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "How Does Mortgage Interest Work? - Experian",
          "url": "https://www.experian.com/blogs/ask-experian/how-mortgage-interest-works/",
          "date": "2026-04-23",
          "last_updated": "2026-05-27",
          "snippet": "To calculate the mortgage interest on a home loan, your lender typically takes your annual interest rate, divides it by 12 to get a monthly rate and then ...",
          "source": "web"
        },
        {
          "title": "How Do Mortgage Interest Rates Work? | Leader Bank",
          "url": "https://www.leaderbank.com/blog/how-do-mortgage-interest-rates-work",
          "date": "2025-08-13",
          "last_updated": "2026-05-27",
          "snippet": "Mortgage interest rates are determined by a range of factors including both broad economic conditions and the personal finances of individuals borrowers.",
          "source": "web"
        },
        {
          "title": "What Factors Determine And Move Mortgage Rates? | Bankrate",
          "url": "https://www.bankrate.com/mortgages/how-interest-rates-are-set/",
          "date": "2025-09-12",
          "last_updated": "2026-05-26",
          "snippet": "Other market factors impacting mortgage interest rates · Overall economy · Inflation · Federal Reserve · Mortgage spreads · Government policies.",
          "source": "web"
        },
        {
          "title": "How are mortgage rates determined? | The Federal Savings Bank",
          "url": "https://www.thefederalsavingsbank.com/Blog/how-are-mortgage-rates-determined/",
          "date": "2025-09-19",
          "last_updated": "2026-05-27",
          "snippet": "Mortgage rates are determined by a range of factors from larger economic inputs down to your personal financial profile.",
          "source": "web"
        },
        {
          "title": "How Do Banks Set Mortgage Rates",
          "url": "https://www.bankatfirst.com/personal/discover/flourish/how-banks-determine-mortgage-rates.html",
          "date": "2020-11-30",
          "last_updated": "2026-05-17",
          "snippet": "Understand the key factors that banks consider for your mortgage interest rate, including credit score, size & length of loan, and economic factors.",
          "source": "web"
        },
        {
          "title": "What Determines the Rate on a 30-Year Mortgage? | Fannie Mae",
          "url": "https://www.fanniemae.com/research-and-insights/publications/housing-insights/rate-30-year-mortgage",
          "date": "2024-12-11",
          "last_updated": "2026-05-26",
          "snippet": "Mortgage rates are determined by adding a spread to the benchmark 10-year Treasury note. The spread, or difference, between the rate offered on ...",
          "source": "web"
        },
        {
          "title": "Seven factors that determine your mortgage interest rate",
          "url": "https://www.consumerfinance.gov/about-us/blog/7-factors-determine-your-mortgage-interest-rate/",
          "date": "2017-09-29",
          "last_updated": "2026-05-27",
          "snippet": "1. Credit scores · 2. Home location · 3. Home price and loan amount · 4. Down payment · 5. Loan term · 6. Interest rate type · 7. Loan type.",
          "source": "web"
        },
        {
          "title": "Mortgage Rates - Freddie Mac",
          "url": "https://www.freddiemac.com/pmms",
          "date": "2022-11-17",
          "last_updated": "2026-05-27",
          "snippet": "The 30-year fixed-rate mortgage averaged 6.51% as of May 21, 2026, up from last week when it averaged 6.36%. A year ago at this time, the 30- ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 2040,
        "cost": {
          "input_tokens_cost": 8e-05,
          "output_tokens_cost": 0.0306,
          "total_cost": 0.03667,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 25,
        "total_tokens": 2065,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Info>
  Language codes must be valid ISO 639-1 codes (e.g., `"en"`, `"fr"`, `"de"`). You can filter by up to 10 languages per request.
</Info>

## Academic Filter

Prioritize scholarly sources and peer-reviewed content by setting `search_mode` to `"academic"`.

**Key parameters:**

* `search_mode`: Set to `"academic"` to target academic sources

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What is lion's mane mushroom (Hericium erinaceus), and what mechanisms have been proposed in the published literature for its claimed cognitive effects?"}],
    search_mode="academic",
    web_search_options={"search_context_size": "low"}
)
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "1e485ec9-3f7b-4ba1-b00d-c6e31930403f",
    "choices": [
      {
        "delta": {
          "content": "",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "index": 0,
        "message": {
          "content": "Lion’s mane (Hericium erinaceus) is an edible/medicinal mushroom long used in East Asian traditional medicine and now marketed globally as a “nootropic.” It contains a variety of bioactive compounds and has shown interesting effects in cells and animal models, with early, small human trials suggesting possible cognitive and mood benefits. However, evidence in humans is still limited and mixed.\n\nBelow is a structured summary focused on mechanisms proposed in the scientific literature.\n\n---\n\n## 1. What is Lion’s Mane (Hericium erinaceus)?\n\n- **Species:** Hericium erinaceus, a tooth fungus with white, cascading spines (“lion’s mane” appearance).\n- **Traditional use:** In Traditional Chinese and Japanese medicine for digestive and general tonic purposes.\n- **Key bioactive classes** (from fruiting body and mycelium) [3][4][5]:\n  - **Terpenoids:**  \n    - *Hericenones* – mainly from the fruiting body  \n    - *Erinacines* – mainly from the mycelium  \n  - **Polysaccharides (β-glucans)**\n  - **Phenolic compounds & ergothioneine**\n  - Other sterols and small molecules (e.g., isoindolinones)\n\nThese compounds are being investigated particularly for **neuroprotective and neuroregenerative** properties.\n\n---\n\n## 2. Main Proposed Mechanisms for Cognitive / Neurological Effects\n\n### 2.1 Nerve Growth Factor (NGF) & Other Neurotrophic Factors\n\nThis is the central proposed mechanism.\n\n- **NGF stimulation:**  \n  - Hericenones and erinacines have repeatedly been shown in vitro and in animal models to **stimulate NGF synthesis and expression** [3][4][5][6].\n  - NGF is critical for **growth, maintenance, and survival of neurons**, particularly cholinergic neurons implicated in learning and memory.\n\n- **Neurite outgrowth & connectivity:**  \n  - UQ work and related studies found lion’s mane extracts and isolated compounds **promote neurite outgrowth (axon/dendrite growth)** and **increase the size of growth cones** in cultured neurons, enhancing the ability of neurons to extend processes and form new connections [1].\n  - This is consistent with **increased structural plasticity**, a basis for learning and memory.\n\n- **Blood–brain barrier penetration:**  \n  - Erinacines especially are reported to **cross the blood–brain barrier** and exert neurotrophic effects in the brain [3][4].\n  - This is important because many NGF-modulating agents can’t reach the CNS when taken orally.\n\n- **Other neurotrophic factors:**  \n  - Some studies suggest upregulation of **BDNF (brain-derived neurotrophic factor)**, another key molecule for **synaptic plasticity, learning, and memory consolidation** [2][4], though this is less well established than NGF.\n\n**Relevance to cognition:**  \nEnhancement of NGF/BDNF and neurite outgrowth could support **neurogenesis, synaptic remodeling, and resilience of existing circuits**, all relevant to memory and learning, especially in aging or neurodegenerative conditions.\n\n---\n\n### 2.2 Neuroprotection: Anti-Oxidant & Anti-Inflammatory Actions\n\nLion’s mane appears to protect neurons not only by promoting growth, but also by reducing damage.\n\n- **Antioxidant effects** [3][4][5]:\n  - Phenolics, ergothioneine, and polysaccharides show **free radical scavenging** and **reduction of oxidative stress** in cell and animal models.\n  - Oxidative stress is a major driver of neuronal damage in aging and neurodegenerative diseases.\n\n- **Anti-inflammatory effects** [3][4]:\n  - Extracts modulate inflammatory pathways such as **NF-κB** and **COX-2**, reducing pro-inflammatory cytokines.\n  - In animal models, this neuroinflammatory reduction is associated with **neuroprotection** and improved behavior.\n\n- **Protection in disease models:**  \n  In various rodent models (e.g., amyloid-β–induced Alzheimer’s-like pathology, aluminum chloride models) [3][4]:\n  - Lion’s mane increased NGF mRNA in the hippocampus.\n  - Reduced neuroinflammatory markers.\n  - Preserved or improved **spatial, short-term, and visual recognition memory** relative to untreated controls.\n\n**Relevance to cognition:**  \nBy reducing oxidative damage and inflammation in the brain, lion’s mane might **slow or mitigate processes that degrade cognitive function**, particularly in neurodegenerative conditions.\n\n---\n\n### 2.3 Cholinergic System Modulation\n\nThe cholinergic system is heavily implicated in attention and memory, and is one of the main targets in Alzheimer’s disease therapy.\n\n- In an aluminum chloride-induced Alzheimer’s model, lion’s mane **increased acetylcholine and choline acetyltransferase levels** in a dose-dependent manner [3].\n- This suggests potential support for **cholinergic neurotransmission**, which is typically impaired in Alzheimer’s and age-related cognitive decline.\n\n**Relevance to cognition:**  \nImproved cholinergic signaling is associated with better **attention, working memory, and learning**.\n\n---\n\n### 2.4 Neurogenesis and Synaptic Plasticity\n\n- Animal work suggests lion’s mane may **promote neurogenesis**, particularly in the hippocampus (a key learning and memory center), via NGF and possibly BDNF upregulation [3][4].\n- Enhanced **synaptic plasticity** (changes in synaptic strength and number) is inferred from:\n  - Increased neurite outgrowth.\n  - Improved behavioral outcomes in learning/memory tasks.\n\n**Relevance to cognition:**  \nNeurogenesis and synaptic plasticity are core mechanisms underlying **long-term memory formation and adaptation**.\n\n---\n\n### 2.5 Stress, Mood, and HPA Axis Modulation\n\nSome human and animal data point to **anxiolytic and stress-reducing** effects.\n\n- A placebo-controlled trial in healthy adults found that 28 days of lion’s mane supplementation:\n  - **Improved speed of performance on certain cognitive tasks.**\n  - Showed a **trend toward reduced subjective stress levels** compared with placebo [2][7].\n- Proposed mechanisms:\n  - NGF/BDNF-related changes in **neural circuits for mood and stress**.\n  - Anti-inflammatory and antioxidant effects dampening **neuroinflammation-related mood disturbances**.\n  - Possible modulation of the **HPA axis**, though direct evidence is limited.\n\n**Relevance to cognition:**  \nReduced stress and improved mood can secondarily improve **cognitive performance**, particularly in tasks requiring sustained attention or working memory.\n\n---\n\n### 2.6 Immunomodulation and Gut–Brain Axis (Emerging)\n\n- β-glucans and other polysaccharides have **immunomodulatory** actions and may influence the **gut microbiota** [3][4].\n- Since immune activation and gut–brain signaling affect brain function, some authors speculate that part of lion’s mane’s cognitive/mood effects may occur via:\n  - Reduced **systemic inflammation**.\n  - Changes in **microbial metabolites** that affect the brain.\n\nThese pathways are plausible but less directly demonstrated for cognition than NGF/BDNF-related mechanisms.\n\n---\n\n## 3. Evidence in Humans vs. Mechanistic Hype\n\nThe mechanistic data (cell culture and animal studies) are relatively strong for several points:\n\n- NGF stimulation and neurite outgrowth.\n- Neuroprotection in toxin or amyloid-based models.\n- Anti-oxidant and anti-inflammatory effects.\n- Improved learning/memory in rodent models.\n\nHowever, human data are still modest:\n\n- A few **small, short-duration clinical trials** in older adults and healthy volunteers show:\n  - Some improvements in **memory measures, performance speed, or mild cognitive impairment scores**.\n  - Some improvements in **mood, anxiety, or stress**.\n- Reviews (e.g., Alzheimer’s Drug Discovery Foundation reports) emphasize that:\n  - **Cognitive effects are mixed**, and\n  - **Larger, longer, better-controlled trials** are needed to confirm efficacy and determine dosing, duration, and which preparations (fruiting body vs. mycelium, specific erinacine/hericenone content) matter most [5][6].\n\n---\n\n## 4. Concise Mechanism Summary\n\nProposed mechanisms for lion’s mane’s cognitive and neurological effects, based on current literature, include:\n\n1. **Neurotrophic stimulation**  \n   - Hericenones and erinacines stimulate **NGF (and possibly BDNF)** synthesis, promoting neurite outgrowth, synaptic plasticity, and neuronal survival.\n\n2. **Neuroprotection**  \n   - Antioxidant and anti-inflammatory effects protect neurons from oxidative stress and neuroinflammation.\n\n3. **Cholinergic enhancement**  \n   - Increased acetylcholine and choline acetyltransferase in animal models suggests support of key neurotransmission for memory.\n\n4. **Neurogenesis and structural plasticity**  \n   - Promotion of neurogenesis and improved structural connectivity in cognitive brain regions (hippocampus, cortex).\n\n5. **Stress and mood modulation**  \n   - Likely via neurotrophic changes, reduced inflammation, and possibly HPA axis modulation, which can indirectly improve cognitive performance.\n\n6. **Immune and gut–brain interactions** (emerging, less direct)  \n   - Immunomodulatory effects and potential microbiome changes may influence brain function and mood.\n\n---\n\nIf you’d like, I can next:  \n- Summarize specific key human trials (design, dose, outcomes), or  \n- Compare fruiting-body vs. mycelium extracts and their different active compounds (hericenones vs. erinacines) in more detail.",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779391793,
    "model": "sonar-pro",
    "citations": [
      "https://news.uq.edu.au/2023-02-10-mushrooms-magnify-memory-boosting-nerve-growth",
      "https://www.nutraingredients.com/Article/2023/12/01/Mushrooms-for-the-mind-Research-concludes-Lion-s-Mane-improves-cognitive-performance-and-reduces-stress/",
      "https://restorativemedicine.org/journal/neurological-activity-lions-mane-hericium-erinaceus/",
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC12030463/",
      "https://www.alzdiscovery.org/uploads/cognitive_vitality_media/Lions-Mane-Cognitive-Vitality-For-Researchers.pdf",
      "https://www.alzdiscovery.org/cognitive-vitality/ratings/lions-mane",
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC10675414/"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "Mushrooms magnify memory by boosting nerve growth - UQ News",
        "url": "https://news.uq.edu.au/2023-02-10-mushrooms-magnify-memory-boosting-nerve-growth",
        "date": "2023-02-10",
        "last_updated": "2026-05-21",
        "snippet": "“Pre-clinical testing found the lion's mane mushroom had a significant impact on the growth of brain cells and improving memory. “Laboratory ...",
        "source": "web"
      },
      {
        "title": "Mushrooms for the mind: Research concludes Lion's Mane improves ...",
        "url": "https://www.nutraingredients.com/Article/2023/12/01/Mushrooms-for-the-mind-Research-concludes-Lion-s-Mane-improves-cognitive-performance-and-reduces-stress/",
        "date": "2024-01-08",
        "last_updated": "2026-05-14",
        "snippet": "Previous studies have observed memory and mood enhancements following intakes of Lion's Mane, whilst associations have been noted with cognitive ...",
        "source": "web"
      },
      {
        "title": "Neurological Activity of Lion's Mane (Hericium erinaceus)",
        "url": "https://restorativemedicine.org/journal/neurological-activity-lions-mane-hericium-erinaceus/",
        "date": "2017-12-19",
        "last_updated": "2025-06-15",
        "snippet": "Lion's Mane may be an important herbal remedy for Alzheimer's disease based on early research. This botanical medicine review explores the ...",
        "source": "web"
      },
      {
        "title": "Lion's Mane Mushroom (Hericium erinaceus): A Neuroprotective ...",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12030463/",
        "date": "2025-04-09",
        "last_updated": "2026-05-07",
        "snippet": "Among them, erinacines have been extensively studied for their ability to cross the blood–brain barrier and exert potent neuroprotective effects [30,72].",
        "source": "web"
      },
      {
        "title": "[PDF] Lion's Mane Mushroom - Alzheimer's Drug Discovery Foundation",
        "url": "https://www.alzdiscovery.org/uploads/cognitive_vitality_media/Lions-Mane-Cognitive-Vitality-For-Researchers.pdf",
        "date": null,
        "last_updated": "2026-05-15",
        "snippet": "Cognitive effects with lion's mane supplementation have been mixed based on a few small pilot clinical trials. Larger, longer duration trials are needed to ...",
        "source": "web"
      },
      {
        "title": "Lion's Mane & Your Brain | Cognitive Vitality",
        "url": "https://www.alzdiscovery.org/cognitive-vitality/ratings/lions-mane",
        "date": "2025-09-03",
        "last_updated": "2026-05-02",
        "snippet": "Cognitive effects with Lion's mane have been mixed based on small and short-duration clinical trials. Preclinical studies suggest that Lion's ...",
        "source": "web"
      },
      {
        "title": "The Acute and Chronic Effects of Lion's Mane Mushroom ... - PMC",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10675414/",
        "date": "2023-11-20",
        "last_updated": "2026-05-16",
        "snippet": "Conclusions: The findings tentatively suggest that Hericium erinaceus may improve speed of performance and reduce subjective stress in healthy, ...",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 2063,
      "cost": {
        "input_tokens_cost": 0.0001,
        "output_tokens_cost": 0.03095,
        "total_cost": 0.03704,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 32,
      "total_tokens": 2095,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

<Warning>
  Date filters are **not supported** with `search_mode="academic"` and are silently ignored. This includes `search_after_date_filter`, `search_before_date_filter`, `search_recency_filter`, `last_updated_after_filter`, and `last_updated_before_filter`. To narrow academic results by date, include the desired time range directly in your query text (e.g., "findings on neural networks since 2023").
</Warning>

## SEC Filings Filter

Target U.S. Securities and Exchange Commission filings and official financial documents.

**Key parameters:**

* `search_mode`: Set to `"sec"` to target SEC filings

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Prepare me for markets opening."}],
    search_mode="sec"
)

# Combine with date filters for recent filings
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Explain what a 10-K filing is, who is required to file one, and the typical structure of the document."}],
    search_mode="sec",
    search_after_date_filter="1/1/2023"
)
```

<AccordionGroup>
  <Accordion title="Response — Prepare me for markets opening.">
    ```json theme={null}
    {
      "id": "ffc90d76-a3a0-43e8-bd5c-b061c1986c0f",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "Here’s a concise, practical pre‑market checklist you can follow before the next US session (NYSE/NASDAQ open at 9:30 a.m. ET).\n\n---\n\n## 1. Know the Session You’re Trading\n\n- Regular US cash session: 9:30–16:00 ET  \n- Pre‑market (depending on broker): often ~4:00–9:30 ET  \nDecide:  \n- Are you trading only regular hours, or also pre‑market/after‑hours?  \n- Are you a day trader, swing trader, or longer‑term? Your routine should match that.\n\n---\n\n## 2. Review the Bigger Picture (Top‑Down)\n\n**A. Index futures & global markets**  \nBefore the open, check:\n\n- S&P 500 / Nasdaq / Dow futures (ES, NQ, YM) – are they strongly up, down, or flat?\n- Key foreign markets that traded before the US:\n  - Europe (DAX, FTSE, Euro Stoxx)\n  - Asia (Nikkei, Hang Seng, etc.)\n\nThis tells you: “Risk‑on or risk‑off?” If risk is off and everything is red, you’ll weigh shorts/defensive names more heavily; if risk‑on, focus on long setups.\n\n**B. Economic calendar & events**\n\nCheck a reliable calendar (e.g., Forex Factory, Investing.com, your broker) for:\n\n- Major releases: CPI, PPI, NFP, GDP, FOMC, Fed speakers, etc.\n- Time of the event vs. your planned trades:\n  - Before open: may cause big gaps.\n  - Shortly after open: volatility spikes around the release.\n\nIf a huge report is 10–15 minutes after the open, consider reducing exposure or waiting until after the data.\n\n---\n\n## 3. Build/Update Your Watchlist the Day Before\n\nDo this after the close, then refine it pre‑market:\n\n1. **Scan for strong/weak names**:\n   - Strong uptrends, holding above key moving averages / prior resistance.\n   - Weak downtrends, rejecting resistance, breaking support.\n2. **Separate lists**:\n   - “Bullish list”: names you’re interested in buying if market confirms strength.\n   - “Bearish list”: names you’re interested in shorting if market is weak.\n3. **No hard decisions a day ahead**  \nHave *ideas*, not commitments. Your direction depends on how things actually look near the open.\n\n---\n\n## 4. Pre‑Market Routine (Morning of the Session)\n\n### A. News & Catalysts\n\nFocus on **fresh catalysts**, especially for day trades:\n\n- Earnings (beats/misses, guidance).\n- M&A, FDA approvals, major contracts, upgrades/downgrades.\n- Sector or macro news (oil, rates, geopolitics).\n\nFor each candidate, ask:\n- What is the catalyst?\n- Is it big enough to justify today’s move?\n- Is it in line with the broader market theme?\n\n### B. Use Scanners (If You Day Trade)\n\nFrom the scanner, filter for:\n\n- **Pre‑market gappers**: up or down with significant % change.\n- **High volume** vs. normal (relative volume).\n- **Float**: Low float + big volume + fresh news = potential explosive mover (and higher risk).\n\nNarrow to a small list (3–10 names) with:\n- Strong volume.\n- Clear news.\n- Clear price levels (see next step).\n\n---\n\n## 5. Mark Your Key Levels\n\nOn your charting platform, for each watchlist name:\n\n1. Start with **daily chart**:\n   - Recent highs/lows.\n   - Major support/resistance.\n   - Gaps.\n2. Then **intraday (e.g., 15m/5m)**:\n   - Yesterday’s high/low/close.\n   - Pre‑market high and low.\n   - Volume‑heavy zones (VWAP if you use it).\n\nIf you trade ORBs (Opening Range Breakouts) or key‑level breaks:\n- Pre‑market high = key resistance.\n- Pre‑market low = key support.\n- Plan potential entries around these.\n\n---\n\n## 6. Define Trade Plans in Advance\n\nFor each A‑setup on your list, write:\n\n- Direction: Long or short?\n- Trigger:  \n  - Example: “Long above pre‑market high with volume confirmation.”  \n  - Example: “Short on failed breakout above yesterday’s high.”\n- Stop loss:\n  - Based on technical level (below recent low, above resistance, etc.).\n- Profit targets:\n  - First target at logical resistance/support.\n  - Decide partial vs full exits.\n- Maximum risk per trade and per day:\n  - e.g., 0.5–1% of account per trade; 2–3% max daily loss.\n\nIf you cannot write the plan in one or two clear sentences, the trade is probably not clean enough.\n\n---\n\n## 7. Risk Management & “No‑Go” Rules\n\nDecide beforehand:\n\n- Max **number of trades**.\n- Max **daily loss** after which you stop trading.\n- No trading after:\n  - Hitting max loss.\n  - Breaking your rules emotionally.\n\nAvoid:\n- Illiquid symbols (thin volume, wide spreads).\n- Names at or near **market‑wide position limit** extremes or with unusual restrictions in derivatives, unless you fully understand the risk.\n\n---\n\n## 8. Time‑of‑Day Discipline\n\nHave a schedule:\n\n- **First 5–10 minutes after the open**:\n  - Volatility & spreads can be extreme.\n  - Consider either small size or no trading until price settles and levels are tested.\n- **Midday (“lunch hour”)**:\n  - Often choppy, low‑volume; many pros avoid initiating new trades then.\n- **Last 5–10 minutes**:\n  - Order imbalances, funds rebalancing; better for experienced traders or closing/adjusting swing positions, not impulsive new entries.\n\n---\n\n## 9. Mental & Practical Setup\n\n- Check platform: orders go through, quotes are real‑time, charts are correct.\n- Prepare order types you’ll use:\n  - Limit vs market, stop vs stop‑limit, bracket orders if available.\n- Clear your head:\n  - No revenge trading from yesterday.\n  - Accept that missing a trade is better than forcing a bad one.\n\nHave one sentence in mind:\n- “My only job is to follow my plan and protect my capital.”\n\n---\n\n## 10. Quick Template You Can Reuse Daily\n\nYou can literally fill this out each morning:\n\n1. Market bias (futures, global markets):  \n   - Bias: Bullish / Bearish / Neutral  \n2. Key macro events today & times:  \n3. Sectors in play (strong/weak):  \n4. Main watchlist (3–10 tickers) with catalysts:  \n   - Ticker – Long/Short – Catalyst – Key levels  \n5. A‑setups (max 3):  \n   - Entry, stop, targets, size  \n6. Risk limits:  \n   - Max loss per trade:  \n   - Max loss per day:  \n7. “No trade” conditions:  \n   - (e.g., choppy open, spreads too wide, news event in 5 min, etc.)\n\n---\n\nIf you tell me:\n- Your time zone,\n- Whether you’re day trading, swing trading, or investing,\n- And what tools/broker you use,\n\nI can turn this into a very specific, timed routine (e.g., what to do from 8:30–9:30 a.m. ET) tailored to you.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779391587,
      "model": "sonar-pro",
      "citations": [
        "https://www.youtube.com/watch?v=RamId6Zyq3o",
        "https://www.timothysykes.com/blog/how-to-prepare-for-the-stock-market-open-tomorrow/",
        "https://www.youtube.com/watch?v=QlYbiDi4vOU",
        "https://www.youtube.com/watch?v=_LoiBT5LoSo",
        "https://www.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis",
        "https://www.ig.com/uk/trading-strategies/us-stock-market-hours--when-do-the-nyse--nasdaq--dow-jones-and-s-200812",
        "https://vocal.media/journal/5-things-to-know-before-the-stock-market-opens"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "How to Prepare for Your Trading Day in 8 Simple Steps - YouTube",
          "url": "https://www.youtube.com/watch?v=RamId6Zyq3o",
          "date": "2019-12-11",
          "last_updated": "2025-07-17",
          "snippet": "... (Smart Money Approved). Pro Trading School•259K views · 15:46 · Go to channel Equitymaster · If the Market Falls, I Will Do This… Equitymaster• ...",
          "source": "web"
        },
        {
          "title": "How To Prepare For The Stock Market Open Tomorrow",
          "url": "https://www.timothysykes.com/blog/how-to-prepare-for-the-stock-market-open-tomorrow/",
          "date": "2023-01-10",
          "last_updated": "2026-05-21",
          "snippet": "Don't wait until 9:20am EST tomorrow to prepare your watchlist, do it TODAY/TONIGHT and be 100% ready for all the opportunities tomorrow morning!",
          "source": "web"
        },
        {
          "title": "Pre-Market Routine: How I Find The Best Stocks Every Morning",
          "url": "https://www.youtube.com/watch?v=QlYbiDi4vOU",
          "date": "2026-04-07",
          "last_updated": "2026-05-21",
          "snippet": "Most traders waste their pre-market time or skip preparation entirely, and it shows in their results ... market opens at 9:30 AM. This is ...",
          "source": "web"
        },
        {
          "title": "The AXIA Pre-Market Blueprint: How To Prepare Before Markets Open",
          "url": "https://www.youtube.com/watch?v=_LoiBT5LoSo",
          "date": "2026-01-14",
          "last_updated": "2026-05-16",
          "snippet": "... let mevolaxy beats wash over me as I work. 26:44 · Go to channel Axia Futures · 3 Trading Setups Used By Pro Traders. Axia Futures•13K views.",
          "source": "web"
        },
        {
          "title": "Market research and competitive analysis | U.S. Small Business ...",
          "url": "https://www.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis",
          "date": "2026-03-24",
          "last_updated": "2026-05-05",
          "snippet": "Use market research to find customers. Market research blends consumer behavior and economic trends to confirm and improve your business idea.",
          "source": "web"
        },
        {
          "title": "US Stock Markets Opening Hours (UK Hours) - IG",
          "url": "https://www.ig.com/uk/trading-strategies/us-stock-market-hours--when-do-the-nyse--nasdaq--dow-jones-and-s-200812",
          "date": "2026-02-25",
          "last_updated": "2026-05-20",
          "snippet": "Learn the opening hours of the New York Stock Exchange (NYSE), NASDAQ and NASDAQ 100, as well as the Dow Jones and S&P 500, with IG UK.",
          "source": "web"
        },
        {
          "title": "5 Things to Know Before the Stock Market Opens - Vocal Media",
          "url": "https://vocal.media/journal/5-things-to-know-before-the-stock-market-opens",
          "date": "2025-04-04",
          "last_updated": "2025-07-28",
          "snippet": "Before the stock market opens, here are five essential facts to know: 1. Futures on Stock Indexes and the Performance of Global Markets One of the first ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1598,
        "cost": {
          "input_tokens_cost": 2e-05,
          "output_tokens_cost": 0.02397,
          "total_cost": 0.02999,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 7,
        "total_tokens": 1605,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — Explain what a 10-K filing is, who is required to file one, and the typical structure o...">
    ```json theme={null}
    {
      "id": "0fe07f20-b9f9-4f5d-a122-c85f37ed5e47",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "A **Form 10‑K** is the detailed **annual report that U.S. public companies must file with the Securities and Exchange Commission (SEC)**, providing a comprehensive picture of their business, risks, and audited financial performance for the fiscal year.[2][3][7]\n\n### What a 10‑K filing is\n\n- Form 10‑K is an **SEC‑mandated annual disclosure** that gives a full summary of a company’s **business, risk factors, operations, and financial results**, including audited financial statements.[2][3][7]  \n- It is **more detailed and standardized** than the glossy “annual report to shareholders,” although some companies combine the two.[2][3][7][9]  \n- Typical content includes: company history and operations, organizational structure, markets, subsidiaries, executive compensation, major risks, and full financial statements (balance sheet, income statement, cash flow).[1][2][3][7]\n\n### Who is required to file a 10‑K\n\n- **Most U.S. public companies** are required to file a 10‑K annually with the SEC.[3][7][8]  \n- Under SEC rules, companies with **more than \\$10 million in assets** and a class of equity securities held by **more than 2,000 owners** must file annual and other periodic reports, whether or not the securities are exchange‑listed.[2]  \n- The form is used for annual reports filed under **Sections 13 or 15(d) of the Securities Exchange Act of 1934**.[4]  \n- **Non‑U.S. public companies** typically file on other forms (such as Form 20‑F or 40‑F) rather than 10‑K.[5][7]  \n- **Private companies** that do not have registered public securities generally do **not** file 10‑Ks.[8]\n\n### Filing deadlines\n\nThe deadline depends on filer status under SEC rules:[4][5][6]\n\n- **Large accelerated filers**: within **60 days** after fiscal year‑end.[4][5]  \n- **Accelerated filers**: within **75 days** after fiscal year‑end.[4][5]  \n- **All other registrants** (including smaller reporting companies): within **90 days**.[4][5][6]\n\n### Typical structure and required items in a 10‑K\n\nSEC rules require 10‑Ks to follow a **standard order of topics**, divided into parts and items.[4][6][7] A common structure (for domestic issuers on the modern form) is:\n\n**Part I** – Company and risk overview[6][7]  \n- **Item 1 – Business**: Description of the company’s business, principal products and services, business segments, significant customers, and the markets and geographies in which it operates.[6][7]  \n- **Item 1A – Risk Factors**: Material risks the company faces, such as market, operational, regulatory, liquidity, or cybersecurity risks.  \n- **Item 1B – Unresolved Staff Comments**: Certain outstanding SEC staff comments, if any.  \n- **Item 2 – Properties**: Principal physical properties (offices, plants, facilities) used in operations.[6]  \n- **Item 3 – Legal Proceedings**: Material pending or threatened legal proceedings involving the company.[6][7]  \n- **Item 4 – Mine Safety Disclosures** (for mining companies) or other specialized disclosures, if applicable.\n\n**Part II** – Market information and financial data  \n- **Item 5 – Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities**: Where the stock trades, number of holders, dividends, stock repurchases, etc.[6]  \n- **Item 6 – Selected Financial Data** (required historically; smaller companies may have scaled or modified requirements): Multi‑year summary of key financial metrics.[6]  \n- **Item 7 – Management’s Discussion and Analysis (MD&A)**: Management’s narrative explanation of financial condition, results of operations, liquidity, capital resources, and known trends or uncertainties.[6][7]  \n- **Item 7A – Quantitative and Qualitative Disclosures About Market Risk**: Exposures to interest rate, foreign exchange, commodity price and other market risks.[6]  \n- **Item 8 – Financial Statements and Supplementary Data**: **Audited financial statements** (balance sheet, income statement, cash flow statement, and notes), plus any required supplementary schedules.[1][6][7]  \n- **Item 9 – Changes in and Disagreements with Accountants on Accounting and Financial Disclosure**: Disclosures about auditor changes or disagreements.[6]\n\n**Part III** – Governance, management, and ownership  \n- **Item 10 – Directors, Executive Officers and Corporate Governance**: Biographical information and governance details.[6]  \n- **Item 11 – Executive Compensation**: Detailed compensation information for top executives and directors.[2][6]  \n- **Item 12 – Security Ownership of Certain Beneficial Owners and Management**: Major shareholders and management ownership.[6]  \n- **Item 13 – Certain Relationships and Related Transactions, and Director Independence**: Related‑party transactions and independence disclosures.[6]  \n- **Item 14 – Principal Accounting Fees and Services** (auditor fees and services; in older guidance this was grouped with controls/procedures).[6]\n\n**Part IV** – Exhibits and signatures  \n- **Item 15 – Exhibits and Financial Statement Schedules** (and, under older structure, “Controls and Procedures” and “Reports on Form 8‑K”)[4][6]  \n  - Includes lists of exhibits (e.g., material contracts, bylaws, credit agreements), certifications by officers, and any additional financial statement schedules.[4][6]\n\nIn practice, companies may add front‑matter sections (cover page, index, forward‑looking statements disclaimer) and detailed notes, but the **core items and sequence are dictated by the SEC instructions to Form 10‑K**.[4][7]",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896034,
      "model": "sonar-pro",
      "citations": [
        "https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/what-10-k-filing",
        "https://en.wikipedia.org/wiki/Form_10-K",
        "https://www.investor.gov/introduction-investing/investing-basics/glossary/form-10-k",
        "https://www.sec.gov/files/form10-k.pdf",
        "https://www.toppanmerrill.com/blog/how-to-navigate-forms-10-k-10-q-20-f-40-f-8-k-and-6-k/",
        "https://guides.newman.baruch.cuny.edu/c.php?g=188202&p=1244183",
        "https://www.sec.gov/files/reada10k.pdf",
        "https://chat.library.berkeleycollege.edu/faq/53831",
        "https://en.wikipedia.org/wiki/Annual_report",
        "https://investors.coca-colacompany.com/filings-reports/annual-filings-10-k"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "What Is A 10-K Filing? - DFIN",
          "url": "https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/what-10-k-filing",
          "date": "2021-04-02",
          "last_updated": "2026-05-11",
          "snippet": "A Form 10-K discloses all the important business information that investors want to know about companies that are traded on the stock exchange.",
          "source": "web"
        },
        {
          "title": "Form 10-K - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Form_10-K",
          "date": "2005-02-23",
          "last_updated": "2026-03-07",
          "snippet": "A Form 10-K is an annual report required by the U.S. Securities and Exchange Commission (SEC), that gives a comprehensive summary of a company's financial ...",
          "source": "web"
        },
        {
          "title": "Form 10-K - Investor.gov",
          "url": "https://www.investor.gov/introduction-investing/investing-basics/glossary/form-10-k",
          "date": null,
          "last_updated": "2026-05-23",
          "snippet": "The annual report on Form 10-K provides a comprehensive overview of the company's business and financial condition and includes audited financial statements.",
          "source": "web"
        },
        {
          "title": "[PDF] Form 10-K - SEC.gov",
          "url": "https://www.sec.gov/files/form10-k.pdf",
          "date": null,
          "last_updated": "2025-06-03",
          "snippet": "A. Rule as to Use of Form 10-K. (1) This Form shall be used for annual reports pursuant to Section 13 or 15(d) of the. Securities Exchange Act of 1934 (15 ...",
          "source": "web"
        },
        {
          "title": "How to navigate Forms 10-K, 10-Q, 20-F, 40-F, 8-K and 6-K",
          "url": "https://www.toppanmerrill.com/blog/how-to-navigate-forms-10-k-10-q-20-f-40-f-8-k-and-6-k/",
          "date": "2025-03-19",
          "last_updated": "2026-05-24",
          "snippet": "Form 10-K: The annual financial story. SEC Form 10-K is a report that public companies are required to file annually with the SEC within a ...",
          "source": "web"
        },
        {
          "title": "The 10-K - SEC Filings - Research Guides at Baruch College",
          "url": "https://guides.newman.baruch.cuny.edu/c.php?g=188202&p=1244183",
          "date": "2009-11-02",
          "last_updated": "2026-05-09",
          "snippet": "Filing Dates. Depending on their market cap, companies have 60 to 90 days after the end of their fiscal year to file their 10-K report. Find Bad News.",
          "source": "web"
        },
        {
          "title": "[PDF] Investor Bulletin: How to Read a 10-K - SEC.gov",
          "url": "https://www.sec.gov/files/reada10k.pdf",
          "date": null,
          "last_updated": "2025-05-22",
          "snippet": "The 10-K typically includes more detailed information than the annual report to shareholders. The annual report to shareholders, unlike the 10-K, sometimes ...",
          "source": "web"
        },
        {
          "title": "Q. How do I find a company's 10-K report? - LibAnswers",
          "url": "https://chat.library.berkeleycollege.edu/faq/53831",
          "date": "2023-02-06",
          "last_updated": "2026-03-19",
          "snippet": "A 10-K is an annual report required by the U.S. Securities and Exchange Commission (SEC) that gives a comprehensive summary of a public ...",
          "source": "web"
        },
        {
          "title": "Annual report",
          "url": "https://en.wikipedia.org/wiki/Annual_report",
          "date": "2004-12-13",
          "last_updated": "2026-05-05",
          "snippet": "An annual report is a comprehensive report on a company's activities throughout the preceding year. Annual reports are intended to give shareholders and other interested people information about the company's activities and financial performance....",
          "source": "web"
        },
        {
          "title": "Annual Filings (10-K) - Coca-Cola Investor Relations",
          "url": "https://investors.coca-colacompany.com/filings-reports/annual-filings-10-k",
          "date": "2026-02-20",
          "last_updated": "2026-05-21",
          "snippet": "Filings & Reports · All SEC Filings · Annual Publications · Annual Filings (10-K) · Quarterly Filings (10-Q). Filing Type. View All, 10-K, 10 ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1258,
        "cost": {
          "input_tokens_cost": 8e-05,
          "output_tokens_cost": 0.01887,
          "total_cost": 0.02495,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 26,
        "total_tokens": 1284,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

## Context Size Control

Control how much search context is retrieved to balance cost and comprehensiveness.

**Key parameters:**

* `search_context_size`: Set to `"low"` (default), `"medium"`, or `"high"` within `web_search_options`

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Low context (cost-efficient, default)
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "How many stars are estimated to be in the Milky Way galaxy?"}],
    web_search_options={"search_context_size": "low"}
)

# High context (comprehensive)
completion = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Explain the main causes of the 2008 financial crisis: subprime mortgages, securitization, and the Lehman Brothers collapse."}],
    web_search_options={"search_context_size": "high"}
)
```

<AccordionGroup>
  <Accordion title="Response — How many stars are estimated to be in the Milky Way galaxy?">
    ```json theme={null}
    {
      "id": "c60435ea-ca68-400f-b997-a588b269c449",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "Astronomers estimate that the **Milky Way contains on the order of a few hundred billion stars, roughly between 100–400 billion**, with many recent discussions centering around **~200–400 billion** as the most plausible range.[1][2][3]  \n\nBecause we cannot count every star directly, this is an informed estimate rather than an exact number:\n\n- **Commonly cited range:** Most references give **100–400 billion stars**.[2][3][7]  \n- **More up‑to‑date analyses:** Work combining star counts with mass estimates and Gaia data suggests the total is **unlikely as low as 100 billion and more likely in the ~200–400 billion range**.[1]  \n- **Why there is uncertainty:**  \n  - Very faint, low‑mass stars are hard to detect, especially far from the Sun.[2]  \n  - Estimates rely on measuring the **total stellar mass** of the galaxy and dividing by an assumed *average* stellar mass, which depends on models of the stellar mass distribution.[1][3]  \n\nSo the best concise answer is: **the Milky Way probably contains a few hundred billion stars, on the order of 10¹¹, typically quoted as about 100–400 billion, with ~200–400 billion considered most likely.**[1][2][3]",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896024,
      "model": "sonar-pro",
      "citations": [
        "https://bigthink.com/starts-with-a-bang/how-many-stars-milky-way/",
        "https://en.wikipedia.org/wiki/Milky_Way",
        "https://asd.gsfc.nasa.gov/blueshift/index.php/2015/07/22/how-many-stars-in-the-milky-way/",
        "https://arxiv.org/html/2508.13665v1",
        "https://www.youtube.com/watch?v=gPZABF3Kssw",
        "https://lco.global/spacebook/galaxies/the-milky-way-galaxy/",
        "https://www.cloudynights.com/forums/topic/951234-number-of-stars-in-the-milky-way-estimate-question/"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "Why we still don't know how many stars are in the Milky Way",
          "url": "https://bigthink.com/starts-with-a-bang/how-many-stars-milky-way/",
          "date": "2025-04-02",
          "last_updated": "2025-09-23",
          "snippet": "Current estimates place the most likely number for “stars within the Milky Way” at between 200 billion and 400 billion: an enormous uncertainty.",
          "source": "web"
        },
        {
          "title": "Milky Way - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Milky_Way",
          "date": "2001-09-15",
          "last_updated": "2026-05-22",
          "snippet": "It is estimated to contain 100–400 billion stars and at least that number of planets. The Solar System is located at a radius ...",
          "source": "web"
        },
        {
          "title": "How Many Stars in the Milky Way? | NASA Blueshift",
          "url": "https://asd.gsfc.nasa.gov/blueshift/index.php/2015/07/22/how-many-stars-in-the-milky-way/",
          "date": "2015-07-22",
          "last_updated": "2026-03-29",
          "snippet": "To make an estimate, we have to calculate the mass of our galaxy, and then the percentage of that mass that is made up of stars. Then we have to ...",
          "source": "web"
        },
        {
          "title": "The Milky Way is a less massive galaxy—new estimates of ... - arXiv",
          "url": "https://arxiv.org/html/2508.13665v1",
          "date": "2025-08-19",
          "last_updated": "2026-05-17",
          "snippet": "Adopting our revised total stellar mass estimate of 2.607 × 10 10 ​ M ⊙ 2.607\\ \\times 10^{10}\\ {\\rm M_{\\odot}} gives a new ratio of 1.6 × 10 − 4 ...",
          "source": "web"
        },
        {
          "title": "Ch. 28: The Milky Way (14 of 27) What is the Mass of the Galaxy?",
          "url": "https://www.youtube.com/watch?v=gPZABF3Kssw",
          "date": "2020-05-21",
          "last_updated": "2026-05-19",
          "snippet": "We will learn how to calculate the mass of our Milky Way Galaxy. ... 28: The Milky Way (15 of 27) Globular Star Clusters. Michel van Biezen ...",
          "source": "web"
        },
        {
          "title": "The Milky Way Galaxy - Las Cumbres Observatory",
          "url": "https://lco.global/spacebook/galaxies/the-milky-way-galaxy/",
          "date": null,
          "last_updated": "2026-05-15",
          "snippet": "The galaxy we live in, called the Milky Way Galaxy, is a barred spiral galaxy composed of at least 100 billion stars. It is approximately 100,000 light years ...",
          "source": "web"
        },
        {
          "title": "Number of Stars in the Milky Way Estimate question - Cloudy Nights",
          "url": "https://www.cloudynights.com/forums/topic/951234-number-of-stars-in-the-milky-way-estimate-question/",
          "date": "2025-01-14",
          "last_updated": null,
          "snippet": "So, 100-400 billion stars is as good an estimate as any, but the number is a guess based on density and size. Each time the size estimate ...",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 278,
        "cost": {
          "input_tokens_cost": 4e-05,
          "output_tokens_cost": 0.00417,
          "total_cost": 0.01021,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 14,
        "total_tokens": 292,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>

  <Accordion title="Response — Explain the main causes of the 2008 financial crisis: subprime mortgages, securitizatio...">
    ```json theme={null}
    {
      "id": "23d8e2d8-9b67-4ccc-a84a-3b3f25108749",
      "choices": [
        {
          "delta": {
            "content": "",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "index": 0,
          "message": {
            "content": "The 2008 financial crisis grew out of a housing bubble financed by **subprime mortgages**, amplified by **securitization of those mortgages into complex securities**, and turned into a global panic when **Lehman Brothers was allowed to fail in September 2008**.[2][5]  \n\nBelow is how those three pieces fit together.\n\n---\n\n## 1. Subprime mortgages: risky loans at the core\n\n**What “subprime” means**\n\n- **Subprime mortgages** are home loans to borrowers with **poor credit histories, low incomes, or high debt**, meaning a higher risk they will not repay.[2][5]  \n- Through the early–mid‑2000s, **low interest rates and relaxed lending standards** encouraged banks to issue a high volume of these loans.[2][3]  \n\n**How subprime lending helped create a bubble**\n\n- Cheap credit plus loose standards led to a **surge in mortgage lending**, including to people who previously would not have qualified.[2][4]  \n- This helped push **house prices to “ever-greater heights”** in the 2000s, forming a housing bubble.[2][6]  \n- Lenders increasingly used **“exotic” or non‑traditional mortgages**—adjustable-rate, low‑documentation (“no income/no job”), interest-only, and high loan‑to‑value loans—which made repayment more fragile.[3][4][5]  \n\n**Why subprime loans blew up**\n\n- Many subprime mortgages had **teaser rates**: low initial payments that **reset to much higher interest rates** after a few years.[1][2]  \n- Borrowers and lenders often assumed **house prices would keep rising**, so borrowers could refinance before payments jumped or, failing that, lenders could foreclose and sell at a profit.[1][3]  \n- When house price growth slowed and then reversed around 2006–2007, that assumption broke.  \n  - Research finds a **“classic lending boom‑bust”**: lending standards deteriorated for at least six years, while loan quality fell, but poor performance was hidden by rapid house price appreciation until prices stalled.[3][6]  \n- As teaser rates reset and prices fell, **defaults and foreclosures surged**, especially among 2006–2007 “vintage” loans.[2][3][5]  \n- The resulting **collapse in housing prices** was the first broad national drop since the Great Depression and triggered massive losses for institutions exposed to those loans.[2][5][6]  \n\nSo, subprime mortgages created a large pool of **toxic assets**—loans very likely to default once house prices stopped rising.\n\n---\n\n## 2. Securitization: turning bad loans into global “safe” assets\n\n**What securitization is**\n\n- **Securitization** is the process by which banks **bundle loans (like mortgages) and sell them as tradable securities**, such as **mortgage‑backed securities (MBS)** and more complex **collateralized debt obligations (CDOs)**.[2][5][6]  \n- Instead of holding mortgages to maturity, **originators sold them into the bond market**, collecting fees and shifting the credit risk to investors.[1][2][3]  \n\n**How securitization fueled risky lending**\n\n- As investor demand for higher‑yield, “safe” assets grew after the early‑2000s recession, **private‑label MBS backed by subprime loans exploded**.[2][3][6]  \n- Because banks could quickly sell mortgages, they had **weaker incentives to enforce traditional lending standards** (thorough income verification, reasonable loan‑to‑value ratios, etc.).[2][3][4]  \n- A study of subprime loans shows **monotonic deterioration in loan quality**, rising combined loan‑to‑value ratios, and more low‑documentation loans throughout 2001–2007—evidence of **lending standards eroding as securitization volumes rose**.[3]  \n- Each step of the securitization chain—from originators to investment banks to structured‑product desks—earned **fees for “packaging and repackaging”** the same underlying mortgages.[1][5]  \n\n**Why the risks were mispriced**\n\n- **Credit‑rating agencies** (Moody’s, S&P, Fitch) frequently rated tranches of MBS and CDOs backed by subprime loans as **AAA**, comparable to **U.S. Treasuries**.[2][5]  \n- Fund managers and banks **relied on these ratings instead of doing their own analysis**, assuming mortgage‑backed securities were low‑risk.[2][7]  \n- Many of these securities were **opaque and complex**, with little regulatory oversight; investors did not fully understand how exposed they were to a downturn in U.S. housing.[2][4][5][7]  \n\n**How securitization transmitted the shock**\n\n- When subprime defaults rose, the value of **MBS and CDOs fell sharply**, inflicting losses on banks, investment funds, and institutions around the world.[2][5][6]  \n- Because many of these securities were used as **collateral in short‑term funding markets (like repo)**, doubts about their value quickly morphed into **funding crises** for heavily leveraged firms.[5][6][7]  \n- The FDIC describes the process as a **housing boom‑bust that exposed vulnerabilities in a highly leveraged, interconnected financial system**, centered on securitized mortgage credit.[6]  \n\nSecuritization transformed a U.S. housing problem into a **global financial crisis** by dispersing subprime risk widely—often under the label of “safe” assets.\n\n---\n\n## 3. Lehman Brothers’ collapse: from crisis to full‑blown panic\n\n**Lehman’s role in the system**\n\n- **Lehman Brothers** was a major Wall Street investment bank heavily involved in **underwriting, trading, and holding mortgage‑backed securities and related derivatives**.[2][5][6]  \n- Like other investment banks, Lehman relied heavily on **short‑term wholesale funding** and was **highly leveraged**, making it vulnerable if lenders lost confidence.[5][6]  \n\n**The lead‑up to failure**\n\n- As subprime defaults rose in 2007 and early 2008, large mortgage‑exposed institutions began to fail or be rescued:  \n  - **Bear Stearns** was taken over by JPMorgan Chase with Federal Reserve support in March 2008.[2]  \n  - **Fannie Mae and Freddie Mac**, which held or guaranteed trillions in mortgages, were placed into U.S. government conservatorship in early September 2008.[2]  \n- Despite writing down mortgage assets and seeking capital, Lehman could not convince markets it was solvent. Counterparties and short‑term lenders began to pull back.  \n\n**Bankruptcy and its impact**\n\n- On **September 15, 2008**, Lehman Brothers filed for **bankruptcy protection**, the largest bankruptcy in U.S. history.[2][5][6]  \n- Unlike Bear Stearns, Fannie, or Freddie, **Lehman was not rescued**, signaling to markets that major institutions could fail with little warning.  \n- According to contemporary accounts and later analyses, Lehman’s failure:  \n  - **Shocked global financial markets**, triggering a **worldwide panic**.[2][5]  \n  - Caused **money markets and interbank lending to seize up**, as institutions no longer trusted each other’s solvency or the value of their collateral.[5][6]  \n  - Forced fire‑sales of assets, further depressing prices of mortgage‑related and other securities, and **amplifying losses across the system**.[6][7]  \n\nThe Lehman collapse did not *cause* the underlying housing or securitization problems, but it **crystallized fears and turned a severe credit crisis into a full systemic meltdown**.\n\n---\n\n## How the three causes fit together\n\nYou can think of the crisis as a chain:\n\n1. **Subprime mortgages**  \n   - Aggressive, poorly underwritten loans, often with teaser rates and high leverage, created a **large stock of fragile debt** tied to ever‑rising home prices.[1][2][3][5]  \n\n2. **Securitization of those mortgages**  \n   - These risky loans were **bundled and sold globally** as supposedly safe MBS and CDOs, encouraged by ratings, fee incentives, and weak oversight.[2][3][5][6]  \n   - As defaults rose, the losses were **transmitted across the global financial system**, hitting highly leveraged banks and investors.[2][5][7]  \n\n3. **Lehman Brothers’ collapse**  \n   - Lehman’s failure **validated fears that major institutions holding mortgage‑related assets could suddenly fail**, freezing credit markets and turning a contained financial shock into a **full‑scale global crisis**.[2][5][6]  \n\nIf you like, I can add a short timeline (2001–2009) or a simple diagram-style explanation you could use in an essay or presentation.",
            "role": "assistant",
            "reasoning_steps": null,
            "tool_call_id": null,
            "tool_calls": null
          },
          "finish_reason": "stop"
        }
      ],
      "created": 1779896046,
      "model": "sonar-pro",
      "citations": [
        "https://www.heritage.org/report/the-subprime-mortgage-market-collapse-primer-the-causes-and-possible-solutions",
        "https://www.ebsco.com/research-starters/economics/subprime-mortgage-crisis",
        "https://www.stlouisfed.org/~/media/files/pdfs/banking/spa_2007_05.pdf",
        "https://predatorylending.duke.edu/business-analysis/evolution-of-mortgage-lending/subprime-lending/",
        "https://en.wikipedia.org/wiki/Subprime_mortgage_crisis",
        "https://www.fdic.gov/media/18636",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC10009346/",
        "https://www.youtube.com/watch?v=ofVzJIW7dms",
        "https://www.cato.org/policy-report/january/february-2009/lessons-subprime-crisis"
      ],
      "object": "chat.completion",
      "search_results": [
        {
          "title": "The Subprime Mortgage Market Collapse: A Primer on the Causes ...",
          "url": "https://www.heritage.org/report/the-subprime-mortgage-market-collapse-primer-the-causes-and-possible-solutions",
          "date": "2008-04-22",
          "last_updated": "2026-03-28",
          "snippet": "Economic Adversity. In some cases, economic adversity has been an important contributing factor in mortgage defaults and foreclosures, notably in the ...",
          "source": "web"
        },
        {
          "title": "Subprime mortgage crisis | Economics | Research Starters - EBSCO",
          "url": "https://www.ebsco.com/research-starters/economics/subprime-mortgage-crisis",
          "date": "2022-01-01",
          "last_updated": "2026-05-24",
          "snippet": "Fueled by low interest rates and relaxed lending standards, banks began issuing a high volume of subprime mortgages to borrowers with poor credit histories, ...",
          "source": "web"
        },
        {
          "title": "[PDF] Understanding the Subprime Mortgage Crisis",
          "url": "https://www.stlouisfed.org/~/media/files/pdfs/banking/spa_2007_05.pdf",
          "date": null,
          "last_updated": "2026-04-20",
          "snippet": "We focus on first-lien loans and consider the 2001 through 2008 sample period. We first discuss the main characteristics of the loans in our database at ...",
          "source": "web"
        },
        {
          "title": "Subprime Lending - American Predatory Lending",
          "url": "https://predatorylending.duke.edu/business-analysis/evolution-of-mortgage-lending/subprime-lending/",
          "date": null,
          "last_updated": "2026-05-11",
          "snippet": "The emergence of these mortgage types was one of many contributing factors to the housing bubble that set the stage for the 2008 financial crisis. After ...",
          "source": "web"
        },
        {
          "title": "Subprime mortgage crisis - Wikipedia",
          "url": "https://en.wikipedia.org/wiki/Subprime_mortgage_crisis",
          "date": "2007-03-15",
          "last_updated": "2026-05-18",
          "snippet": "A continuous buildup of toxic assets in the form of subprime mortgages acted as a catalyst for the Great Recession in the United States. The collapse of the ...",
          "source": "web"
        },
        {
          "title": "[PDF] Origins of the Crisis - FDIC",
          "url": "https://www.fdic.gov/media/18636",
          "date": null,
          "last_updated": "2026-05-06",
          "snippet": "The U.S. financial crisis of 2008 followed a boom and bust cycle in the housing market that originated several years earlier and exposed vulnerabilities in ...",
          "source": "web"
        },
        {
          "title": "Financial production and the subprime mortgage crisis - PMC - NIH",
          "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10009346/",
          "date": "2023-03-13",
          "last_updated": "2026-04-12",
          "snippet": "The causes of the 2007-8 subprime crisis continue to be the subject of much debate, with explanations ranging from de-regulation and fraudulent behavior to ...",
          "source": "web"
        },
        {
          "title": "The Subprime Mortgage Crisis - Causes and Lessons Learned",
          "url": "https://www.youtube.com/watch?v=ofVzJIW7dms",
          "date": "2021-06-29",
          "last_updated": "2026-03-25",
          "snippet": "Visit us at https://lawshelf.com to earn college credit for only $20 a credit! We now offer multi-packs, which allow you to purchase 5 exams ...",
          "source": "web"
        },
        {
          "title": "Lessons from the Subprime Crisis | Cato Institute",
          "url": "https://www.cato.org/policy-report/january/february-2009/lessons-subprime-crisis",
          "date": "2012-08-13",
          "last_updated": "2026-04-03",
          "snippet": "Policies to encourage affordable housing fostered the growth of subprime lending and complex financial products to finance that lending.",
          "source": "web"
        }
      ],
      "status": null,
      "type": null,
      "usage": {
        "completion_tokens": 1929,
        "cost": {
          "input_tokens_cost": 9e-05,
          "output_tokens_cost": 0.02894,
          "total_cost": 0.03503,
          "citation_tokens_cost": null,
          "reasoning_tokens_cost": null,
          "request_cost": 0.006,
          "search_queries_cost": null
        },
        "prompt_tokens": 30,
        "total_tokens": 1959,
        "citation_tokens": null,
        "num_search_queries": null,
        "reasoning_tokens": null,
        "search_context_size": "low"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Warning>
  Selecting `"high"` increases search costs due to more extensive web retrieval. Use `"low"` when cost efficiency is critical.
</Warning>

## Search Control

Control when web search is performed using the search classifier or by disabling search entirely.

**Key parameters:**

* `enable_search_classifier`: Let AI decide when to search (boolean)
* `disable_search`: Disable web search completely (boolean)

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Search classifier (AI decides when to search)
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What is the difference between superconducting, trapped-ion, and photonic qubit architectures?"}],
    enable_search_classifier=True
)

# Disable search completely
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "What is 2 + 2?"}],
    disable_search=True
)
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "5ca2fa94-7a99-436d-9ff1-8568f0166f4f",
    "choices": [
      {
        "delta": {
          "content": "",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "index": 0,
        "message": {
          "content": "Here’s the high-level difference among the three qubit architectures:\n\n## 1) Superconducting qubits\n- **What they are:** Tiny circuits made from superconducting materials, usually involving **Josephson junctions**.\n- **How they work:** Information is stored in microwave-frequency quantum states of the circuit.\n- **Control:** Driven with **microwave pulses**.\n- **Strengths:**\n  - Very fast gate operations\n  - Mature chip-fabrication style technology\n  - Good for scalable, on-chip integration\n- **Weaknesses:**\n  - Shorter coherence times than trapped ions\n  - Sensitive to noise and materials imperfections\n  - Connectivity is often limited to near-neighbor qubits\n\n## 2) Trapped-ion qubits\n- **What they are:** Individual **ions** held in place by electromagnetic fields.\n- **How they work:** Quantum information is stored in internal atomic states of the ions.\n- **Control:** Manipulated mainly with **lasers**.\n- **Strengths:**\n  - Very long coherence times\n  - High-fidelity gates\n  - Often **all-to-all connectivity** in small systems\n- **Weaknesses:**\n  - Gates are slower than superconducting qubits\n  - Hardware is more complex and harder to scale\n  - Large systems require sophisticated ion-shuttling or photonic linking schemes\n\n## 3) Photonic qubits\n- **What they are:** Qubits encoded in **photons**.\n- **How they work:** Quantum information is stored in properties of light, such as polarization, path, or time-bin.\n- **Control:** Uses **optical components** like beam splitters, phase shifters, and detectors.\n- **Strengths:**\n  - Excellent for communication and networking\n  - Photons are robust against some types of decoherence\n  - Can operate at or near room temperature in some setups\n- **Weaknesses:**\n  - Two-qubit gates are difficult because photons don’t naturally interact strongly\n  - Building large-scale universal photonic computers is challenging\n  - Often relies on probabilistic operations or measurement-based schemes\n\n## Simple comparison\n- **Superconducting:** fast, chip-based, but noisier\n- **Trapped-ion:** precise, long-lived, but slower\n- **Photonic:** great for transmitting quantum information, but harder to make qubits interact\n\n## Rule of thumb\n- If you want **speed and chip integration**: superconducting\n- If you want **high fidelity and long coherence**: trapped-ion\n- If you want **quantum communication or light-based computing**: photonic\n\nIf you want, I can also give you a **table comparing coherence time, gate speed, connectivity, and scalability** for these three.",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779391592,
    "model": "sonar-pro",
    "citations": [
      "https://www.pnas.org/doi/10.1073/pnas.1618020114",
      "https://pennylane.ai/qml/demos/tutorial_trapped_ions",
      "https://iontrap.duke.edu/2017/03/13/trapped-ions-vs-superconductors/",
      "https://www.youtube.com/watch?v=floIDDd6ZXA",
      "https://www.spinquanta.com/news-detail/main-types-of-qubits",
      "https://pubs.aip.org/avs/aqs/article/3/3/033801/570603/Comparison-of-cloud-based-ion-trap-and"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "Experimental comparison of two quantum computing architectures",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1618020114",
        "date": "2017-03-28",
        "last_updated": "2026-05-19",
        "snippet": "Whereas the superconducting system offers faster gate clock speeds and a solid-state platform, the ion-trap system features superior qubits and reconfigurable ...",
        "source": "web"
      },
      {
        "title": "Trapped ion quantum computers | PennyLane Demos",
        "url": "https://pennylane.ai/qml/demos/tutorial_trapped_ions",
        "date": "2021-11-09",
        "last_updated": "2026-05-16",
        "snippet": "Trapped ions have relatively long coherence times, which means that the qubits are long-lived. Moreover, they can easily interact with their ...",
        "source": "web"
      },
      {
        "title": "Trapped Ions vs. Superconductors",
        "url": "https://iontrap.duke.edu/2017/03/13/trapped-ions-vs-superconductors/",
        "date": "2017-03-13",
        "last_updated": "2026-03-10",
        "snippet": "The performance is seen to mirror the connectivity of the systems, with the ion trap system out-performing the superconducting system on all ...",
        "source": "web"
      },
      {
        "title": "Superconducting Qubits vs Trapped Ions. Ilya Besedin and Moritz ...",
        "url": "https://www.youtube.com/watch?v=floIDDd6ZXA",
        "date": "2023-11-15",
        "last_updated": "2025-10-23",
        "snippet": "Dr. Ilya Besedin is a PostDoc in the Quantum Device Lab at ETH Zurich. He is working in quantum computing based on superconducting circuits.",
        "source": "web"
      },
      {
        "title": "9 Types of Qubits Driving Quantum Computing Forward [2025] - SpinQ",
        "url": "https://www.spinquanta.com/news-detail/main-types-of-qubits",
        "date": "2025-03-28",
        "last_updated": "2026-05-09",
        "snippet": "Trapped ion qubits are based on individual ions (charged atoms) that are trapped in electromagnetic fields. Quantum information is stored in the ...",
        "source": "web"
      },
      {
        "title": "Comparison of cloud-based ion trap and superconducting quantum ...",
        "url": "https://pubs.aip.org/avs/aqs/article/3/3/033801/570603/Comparison-of-cloud-based-ion-trap-and",
        "date": "2021-09-29",
        "last_updated": "2025-02-14",
        "snippet": "Superconducting systems generally have fewer connections because of the two-dimensional wiring between nearest-neighbor Josephson junctions. On ...",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 579,
      "cost": {
        "input_tokens_cost": 6e-05,
        "output_tokens_cost": 0.00869,
        "total_cost": 0.01474,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 20,
      "total_tokens": 599,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

<Warning>
  Pricing remains the same regardless of whether search is triggered. Search control is for performance optimization, not cost reduction.
</Warning>

## Combining Filters

You can combine multiple filters for precise control over search results:

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Combine domain, language, date, and context size filters
completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[{"role": "user", "content": "Explain what quantum error correction is and why it is essential for fault-tolerant quantum computing."}],
    search_domain_filter=["nature.com", "science.org", "arxiv.org"],
    search_language_filter=["en", "de"],
    search_recency_filter="month",
    web_search_options={"search_context_size": "high"}
)
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "74bf0b53-1c08-4d5a-bcf9-8d87acc51944",
    "choices": [
      {
        "delta": {
          "content": "",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "index": 0,
        "message": {
          "content": "Quantum error correction (QEC) is a set of techniques that **encode one “logical” qubit into many “physical” qubits** so that errors from noise and decoherence can be *detected and corrected without measuring or destroying the quantum information*.[1][2][6] It is essential for **fault‑tolerant quantum computing** because, without it, the high error rates of physical qubits make long or large‑scale quantum algorithms effectively impossible.[2][3][7]\n\n### What quantum error correction is\n\n- **Basic idea**  \n  Quantum error correction protects quantum information from **decoherence, noise, and imperfect operations** by spreading the information of a single qubit across an entangled state of many qubits, forming a **quantum error‑correcting code (QECC)**.[1][6][7]  \n  The encoded qubit is called a **logical qubit**, and the underlying qubits are **physical qubits**.[2][6]\n\n- **How it works (conceptual steps)**[1][6][7]  \n  1. **Encoding**: Extra **ancilla** (helper) qubits are added and an encoding circuit maps a single‑qubit state into a special subspace of a larger Hilbert space (the code space).[1]  \n  2. **Storage / computation**: The encoded logical qubits undergo gates and idle time, during which **local errors** (bit flips, phase flips, or combinations) may occur on some physical qubits.[1][4]  \n  3. **Syndrome measurement and recovery**: Carefully designed measurements (often “stabilizer” measurements) extract an **error syndrome**—information about *which error occurred*—without revealing the encoded quantum state itself.[1][3][4] Based on the syndrome, a **recovery operation** is applied to correct the error and return the state to the code space.[1][4][7]\n\n- **Key properties that make QEC possible**  \n  - **Digitization of errors**: Although physical noise is continuous, QEC theory shows that it is enough to correct a finite set of basic errors (typically Pauli \\(X\\), \\(Z\\), and \\(Y\\)); any small error can be decomposed into these and is effectively corrected if those are corrected.[4][5]  \n  - **No‑cloning workaround**: Because we cannot copy an unknown quantum state, QEC uses **entanglement** and **indirect measurements** of stabilizers (not of the qubit itself) to detect errors without collapsing superpositions.[1][3][4]  \n  - **Stabilizer codes**: Many practical codes (e.g., Shor code, surface code) are **stabilizer codes**, defined by a set of commuting operators whose joint +1 eigenspace is the code space.[1][4] Measuring stabilizers gives error syndromes.\n\n### Why QEC is essential for fault‑tolerant quantum computing\n\n- **Physical qubits are very noisy**  \n  Real qubits suffer from **decoherence, control errors, crosstalk, and imperfect measurements**, with error rates far above what is acceptable for large algorithms.[2][3][7] Even a single uncorrected error can invalidate an entire computation, and long algorithms require **millions to trillions of gate operations**.[2][7] Without protection, errors accumulate faster than we can compute.\n\n- **From noisy physical qubits to reliable logical qubits**  \n  QEC allows us to construct **logical qubits whose effective error rate is much lower** than that of the underlying physical qubits, by adding redundancy and performing continuous error detection and correction.[2][3][6][7]  \n  By increasing the code size (more physical qubits per logical qubit), the logical error rate can, in principle, be **suppressed arbitrarily**, as long as physical error rates are below a certain **fault‑tolerance threshold**.[4][8]\n\n- **Fault tolerance vs. error correction**  \n  - **Quantum error correction**: A scheme for protecting encoded information from noise by detecting and correcting errors.[1][7]  \n  - **Fault tolerance**: Builds on QEC to ensure that **errors anywhere in the circuit—including during gates, measurements, and syndrome extraction—do not spread uncontrollably or overwhelm the code**.[1][4][7] Fault‑tolerant designs require that each logical gate, measurement, and QEC step is implemented so that a small number of physical faults leads to at most a bounded number of logical errors.[4][7]  \n  To build a **useful large‑scale quantum computer**, we need **fault tolerance, not just passive error protection**, and fault tolerance fundamentally relies on QEC.[3][4][7][8]\n\n- **Enabling long and large‑scale algorithms**  \n  Many promising quantum algorithms (e.g., quantum chemistry, materials simulation, breaking large‑key cryptosystems) demand **deep circuits with enormous operation counts**. Hardware improvements alone are unlikely to reduce raw physical error rates enough to run these algorithms reliably.[7][8]  \n  QEC is therefore seen as **the foundational technology** that will turn today’s “fragile demonstrations” into **reliable, industrial‑scale quantum machines**.[2][6][7]\n\n### Intuitive comparison to classical error correction\n\n- In **classical** systems, we add redundancy (e.g., repetition codes, parity bits) to detect and correct bit‑flip errors.  \n- In the **quantum** case, we must handle:\n  - More kinds of errors (bit flip, phase flip, combinations, and general noise)[1][4]  \n  - The **no‑cloning theorem**, which forbids copying unknown quantum states  \n  - The risk that **measurements collapse superpositions**, destroying the computation  \n  QEC overcomes these obstacles by using **entangled codewords and syndrome measurements** that reveal *only* error information, not the encoded logical state.[1][3][4]\n\nIf you’d like, I can next walk through a concrete example like the **Shor code** or the **surface code** to illustrate how a specific quantum error‑correcting code detects and corrects errors step by step.",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779896036,
    "model": "sonar-pro",
    "citations": [
      "https://en.wikipedia.org/wiki/Quantum_error_correction",
      "https://www.quera.com/quantum-error-correction",
      "https://www.ibm.com/quantum/blog/quantum-error-suppression-mitigation-correction",
      "https://iontrap.duke.edu/files/2025/03/arxiv_sub_v2.pdf",
      "https://www.youtube.com/watch?v=OoQSdcKAIZc",
      "https://q-ctrl.com/topics/what-is-quantum-error-correction",
      "https://www.riverlane.com/quantum-error-correction",
      "https://arxiv.org/abs/1907.11157",
      "https://thequantuminsider.com/2026/03/16/understanding-quantum-error-correction/"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "Quantum error correction - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Quantum_error_correction",
        "date": "2004-08-11",
        "last_updated": "2026-04-18",
        "snippet": "Quantum error correction (QEC) comprises a set of techniques used in quantum memory and quantum computing to protect quantum information from errors arising ...",
        "source": "web"
      },
      {
        "title": "Quantum Error Correction - QuEra",
        "url": "https://www.quera.com/quantum-error-correction",
        "date": "2026-05-19",
        "last_updated": "2026-05-26",
        "snippet": "Quantum Error Correction (QEC) is the essential foundation of moving quantum computing from fragile demonstrations to reliable, industrial-scale machines.",
        "source": "web"
      },
      {
        "title": "Differences in error suppression, mitigation, and correction - IBM",
        "url": "https://www.ibm.com/quantum/blog/quantum-error-suppression-mitigation-correction",
        "date": "2022-10-20",
        "last_updated": "2025-09-21",
        "snippet": "Error correction is how we hope to achieve our ultimate goal: fault-tolerant quantum computation, where we build up redundancies so that even if ...",
        "source": "web"
      },
      {
        "title": "[PDF] Quantum error correction : an introductory guide",
        "url": "https://iontrap.duke.edu/files/2025/03/arxiv_sub_v2.pdf",
        "date": null,
        "last_updated": "2026-05-25",
        "snippet": "Quantum error correction protocols will play a central role in the realisation of quantum computing; the choice of error correction code will influence the ...",
        "source": "web"
      },
      {
        "title": "Correcting Quantum Errors | Lesson 13 - YouTube",
        "url": "https://www.youtube.com/watch?v=OoQSdcKAIZc",
        "date": "2024-11-13",
        "last_updated": "2026-03-25",
        "snippet": "... quantum.ibm.com/course/foundations-of-quantum-error-correction/correcting-quantum-errors #qiskit #ibmquantum #learnquantum.",
        "source": "web"
      },
      {
        "title": "What is quantum error correction? | Q-CTRL",
        "url": "https://q-ctrl.com/topics/what-is-quantum-error-correction",
        "date": "2026-01-16",
        "last_updated": "2026-05-15",
        "snippet": "Quantum Error Correction - or QEC for short - is an algorithm known to identify and fix errors in quantum computers.",
        "source": "web"
      },
      {
        "title": "Quantum Error Correction: the grand challenge - Riverlane",
        "url": "https://www.riverlane.com/quantum-error-correction",
        "date": "2025-02-26",
        "last_updated": "2025-07-09",
        "snippet": "Quantum error correction is a set of techniques to protect the information stored in qubits from errors and decoherence caused by noise.",
        "source": "web"
      },
      {
        "title": "[1907.11157] Quantum Error Correction: An Introductory Guide - arXiv",
        "url": "https://arxiv.org/abs/1907.11157",
        "date": "2019-07-25",
        "last_updated": "2026-03-23",
        "snippet": "In this review, we provide an introductory guide to the theory and implementation of quantum error correction codes.",
        "source": "web"
      },
      {
        "title": "What Is Quantum Error Correction & How Does It Work",
        "url": "https://thequantuminsider.com/2026/03/16/understanding-quantum-error-correction/",
        "date": "2026-03-16",
        "last_updated": "2026-05-27",
        "snippet": "Quantum error correction is a set of techniques for protecting quantum information from errors caused by decoherence, noise, and imperfect ...",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 1306,
      "cost": {
        "input_tokens_cost": 6e-05,
        "output_tokens_cost": 0.01959,
        "total_cost": 0.02565,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 21,
      "total_tokens": 1327,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

## Next Steps

<Card title="Sonar Quickstart" icon="rocket" href="/docs/sonar/quickstart">
  Get started with the Sonar API and learn the basics
</Card>
