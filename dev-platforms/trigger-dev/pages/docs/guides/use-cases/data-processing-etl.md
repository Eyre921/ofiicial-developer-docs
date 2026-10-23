---
title: "Data processing & ETL workflows"
source: https://trigger.dev/docs/guides/use-cases/data-processing-etl
path: docs/guides/use-cases/data-processing-etl
---

Learn how to use Trigger.dev for data processing and ETL (Extract, Transform, Load), including web scraping, database synchronization, batch enrichment and more.

## Overview

Build complex data pipelines that process large datasets without timeouts. Handle streaming analytics, batch enrichment, web scraping, database sync, and file processing with automatic retries and progress tracking.

## Featured examples

> **[Realtime CSV importer](/docs/guides/example-projects/realtime-csv-importer)**
>
> Import CSV files with progress streamed live to frontend.

> **[Web scraper with BrowserBase](/docs/guides/examples/scrape-hacker-news)**
>
> Scrape websites using BrowserBase and Puppeteer.

> **[Supabase database webhooks](/docs/guides/frameworks/supabase-edge-functions-database-webhooks)**
>
> Trigger tasks from Supabase database webhooks.

## Benefits of using Trigger.dev for data processing & ETL workflows

**Process datasets for hours without timeouts:** Handle multi-hour transformations, large file processing, or complete database exports. No execution time limits.

**Parallel processing with built-in rate limiting:** Process thousands of records simultaneously while respecting API rate limits. Scale efficiently without overwhelming downstream services.

**Stream progress to your users in real-time:** Show row-by-row processing status updating live in your dashboard. Users see exactly where processing is and how long remains.

## Production use cases

> **[MagicSchool AI customer story](https://trigger.dev/customers/magicschool-ai-customer-story)**
>
> Read how MagicSchool AI uses Trigger.dev to generate insights from millions of student interactions.

> **[Comp AI customer story](https://trigger.dev/customers/comp-ai-customer-story)**
>
> Read how Comp AI uses Trigger.dev to automate evidence collection at scale, powering their open source, AI-driven compliance platform.

> **[Midday customer story](https://trigger.dev/customers/midday-customer-story)**
>
> Read how Midday use Trigger.dev to sync large volumes of bank transactions in their financial management platform.

## Example workflow patterns

**CSV file import**

Simple CSV import pipeline. Receives file upload, parses CSV rows, validates data, imports to database with progress tracking.

```mermaid theme={"theme":"css-variables"}
graph TB
    A[importCSV] --> B[parseCSVFile]
    B --> C[validateRows]
    C --> D[bulkInsertToDB]
    D --> E[notifyCompletion]
```

**Multi-source ETL pipeline**

**Coordinator pattern with parallel extraction**. Batch triggers parallel extraction from multiple sources (APIs, databases, S3), transforms and validates data, loads to data warehouse with monitoring.

```mermaid theme={"theme":"css-variables"}
graph TB
    A[runETLPipeline] --> B[coordinateExtraction]
    B --> C[batchTriggerAndWait]

    C --> D[extractFromAPI]
    C --> E[extractFromDatabase]
    C --> F[extractFromS3]

    D --> G[transformData]
    E --> G
    F --> G

    G --> H[validateData]
    H --> I[loadToWarehouse]
```

**Parallel web scraping**

**Coordinator pattern with browser automation**. Launches headless browsers in parallel to scrape multiple pages, extracts structured data, cleans and normalizes content, stores in database.

```mermaid theme={"theme":"css-variables"}
graph TB
    A[scrapeSite] --> B[coordinateScraping]
    B --> C[batchTriggerAndWait]

    C --> D[scrapePage1]
    C --> E[scrapePage2]
    C --> F[scrapePageN]

    D --> G[cleanData]
    E --> G
    F --> G

    G --> H[normalizeData]
    H --> I[storeInDatabase]
```

**Batch data enrichment**

**Coordinator pattern with rate limiting**. Fetches records needing enrichment, batch triggers parallel API calls with configurable concurrency to respect rate limits, validates enriched data, updates database.

```mermaid theme={"theme":"css-variables"}
graph TB
    A[enrichRecords] --> B[fetchRecordsToEnrich]
    B --> C[coordinateEnrichment]
    C --> D[batchTriggerAndWait]

    D --> E[enrichRecord1]
    D --> F[enrichRecord2]
    D --> G[enrichRecordN]

    E --> H[validateEnrichedData]
    F --> H
    G --> H

    H --> I[updateDatabase]
```

## Featured use cases

> **[Data processing & ETL workflows](/docs/guides/use-cases/data-processing-etl)**
>
> Build complex data pipelines that process large datasets without timeouts.

> **[Media processing workflows](/docs/guides/use-cases/media-processing)**
>
> Batch process videos, images, audio, and documents with no execution time limits.

> **[AI media generation workflows](/docs/guides/use-cases/media-generation)**
>
> Generate images, videos, audio, documents and other media using AI models.

> **[Marketing workflows](/docs/guides/use-cases/marketing)**
>
> Build drip campaigns, create marketing content, and orchestrate multi-channel campaigns.
