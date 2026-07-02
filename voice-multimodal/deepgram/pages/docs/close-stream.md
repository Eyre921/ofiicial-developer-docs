---
title: "Close Stream"
source: https://developers.deepgram.com/docs/close-stream.md
path: docs/close-stream
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Close Stream

&#x20;Streaming:Nova

Use the `CloseStream` message to close the WebSocket stream. This forces the server to immediately process any unprocessed audio data and return the final transcription results.

## Purpose

In real-time audio processing, there are scenarios where you may need to force the server to close. Deepgram supports a `CloseStream` message to handle such situations. This message will send a shutdown command to the server instructing it to finish processing any cached data, send the response to the client, send a summary metadata object, and then terminate the WebSocket connection.

## Example Payloads

To send the `CloseStream` message, you need to send the following JSON message to the server:

```json JSON
{
  "type": "CloseStream"
}
```

Upon receiving the `CloseStream` message, the server will process all remaining audio data and return the following:

```json JSON
{
    "type": "Metadata",
    "transaction_key": "deprecated",
    "request_id": "8c8ebea9-dbec-45fa-a035-e4632cb05b5f",
    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "created": "2024-08-29T22:37:55.202Z",
    "duration": 0.0,
    "channels": 0
}
```

## Language-Specific Implementations

Below are code examples to help you get started using `CloseStream`.

```javascript JavaScript
const WebSocket = require("ws");

// Assuming 'headers' is already defined for authorization
const ws = new WebSocket("wss://api.deepgram.com/v1/listen", { headers });

ws.on('open', function open() {
  // Construct CloseStream message
  const closeStreamMsg = JSON.stringify({ type: "CloseStream" });

  // Send CloseStream message
  ws.send(closeStreamMsg);
});
```

```python Python
import json
import websocket

# Assuming 'headers' is already defined for authorization
ws = websocket.create_connection("wss://api.deepgram.com/v1/listen", header=headers)

# Construct CloseStream message
closestream_msg = json.dumps({"type": "CloseStream"})

# Send CloseStream message
ws.send(closestream_msg)
```

```go Go
package main

import (
    "encoding/json"
    "log"
    "net/http"
    "github.com/gorilla/websocket"
)

func main() {
    // Define headers for authorization
    headers := http.Header{}
    headers.Add("Authorization", "Token YOUR_API_KEY") // Replace with your actual API key

    // Connect to the WebSocket server
    conn, _, err := websocket.DefaultDialer.Dial("wss://api.deepgram.com/v1/listen", headers)
    if err != nil {
        log.Fatal("Error connecting to WebSocket:", err)
    }
    defer conn.Close()

    // Construct CloseStream message
    closeStreamMsg := map[string]string{"type": "CloseStream"}
    jsonMsg, err := json.Marshal(closeStreamMsg)
    if err != nil {
        log.Fatal("Error encoding JSON:", err)
    }

    // Send CloseStream message
    err = conn.WriteMessage(websocket.TextMessage, jsonMsg)
    if err != nil {
        log.Fatal("Error sending CloseStream message:", err)
    }
}
```

```csharp C#
using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Set up the WebSocket URL and headers
        Uri uri = new Uri("wss://api.deepgram.com/v1/listen");
        string apiKey = "YOUR_API_KEY"; // Replace with your actual API key

        // Create a new client WebSocket instance
        using (ClientWebSocket ws = new ClientWebSocket())
        {
            // Set the authorization header
            ws.Options.SetRequestHeader("Authorization", "Token " + apiKey);

            try
            {
                // Connect to the WebSocket server
                await ws.ConnectAsync(uri, CancellationToken.None);

                // Construct the CloseStream message
                string closeStreamMsg = "{\"type\": \"CloseStream\"}";

                // Convert the CloseStream message to a byte array
                byte[] finalizeBytes = Encoding.UTF8.GetBytes(closeStreamMsg);

                // Send the CloseStream message asynchronously
                await ws.SendAsync(new ArraySegment<byte>(finalizeBytes), WebSocketMessageType.Text, true, CancellationToken.None);
            }
            catch (WebSocketException ex)
            {
                Console.WriteLine("WebSocket error: " + ex.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("General error: " + ex.Message);
            }
        }
    }
}
```

```java Java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.WebSocket;

// Assuming 'headers' is already defined for authorization
HttpClient client = HttpClient.newHttpClient();
WebSocket ws = client.newWebSocketBuilder()
    .header("Authorization", "Token DEEPGRAM_API_KEY")
    .buildAsync(URI.create("wss://api.deepgram.com/v1/listen"), new WebSocket.Listener() {
        @Override
        public void onOpen(WebSocket webSocket) {
            // Construct and send CloseStream message
            webSocket.sendText("{\"type\": \"CloseStream\"}", true);
            WebSocket.Listener.super.onOpen(webSocket);
        }
    })
    .join();
```

***
