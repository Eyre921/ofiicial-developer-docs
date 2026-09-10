---
title: "Upload media"
source: https://docs.x.com/x-api/media/upload-media
path: x-api/media/upload-media
---

post /2/media/upload
Uploads a media file for use in posts, direct messages, or ads. The response carries the media identifiers, including the media_key used to reference the asset in later calls. The media field carries the file content base64-encoded in JSON bodies (raw bytes in multipart bodies); media_category is tweet_image, tweet_video, or tweet_gif for posts and ads, dm_image/dm_video/dm_gif for DMs, or subtitles. For X Ads accounts, register the returned media_key via create_media_library_item to add it to the account's media library and use it in campaigns.
