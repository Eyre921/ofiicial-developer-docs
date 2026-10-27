---
title: "Embedded Replicas on Fly"
source: https://docs.turso.tech/features/embedded-replicas/with-fly
path: features/embedded-replicas/with-fly
---

Deploy a JavaScript app using [Turso Cloud embedded replicas](/features/embedded-replicas) to [Fly.io](https://www.fly.io/).

![Koyeb banner](https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/fly-banner.png?fit=max\&auto=format\&n=7mjM7fXIfeZ8ZwNC\&q=85\&s=f3d7f266e79052e9d176d519a4a277fc)

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso Cloud](/cli/authentication#signup)
* [Install the Fly.io CLI](https://fly.io/docs/hands-on/install-flyctl/)

**1. Locate your application**

You should have an application ready using your Turso Cloud database that you want to deploy to Fly.

**2. Launch with Fly**

Using the Fly CLI, launch it:

```bash theme={null}
fly launch
```

Your application will automatically deploy to Fly, but we're not ready yet.

**3. Create a shared volume**

Now create a volume that will be used to store the embedded replica(s):

```bash theme={null}
fly volumes create libsql_data
```

**4. Mount and configure volumes**

The files `fly.toml` and `Dockerfile` created created when you launched previously.

Update `fly.toml` this file to mount the new volume:

```toml theme={null}
[[mounts]]
source = "libsql_data"
destination = "/app/data"
```

Then inside `Dockerfile`, make sure you install and update `ca-certificates`:

```dockerfile theme={null}
RUN apt-get update -qq && \
    apt-get install -y ca-certificates && \
    update-ca-certificates
```

Make sure to also add the following line after any `COPY` commands to copy the certificates:

```dockerfile theme={null}
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
```

**5. Configure the libSQL client**

You will want to change the `url` to point to a local file, and set the `syncUrl` to be your Turso Cloud database URL:

```ts theme={null}
import { createClient } from "@libsql/client";

const client = createClient({
  url: "file:/app/data/local.db",
  syncUrl: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
  syncInterval: 60,
});
```

**6. Deploy your updated app**

```bash theme={null}
fly deploy
```
