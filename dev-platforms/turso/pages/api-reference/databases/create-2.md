---
title: "Create Database"
source: https://docs.turso.tech/api-reference/databases/create
path: api-reference/databases/create
---

POST /v1/organizations/{organizationSlug}/databases
Creates a new database in a group for the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "new-database",
        "group": "default"
    }'
  ```

  ```bash cURL (for upload) theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "new-database",
        "group": "default",
        "seed": {
          "type": "database_upload"
        }
    }'
  ```

  ```bash cURL (for encrypted upload) theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "new-database",
        "group": "default",
        "seed": {
          "type": "database_upload"
        },
        "remote_encryption": {
          "encryption_key": "BASE64_ENCRYPTION_KEY",
          "encryption_cipher": "aes256gcm"
        }
    }'
  ```

  ```bash cURL (new encrypted database) theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "new-database",
        "group": "default",
        "remote_encryption": {
          "encryption_key": "BASE64_ENCRYPTION_KEY",
          "encryption_cipher": "aes256gcm"
        }
    }'
  ```

  ```bash cURL (fork encrypted database) theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "new-database",
        "group": "default",
        "seed": {
          "type": "database",
          "name": "source-encrypted-db"
        },
        "remote_encryption": {
          "encryption_key": "BASE64_ENCRYPTION_KEY",
          "encryption_cipher": "aes256gcm"
        }
    }'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const database = await turso.databases.create("new-database", {
    group: "default",
  });
  ```
</RequestExample>
