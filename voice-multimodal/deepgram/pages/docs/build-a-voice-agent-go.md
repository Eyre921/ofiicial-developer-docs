---
title: "Build a Voice Agent with Go"
source: https://developers.deepgram.com/docs/build-a-voice-agent-go.md
path: docs/build-a-voice-agent-go
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with Go

This tutorial walks you through building a basic voice agent using Go and the Deepgram SDK. You will learn how to connect to the Agent API, configure its behavior, and stream audio for processing.

## Prerequisites

Before you begin, ensure you have the following:

* A Deepgram API key. You can get one in the [Deepgram Console](https://console.deepgram.com/).
* Go installed on your machine.

## 1. Set up your environment

Create a new directory for your project and initialize a Go module.

```shell
mkdir deepgram-agent-demo
cd deepgram-agent-demo
go mod init deepgram-agent-demo
touch main.go
```

Export your Deepgram API key as an environment variable.

```shell
export DEEPGRAM_API_KEY="your_api_key"
```

## 2. Install the Deepgram SDK

Install the Deepgram Go SDK. The `/v3` suffix is required because Go uses major-version module paths.

```shell
go get github.com/deepgram/deepgram-go-sdk/v3
```

## 3. Create the Voice Agent

Open `main.go` and add the following code. This script connects to Deepgram, configures the agent, and streams a sample audio file.

```go
package main

import (
	"bufio"
	"context"
	"fmt"
	"net/http"
	"os"

	msginterfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/agent/v1/websocket/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/agent"
	"github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
)

type MyHandler struct {
	binaryChan chan *[]byte
}

func (dch MyHandler) GetBinary() []*chan *[]byte                                                   { return []*chan *[]byte{&dch.binaryChan} }
func (dch MyHandler) GetOpen() []*chan *msginterfaces.OpenResponse                                 { return nil }
func (dch MyHandler) GetWelcome() []*chan *msginterfaces.WelcomeResponse                           { return nil }
func (dch MyHandler) GetConversationText() []*chan *msginterfaces.ConversationTextResponse         { return nil }
func (dch MyHandler) GetUserStartedSpeaking() []*chan *msginterfaces.UserStartedSpeakingResponse   { return nil }
func (dch MyHandler) GetAgentThinking() []*chan *msginterfaces.AgentThinkingResponse               { return nil }
func (dch MyHandler) GetAgentStartedSpeaking() []*chan *msginterfaces.AgentStartedSpeakingResponse { return nil }
func (dch MyHandler) GetAgentAudioDone() []*chan *msginterfaces.AgentAudioDoneResponse             { return nil }
func (dch MyHandler) GetClose() []*chan *msginterfaces.CloseResponse                               { return nil }
func (dch MyHandler) GetError() []*chan *msginterfaces.ErrorResponse                               { return nil }
func (dch MyHandler) GetUnhandled() []*chan *[]byte                                                { return nil }
func (dch MyHandler) GetInjectionRefused() []*chan *msginterfaces.InjectionRefusedResponse         { return nil }
func (dch MyHandler) GetKeepAlive() []*chan *msginterfaces.KeepAlive                               { return nil }
func (dch MyHandler) GetFunctionCallRequest() []*chan *msginterfaces.FunctionCallRequestResponse   { return nil }
func (dch MyHandler) GetSettingsApplied() []*chan *msginterfaces.SettingsAppliedResponse           { return nil }

func main() {
	ctx := context.Background()

	client.Init(client.InitLib{LogLevel: client.LogLevelDefault})

	cOptions := &interfaces.ClientOptions{EnableKeepAlive: true}
	tOptions := client.NewSettingsConfigurationOptions()
	tOptions.Audio.Output.Encoding = "linear16"
	tOptions.Audio.Output.SampleRate = 24000
	tOptions.Audio.Output.Container = "wav"
	tOptions.Agent.Language = "en"
	tOptions.Agent.Greeting = "Hello! How can I help you today?"
	tOptions.Agent.Listen.Provider = map[string]interface{}{
		"type":  "deepgram",
		"model": "nova-3",
	}
	tOptions.Agent.Think.Provider = map[string]interface{}{
		"type":  "open_ai",
		"model": "gpt-4o-mini",
	}
	tOptions.Agent.Think.Prompt = "You are a friendly AI assistant."
	tOptions.Agent.Speak.Provider = map[string]interface{}{
		"type":  "deepgram",
		"model": "aura-2-thalia-en",
	}

	handler := &MyHandler{binaryChan: make(chan *[]byte)}

	go func() {
		counter := 0
		for br := range handler.binaryChan {
			counter++
			file, _ := os.Create(fmt.Sprintf("output_%d.wav", counter))
			file.Write(*br)
			file.Close()
		}
	}()

	dgClient, _ := client.NewWSUsingChan(ctx, "", cOptions, tOptions, msginterfaces.AgentMessageChan(*handler))
	dgClient.Connect()

	resp, _ := http.Get("https://dpgr.am/spacewalk.wav")
	defer resp.Body.Close()

	dgClient.Stream(bufio.NewReader(resp.Body))

	fmt.Println("Press ENTER to exit")
	bufio.NewScanner(os.Stdin).Scan()
	dgClient.Stop()
}
```

## 4. Run the Voice Agent

Run your script using the Go CLI.

```shell
go run main.go
```

The agent will process the audio and generate responses. You can find the agent's audio responses in `output_*.wav` files in your project directory.

## Next steps

Now that you have built a basic agent, you can customize its behavior:

* [Configure the Voice Agent](/docs/configure-voice-agent): Explore all available settings for models and voices.
* [Build a Voice Agent](/docs/build-a-voice-agent): Return to the overview to see other language options.
