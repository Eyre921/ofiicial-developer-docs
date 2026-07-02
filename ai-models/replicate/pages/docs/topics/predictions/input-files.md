---
title: "Input files"
source: https://replicate.com/docs/topics/predictions/input-files.md
path: docs/topics/predictions/input-files
---

Some models accept files as input, like images, audio, or video, zip files, PDFs, etc.

There are multiple ways to use files as input when running a model on Replicate. You can provide a file as input using a URL, a local file on your computer, or a base64-encoded object.

[](#option-1-hosted-file)Option 1: Hosted file
----------------------------------------------

Use a URL to provide a hosted file:

This is useful if you already have a file hosted somewhere on the internet.

[](#option-2-local-file)Option 2: Local file
--------------------------------------------

You can provide Replicate with a `Blob`, `File`, or `Buffer` object, and the library will handle the upload for you. This will work for files up to 100MB:

[](#option-3-data-uri)Option 3: Data URI
----------------------------------------

Create a data URI consisting of the base64 encoded data for your file. This is only recommended if the file is less than 1MB:

[](#using-the-file-input)Using the file input
---------------------------------------------

Once you have your file input ready, you can use it in your prediction:
