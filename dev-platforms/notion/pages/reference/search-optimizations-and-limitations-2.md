---
title: "Search optimizations and limitations"
source: https://developers.notion.com/reference/search-optimizations-and-limitations
path: reference/search-optimizations-and-limitations
---

Find out what search can return and how to narrow the results.

## Optimizations

[Search](/reference/post-search) matches page and data source titles. Pass a `query` to narrow the matches. To return only pages or only data sources, set `filter.property` to `"object"` and `filter.value` to `"page"` or `"data_source"`.

Use a smaller `page_size` if you only need a few matches. To reduce the size of each page result, [request only the properties you need](/reference/post-search#return-fewer-page-properties).

## Limitations

Search results can change as you paginate. The index takes time to reflect changes, including pages shared after authorization and pages moved to the trash. Search can't provide a complete inventory of the content a connection can access. If your app uses search to show newly shared pages, give users a way to refresh the results.

To find rows in a specific data source, use [Query a data source](/reference/query-a-data-source) with the data source ID.
