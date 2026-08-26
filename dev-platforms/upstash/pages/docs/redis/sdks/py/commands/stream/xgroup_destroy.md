---
title: "XGROUP DESTROY"
source: https://upstash.com/docs/redis/sdks/py/commands/stream/xgroup_destroy
path: docs/redis/sdks/py/commands/stream/xgroup_destroy
---

> Delete an entire consumer group.

## Arguments

<ParamField body="key" type="str" required>
  The key of the stream.
</ParamField>

<ParamField body="group" type="str" required>
  The consumer group name to destroy.
</ParamField>

## Response

<ResponseField type="int">
  Returns 1 if the group was destroyed, 0 if it didn't exist.
</ResponseField>

<RequestExample>
```py Destroy existing group
result = redis.xgroup_destroy("mystream", "mygroup")
```
</RequestExample>
