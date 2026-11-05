---
title: "Changes by version"
source: https://developers.notion.com/reference/changes-by-version
path: reference/changes-by-version
---

| Version | Breaking changes |
| :- | :- |
| `2026-03-11` | The `after` parameter on Append Block Children is replaced by a `position` object. The `archived` field is removed in favor of `in_trash` across all request parameters and response bodies. The `transcription` block type is renamed to `meeting_notes`.   See [Upgrading to 2026-03-11](/guides/get-started/upgrade-guide-2026-03-11) for details. |
| `2025-09-03` | `/v1/databases` APIs are re-organized into `/v1/data_sources` (for managing individual data sources under a database container) and `/v1/databases` (for managing the database container.)       Existing database IDs stay the same, but a new concept of data source IDs is introduced, and required in order to manage data source properties, to support multi-source databases (new in the Notion app as of September 2025.)       See [changelog](/page/changelog) and [Upgrading to 2025-09-03](/guides/get-started/upgrade-guide-2025-09-03) guide for more details. |
| `2022-06-28` | Page properties must be retrieved using the page properties endpoint.       Parents are now always direct parents; a parent field has been added to block.       Database relations have a type of `single_property` and `dual_property`.         See [changelog](/changelog/releasing-notion-version-2022-06-28) for more details. |
| `2022-02-22` | See [changelog](/changelog/releasing-notion-version-2022-02-22). |
| `2021-08-16` | The [Append block children](/reference/patch-block-children) endpoint returns a list of new [Block object](/reference/block) children instead of the parent block.       Array rollup property types changed from `file`, `text` and `person` to `files`, `rich_text` and `people`.       Property IDs are now encoded to be URL safe.       Empty number, email, select, date, and rollup properties are now returned in page responses as `null`.       [More information](/changelog/notion-version-2021-08-16) |
| `2021-05-13` | Rich text property values use the type `rich_text` instead of `text`.       [Migration details](/changelog/unversioned-requests-no-longer-accepted) |
