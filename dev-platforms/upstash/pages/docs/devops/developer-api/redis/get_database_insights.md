---
title: "Get Database Insights"
source: https://upstash.com/docs/devops/developer-api/redis/get_database_insights
path: docs/devops/developer-api/redis/get_database_insights
---

/devops/developer-api/openapi.yaml get /redis/insights/{id}
This endpoint returns the Insights series of a database: service latency percentiles, read, write, engine, replication, lock-wait and Lua latency, expired entries, replication lag, throughput, bandwidth and disk size, for the whole database, one replica or every region, with each series' latest window compared to the one before it, and how much the limit, security and Lua counters grew over the period. Latencies are in milliseconds. Available for databases on a Pro plan or with the Production Pack.
