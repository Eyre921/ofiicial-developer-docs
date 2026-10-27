---
title: "pg_pinecone support"
source: https://docs.pinecone.io/guides/pg-pinecone/support
path: guides/pg-pinecone/support
---

Ask questions about pg_pinecone in the Pinecone Discord community, and report bugs or request features in GitHub issues.

* **Questions and feedback**: Ask in the [Pinecone Discord community](https://discord.gg/tJ8V62S3sH), where other users and the Pinecone team answer.
* **Bugs and feature requests**: Open an issue in the [pg\_pinecone repository](https://github.com/pinecone-io/pg_pinecone/issues). To propose a code change, open an issue first so the approach can be agreed on before any work starts.
* **Security issues**: Don't open a public issue. Email [security@pinecone.io](mailto:security@pinecone.io), or follow the [security policy](https://github.com/pinecone-io/pg_pinecone/blob/main/SECURITY.md) to report it privately on GitHub.
* **Your Pinecone account or index**: For a problem with the Pinecone index that the `remote` engine or full-text search uses, [contact Pinecone Support](/admin/support/contact-support).

When you report a bug, include your pg\_pinecone and Postgres versions, your operating system, the table's engine, and the full error message. To find the versions, run:

```sql SQL theme={null}
SELECT extversion FROM pg_extension WHERE extname = 'pg_pinecone';
SELECT version();
```
