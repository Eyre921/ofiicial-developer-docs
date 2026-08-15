---
title: "Generating and Saving Transcripts From the Terminal"
source: https://developers.deepgram.com/docs/generating-and-saving-transcripts-from-the-terminal.md
path: docs/generating-and-saving-transcripts-from-the-terminal
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Generating and Saving Transcripts From the Terminal

## Before You Start

Before you run the code, you'll need to do a few things.

### Create a Deepgram Account

Before you can use Deepgram, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes **\$200** in free credit and access to all of Deepgram's features!

### Create a Deepgram API Key

Before you start, you'll need to follow the steps in the [Make Your First API Request](/guides/fundamentals/make-your-first-api-request) guide to obtain a Deepgram API key, and configure your environment if you are choosing to use a Deepgram SDK.

### Install JQ

In this guide, we use `jq`, which is an excellent command-line utility that allows you to display and manipulate JSON data, so you will also need to install [jq](https://stedolan.github.io/jq/).

## Making a curl Request

Open your terminal, and run the following curl command:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"url":"https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"}' \
  --url 'https://api.deepgram.com/v1/listen?punctuate=true'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

Let’s look more closely at this request:

* `--request POST`: An HTTP request with the POST method.
* `--header 'Authorization: Token YOUR_DEEPGRAM_API_KEY'`: Includes authorization details and links the request with your Deepgram account and Project.
* `--header 'Content-Type: application/json'`: JSON data that will be sent with this request.
* `--data '{"url":"<https://static.deepgram.com/examples/nasa-spacewalk-interview.wav>"}'`: JSON data sent to Deepgram (an object containing one URL parameter).
* `--url 'https://api.deepgram.com/v1/listen?punctuate=true'`: URL to which the request should be made (Deepgram's endpoint). `punctuate=true` enables the [punctuation](/docs/punctuation/) feature.
* `\`: Allows you to break one command over several lines for readability.

When you run this command and it is finished processing (often after only a few seconds), you’ll receive a JSON response that looks similar to the following:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/317326d600ee839975a185fad761e37495c8d6269e411de69cffffeb96f731bd/images/080c686-full-output.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T233214Z&X-Amz-Expires=604800&X-Amz-Signature=17c67a2b98c9919b0595c443b79b1ad51f77848e56ca7f2a3b639db0d59d41d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

This may look daunting, so let's look at a way to make both our curl request and our response easier to read.

## Shortening Your curl Request

Now that you've seen a full curl request and understand the required parameters, let's look at a more concise way to make the same request:

```bash cURL
curl https://api.deepgram.com/v1/listen?punctuate=true \
     -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"url":"https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"}'
```

In this example, notice:

* The URL comes immediately after the `curl` command.
* No HTTP method is present. Normally, this would default to a GET request, but because this request has a body, curl assumes a POST request.
* `--header` is shortened to `-H`
* `--data` is shortened to `-d`.

## Formatting Your JSON Response

To make the JSON response more readable, you can use `jq`, which is an excellent command-line utility that allows you to display and manipulate JSON data.

In the terminal, a pipe (`|`) is often used to send the output of one command as an input for a second command. `jq` expects some JSON as input, plus an expression to describe how to display it.

The following `jq` expression will extract just the transcript from the returned data object:

` | jq '.results.channels[0].alternatives[0].transcript'`

To use it, add it to the end of your curl request:

```bash cURL
curl https://api.deepgram.com/v1/listen?punctuate=true \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"}' \
  | jq '.results.channels[0].alternatives[0].transcript'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

When you run this command and it is finished processing (often after only a few seconds), you’ll receive a JSON response that looks similar to the following:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/4e327ad3b8562595dbc6590b7b8d56e215974c91d53bfce7cdfd692e94c08b2b/images/7e3313c-jq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260815%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260815T233214Z&X-Amz-Expires=604800&X-Amz-Signature=d5e31cd184373bb05b3b987af26f46533e711836a4e6313bfbb780f1e4bf6dda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Saving Output to a File

Once you have the transcript extracted and formatted using `jq`, you can redirect the output to a new file by appending `> output.txt` to any command that prints to the terminal. For example:

```bash cURL
curl https://api.deepgram.com/v1/listen?punctuate=true \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"}' \
  | jq '.results.channels[0].alternatives[0].transcript'
  > output.txt
```

## Processing Multiple Files

To process multiple files, you can create `.sh` files containing multiple lines of `bash` script to execute from your terminal.

Create a new file called `transcripts.sh`, and open it in a code editor. Populate it with the following:

```shell Shell
#!/bin/bash

urls=("https://static.deepgram.com/examples/TrumpDemocratsMeeting.nancyshort.wav" "https://static.deepgram.com/examples/nasa-spacewalk-interview.wav" "https://static.deepgram.com/examples/deep-learning-podcast-clip.wav")

dg_features="punctuate=true&utterances=true&diarize=true&tier=enhanced"
dg_key="YOUR_DEEPGRAM_API_KEY"

for url in ${urls[@]}; do
  filename=${url##*/}

  RESPONSE=$(
    curl -X POST https://api.deepgram.com/v1/listen?$dg_features \
         -H "Authorization: Token $dg_key" \
         -H "Content-Type: application/json" \
         -d "{\"url\":\"$url\"}"
  )

  echo $RESPONSE | jq '.results.channels[0].alternatives[0].transcript' > $filename.txt
done
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

In this file, notice:

* The first line (`#!/bin/bash`) is a shebang and specifies which program should be called to run the script. In this case, `bash`.

* `urls` is a variable containing an array with three URLs. The arrays use parentheses, and items are separated by only one space.

* `dg_features` and `dg_key` are variables you should alter for your exact use case. Note that the request, as written, uses Deepgram's punctuation, utterances, diarize, and tier features included in the `dg_features` variable.

* Inside the `for` loop:

  * `filename` extracts the last part of the URL (the filename), which will later be used to name the output file.
  * The `curl` command is the same as before, but with variables interpolated. The output is stored in a new variable called `RESPONSE`.
  * `RESPONSE` is sent to `jq`, and then redirected into a new text file.

Run the file in your terminal:

```shell Shell
./transcripts.sh
```

## Experimenting with jq

`jq` is a remarkable powerful tool that you can use to format data in more advanced ways. For example, the following expression will loop through the `results.utterances` array and format a string for each item, interpolating the speaker identifier and transcript text:

```shell Shell
echo $RESPONSE | jq -r '.results.utterances[] | "[Speaker:\(.speaker)] \(.transcript)"' > $filename.txt
```

When you run a previous curl command with this `jq` appended and it is finished processing, you’ll receive a JSON response formatted in the following way:

```json JSON
[Speaker:0] agreement on other things that are really good. Nancy, would you like to say something?
[Speaker:1] Well, thank you, mister president for the opportunity to meet with you so that we can work together in a bipartisan way
[Speaker:1] to meet the needs of the American people. I think the American people recognize
[Speaker:1] that we must keep government open, that a shutdown is not worth anything.
[Speaker:1] And that you should
```

---
