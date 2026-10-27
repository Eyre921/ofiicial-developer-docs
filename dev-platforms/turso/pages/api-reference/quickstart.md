---
title: "Quickstart"
source: https://docs.turso.tech/api-reference/quickstart
path: api-reference/quickstart
---

Get started with Turso API in a few easy steps.

> [!NOTE]
>
> **Using TypeScript?** You can skip the raw HTTP examples and use the [`@tursodatabase/api`](https://www.npmjs.com/package/@tursodatabase/api) client instead. See the [SDK quickstart](/api-reference/introduction#quickstart-with-the-typescript-sdk).

**1. Signup or Login using the Turso CLI**

Make sure to [install the Turso CLI](/cli/installation) if you haven't
already.

```bash Signup theme={null}
turso auth signup
```

```bash Login theme={null}
turso auth login
```

**2. Retrieve your account or organization slug**

The Platform API can be used with your personal account or with an organization. You'll need the obtain the `slug` of your account or organization using using the Turso CLI:

```bash theme={null}
turso org list
```

**3. Create a new Platform API Token**

Now create a new API Token using the Turso CLI:

```bash theme={null}
turso auth api-tokens mint quickstart
```

You can scope the token to a specific organization with `--org`:

```bash theme={null}
turso auth api-tokens mint quickstart --org my-org
```

> [!NOTE]
>
> Make sure to save the token somewhere safe. We'll need it next.

**4. Fetch available Locations**

Before we can create a group or database in a specific region, we'll need to fetch the list of available regions:

```bash cURL theme={null}
curl -L 'https://api.turso.tech/v1/locations' \
  -H 'Authorization: Bearer TOKEN' \
```

```ts Node.js theme={null}
import { createClient } from "@tursodatabase/api";

const turso = createClient({
  org: "...",
  token: "",
});

const locations = await turso.locations.list();
```

> [!NOTE]
>
> The `organizationSlug` is the name of your organization or personal account.

**5. Create a Group**

All databases belong to a group that can exist in one or more locations.

Begin by creating a group, giving it a `name` and primary `location`:

```bash cURL theme={null}
curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups' \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "default",
      "location": "lhr"
  }'
```

```ts Node.js theme={null}
import { createClient } from "@tursodatabase/api";

const turso = createClient({
  org: "...",
  token: "",
});

const group = await turso.groups.addLocation("default", "lhr");
```

**6. Create a Database**

Now create your first database in the group you created above:

```bash cURL theme={null}
curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "my-db",
      "group": "default"
  }'
```

```ts Node.js theme={null}
import { createClient } from "@tursodatabase/api";

const turso = createClient({
  org: "...",
  token: "",
});

const database = await turso.databases.create("my-db", "ams");
```

**7. Connect to your database**

You now have a database, distributed across multiple regions that you can connect to using one of the official or experimental SDKs:

<Snippet />
