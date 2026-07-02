---
title: "ERR max key size exceeded"
source: https://upstash.com/docs/redis/troubleshooting/max_key_size_exceeded
path: docs/redis/troubleshooting/max_key_size_exceeded
---

### Symptom

The client gets an exception similar to:

```
ReplyError: ERR max key size exceeded. Limit: X bytes, Actual: Z bytes
```

### Diagnosis

Size of the key in the request exceeds the max key size limit, which is `32Kb`.

### Solution

This is a hardcoded limit and cannot be configured per database. You should
reduce the key size.
