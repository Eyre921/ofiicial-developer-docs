---
title: "Advanced"
source: https://upstash.com/docs/redis/sdks/ts/advanced
path: docs/redis/sdks/ts/advanced
---

## Disable automatic serialization

Your data is (de)serialized as `json` by default. This works for most use cases
but you can disable it if you want:

```ts
const redis = new Redis({
  // ...
  automaticDeserialization: false,
});

// or
const redis = Redis.fromEnv({
  automaticDeserialization: false,
});
```

This probably breaks quite a few types, but it's a first step in that direction.
Please report bugs and broken types
[here](https://github.com/upstash/upstash-redis/issues/49).

## Keep-Alive

`@upstash/redis` optimizes performance by reusing connections wherever possible, reducing latency.
This is achieved by keeping the client in memory instead of reinitializing it with each new function invocation.
As a result, when a hot lambda function receives a new request, it uses the already initialized client, allowing for the reuse of existing connections to Upstash.

<Tip>This functionality is enabled by default.</Tip>

## Request Timeout

You can configure the SDK so that it will throw an error if the request takes longer than a specified time.

You can achieve this using the signal parameter like this:

```ts
const redis = new Redis({
  url: "<UPSTASH_REDIS_REST_URL>",
  token: "<UPSTASH_REDIS_REST_TOKEN>",
  // set a timeout of 1 second
  signal: () => AbortSignal.timeout(1000),
});

try {
  await redis.get( ... )
} catch (error) {
  if (error.name === "TimeoutError") {
    console.error("Request timed out");
  } else {
    console.error("An error occurred:", error);
  }
}
```

## Telemetry

This library sends anonymous telemetry data to help us improve your experience.
We collect the following:

* SDK version
* Platform (Deno, Cloudflare, Vercel)
* Runtime version (node@18.x)

You can opt out by setting the `UPSTASH_DISABLE_TELEMETRY` environment variable
to any truthy value.

```sh
UPSTASH_DISABLE_TELEMETRY=1
```

Alternatively, you can pass `enableTelemetry: false` when initializing the Redis client:

```ts
const redis = new Redis({
  // ...,
  enableTelemetry: false,
});
```

- [ECHO](https://upstash.com/docs/redis/sdks/ts/commands/auth/echo.md)
- [PING](https://upstash.com/docs/redis/sdks/ts/commands/auth/ping.md): Send a ping to the server and get a response if the server is alive.
- [BITCOUNT](https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitcount.md): Count the number of set bits.
- [BITOP](https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitop.md): Perform bitwise operations between strings.
- [BITPOS](https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitpos.md): Find the position of the first set or clear bit (bit with a value of 1 or 0) in a Redis string key.
- [GETBIT](https://upstash.com/docs/redis/sdks/ts/commands/bitmap/getbit.md): Retrieve a single bit.
- [SETBIT](https://upstash.com/docs/redis/sdks/ts/commands/bitmap/setbit.md): Set a single bit in a string.
- [CLIENT SETINFO](https://upstash.com/docs/redis/sdks/ts/commands/connection/client_setinfo.md): Set client library name and version information.
- [FCALL](https://upstash.com/docs/redis/sdks/ts/commands/functions/call.md): Invoke a function.
- [FCALL_RO](https://upstash.com/docs/redis/sdks/ts/commands/functions/call_ro.md): Invoke a read-only function
- [FUNCTION DELETE](https://upstash.com/docs/redis/sdks/ts/commands/functions/delete.md): Delete a library and all its functions.
- [FUNCTION FLUSH](https://upstash.com/docs/redis/sdks/ts/commands/functions/flush.md): Delete all the libraries and functions.
- [FUNCTION LIST](https://upstash.com/docs/redis/sdks/ts/commands/functions/list.md): List details about the registered libraries and functions.
- [FUNCTION LOAD](https://upstash.com/docs/redis/sdks/ts/commands/functions/load.md): Load a library to Redis.
- [FUNCTION STATS](https://upstash.com/docs/redis/sdks/ts/commands/functions/stats.md): Return information about the function running engine.
- [DEL](https://upstash.com/docs/redis/sdks/ts/commands/generic/del.md): Removes the specified keys. A key is ignored if it does not exist.
- [EXISTS](https://upstash.com/docs/redis/sdks/ts/commands/generic/exists.md): Check if a key exists.
- [EXPIRE](https://upstash.com/docs/redis/sdks/ts/commands/generic/expire.md): Sets a timeout on key. The key will automatically be deleted.
- [EXPIREAT](https://upstash.com/docs/redis/sdks/ts/commands/generic/expireat.md): Sets a timeout on key. The key will automatically be deleted.
- [KEYS](https://upstash.com/docs/redis/sdks/ts/commands/generic/keys.md): Returns all keys matching pattern.
- [PERSIST](https://upstash.com/docs/redis/sdks/ts/commands/generic/persist.md): Remove any timeout set on the key.
- [PEXPIRE](https://upstash.com/docs/redis/sdks/ts/commands/generic/pexpire.md): Sets a timeout on key. After the timeout has expired, the key will automatically be deleted.
- [PEXPIREAT](https://upstash.com/docs/redis/sdks/ts/commands/generic/pexpireat.md): Sets a timeout on key. After the timeout has expired, the key will automatically be deleted.
- [PTTL](https://upstash.com/docs/redis/sdks/ts/commands/generic/pttl.md): Return the expiration in milliseconds of a key.
- [RANDOMKEY](https://upstash.com/docs/redis/sdks/ts/commands/generic/randomkey.md): Returns a random key from database
- [RENAME](https://upstash.com/docs/redis/sdks/ts/commands/generic/rename.md): Rename a key
- [RENAMENX](https://upstash.com/docs/redis/sdks/ts/commands/generic/renamenx.md): Rename a key if it does not already exist.
- [SCAN](https://upstash.com/docs/redis/sdks/ts/commands/generic/scan.md): Scan the database for keys.
- [TOUCH](https://upstash.com/docs/redis/sdks/ts/commands/generic/touch.md): Alters the last access time of one or more keys
- [TTL](https://upstash.com/docs/redis/sdks/ts/commands/generic/ttl.md): Return the expiration in seconds of a key.
- [TYPE](https://upstash.com/docs/redis/sdks/ts/commands/generic/type.md): Get the type of a key.
- [UNLINK](https://upstash.com/docs/redis/sdks/ts/commands/generic/unlink.md): Removes the specified keys. A key is ignored if it does not exist.
- [HDEL](https://upstash.com/docs/redis/sdks/ts/commands/hash/hdel.md): Deletes one or more hash fields.
- [HEXISTS](https://upstash.com/docs/redis/sdks/ts/commands/hash/hexists.md): Checks if a field exists in a hash.
- [HEXPIRE](https://upstash.com/docs/redis/sdks/ts/commands/hash/hexpire.md): Sets an expiration time for one or more fields in a hash.
- [HEXPIREAT](https://upstash.com/docs/redis/sdks/ts/commands/hash/hexpireat.md): Sets an expiration time for field(s) in a hash in seconds since the Unix epoch.
- [HEXPIRETIME](https://upstash.com/docs/redis/sdks/ts/commands/hash/hexpiretime.md): Retrieves the expiration time of field(s) in a hash in seconds.
- [HGET](https://upstash.com/docs/redis/sdks/ts/commands/hash/hget.md): Retrieves the value of a hash field.
- [HGETALL](https://upstash.com/docs/redis/sdks/ts/commands/hash/hgetall.md): Retrieves all fields from a hash.
- [HGETDEL](https://upstash.com/docs/redis/sdks/ts/commands/hash/hgetdel.md): Get and delete hash fields atomically.
- [HGETEX](https://upstash.com/docs/redis/sdks/ts/commands/hash/hgetex.md): Get hash fields with expiration support.
- [HINCRBY](https://upstash.com/docs/redis/sdks/ts/commands/hash/hincrby.md): Increments the value of a hash field by a given amount
- [HINCRBYFLOAT](https://upstash.com/docs/redis/sdks/ts/commands/hash/hincrbyfloat.md): Increments the value of a hash field by a given float value.
- [HKEYS](https://upstash.com/docs/redis/sdks/ts/commands/hash/hkeys.md): Return all field names in the hash stored at key.
- [HLEN](https://upstash.com/docs/redis/sdks/ts/commands/hash/hlen.md): Returns the number of fields contained in the hash stored at key.
- [HMGET](https://upstash.com/docs/redis/sdks/ts/commands/hash/hmget.md): Return the requested fields and their values.
- [HPERSIST](https://upstash.com/docs/redis/sdks/ts/commands/hash/hpersist.md): Remove the expiration from one or more fields in a hash.
- [HPEXPIRE](https://upstash.com/docs/redis/sdks/ts/commands/hash/hpexpire.md): Sets an expiration time for a field in a hash in milliseconds.
- [HPEXPIREAT](https://upstash.com/docs/redis/sdks/ts/commands/hash/hpexpireat.md): Sets an expiration time for field(s) in a hash in milliseconds since the Unix epoch.
- [HPEXPIRETIME](https://upstash.com/docs/redis/sdks/ts/commands/hash/hpexpiretime.md): Retrieves the expiration time of a field in a hash in milliseconds.
- [HPTTL](https://upstash.com/docs/redis/sdks/ts/commands/hash/hpttl.md): Retrieves the remaining time-to-live (TTL) for field(s) in a hash in milliseconds.
- [HRANDFIELD](https://upstash.com/docs/redis/sdks/ts/commands/hash/hrandfield.md): Return a random field from a hash
- [HSCAN](https://upstash.com/docs/redis/sdks/ts/commands/hash/hscan.md): Scan a hash for fields.
- [HSET](https://upstash.com/docs/redis/sdks/ts/commands/hash/hset.md): Write one or more fields to a hash.
- [HSETEX](https://upstash.com/docs/redis/sdks/ts/commands/hash/hsetex.md): Set hash fields with expiration support.
- [HSETNX](https://upstash.com/docs/redis/sdks/ts/commands/hash/hsetnx.md): Write a field to a hash but only if the field does not exist.
- [HSTRLEN](https://upstash.com/docs/redis/sdks/ts/commands/hash/hstrlen.md): Returns the string length of a value in a hash.
- [HTTL](https://upstash.com/docs/redis/sdks/ts/commands/hash/httl.md): Retrieves the remaining time-to-live (TTL) for field(s) in a hash in seconds.
- [HVALS](https://upstash.com/docs/redis/sdks/ts/commands/hash/hvals.md): Returns all values in the hash stored at key.
- [JSON.ARRAPPEND](https://upstash.com/docs/redis/sdks/ts/commands/json/arrappend.md): Append values to the array at path in the JSON document at key.
- [JSON.ARRINDEX](https://upstash.com/docs/redis/sdks/ts/commands/json/arrindex.md): Search for the first occurrence of a JSON value in an array.
- [JSON.ARRINSERT](https://upstash.com/docs/redis/sdks/ts/commands/json/arrinsert.md): Insert the json values into the array at path before the index (shifts to the right).
- [JSON.ARRLEN](https://upstash.com/docs/redis/sdks/ts/commands/json/arrlen.md): Report the length of the JSON array at `path` in `key`.
- [JSON.ARRPOP](https://upstash.com/docs/redis/sdks/ts/commands/json/arrpop.md): Remove and return an element from the index in the array. By default the last element from an array is popped.
- [JSON.ARRTRIM](https://upstash.com/docs/redis/sdks/ts/commands/json/arrtrim.md): Trim an array so that it contains only the specified inclusive range of elements.
- [JSON.CLEAR](https://upstash.com/docs/redis/sdks/ts/commands/json/clear.md): Clear container values (arrays/objects) and set numeric values to 0.
- [JSON.DEL](https://upstash.com/docs/redis/sdks/ts/commands/json/del.md): Delete a key from a JSON document.
- [JSON.FORGET](https://upstash.com/docs/redis/sdks/ts/commands/json/forget.md): Delete a key from a JSON document.
- [JSON.GET](https://upstash.com/docs/redis/sdks/ts/commands/json/get.md): Get a single value from a JSON document.
- [JSON.MERGE](https://upstash.com/docs/redis/sdks/ts/commands/json/merge.md): Merges the JSON value at path in key with the provided value.
- [JSON.MGET](https://upstash.com/docs/redis/sdks/ts/commands/json/mget.md): Get the same path from multiple JSON documents.
- [JSON.MSET](https://upstash.com/docs/redis/sdks/ts/commands/json/mset.md): Sets multiple JSON values at multiple paths in multiple keys.
- [JSON.NUMINCRBY](https://upstash.com/docs/redis/sdks/ts/commands/json/numincrby.md): Increment the number value stored at `path` by number.
- [JSON.NUMMULTBY](https://upstash.com/docs/redis/sdks/ts/commands/json/nummultby.md): Multiply the number value stored at `path` by number.
- [JSON.OBJKEYS](https://upstash.com/docs/redis/sdks/ts/commands/json/objkeys.md): Return the keys in the object that`s referenced by path.
- [JSON.OBJLEN](https://upstash.com/docs/redis/sdks/ts/commands/json/objlen.md): Report the number of keys in the JSON object at `path` in `key`.
- [JSON.SET](https://upstash.com/docs/redis/sdks/ts/commands/json/set.md): Set the JSON value at path in key.
- [JSON.STRAPPEND](https://upstash.com/docs/redis/sdks/ts/commands/json/strappend.md): Append the json-string values to the string at path.
- [JSON.STRLEN](https://upstash.com/docs/redis/sdks/ts/commands/json/strlen.md): Report the length of the JSON String at path in key
- [JSON.TOGGLE](https://upstash.com/docs/redis/sdks/ts/commands/json/toggle.md): Toggle a boolean value stored at `path`.
- [JSON.TYPE](https://upstash.com/docs/redis/sdks/ts/commands/json/type.md): Report the type of JSON value at `path`.
- [LINDEX](https://upstash.com/docs/redis/sdks/ts/commands/list/lindex.md): Returns the element at index index in the list stored at key.
- [LINSERT](https://upstash.com/docs/redis/sdks/ts/commands/list/linsert.md): Insert an element before or after another element in a list
- [LLEN](https://upstash.com/docs/redis/sdks/ts/commands/list/llen.md): Returns the length of the list stored at key.
- [LMOVE](https://upstash.com/docs/redis/sdks/ts/commands/list/lmove.md): Move an element from one list to another.
- [LPOP](https://upstash.com/docs/redis/sdks/ts/commands/list/lpop.md): Remove and return the first element(s) of a list
- [LPOS](https://upstash.com/docs/redis/sdks/ts/commands/list/lpos.md): Returns the index of matching elements inside a list.
- [LPUSH](https://upstash.com/docs/redis/sdks/ts/commands/list/lpush.md): Push an element at the head of the list.
- [LPUSHX](https://upstash.com/docs/redis/sdks/ts/commands/list/lpushx.md): Push an element at the head of the list only if the list exists.
- [LRANGE](https://upstash.com/docs/redis/sdks/ts/commands/list/lrange.md): Returns the specified elements of the list stored at key.
- [LREM](https://upstash.com/docs/redis/sdks/ts/commands/list/lrem.md): Remove the first `count` occurrences of an element from a list.
- [LSET](https://upstash.com/docs/redis/sdks/ts/commands/list/lset.md): Set a value at a specific index.
- [LTRIM](https://upstash.com/docs/redis/sdks/ts/commands/list/ltrim.md): Trim a list to the specified range
- [RPOP](https://upstash.com/docs/redis/sdks/ts/commands/list/rpop.md): Remove and return the last element(s) of a list
- [RPUSH](https://upstash.com/docs/redis/sdks/ts/commands/list/rpush.md): Push an element at the end of the list.
- [RPUSHX](https://upstash.com/docs/redis/sdks/ts/commands/list/rpushx.md): Push an element at the end of the list only if the list exists.
- [Overview](https://upstash.com/docs/redis/sdks/ts/commands/overview.md): Available Commands in @upstash/redis
- [PSUBSCRIBE](https://upstash.com/docs/redis/sdks/ts/commands/pubsub/psubscribe.md): Subscribe to a channel by patterns/wildcards
- [PUBLISH](https://upstash.com/docs/redis/sdks/ts/commands/pubsub/publish.md): Publish a message to a channel
- [SUBSCRIBE](https://upstash.com/docs/redis/sdks/ts/commands/pubsub/subscribe.md): Subscribe to a channel
- [EVAL](https://upstash.com/docs/redis/sdks/ts/commands/scripts/eval.md): Evaluate a Lua script server side.
- [EVAL_RO](https://upstash.com/docs/redis/sdks/ts/commands/scripts/eval_ro.md): Evaluate a read-only Lua script server side.
- [EVALSHA](https://upstash.com/docs/redis/sdks/ts/commands/scripts/evalsha.md): Evaluate a cached Lua script server side.
- [EVALSHA_RO](https://upstash.com/docs/redis/sdks/ts/commands/scripts/evalsha_ro.md): Evaluate a cached read-only Lua script server side.
- [SCRIPT EXISTS](https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_exists.md): Check if scripts exist in the script cache.
- [SCRIPT FLUSH](https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_flush.md): Removes all scripts from the script cache.
- [SCRIPT LOAD](https://upstash.com/docs/redis/sdks/ts/commands/scripts/script_load.md): Load the specified Lua script into the script cache.
- [DBSIZE](https://upstash.com/docs/redis/sdks/ts/commands/server/dbsize.md): Count the number of keys in the database.
- [FLUSHALL](https://upstash.com/docs/redis/sdks/ts/commands/server/flushall.md)
- [FLUSHDB](https://upstash.com/docs/redis/sdks/ts/commands/server/flushdb.md)
- [SADD](https://upstash.com/docs/redis/sdks/ts/commands/set/sadd.md): Adds one or more members to a set.
- [SCARD](https://upstash.com/docs/redis/sdks/ts/commands/set/scard.md): Return how many members are in a set
- [SDIFF](https://upstash.com/docs/redis/sdks/ts/commands/set/sdiff.md): Return the difference between sets
- [SDIFFSTORE](https://upstash.com/docs/redis/sdks/ts/commands/set/sdiffstore.md): Write the difference between sets to a new set
- [SINTER](https://upstash.com/docs/redis/sdks/ts/commands/set/sinter.md): Return the intersection between sets
- [SINTERSTORE](https://upstash.com/docs/redis/sdks/ts/commands/set/sinterstore.md): Return the intersection between sets and store the resulting set in a key
- [SISMEMBER](https://upstash.com/docs/redis/sdks/ts/commands/set/sismember.md): Check if a member exists in a set
- [SMEMBERS](https://upstash.com/docs/redis/sdks/ts/commands/set/smembers.md): Return all the members of a set
- [SMISMEMBER](https://upstash.com/docs/redis/sdks/ts/commands/set/smismember.md): Check if multiple members exist in a set
- [SMOVE](https://upstash.com/docs/redis/sdks/ts/commands/set/smove.md): Move a member from one set to another
- [SPOP](https://upstash.com/docs/redis/sdks/ts/commands/set/spop.md): Removes and returns one or more random members from a set.
- [SRANDMEMBER](https://upstash.com/docs/redis/sdks/ts/commands/set/srandmember.md): Returns one or more random members from a set.
- [SREM](https://upstash.com/docs/redis/sdks/ts/commands/set/srem.md): Remove one or more members from a set
- [SSCAN](https://upstash.com/docs/redis/sdks/ts/commands/set/sscan.md): Scan a set
- [SUNION](https://upstash.com/docs/redis/sdks/ts/commands/set/sunion.md): Return the union between sets
- [SUNIONSTORE](https://upstash.com/docs/redis/sdks/ts/commands/set/sunionstore.md): Return the union between sets and store the resulting set in a key
- [XACK](https://upstash.com/docs/redis/sdks/ts/commands/stream/xack.md): Removes one or multiple messages from the pending entries list of a stream consumer group.
- [XACKDEL](https://upstash.com/docs/redis/sdks/ts/commands/stream/xackdel.md): Acknowledge and delete stream entries atomically.
- [XADD](https://upstash.com/docs/redis/sdks/ts/commands/stream/xadd.md): Appends one or more new entries to a stream.
- [XAUTOCLAIM](https://upstash.com/docs/redis/sdks/ts/commands/stream/xautoclaim.md): Changes the ownership of pending messages from one consumer to another in a stream consumer group.
- [XCLAIM](https://upstash.com/docs/redis/sdks/ts/commands/stream/xclaim.md): Changes the ownership of pending messages from one consumer to another in a stream consumer group.
- [XDEL](https://upstash.com/docs/redis/sdks/ts/commands/stream/xdel.md): Removes the specified entries from a stream, and returns the number of entries deleted.
- [XDELEX](https://upstash.com/docs/redis/sdks/ts/commands/stream/xdelex.md): Extended delete for streams with reference control.
- [XGROUP](https://upstash.com/docs/redis/sdks/ts/commands/stream/xgroup.md): Manage consumer groups for Redis streams.
- [XINFO](https://upstash.com/docs/redis/sdks/ts/commands/stream/xinfo.md): Returns information about streams, consumer groups, and consumers.
- [XLEN](https://upstash.com/docs/redis/sdks/ts/commands/stream/xlen.md): Returns the number of entries inside a stream.
- [XPENDING](https://upstash.com/docs/redis/sdks/ts/commands/stream/xpending.md): Returns information about pending messages in a stream consumer group.
- [XRANGE](https://upstash.com/docs/redis/sdks/ts/commands/stream/xrange.md): Returns stream entries matching a given range of IDs.
- [XREAD](https://upstash.com/docs/redis/sdks/ts/commands/stream/xread.md): Reads data from one or multiple streams, starting from the specified IDs.
- [XREADGROUP](https://upstash.com/docs/redis/sdks/ts/commands/stream/xreadgroup.md): Reads data from a stream as part of a consumer group.
- [XREVRANGE](https://upstash.com/docs/redis/sdks/ts/commands/stream/xrevrange.md): Returns stream entries matching a given range of IDs in reverse order.
- [XTRIM](https://upstash.com/docs/redis/sdks/ts/commands/stream/xtrim.md): Trims the stream by removing entries to keep it at a reasonable size.
- [String Commands](https://upstash.com/docs/redis/sdks/ts/commands/string.md)
- [APPEND](https://upstash.com/docs/redis/sdks/ts/commands/string/append.md): Append a value to a string stored at key.
- [DECR](https://upstash.com/docs/redis/sdks/ts/commands/string/decr.md): Decrement the integer value of a key by one
- [DECRBY](https://upstash.com/docs/redis/sdks/ts/commands/string/decrby.md): Decrement the integer value of a key by a given number.
- [GET](https://upstash.com/docs/redis/sdks/ts/commands/string/get.md): Return the value of the specified key or `null` if the key doesn't exist.
- [GETDEL](https://upstash.com/docs/redis/sdks/ts/commands/string/getdel.md): Return the value of the specified key and delete the key.
- [GETRANGE](https://upstash.com/docs/redis/sdks/ts/commands/string/getrange.md): Return a substring of value at the specified key.
- [GETSET](https://upstash.com/docs/redis/sdks/ts/commands/string/getset.md): Return the value of the specified key and replace it with a new value.
- [INCR](https://upstash.com/docs/redis/sdks/ts/commands/string/incr.md): Increment the integer value of a key by one
- [INCRBY](https://upstash.com/docs/redis/sdks/ts/commands/string/incrby.md): Increment the integer value of a key by a given number.
- [INCRBYFLOAT](https://upstash.com/docs/redis/sdks/ts/commands/string/incrbyfloat.md): Increment the float value of a key by a given number.
- [MGET](https://upstash.com/docs/redis/sdks/ts/commands/string/mget.md): Load multiple keys from Redis in one go.
- [MSET](https://upstash.com/docs/redis/sdks/ts/commands/string/mset.md): Set multiple keys in one go.
- [MSETNX](https://upstash.com/docs/redis/sdks/ts/commands/string/msetnx.md): Set multiple keys in one go unless they exist already.
- [SET](https://upstash.com/docs/redis/sdks/ts/commands/string/set.md): Set a key to hold a string value.
- [SETRANGE](https://upstash.com/docs/redis/sdks/ts/commands/string/setrange.md): Writes the value of key at offset.
- [STRLEN](https://upstash.com/docs/redis/sdks/ts/commands/string/strlen.md): Return the length of a string stored at a key.
- [Transactions](https://upstash.com/docs/redis/sdks/ts/commands/transaction.md): Transactions
- [ZADD](https://upstash.com/docs/redis/sdks/ts/commands/zset/zadd.md): Add a member to a sorted set, or update its score if it already exists.
- [ZCARD](https://upstash.com/docs/redis/sdks/ts/commands/zset/zcard.md): Returns the number of elements in the sorted set stored at key.
- [ZCOUNT](https://upstash.com/docs/redis/sdks/ts/commands/zset/zcount.md): Returns the number of elements in the sorted set stored at key filterd by score.
- [ZDIFFSTORE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zdiffstore.md): Writes the difference between sets to a new key.
- [ZINCRBY](https://upstash.com/docs/redis/sdks/ts/commands/zset/zincrby.md): Increment the score of a member.
- [ZINTERSTORE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zinterstore.md): Writes the intersection between sets to a new key.
- [ZLEXCOUNT](https://upstash.com/docs/redis/sdks/ts/commands/zset/zlexcount.md): Returns the number of elements in the sorted set stored at key filtered by lex.
- [ZMSCORE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zmscore.md): Returns the scores of multiple members.
- [ZPOPMAX](https://upstash.com/docs/redis/sdks/ts/commands/zset/zpopmax.md): Removes and returns up to count members with the highest scores in the sorted set stored at key.
- [ZPOPMIN](https://upstash.com/docs/redis/sdks/ts/commands/zset/zpopmin.md): Removes and returns up to count members with the lowest scores in the sorted set stored at key.
- [ZRANGE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zrange.md): Returns the specified range of elements in the sorted set stored at key.
- [ZRANK](https://upstash.com/docs/redis/sdks/ts/commands/zset/zrank.md): Returns the rank of a member
- [ZREM](https://upstash.com/docs/redis/sdks/ts/commands/zset/zrem.md): Remove one or more members from a sorted set
- [ZREMRANGEBYLEX](https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebylex.md): Remove all members in a sorted set between the given lexicographical range.
- [ZREMRANGEBYRANK](https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyrank.md): Remove all members in a sorted set between the given ranks.
- [ZREMRANGEBYSCORE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zremrangebyscore.md): Remove all members in a sorted set between the given scores.
- [ZREVRANK](https://upstash.com/docs/redis/sdks/ts/commands/zset/zrevrank.md): Returns the rank of a member in a sorted set, with scores ordered from high to low.
- [ZSCAN](https://upstash.com/docs/redis/sdks/ts/commands/zset/zscan.md): Scan a sorted set
- [ZSCORE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zscore.md): Returns the scores of a member.
- [ZUNIONSTORE](https://upstash.com/docs/redis/sdks/ts/commands/zset/zunionstore.md): Writes the union between sets to a new key.
