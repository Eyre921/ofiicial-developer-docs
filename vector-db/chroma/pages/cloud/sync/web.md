---
title: "Web Sync"
source: https://docs.trychroma.com/cloud/sync/web
path: cloud/sync/web
---

Crawl and sync website content into Chroma Cloud.

Web Sync allows you to easily sync content from any publicly accessible website into your Chroma Cloud database. Given a starting URL, Sync will crawl the website and its links up to a specified depth, extracting the content as Markdown, chunking it, and inserting it into your Chroma database with embeddings.

# Walkthrough

If you do not already have a Chroma Cloud account, you will need to create one at [trychroma.com](https://www.trychroma.com). After creating an account, you can create a database by specifying a name:

![Create database screen](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_web_new_db.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=a95b9721659ae44ff9348e38c6b25003)

Then, select the Web source during onboarding:

![Onboarding screen](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_web_onboarding.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=a3346a4ef4a8ce323d029097e717ab71)

Next, configure the Web source by providing a starting URL:

![Web source config](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_web_url_config.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=b1f9167131b02bd843f1fdfc2604246e)

Optionally, you can configure other parameters like the page limit and include path regexes. Here, we're scraping a maximum of 50 pages under `https://docs.trychroma.com/cloud` (all our cloud docs):

![Web source config](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_web_advanced_config.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=a9a61673fbf9703ff59b6f3096eba02d)

You can also change the default collection name if you want. After clicking "Create Sync Source", an initial sync will start:

![Web sync in progress](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/sync/sync_web_progress.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=9b137c480f6263447fa5ae2e18834250)

After it finishes, you'll be redirected to the created collection.
