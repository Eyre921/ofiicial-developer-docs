---
title: "Zoom and Deepgram"
source: https://developers.deepgram.com/docs/integrate-deepgram-with-zoom.md
path: docs/integrate-deepgram-with-zoom
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Zoom and Deepgram

[Zoom](https://zoom.us/) is a widely-used cloud-based video communications tool that lets you host virtual one-on-one or team meetings, webinars, and live chats and provides audio, video, screen-sharing, and other collaboration features. Zoom offers enhanced Real-Time Messaging Protocol (RTMP) support, which allows you to extract the audio from your content and stream it to Deepgram to get real-time automatic speech recognition for all of your Zoom calls.

In this guide, the audio from a Zoom conference call will be streamed to a local server. We will fork the stream to our Python script, which will send the audio to Deepgram, then receive and print transcriptions to the screen.

In a real implementation, you will likely want to modify the script to provide a callback URL to which transcriptions can be sent.

## Before you Begin

Before you can use Deepgram, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes **\$200** in free credit and access to all of Deepgram's features!

Before you start, you'll need to follow the steps in the [Make Your First API Request](/guides/fundamentals/make-your-first-api-request) guide to obtain a Deepgram API key, and configure your environment if you are choosing to use a Deepgram SDK.

### Create a Zoom Pro Account

Before you can use Zoom’s live streaming, you'll need to [create a Zoom Pro account](https://zoom.us/signup). Then:

* [enable livestreaming for meetings and webinars](https://support.zoom.us/hc/en-us/articles/360061534591-Enabling-Allow-livestreaming-of-meetings)
* [allow livestreaming on a custom service](https://support.zoom.us/hc/en-us/articles/115001777826-Live-streaming-meetings-or-webinars-using-a-custom-service)

### Install Development Dependencies

In order to run the services required for this integration, you will need:

* [npm](https://www.npmjs.com/)
* [FFmpeg](https://www.ffmpeg.org/download.html)
* [ngrok](https://ngrok.com/)
* [rtmpdump](https://github.com/mstorsjo/rtmpdump)

If you're using macOS, we recommend using [Homebrew](https://brew.sh/) to install the above dependencies with `brew install <dependency name>`. On Linux, your OS package manager can be substituted instead.

You will also need a working Python environment with `Python >= 3.6`. We will install the required Python packages in the section "Download and Configure the Streaming Script".

### Start the RTMP Server

Because Zoom supports Real-Time Messaging Protocol streaming, we will use a GitHub project called [Node Media Server](https://github.com/illuspas/Node-Media-Server) to create a simple RTMP server to receive and view the stream data.

To install and start the Node Media Server, run the following command:

`npm i node-media-server -g && node-media-server`

That should result in output like:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/b80f8614496090fa2e53fda6fada410e4b3ee983a7297de2830a2a44f29cacd0/images/3014887-image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=10268b38852af00ba980eb577e5d82377d2e7a8697e9e0d071c67942889c1ddd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To visit your new server and verify everything is working, navigate to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with the username `admin` and the password `admin`. You should see the following interface if everything is set up correctly:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/0fc292b7c9e9ed3eed9919aa72a19b09e0ddefb037137d09cdd7067efa28dbbc/images/e0da771-image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=4e1f102315412ec029a7b9e8d4129de3e4bf9dbb82d632b0bb7dadc50c77d9de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Make the Server Publicly Available

Now that we have confirmed the server is running, we’ll need to make it available over the internet so Zoom can send data to it. To do this, we'll use Ngrok.

We’ll tell Ngrok to forward TCP traffic for port 1935 (the default port Node Media Server uses for RTMP) through a public tunnel. Open a new terminal window and run:

`ngrok tcp 1935`

The output should look like this:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/89f8c55b58da6eb69aa455b0042bc0d28f4b28678449506e851c9e3ab33a8d2c/images/3d6e5ee-image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=4533b3a25ac81b036145f75340264cd58b8a102f1501af5e77be54e39e304f1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Make sure to save the forwarding URL which in this case is `tcp://2.tcp.ngrok.io:12024`. We'll need to enter this URL in the next step.

This environment is designed for development, not production. Using ngrok will impact the latency and bandwidth of your stream. Do not use ngrok when conducting performance or latency testing.

### Download and Configure the Streaming Script

Next, clone our [Deepgram + Zoom repo](https://github.com/deepgram-devs/deepgram-zoom).

#### Install Python Dependencies

Navigate to the location where you cloned the Deepgram + Zoom repo. Then run:

`pip install -r requirements.txt`

There are a few dependencies required for this code. The [websockets](https://pypi.org/project/websockets/) library is used to send and receive messages from Deepgram. We also need [scipy](https://pypi.org/project/scipy/) (a scientific library we will use to handle WAV files), [streamlink](https://pypi.org/project/streamlink/) (a command-line utility that extracts streams from various services and pipes them into a chosen video player), and [requests](https://pypi.org/project/requests/) (a simple HTTP library).

#### Configure Deepgram Authentication

Prior to running the script, you must replace the authentication with your Deepgram username and password.

On line 17 of `stream.py`, replace `YOUR_DEEPGRAM_API_KEY` with the API Key you created earlier in this tutorial:

```python Python
17        'Authorization': 'Token YOUR_DEEPGRAM_API_KEY'
```

### Set Up Your Zoom Conference Call

Next, you will need to start your Zoom meeting and configure your Zoom live-streaming service:

1. Start your Zoom meeting and join the meeting with computer audio.

   ![Join Zoom with Computer Audio](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/ec9b89fcac412d0f67c09668ce34b79738a3c77076b3e4a9cf27aaefe4a50953/images/2d38ff0-integrate-zoom_join-computer-audio.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=08f21ab034d78a2f7ebc959e981ed7b4ef594ea94d9ebcc331b19277954458c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

2. Select **More…** and then **Live on Custom Live Streaming Service**.

   ![Zoom More menu](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/761e3ecb5fbe4180eb7dd9c23d7bd6e342ea8e263798c66b5690442cea5a6e29/images/e9f93f4-integrate-zoom_more-livestream.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=46fa97c0da5c2ad1716522ffce9c8af8204f056a237c16c3fccd9f1d0796a8a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

3. Configure streaming, and select **Go Live!**.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/8dda6d7650d4690293f5cbb0880a14feef0a6d398dd154629a6eb446b533ab0c/images/27cd0af-image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=67890d83aefd86e505fb22ec3358a1a36e2b998eb96999eaf3a0239235a2588f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

| Field                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Streaming URL**           | URL or IP address to which you would like to send audio. Zoom will stream media to this URL, so that other apps can subscribe to the stream. Use the ngrok URL created in the previous step, plus `/live`. Modify the url to start with `rtmp://` instead of `tcp://`.                                                                                                                                                                                                                                                                                             |
| **Streaming key**           | Unique identifier for your meeting instance. Use any unique ID (such as `DEEPGRAM` or `ZOOM`). Make note of the value you enter because you will need it again later.                                                                                                                                                                                                                                                                                                                                                                                              |
| **Live streaming page URL** | URL to a front-end where users can view the live stream. In this example, we intend to use our `stream.py` script to display results in the terminal on the same machine that hosts the RTMP server indicated in the Streaming URL, so we won't have a live streaming page. Use any URL in this field (like `https://deepgram.com`). This field is required by Zoom but not needed for our application. If you modified our example streaming script to use a callback URL, then instead, enter the URL to the page that will process and display the transcripts. |

### Send Streaming Results to Deepgram

We're ready to start sending Zoom audio to Deepgram and receiving transcriptions!

#### Configure the Zoom Streaming Key

Because you could be streaming multiple instances of Zoom at the same time, the script needs to know from which Zoom instance it should get results.

We'll use [RTMPDump](https://rtmpdump.mplayerhq.hu/) to fork Zoom's audio to Deepgram via our `stream.py` script .

To do this, run `stream_rtmp.sh`, found in our [Deepgram + Zoom repo](https://github.com/deepgram-devs/deepgram-zoom/blob/main/stream_rtmp.sh). The shell script contains the following:

```bash Bash
rtmpdump -r $1/$2 --live -o - | python3 stream.py
```

Here, `rtmpdump` makes a connection to a specific stream on the specified RTMP server and directs the media content of the stream to our example streaming script (`stream.py`) for display in your terminal. Parameters include:

| Parameter | Description                                                                                                                                                                                                                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| −r url    | URL of the server and media content. Should be in the form `rtmp[t][e]://hostname[:port][/app[/playpath]]`. In this example, this is the local IP of the RTMP server we are running. When you run the script, you will pass in the **Streaming URL** and **Streaming key** you configured in Zoom, which will replace the `$1` and `$2` variables. |
| −-live    | Specifies that the media is a live stream. You may not resume or seek in live streams.                                                                                                                                                                                                                                                             |
| −o output | Specifies the output file name. In this case, the output is piped to our example streaming script (`stream.py`) for live display.                                                                                                                                                                                                                  |

#### Run the Script

To run the script, from the command line, open a new terminal window. Navigate to the location where you cloned the [Deepgram + Zoom repo](https://github.com/deepgram-devs/deepgram-zoom).

Then, run the following command:

```bash Bash
source stream_rtmp.sh url keyname
```

Replace `url` with the the **Streaming URL** you entered in Zoom. This will be the ngrok URL created in the previous step, plus `/live`. Remember to modify the URL to start with `rtmp://` instead of `tcp://`.

Replace `keyname` with the **Streaming key** you entered in Zoom.

Depending on your environment, you may need to modify the shell script to use `python` instead of `python3`.

### See Results

Start speaking into your microphone. After a brief delay, you should see results of the audio transcription of your livestreaming Zoom call start to appear on your screen.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/d8aaa167806266d7a1b094f7a4f9b3c11a689fece091c84da5d08d57522aa0be/images/7f67ed9-image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260724T233113Z&X-Amz-Expires=604800&X-Amz-Signature=0ef8dde0b649c59f464773415d01ee3187471eb6ec7e8f533fbcf5e8f6b51d51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The speed of returned results depends on both Deepgram and Zoom availability, and the setup of your hosting environment. As mentioned above, using ngrok may introduce additional latency.

By default, this script does not return interim results, only finalized transcripts. If you require the fastest possible transcripts (with the potential for less accurate transcriptions), modify line 20 in `stream.py` to add the parameter `interim_results=true`.

When interim results are turned on, red output represents interim transcripts, while green text represents final transcripts. To learn more about interim and final transcripts, see [Interim Results](/docs/interim-results/).
