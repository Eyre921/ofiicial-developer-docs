---
title: "Using Custom Add On Parameters with SDKs"
source: https://developers.deepgram.com/guides/fundamentals/using-custom-parameters-sdks.md
path: guides/fundamentals/using-custom-parameters-sdks
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Using Custom Add On Parameters with SDKs

# JS SDK

The Deepgram JS SDK has defined[ typed parameters](https://github.com/deepgram/deepgram-js-sdk/tree/main/src/lib/types), but also allows for arbitrary key/value pairs. You can provide custom parameters when using the JS SDK to make an API Request even if the parameter isn't defined as a type.

This is useful if you want to use a feature of the Deepgram API that isn't officially supported in the JS SDK.

## Example

```javascript JavaScript
// install our SDK @deepgram/sdk

import { DeepgramClient } from "@deepgram/sdk";
// - or -
// const { DeepgramClient } = require("@deepgram/sdk");

const result = await deepgram.listen.v1.media.transcribeUrl({
  url: "https://dpgr.am/spacewalk.wav",
  model: "nova-3",
  // To demonstrate using the custom addon parameters, you could enable it like this
  custom_parameter: option,
});
```

# Python SDK

The Deepgram Python SDK has defined option parameters, but also allows for arbitrary key/value pairs. You can provide custom parameters when using the Python SDK to make an API Request even if the parameter isn't defined as an option.

This is useful if you want to use a feature of the Deepgram API that isn't officially supported in the Python SDK.

## Example

```python Threaded
# Install the SDK: pip install deepgram-sdk

# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

import os
from dotenv import load_dotenv

from deepgram import DeepgramClient

load_dotenv()

AUDIO_URL = "https://dpgr.am/bueller.wav"

def main():
    # STEP 1 Create a Deepgram client using the API key in the environment variables DEEPGRAM_API_KEY
    client = DeepgramClient()

    try:
        # STEP 2 Call the transcribe_url method with custom parameters
        # To demonstrate using custom parameters, you can pass them directly
        response = client.listen.v1.media.transcribe_url(
            url=AUDIO_URL,
            model="nova-3",
            custom_parameter="option"  # Custom parameter example
        )
        print(response)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
```

```python Async IO
# Install the SDK: pip install deepgram-sdk

# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

import asyncio
import os
from dotenv import load_dotenv

from deepgram import AsyncDeepgramClient

load_dotenv()

AUDIO_URL = "https://dpgr.am/bueller.wav"

async def main():
    # STEP 1 Create a Deepgram client using the API key in the environment variables DEEPGRAM_API_KEY
    client = AsyncDeepgramClient()

    try:
        # STEP 2 Call the transcribe_url method with custom parameters
        # To demonstrate using custom parameters, you can pass them directly
        response = await client.listen.v1.media.transcribe_url(
            url=AUDIO_URL,
            model="nova-3",
            smart_format=True,  # Custom parameter example
            custom_parameter="option"  # Another custom parameter example
        )
        print(response)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

# .NET SDK

The Deepgram .NET SDK has defined option parameters, but also allows for arbitrary key/value pairs. You can provide custom parameters when using the .NET SDK to make an API Request even if the parameter isn't defined as an option.

This is useful if you want to use a feature of the Deepgram API that isn't officially supported in the .NET SDK.

## Example

```csharp C#
//Install the SDK: dotnet add package Deepgram

using Deepgram.Models.Listen.v1.REST;

namespace PreRecorded
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Initialize Library with default logging
            // Normal logging is "Info" level
            Library.Initialize();

            // Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
            var deepgramClient = ClientFactory.CreateListenRESTClient();

            var prerecordedOptions = new PreRecordedSchema()
            {
                Model = "nova-3"
            };

            // but to demonstrate using the custom addon parameters, you could enable it like this
            var customOptions = new Dictionary<string, string>();
            customOptions["custom_parameter"] = "option";

            var response = await deepgramClient.TranscribeUrl(
                new UrlSource("https://dpgr.am/bueller.wav"),
                prerecordedOptions,
                null, // Don't want to specify a cancellation token, use the default
                customOptions,
            	);

            Console.WriteLine(response);

            // Teardown Library
            Library.Terminate();
        }
    }
}
```

# Go SDK

The Deepgram Go SDK has defined option parameters, but also allows for arbitrary key/value pairs. You can provide custom parameters when using the Go SDK to make an API Request even if the parameter isn't defined as an option.

This is useful if you want to use a feature of the Deepgram API that isn't officially supported in the Go SDK.

## Example

```go Go
// Install the SDK: go get github.com/deepgram/deepgram-go-sdk

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	prettyjson "github.com/hokaccha/go-prettyjson"

	api "github.com/deepgram/deepgram-go-sdk/pkg/api/listen/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/pkg/client/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/pkg/client/listen"
)

