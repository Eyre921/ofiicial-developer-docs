---
title: "XINFO GROUPS"
source: https://upstash.com/docs/redis/sdks/py/commands/stream/xinfo_groups
path: docs/redis/sdks/py/commands/stream/xinfo_groups
---

> List all consumer groups for a stream.

## Arguments

<ParamField body="key" type="str" required>
  The key of the stream.
</ParamField>

## Response

<ResponseField type="List[List[Any]]">
  Returns a list of consumer group information. Each group is represented as a list of key-value pairs.
</ResponseField>

<RequestExample>
```py Get groups info
result = redis.xinfo_groups("mystream")
```
</RequestExample>

<ResponseExample>
```py
[
  ["name", "group1", "consumers", 2, "pending", 0, "last-delivered-id", "1638360173533-0"],
  ["name", "group2", "consumers", 0, "pending", 3, "last-delivered-id", "0-0"]
]
```
</ResponseExample>
