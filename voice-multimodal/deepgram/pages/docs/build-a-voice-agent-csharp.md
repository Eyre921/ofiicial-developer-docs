---
title: "Build a Voice Agent with C#"
source: https://developers.deepgram.com/docs/build-a-voice-agent-csharp.md
path: docs/build-a-voice-agent-csharp
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with C#

This tutorial walks you through building a basic voice agent using C# and the Deepgram .NET SDK. You will learn how to connect to the Agent API, configure its behavior, and stream audio for processing.

## Prerequisites

Before you begin, ensure you have the following:

* A Deepgram API key. You can get one in the [Deepgram Console](https://console.deepgram.com/).
* The .NET SDK installed on your machine.

## 1. Set up your environment

Create a new console project and navigate into it.

```shell
mkdir deepgram-agent-demo
cd deepgram-agent-demo
dotnet new console
```

Export your Deepgram API key as an environment variable.

```shell
# macOS/Linux
export DEEPGRAM_API_KEY="your_api_key"

# Windows PowerShell
$env:DEEPGRAM_API_KEY = "your_api_key"
```

## 2. Install the Deepgram SDK

Add the Deepgram .NET SDK to your project.

```shell
dotnet add package Deepgram
```

## 3. Create the Voice Agent

Open `Program.cs` and replace its content with the following code. This script connects to Deepgram, configures the agent, and streams a sample audio file.

```csharp
using Deepgram;
using Deepgram.Logger;
using Deepgram.Models.Authenticate.v1;
using Deepgram.Models.Agent.v2.WebSocket;
using System.Collections.Generic;
using System.Net.Http;

namespace SampleApp
{
    class Program
    {
        static async Task Main(string[] args)
        {
            try
            {
                Deepgram.Library.Initialize(LogLevel.Debug);

                var apiKey = Environment.GetEnvironmentVariable("DEEPGRAM_API_KEY");
                DeepgramWsClientOptions options = new DeepgramWsClientOptions(null, null, true);
                var agentClient = ClientFactory.CreateAgentWebSocketClient(apiKey, options);

                var lastAudioTime = DateTime.Now;
                var audioFileCount = 0;

                var settingsConfiguration = new SettingsSchema();
                settingsConfiguration.Agent.Think.Provider.Type = "open_ai";
                settingsConfiguration.Agent.Think.Provider.Model = "gpt-4o-mini";
                settingsConfiguration.Audio.Output.SampleRate = 24000;
                settingsConfiguration.Audio.Output.Container = "wav";
                settingsConfiguration.Audio.Input.SampleRate = 24000;
                settingsConfiguration.Agent.Greeting = "Hello, how can I help you today?";
                settingsConfiguration.Agent.Listen.Provider.Type = "deepgram";
                settingsConfiguration.Agent.Listen.Provider.Model = "nova-3";
                settingsConfiguration.Agent.Speak.Provider.Type = "deepgram";
                settingsConfiguration.Agent.Speak.Provider.Model = "aura-2-thalia-en";

                bool connected = await agentClient.Connect(settingsConfiguration);
                if (!connected)
                {
                    Console.WriteLine("Failed to connect to Deepgram WebSocket server.");
                    return;
                }

                await agentClient.Subscribe(new EventHandler<AudioResponse>((sender, e) =>
                {
                    if (DateTime.Now.Subtract(lastAudioTime).TotalSeconds > 7)
                    {
                        audioFileCount++;
                        using (BinaryWriter writer = new BinaryWriter(File.Open($"output_{audioFileCount}.wav", FileMode.Create)))
                        {
                            writer.Write(CreateWavHeader(24000, 16, 1));
                        }
                    }

                    if (e.Stream != null)
                    {
                        using (BinaryWriter writer = new BinaryWriter(File.Open($"output_{audioFileCount}.wav", FileMode.Append)))
                        {
                            writer.Write(e.Stream.ToArray());
                        }
                    }
                    lastAudioTime = DateTime.Now;
                }));

                string url = "https://dpgr.am/spacewalk.wav";
                using (var httpClient = new HttpClient())
                {
                    var response = await httpClient.GetAsync(url);
                    var stream = await response.Content.ReadAsStreamAsync();
                    var buffer = new byte[8192];
                    int bytesRead;

                    while ((bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length)) > 0)
                    {
                        var chunk = new byte[bytesRead];
                        Array.Copy(buffer, chunk, bytesRead);
                        await agentClient.SendBinaryImmediately(chunk);
                    }
                }

                Console.WriteLine("Press any key to exit...");
                Console.ReadKey();

                await agentClient.Stop();
                Deepgram.Library.Terminate();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Exception: {ex.Message}");
            }
        }

        static byte[] CreateWavHeader(int sampleRate, short bitsPerSample, short channels)
        {
            int byteRate = sampleRate * channels * (bitsPerSample / 8);
            short blockAlign = (short)(channels * (bitsPerSample / 8));
            byte[] header = new byte[44];

            header[0] = 0x52; // R
            header[1] = 0x49; // I
            header[2] = 0x46; // F
            header[3] = 0x46; // F
            header[8] = 0x57; // W
            header[9] = 0x41; // A
            header[10] = 0x56; // V
            header[11] = 0x45; // E
            header[12] = 0x66; // f
            header[13] = 0x6D; // m
            header[14] = 0x74; // t
            header[15] = 0x20; // Space
            header[16] = 0x10; // Subchunk1Size
            header[20] = 0x01; // AudioFormat
            header[22] = (byte)channels;
            header[24] = (byte)(sampleRate & 0xFF);
            header[25] = (byte)((sampleRate >> 8) & 0xFF);
            header[26] = (byte)((sampleRate >> 16) & 0xFF);
            header[27] = (byte)((sampleRate >> 24) & 0xFF);
            header[28] = (byte)(byteRate & 0xFF);
            header[29] = (byte)((byteRate >> 8) & 0xFF);
            header[30] = (byte)((byteRate >> 16) & 0xFF);
            header[31] = (byte)((byteRate >> 24) & 0xFF);
            header[32] = (byte)blockAlign;
            header[34] = (byte)bitsPerSample;
            header[36] = 0x64; // d
            header[37] = 0x61; // t
            header[38] = 0x74; // t
            header[39] = 0x61; // a

            return header;
        }
    }
}
```

## 4. Run the Voice Agent

Run your project using the .NET CLI.

```shell
dotnet run
```

The agent will process the audio and generate responses. You can find the agent's audio responses in `output_*.wav` files in your project directory.

## Next steps

Now that you have built a basic agent, you can customize its behavior:

* [Configure the Voice Agent](/docs/configure-voice-agent): Explore all available settings for models and voices.
* [Build a Voice Agent](/docs/build-a-voice-agent): Return to the overview to see other language options.
