---
title: "Data Edge (Deprecated)"
source: https://docs.turso.tech/features/data-edge
path: features/data-edge
---

Allow your users to reach local replicas of your database, wherever they are.

<Warning>
  This feature is now deprecated for all new users. Existing users can continue
  to use Edge Replicas on Fly — [read the
  announcement](https://turso.tech/blog/upcoming-changes-to-the-turso-platform-and-roadmap)
</Warning>

For those seeking the ultimate in speed, Turso enables the [embedding of databases](/features/embedded-replicas) directly within your application on the same node. This configuration eliminates inter-regional request hopping, effectively bringing latency down to zero.

<iframe title="YouTube video player" />

## How it works

1. You create a database in a primary location
2. You add additional locations where data should be replicated
3. You query a single URL that automatically routes to the nearest edge

## Add replica location

You can add locations to your database group using the [Turso CLI](/cli/group/locations/add) or [Platform API](/api-reference/groups/add-location):

<CodeGroup>
  ```bash CLI theme={null}
  turso group locations add <group-name> <location-code>
  ```

  ```bash Platform API theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/locations/{location}' \
    -H 'Authorization: Bearer TOKEN'
  ```
</CodeGroup>

## Remove replica location

You can remove locations from your database group using the [Turso CLI](/cli/group/locations/remove) or [Platform API](/api-reference/groups/remove-location):

<CodeGroup>
  ```bash CLI theme={null}
  turso group locations remove <group-name> <...location-codes>
  ```

  ```bash Platform API theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/organizations/{organizationSlug}/groups/{groupName}/locations/{location}' \
    -H 'Authorization: Bearer TOKEN'
  ```
</CodeGroup>
