---
title: "Search"
source: https://developers.deepgram.com/docs/search.md
path: docs/search
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Search

* [Try Search in Deepgram Playground](https://playground.deepgram.com/?endpoint=listen\&search=test\&language=en\&model=nova-3)

`search` *string*

Pre-recorded  Streaming:Nova Streaming: Flux  All available languages

Deepgram’s Search feature searches for terms or phrases by matching acoustic patterns in audio (which we have found is more accurate than matching for text patterns in transcripts) and returns results in the response JSON object. This allows you to accurately identify whether a phrase was uttered in submitted audio by letting Deepgram "hear" whether the phrase was uttered rather than by trying to look for sufficiently close matches in the text transcript.

Because the search feature is looking for phonetic matches, it works best on longer, multisyllabic terms, or even on short to medium-length phrases.

## Enable Feature

To enable Search, when you call Deepgram’s API, add a `search` parameter in the querystring and set it to your chosen search term or phrase:

`search=TERM_OR_PHRASE`

You can include up to 50 search terms per request.

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?search=TERM_OR_PHRASE'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

### Search for a Term

To search for a single term, send one instance of the `search` parameter in the query string when calling the API:

`search=epistemology`

### Search for Multiple Terms

You can search for multiple terms individually:

`search=epistemology&search=warwick`

### Search for a Phrase

You can search for a phrase. URL-encode the phrase when submitting it.

`search=social%20epistemology`

## Analyze Response

The term "epistemology" in this audio file is sufficiently technical that our model may not transcribe it accurately, but our phonetic search will be able to find it.

In our terminal, we run the following cURL command:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @epistemology.wav \
  --url 'https://api.deepgram.com/v1/listen?search=epistemology'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

When the file is finished processing (often after only a few seconds), you’ll receive a JSON response that has the following basic structure:

```json JSON
{
	"metadata": {
		"transaction_key": "string",
		"request_id": "string",
		"sha256": "string",
		"created": "string",
		"duration": 0,
		"channels": 0
	},
	"results": {
		"channels": [
			{
				"search": [],
				"alternatives": []
			}
		]
	}
}
```

Let's look more closely at the `alternatives` object:

```json JSON
...
"alternatives":[
  {
    "transcript": "hello this is steve fuller i'm a professor of social epi at the university of warwick and the question before us today is what is a and why is it important epi is the branch philosophy that is concerned with the nature of knowledge",
    "confidence": 0.9773828,
    "words":[
      {"word":"hello","start":1.2560788,"end":1.3358299,"confidence":0.9822957},
        ...
    ]
  }
]
```

The audio file contains multiple occurrences of the word "epistemology". Nova 2 correctly transcribes `epistemology` each instance correctly.

Now, let's take a look at the `search` object:

```json JSON
...
"search": [
  {
    "query": "epistemology",
    "hits": [
      {"confidence":1,"start":3.9676142,"end":4.7651243,"snippet":"social epistemology"},
      {"confidence":1,"start":13.805,"end":14.645,"snippet":"epistemology"},
      {"confidence":0.9782986,"start":10.605,"end":11.565,"snippet":"is epistemology"},
      {"confidence":0.21875,"start":8.513423,"end":9.625,"snippet":"before us today"},
      {"confidence":0.074074,"start":15.245,"end":16.005,"snippet":"branch of philosophy"},
      {"confidence":0.045138836,"start":5.1240044,"end":5.6822615,"snippet":"university of"},
      {"confidence":0.0234375,"start":17.165,"end":18.115,"snippet":"nature of knowledge"},
      {"confidence":0,"start":1.1763278,"end":1.8940871,"snippet":"hello this is steve"},
      {"confidence":0,"start":5.6025105,"end":7.3969088,"snippet":"of warwick and"}
    ]
  }
]
...
```

In this response, we see that each `search` contains:

* `query`: Word that has been requested.
* `hits`: Object containing each time the search term was found in the transcript, along with its start time and end time (in seconds) from the beginning of the audio stream, and a confidence value.

In this part of the response, notice:

* we have received multiple hits for the word. The first two have high confidence of 1 and the third has a confidence of 97.8%.
* the results contain the `start` and `end` times for each place in the audio where the model heard the word.
* after the first three hits, there's a steep decline in the model's confidence that it heard the requested word, and none of these hits do in fact correspond to the requested word.

---
