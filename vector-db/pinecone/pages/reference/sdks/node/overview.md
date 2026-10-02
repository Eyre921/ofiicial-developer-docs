---
title: "Pinecone Node.js SDK"
source: https://docs.pinecone.io/reference/sdks/node/overview
path: reference/sdks/node/overview
---

Install and use the Pinecone Node.js and TypeScript SDK to manage indexes, upsert vectors, run semantic search, and call the Admin and Inference APIs.

<Tip>
  For installation instructions, usage examples, and reference information, see the [Pinecone Node.js SDK documentation](https://sdk.pinecone.io/typescript/). To report an issue or request a feature, [file an issue on GitHub](https://github.com/pinecone-io/pinecone-ts-client/issues).
</Tip>

## Requirements

The Pinecone Node.js SDK requires Node.js 22 or later. Its type declarations support TypeScript 5.2 to 7.x.

## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and Node.js SDK versions are as follows:

| API version | SDK version |
| :- | :- |
| `2026-07` | v9.x |
| `2026-04` | v8.x |
| `2025-10` | v7.x |
| `2025-04` | v6.x |
| `2025-01` | v5.x |
| `2024-10` | v4.x |
| `2024-07` | v3.x |
| `2024-04` | v2.x |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.

## Install

To install the latest version of the [Node.js SDK](https://github.com/pinecone-io/pinecone-ts-client), written in TypeScript, run the following command:

```Shell theme={null}
npm install @pinecone-database/pinecone
```

To check your SDK version, run the following command:

```Shell theme={null}
npm list | grep @pinecone-database/pinecone
```

## Upgrade

`v9.0.0` targets API version `2026-07`. To stay on API version `2026-04`, keep using `v8`. The flat control methods, such as `pc.createIndex` and `pc.configureIndex`, still work in `v9` but are deprecated in favor of resource clients such as `pc.indexes`.

<Warning>
  Before upgrading to `v9.0.0`, update all relevant code to account for the following breaking changes. See the [v9 migration guide](https://github.com/pinecone-io/pinecone-ts-client/blob/main/guides/upgrading/v9-migration.md) for before-and-after examples.

  * Node.js 22 or later is required.
  * `pc.preview` and the `Preview*` exports are removed. Document operations move to `index.documents`, where `index` comes from `pc.index({ name, namespace })` or `pc.index(name).namespace(namespace)`. Control operations move to resource clients such as `pc.indexes`.
  * Pod-based index creation, legacy metadata-indexing schemas, and the `sourceCollection` and `sourceBackupId` creation options are rejected. Existing pod-based indexes keep working. To restore from a backup, use `pc.backups.createIndex(backupId, options)`.
  * A top-level `embed` option when configuring an index is rejected. Update the semantic field through a `schema.fields` patch instead.
  * Legacy index response properties such as `dimension`, `metric`, and `spec` are compatibility getters derived from `schema` and `deployment`. They are omitted when a response is spread or serialized, and can throw `Errors.PineconeIndexPropertyError` when there is no legacy equivalent.
  * `NamespaceDescription.recordCount` and `sizeBytes` are now decimal strings, and `BackupModel.createdAt` is now a `Date`.
  * Some generated type names are renamed or removed. For example, `BackupPaginationResponse` is now `BackupListPagination`.
</Warning>

If you already have the Node.js SDK, upgrade to the latest version as follows:

```Shell theme={null}
npm install @pinecone-database/pinecone@latest
```

## Initialize

Once installed, you can import the library and then use an [API key](/guides/projects/manage-api-keys) to initialize a client instance:

```JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
});
```

To manage organizations, projects, API keys, and [role-based access control](/guides/production/manage-rbac), initialize an `AdminClient` with [service account](/guides/organizations/manage-service-accounts) credentials instead. This requires v8.2.0 or later:

```JavaScript theme={null}
import { AdminClient } from '@pinecone-database/pinecone';

// Reads PINECONE_CLIENT_ID and PINECONE_CLIENT_SECRET from the environment
const admin = new AdminClient();
```

You can also pass `clientId` and `clientSecret` directly to the constructor instead of setting environment variables.

## Proxy configuration

If your network setup requires you to interact with Pinecone through a proxy, you can pass a custom `ProxyAgent` from the [`undici` library](https://undici.nodejs.org/#/). Below is an example of how to construct an `undici` `ProxyAgent` that routes network traffic through a [`mitm` proxy server](https://mitmproxy.org/) while hitting Pinecone's `/indexes` endpoint.

<Note>
  The following strategy relies on Node's native [`fetch`](https://nodejs.org/docs/latest/api/globals.html#fetch) implementation, released in Node v16 and stabilized in Node v21. If you are running Node versions 18-21, you may experience issues stemming from the instability of the feature. There are currently no known issues related to proxying in Node v18+.
</Note>

```JavaScript JavaScript theme={null}
import {
  Pinecone,
  type PineconeConfiguration,
} from '@pinecone-database/pinecone';
import { Dispatcher, ProxyAgent } from 'undici';
import * as fs from 'fs';

const cert = fs.readFileSync('path/to/mitmproxy-ca-cert.pem');

const client = new ProxyAgent({
  uri: 'https://your-proxy.com',
  requestTls: {
    port: 'YOUR_PROXY_SERVER_PORT',
    ca: cert,
    host: 'YOUR_PROXY_SERVER_HOST',
  },
});

const customFetch = (
  input: string | URL | Request,
  init: RequestInit | undefined
) => {
  return fetch(input, {
    ...init,
    dispatcher: client as Dispatcher,
    keepalive: true,  # optional
  });
};

const config: PineconeConfiguration = {
  apiKey:
    'YOUR_API_KEY',
  fetchApi: customFetch,
};

const pc = new Pinecone(config);

const indexes = async () => {
  return await pc.listIndexes();
};

indexes().then((response) => {
  console.log('My indexes: ', response);
});
```
