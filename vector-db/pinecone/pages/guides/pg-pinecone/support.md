---
title: "pg_pinecone support"
source: https://docs.pinecone.io/guides/pg-pinecone/support
path: guides/pg-pinecone/support
---

Check a pg_pinecone install with pinecone.doctor(), ask questions in the Pinecone Discord community, and report bugs or request features in GitHub issues.

* **Questions and feedback**: Ask in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH), where other users and the Pinecone team answer.
* **Bugs and feature requests**: Open an issue in the [pg_pinecone repository](https://github.com/pinecone-io/pg_pinecone/issues). To propose a code change, open an issue first so the approach can be agreed on before any work starts.
* **Security issues**: Don't open a public issue. Email [security@pinecone.io](mailto:security@pinecone.io), or follow the [security policy](https://github.com/pinecone-io/pg_pinecone/blob/main/SECURITY.md) to report it privately on GitHub.
* **Your Pinecone account or index**: For a problem with the Pinecone index that the `remote` engine or full-text search uses, [contact Pinecone Support](/admin/support/contact-support).

## Check your install

When something doesn't work, run `pinecone.doctor()` first. It checks your install and says how to fix each problem it finds.

1. If you upgraded from a version earlier than 0.13.0, update the extension so `pinecone.doctor()` is available:

   ```sql SQL theme={null}
   ALTER EXTENSION pg_pinecone UPDATE;
   ```

2. Run the check. This query lists only the checks that need attention, so no rows means everything passed:

   ```sql SQL theme={null}
   SELECT check_name, status, detail, hint FROM pinecone.doctor() WHERE status <> 'ok';
   ```

3. For each row, the `hint` column says how to fix that check. Fix rows with a `status` of `fail` first. Some `warn` rows are expected. For example, without an API key, the `credentials` check reports `warn`, which is fine if you bring your own vectors and use only the `native` engine.

On a server that can't reach Pinecone, run `pinecone.doctor(remote => false)` to skip the request to Pinecone.

### Check reference

| Check | What it looks at |
| - | - |
| `version` | Whether the loaded library matches the installed extension version |
| `shared_preload_libraries` | Whether the setting includes `pg_pinecone` |
| `pgvector` | Whether pgvector is installed in this database |
| `credentials` | Which API key the session uses, without showing the key |
| `control_plane_url` | Whether the URL that key goes to uses `https://`, or `http://` to `localhost` |
| `reachability` | One request to Pinecone with that key. If it fails, `detail` starts with `network:` (no answer), `auth:` (key refused), or `plan or permission:` (not allowed) |
| `outbox` | Whether queued writes are being delivered |
| `failed_partitions` | Partitions that Pinecone refused |
| `worker` | Whether the background worker is running |

The function runs with your role's permissions. A check your role can't read reports `warn`, not `fail`.

## Report a bug

When you report a bug, include:

* Your pg_pinecone and Postgres versions
* Your operating system
* The table's engine
* The full error message
* The output of `pinecone.doctor()`

To find the versions, run:

```sql SQL theme={null}
SELECT extversion FROM pg_extension WHERE extname = 'pg_pinecone';
SELECT version();
```