const (
	url string = "https://dpgr.am/bueller.wav"
)

func main() {
	// init library
	client.InitWithDefault()

	// Go context
	ctx := context.Background()

	// set the Transcription options
	options := &interfaces.PreRecordedTranscriptionOptions{
		Model: "nova-3",
	}

	// create a Deepgram client
	c := client.NewRESTWithDefaults()
	dg := api.New(c)

	// but to demonstrate using the custom addon parameters, you could enable it like this
	params := make(map[string][]string, 0)
	params["custom_parameter"] = []string{"option"}
	ctx = interfaces.WithCustomParameters(ctx, params)

	// send/process file to Deepgram
	res, err := dg.FromURL(ctx, url, options)
	if err != nil {
		if e, ok := err.(*interfaces.StatusError); ok {
			fmt.Printf("DEEPGRAM ERROR:\n%s:\n%s\n", e.DeepgramError.ErrCode, e.DeepgramError.ErrMsg)
		}
		fmt.Printf("FromStream failed. Err: %v\n", err)
		os.Exit(1)
	}

	data, err := json.Marshal(res)
	if err != nil {
		fmt.Printf("json.Marshal failed. Err: %v\n", err)
		os.Exit(1)
	}

	// make the JSON pretty
	prettyJSON, err := prettyjson.Format(data)
	if err != nil {
		fmt.Printf("prettyjson.Marshal failed. Err: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("\n\nResult:\n%s\n\n", prettyJSON)
}
```

# Java SDK

The Deepgram Java SDK uses a typed builder pattern for all request parameters. For parameters not yet supported in the SDK, you can pass them as additional query parameters via `RequestOptions`.

## Example

```java Java
// Install: Add to pom.xml:
// <dependency>
//   <groupId>com.deepgram</groupId>
//   <artifactId>deepgram-java-sdk</artifactId>
//   <version>0.7.0</version>
// </dependency>

import com.deepgram.DeepgramClient;
import com.deepgram.resources.listen.v1.media.requests.ListenV1RequestUrl;
import com.deepgram.resources.listen.v1.media.types.MediaTranscribeRequestModel;
import com.deepgram.core.RequestOptions;

DeepgramClient client = DeepgramClient.builder().build();

// Use the typed builder for known parameters.
// To pass a custom parameter not yet in the SDK, use RequestOptions:
var response = client.listen().v1().media().transcribeUrl(
    ListenV1RequestUrl.builder()
        .url("https://dpgr.am/bueller.wav")
        .model(MediaTranscribeRequestModel.NOVA3)
        .build(),
    RequestOptions.builder()
        .addQueryParameter("custom_parameter", "option")
        .build()
);

System.out.println(response);
```

## Flux Multilingual Note

`flux-general-multi` uses the `language_hint` query parameter on the `/v2/listen` WebSocket endpoint.

```javascript JavaScript
import { DeepgramClient } from "@deepgram/sdk";

const client = new DeepgramClient();

const connection = await client.listen.v2.connect({
  model: "flux-general-multi",
  encoding: "linear16",
  sample_rate: 16000,
  Authorization: `Token ${process.env.DEEPGRAM_API_KEY}`,
  queryParams: { language_hint: ["en", "es"] },
});

connection.connect();
await connection.waitForOpen();
```

```python Python
from deepgram import AsyncDeepgramClient

client = AsyncDeepgramClient()

async with client.listen.v2.connect(
    model="flux-general-multi",
    encoding="linear16",
    sample_rate=16000,
    request_options={
        "additional_query_parameters": {
            "language_hint": ["en", "es"],
        }
    },
) as connection:
    await connection.start_listening()
```

```java Java
// Example: set language hints with Configure.

import com.deepgram.DeepgramClient;
import com.deepgram.resources.listen.v2.types.ListenV2Configure;
import com.deepgram.resources.listen.v2.websocket.V2ConnectOptions;
import com.deepgram.resources.listen.v2.websocket.V2WebSocketClient;
import com.deepgram.types.ListenV2Encoding;
import com.deepgram.types.ListenV2Model;
import com.deepgram.types.ListenV2SampleRate;
import java.util.List;
import java.util.concurrent.TimeUnit;

DeepgramClient client = DeepgramClient.builder().build();

V2ConnectOptions options = V2ConnectOptions.builder()
    .model(ListenV2Model.FLUX_GENERAL_MULTI)
    .encoding(ListenV2Encoding.LINEAR16)
    .sampleRate(ListenV2SampleRate.of(16000))
    .build();

V2WebSocketClient connection = client.listen().v2().v2WebSocket();
connection.connect(options).get(10, TimeUnit.SECONDS);
connection.sendConfigure(
    ListenV2Configure.builder()
        .languageHints(List.of("en", "es"))
        .build()
).get(5, TimeUnit.SECONDS);
```
