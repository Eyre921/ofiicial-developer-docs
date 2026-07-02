---
title: "Delete Data"
source: https://docs.trychroma.com/docs/collections/delete-data
path: docs/collections/delete-data
---

Learn how to delete data from Chroma collections.

Chroma supports deleting items from a collection by `id` using `.delete`. The embeddings, documents, and metadata associated with each item will be deleted.

<Danger>
  Naturally, this is a destructive operation, and cannot be undone.
</Danger>

<CodeGroup>
  ```python Python theme={null}
  collection.delete(
      ids=["id1", "id2", "id3",...],
  )
  ```

  ```typescript TypeScript theme={null}
  await collection.delete({
      ids: ["id1", "id2", "id3",...],
  })
  ```

  ```rust Rust theme={null}
  collection.delete(
      Some(vec!["id1".to_string(), "id2".to_string(), "id3".to_string()]),
      None,
  ).await?;
  ```
</CodeGroup>

`.delete` also supports the `where` filter. It will delete all items in the collection that match the `where` filter.

<CodeGroup>
  ```python Python theme={null}
  collection.delete(
  	where={"chapter": "20"}
  )
  ```

  ```typescript TypeScript theme={null}
  await collection.delete({
      where: {"chapter": "20"} //where
  })
  ```

  ```rust Rust theme={null}
  use chroma::types::{MetadataComparison, MetadataExpression, MetadataValue, PrimitiveOperator, Where};

  let where_clause = Where::Metadata(MetadataExpression {
      key: "chapter".to_string(),
      comparison: MetadataComparison::Primitive(
          PrimitiveOperator::Equal,
          MetadataValue::Str("20".to_string()),
      ),
  });

  collection.delete(
      None,
      Some(where_clause),
  ).await?;
  ```
</CodeGroup>
