---
title: "Create a backup of an index"
source: https://docs.pinecone.io/reference/api/2026-07/control-plane/create_backup
path: reference/api/2026-07/control-plane/create_backup
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-07/db_control_2026-07.oas.yaml post /indexes/{index_name}/backups
Create a backup of an index.
The backup records the schema of the index it is taken from and reports it as `schema`. An index created from the backup with [Create index from backup](https://docs.pinecone.io/reference/api/2026-07/control-plane/create_index_from_backup) inherits that schema.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
        "name": "example-backup", 
        "description": "Monthly backup of production index"
        }'
  ```
</RequestExample>
