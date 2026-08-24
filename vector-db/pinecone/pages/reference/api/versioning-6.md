---
title: "API versioning"
source: https://docs.pinecone.io/reference/api/versioning
path: reference/api/versioning
---

Learn how Pinecone versions its APIs by release date, how long each stable version is supported, and how to set the X-Pinecone-Api-Version header.

Pinecone's APIs are versioned to ensure that your applications continue to work as expected as the platform evolves. Versions are named by release date in the format `YYYY-MM`, for example, `2025-10`.

## Release schedule

On a quarterly basis, Pinecone releases a new **stable** API version as well as a **release candidate** of the next stable version.

* **Stable:** Each stable version remains unchanged and supported for a minimum of 12 months. Since stable versions are released every 3 months, this means you have at least 9 months to test and migrate your app to the newest stable version before support for the previous version is removed.

* **Release candidate:** The release candidate gives you insight into the upcoming changes in the next stable version. It is available for approximately 3 months before the release of the stable version and can include new features, improvements, and [breaking changes](#breaking-changes).

Below is an example of Pinecone's release schedule:

<img />

<img />

## Specify an API version

<Warning>
  When using the API directly, it is important to specify an API version in your requests. If you don't, requests default to the oldest supported stable version. Once support for that version ends, your requests will default to the next oldest stable version, which could include breaking changes that require you to update your integration.
</Warning>

To specify an API version, set the `X-Pinecone-Api-Version` header to the version name.

For example, to use the latest stable version (`2026-04`) to describe an index, set the `X-Pinecone-Api-Version` header:

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X GET "https://api.pinecone.io/indexes/movie-recommendations" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-04"
```

To use an older version, specify that version instead.

## SDK versions

Official [Pinecone SDKs](/reference/pinecone-sdks) provide convenient access to Pinecone APIs. SDK versions are pinned to specific API versions. When a new API version is released, a new version of the SDK is also released.

For the mapping between SDK and API versions, see [SDK versions](/reference/pinecone-sdks#sdk-versions).

## Breaking changes

Breaking changes are changes that can potentially break your integration with a Pinecone API. Breaking changes include:

* Removing an entire operation
* Removing or renaming a parameter
* Removing or renaming a response field
* Adding a new required parameter
* Making a previously optional parameter required
* Changing the type of a parameter or response field
* Removing enum values
* Adding a new validation rule to an existing parameter
* Changing authentication or authorization requirements

## Non-breaking changes

Non-breaking changes are additive and should not break your integration. Additive changes include:

* Adding an operation
* Adding an optional parameter
* Adding an optional request header
* Adding a response field
* Adding a response header
* Adding enum values

## Get updates

To ensure you always know about upcoming API changes, follow the [Release notes](/release-notes/).
