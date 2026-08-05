---
title: "Build A Function Call"
source: https://developers.deepgram.com/docs/build-a-function-call.md
path: docs/build-a-function-call
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build A Function Call

This guide walks you through building function calls for your Voice Agent. We start with a basic weather lookup example and then move to a more complex customer management system.

## Basic Example: Weather Lookup

This example demonstrates a simple client-side function call. When a user asks about the weather, the agent extracts the location and requests that your client fetch the data.

### 1. Define the Function in Settings

Include the function definition in your `Settings` message under the `agent.think` object.

```json JSON
{
  "type": "Settings",
  "agent": {
    "think": {
      "provider": {
        "type": "open_ai",
        "model": "gpt-4o-mini"
      },
      "prompt": "You are a helpful AI assistant that can provide weather information.",
      "functions": [
        {
          "name": "get_weather",
          "description": "Get the current weather for a specific location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city or location to get weather for"
              }
            },
            "required": ["location"]
          }
        }
      ]
    }
  }
}
```

### 2. Implement the Function Logic

Your client application must implement the logic to handle the `get_weather` request.

```javascript JavaScript
export const getWeather = async (location: string): Promise<string | null> => {
  const apiKey = import.meta.env.VITE_OPENWEATHER_API_KEY;

  try {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}`
    );

    if (!response.ok) {
      throw new Error('Failed to fetch weather data');
    }

    const data = await response.json();

    return `The current weather in ${data.name} is ${data.weather[0].description} with a temperature of ${data.main.temp}°K.`;
  } catch (err) {
    console.error(err);
    return null;
  }
};
```

```python Python
import os
import requests
from typing import Optional

def get_weather(location: str) -> Optional[str]:
    api_key = os.getenv("OPENWEATHER_API_KEY")

    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather",
            params={"q": location, "appid": api_key}
        )
        response.raise_for_status()

        data = response.json()
        return f"The current weather in {data['name']} is {data['weather'][0]['description']} with a temperature of {data['main']['temp']}°K."
    except Exception as err:
        print(f"Error: {err}")
        return None
```

```CSharp C#
using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

public class WeatherService
{
    private readonly HttpClient _httpClient;

    public WeatherService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<string?> GetWeather(string location)
    {
        var apiKey = Environment.GetEnvironmentVariable("OPENWEATHER_API_KEY");

        try
        {
            var response = await _httpClient.GetAsync(
                $"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}"
            );

            response.EnsureSuccessStatusCode();

            var data = await JsonSerializer.DeserializeAsync<WeatherResponse>(
                await response.Content.ReadAsStreamAsync()
            );

            return $"The current weather in {data?.Name} is {data?.Weather[0].Description} with a temperature of {data?.Main.Temp}°K.";
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"Error: {ex.Message}");
            return null;
        }
    }
}

public class WeatherResponse
{
    public string Name { get; set; }
    public Weather[] Weather { get; set; }
    public Main Main { get; set; }
}

public class Weather
{
    public string Description { get; set; }
}

public class Main
{
    public float Temp { get; set; }
}
```

```Go Go
package main

import (
    "encoding/json"
    "fmt"
    "net/http"
    "os"
)

type WeatherResponse struct {
    Name string `json:"name"`
    Weather []struct {
        Description string `json:"description"`
    } `json:"weather"`
    Main struct {
        Temp float64 `json:"temp"`
    } `json:"main"`
}

func getWeather(location string) (string, error) {
    apiKey := os.Getenv("OPENWEATHER_API_KEY")

    url := fmt.Sprintf("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s", location, apiKey)
    resp, err := http.Get(url)
    if err != nil {
        return "", fmt.Errorf("failed to fetch weather data: %v", err)
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        return "", fmt.Errorf("failed to fetch weather data: status code %d", resp.StatusCode)
    }

    var data WeatherResponse
    if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
        return "", fmt.Errorf("failed to decode response: %v", err)
    }

    return fmt.Sprintf("The current weather in %s is %s with a temperature of %.2f°K.",
        data.Name, data.Weather[0].Description, data.Main.Temp), nil
}
```

***

## Advanced Example: Customer Management System

This section walks you through building a more complex function call system for a demo Voice Agent application. For the complete code, see the [code repository](https://github.com/deepgram-devs/flask-agent-function-calling-demo).

### Getting Started

You'll create two files:

* **`agent_functions.py`**: Contains async functions and configuration for customer lookups, appointments, and order management.
* **`agent_templates.py`**: Defines the agent prompt, settings, and the `AgentTemplates` factory class for industry-specific configuration.

### Prerequisites

* Python 3.7+
* Familiarity with Python
* An understanding of how to use Python Virtual environments.
* Familiarity with the [Deepgram Voice Agent API](/reference/voice-agent/voice-agent)

## Create `agent_functions.py`

This guide doesn't cover the development of the **business logic** for this application. Please see [business\_logic.py](https://github.com/deepgram-devs/flask-agent-function-calling-demo/blob/main/common/business_logic.py) for more details.

First, create a file called: `agent_functions.py`. Then in `agent_functions.py` set up the dependencies and import the business logic.

```python Python
import json
from datetime import datetime, timedelta
import asyncio
from business_logic import (
    get_customer,
    get_customer_appointments,
    get_customer_orders,
    schedule_appointment,
    get_available_appointment_slots,
    prepare_agent_filler_message,
    prepare_farewell_message
)
```

```java Java
import com.deepgram.DeepgramClient;
import com.deepgram.resources.agent.v1.types.*;
import com.deepgram.resources.agent.v1.websocket.V1WebSocketClient;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

// Business logic imports (your application-specific classes)
import com.example.BusinessLogic;
```

### Implement the Functions

We'll implement the following functions in `agent_functions.py` to handle customer and appointment management:

| Function Name        | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| `find_customer`      | Lookup by phone, email, or ID; normalizes input            |
| `get_appointments`   | Retrieve all appointments for a customer                   |
| `get_orders`         | Retrieve order history for a customer                      |
| `create_appointment` | Schedule a new appointment                                 |
| `check_availability` | Find available appointment slots                           |
| `agent_filler`       | Provide conversational filler (requires websocket param)   |
| `end_call`           | End the conversation gracefully (requires websocket param) |

### Find Customer

```python Python
async def find_customer(params):
    """Look up a customer by phone, email, or ID."""
    phone = params.get("phone")
    email = params.get("email")
    customer_id = params.get("customer_id")

    result = await get_customer(phone=phone, email=email, customer_id=customer_id)
    return result
```

```java Java
public Map<String, Object> findCustomer(Map<String, Object> params) {
    String phone = (String) params.get("phone");
    String email = (String) params.get("email");
    String customerId = (String) params.get("customer_id");

    return BusinessLogic.getCustomer(phone, email, customerId);
}
```

### Get Appointments

```python Python
async def get_appointments(params):
    """Get appointments for a customer."""
    customer_id = params.get("customer_id")
    if not customer_id:
        return {"error": "customer_id is required"}

    result = await get_customer_appointments(customer_id)
    return result
```

```java Java
public Map<String, Object> getAppointments(Map<String, Object> params) {
    String customerId = (String) params.get("customer_id");
    if (customerId == null) {
        return Map.of("error", "customer_id is required");
    }

    return BusinessLogic.getCustomerAppointments(customerId);
}
```

### Get Orders

```python Python
async def get_orders(params):
    """Get orders for a customer."""
    customer_id = params.get("customer_id")
    if not customer_id:
        return {"error": "customer_id is required"}

    result = await get_customer_orders(customer_id)
    return result
```

```java Java
public Map<String, Object> getOrders(Map<String, Object> params) {
    String customerId = (String) params.get("customer_id");
    if (customerId == null) {
        return Map.of("error", "customer_id is required");
    }

    return BusinessLogic.getCustomerOrders(customerId);
}
```

### Create Appointment

```python Python
async def create_appointment(params):
    """Schedule a new appointment."""
    customer_id = params.get("customer_id")
    date = params.get("date")
    service = params.get("service")

    if not all([customer_id, date, service]):
        return {"error": "customer_id, date, and service are required"}

    result = await schedule_appointment(customer_id, date, service)
    return result
```

```java Java
public Map<String, Object> createAppointment(Map<String, Object> params) {
    String customerId = (String) params.get("customer_id");
    String date = (String) params.get("date");
    String service = (String) params.get("service");

    if (customerId == null || date == null || service == null) {
        return Map.of("error", "customer_id, date, and service are required");
    }

    return BusinessLogic.scheduleAppointment(customerId, date, service);
}
```

### Check Availability

```python Python
async def check_availability(params):
    """Check available appointment slots."""
    start_date = params.get("start_date")
    end_date = params.get("end_date", (datetime.fromisoformat(start_date) + timedelta(days=7)).isoformat())

    if not start_date:
        return {"error": "start_date is required"}

    result = await get_available_appointment_slots(start_date, end_date)
    return result
```

```java Java
public Map<String, Object> checkAvailability(Map<String, Object> params) {
    String startDate = (String) params.get("start_date");
    String endDate = (String) params.get("end_date");

    if (startDate == null) {
        return Map.of("error", "start_date is required");
    }
    if (endDate == null) {
        endDate = LocalDateTime.parse(startDate)
            .plusDays(7).format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
    }

    return BusinessLogic.getAvailableAppointmentSlots(startDate, endDate);
}
```

### Agent Filler

```python Python

async def agent_filler(websocket, params):
    """
    Handle agent filler messages while maintaining proper function call protocol.
    """
    result = await prepare_agent_filler_message(websocket, **params)
    return result
```

```java Java
public Map<String, Object> agentFiller(
        V1WebSocketClient wsClient, Map<String, Object> params) {
    return BusinessLogic.prepareAgentFillerMessage(wsClient, params);
}
```

### End Call

```python Python

async def end_call(websocket, params):
    """
    End the conversation and close the connection.
    """
    farewell_type = params.get("farewell_type", "general")
    result = await prepare_farewell_message(websocket, farewell_type)
    return result
```

```java Java
public Map<String, Object> endCall(
        V1WebSocketClient wsClient, Map<String, Object> params) {
    String farewellType = (String) params.getOrDefault("farewell_type", "general");
    return BusinessLogic.prepareFarewellMessage(wsClient, farewellType);
}
```

### Create Function Definitions

Next in `agent_functions.py` we'll setup `FUNCTION_DEFINITIONS` which is an array that defines the API contract for the Voice Agent system. It specifies all available operations, their parameters, and usage guidelines.

Each function definition follows a JSON Schema format with:

* Name
* Description
* Parameters specification
* Required fields
* Enumerated values where applicable

```python Python
# Function definitions that will be sent to the Voice Agent API
FUNCTION_DEFINITIONS = [
    {
        "name": "agent_filler",
        "description": """Use this function to provide natural conversational filler before looking up information.
        ALWAYS call this function first with message_type='lookup' when you're about to look up customer information.
        After calling this function, you MUST immediately follow up with the appropriate lookup function (e.g., find_customer).""",
        "parameters": {
            "type": "object",
            "properties": {
                "message_type": {
                    "type": "string",
                    "description": "Type of filler message to use. Use 'lookup' when about to search for information.",
                    "enum": ["lookup", "general"]
                }
            },
            "required": ["message_type"]
        }
    },
    {
        "name": "find_customer",
        "description": """Look up a customer's account information. Use context clues to determine what type of identifier the user is providing:

        Customer ID formats:
        - Numbers only (e.g., '169', '42') → Format as 'CUST0169', 'CUST0042'
        - With prefix (e.g., 'CUST169', 'customer 42') → Format as 'CUST0169', 'CUST0042'

        Phone number recognition:
        - Standard format: '555-123-4567' → Format as '+15551234567'
        - With area code: '(555) 123-4567' → Format as '+15551234567'
        - Spoken naturally: 'five five five, one two three, four five six seven' → Format as '+15551234567'
        - International: '+1 555-123-4567' → Use as is
        - Always add +1 country code if not provided

        Email address recognition:
        - Spoken naturally: 'my email is john dot smith at example dot com' → Format as '[email protected]'
        - With domain: '[email protected]' → Use as is
        - Spelled out: 'j o h n at example dot com' → Format as '[email protected]'""",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer's ID. Format as CUSTXXXX where XXXX is the number padded to 4 digits with leading zeros. Example: if user says '42', pass 'CUST0042'"
                },
                "phone": {
                    "type": "string",
                    "description": """Phone number with country code. Format as +1XXXXXXXXXX:
                    - Add +1 if not provided
                    - Remove any spaces, dashes, or parentheses
                    - Convert spoken numbers to digits
                    Example: 'five five five one two three four five six seven' → '+15551234567'"""
                },
                "email": {
                    "type": "string",
                    "description": """Email address in standard format:
                    - Convert 'dot' to '.'
                    - Convert 'at' to '@'
                    - Remove spaces between spelled out letters
                    Example: 'j dot smith at example dot com' → '[email protected]'"""
                }
            }
        }
    },
    {
        "name": "get_appointments",
        "description": """Retrieve all appointments for a customer. Use this function when:
        - A customer asks about their upcoming appointments
        - A customer wants to know their appointment schedule
        - A customer asks 'When is my next appointment?'

        Always verify you have the customer's account first using find_customer before checking appointments.""",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer's ID in CUSTXXXX format. Must be obtained from find_customer first."
                }
            },
            "required": ["customer_id"]
        }
    },
    {
        "name": "get_orders",
        "description": """Retrieve order history for a customer. Use this function when:
        - A customer asks about their orders
        - A customer wants to check order status
        - A customer asks questions like 'Where is my order?' or 'What did I order?'

        Always verify you have the customer's account first using find_customer before checking orders.""",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer's ID in CUSTXXXX format. Must be obtained from find_customer first."
                }
            },
            "required": ["customer_id"]
        }
    },
    {
        "name": "create_appointment",
        "description": """Schedule a new appointment for a customer. Use this function when:
        - A customer wants to book a new appointment
        - A customer asks to schedule a service

        Before scheduling:
        1. Verify customer account exists using find_customer
        2. Check availability using check_availability
        3. Confirm date/time and service type with customer before booking""",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer's ID in CUSTXXXX format. Must be obtained from find_customer first."
                },
                "date": {
                    "type": "string",
                    "description": "Appointment date and time in ISO format (YYYY-MM-DDTHH:MM:SS). Must be a time slot confirmed as available."
                },
                "service": {
                    "type": "string",
                    "description": "Type of service requested. Must be one of the following: Consultation, Follow-up, Review, or Planning",
                    "enum": ["Consultation", "Follow-up", "Review", "Planning"]
                }
            },
            "required": ["customer_id", "date", "service"]
        }
    },
    {
        "name": "check_availability",
        "description": """Check available appointment slots within a date range. Use this function when:
        - A customer wants to know available appointment times
        - Before scheduling a new appointment
        - A customer asks 'When can I come in?' or 'What times are available?'

        After checking availability, present options to the customer in a natural way, like:
        'I have openings on [date] at [time] or [date] at [time]. Which works better for you?'""",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string",
                    "description": "Start date in ISO format (YYYY-MM-DDTHH:MM:SS). Usually today's date for immediate availability checks."
                },
                "end_date": {
                    "type": "string",
                    "description": "End date in ISO format. Optional - defaults to 7 days after start_date. Use for specific date range requests."
                }
            },
            "required": ["start_date"]
        }
    },
    {
        "name": "end_call",
        "description": """End the conversation and close the connection. Call this function when:
        - User says goodbye, thank you, etc.
        - User indicates they're done ("that's all I need", "I'm all set", etc.)
        - User wants to end the conversation

        Examples of triggers:
        - "Thank you, bye!"
        - "That's all I needed, thanks"
        - "Have a good day"
        - "Goodbye"
        - "I'm done"

        Do not call this function if the user is just saying thanks but continuing the conversation.""",
        "parameters": {
            "type": "object",
            "properties": {
                "farewell_type": {
                    "type": "string",
                    "description": "Type of farewell to use in response",
                    "enum": ["thanks", "general", "help"]
                }
            },
            "required": ["farewell_type"]
        }
    }
]
```

```java Java
// Function definitions sent to the Voice Agent API.
// In the Java SDK, define these as AgentV1Function objects.
List<AgentV1Function> functionDefinitions = List.of(
    AgentV1Function.builder()
        .name("agent_filler")
        .description("Use this function to provide natural conversational filler "
            + "before looking up information. ALWAYS call this function first with "
            + "message_type='lookup' when you're about to look up customer information.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "message_type", Map.of(
                    "type", "string",
                    "description", "Type of filler message to use.",
                    "enum", List.of("lookup", "general")
                )
            ),
            "required", List.of("message_type")
        ))
        .build(),
    AgentV1Function.builder()
        .name("find_customer")
        .description("Look up a customer's account information by phone, email, or ID.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "customer_id", Map.of(
                    "type", "string",
                    "description", "Customer's ID in CUSTXXXX format."
                ),
                "phone", Map.of(
                    "type", "string",
                    "description", "Phone number with country code (+1XXXXXXXXXX)."
                ),
                "email", Map.of(
                    "type", "string",
                    "description", "Email address in standard format."
                )
            )
        ))
        .build(),
    AgentV1Function.builder()
        .name("get_appointments")
        .description("Retrieve all appointments for a customer.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "customer_id", Map.of(
                    "type", "string",
                    "description", "Customer's ID in CUSTXXXX format."
                )
            ),
            "required", List.of("customer_id")
        ))
        .build(),
    AgentV1Function.builder()
        .name("get_orders")
        .description("Retrieve order history for a customer.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "customer_id", Map.of(
                    "type", "string",
                    "description", "Customer's ID in CUSTXXXX format."
                )
            ),
            "required", List.of("customer_id")
        ))
        .build(),
    AgentV1Function.builder()
        .name("create_appointment")
        .description("Schedule a new appointment for a customer.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "customer_id", Map.of("type", "string",
                    "description", "Customer's ID in CUSTXXXX format."),
                "date", Map.of("type", "string",
                    "description", "Appointment date/time in ISO format."),
                "service", Map.of("type", "string",
                    "description", "Service type.",
                    "enum", List.of("Consultation", "Follow-up", "Review", "Planning"))
            ),
            "required", List.of("customer_id", "date", "service")
        ))
        .build(),
    AgentV1Function.builder()
        .name("check_availability")
        .description("Check available appointment slots within a date range.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "start_date", Map.of("type", "string",
                    "description", "Start date in ISO format."),
                "end_date", Map.of("type", "string",
                    "description", "End date in ISO format. Defaults to 7 days after start.")
            ),
            "required", List.of("start_date")
        ))
        .build(),
    AgentV1Function.builder()
        .name("end_call")
        .description("End the conversation and close the connection.")
        .parameters(Map.of(
            "type", "object",
            "properties", Map.of(
                "farewell_type", Map.of(
                    "type", "string",
                    "description", "Type of farewell to use.",
                    "enum", List.of("thanks", "general", "help")
                )
            ),
            "required", List.of("farewell_type")
        ))
        .build()
);
```

### Create a Function Map

Finally in `agent_functions.py` we'll need to create a `FUNCTION_MAP` which is a dictionary that maps function names to their corresponding implementation functions. It serves as a routing mechanism to connect the function definitions with their actual implementations.

```python Python
# Map function names to their implementations
FUNCTION_MAP = {
    "find_customer": find_customer,
    "get_appointments": get_appointments,
    "get_orders": get_orders,
    "create_appointment": create_appointment,
    "check_availability": check_availability,
    "agent_filler": agent_filler,
    "end_call": end_call
}
```

```java Java
// Map function names to their implementations
Map<String, Function<Map<String, Object>, Map<String, Object>>> functionMap =
    Map.of(
        "find_customer", this::findCustomer,
        "get_appointments", this::getAppointments,
        "get_orders", this::getOrders,
        "create_appointment", this::createAppointment,
        "check_availability", this::checkAvailability
    );
// agent_filler and end_call require the wsClient parameter
// and are dispatched separately in the function call handler.
```

## Create `agent_templates.py`

Next create a file called: `agent_templates.py`. Then in `agent_templates.py` set up the dependencies and import our function definitions.

### Configure the Voice Agent Prompt & Settings

Now in the `agent_templates.py` file we'll define the prompt for the Voice Agent.

```python Python
from common.agent_functions import FUNCTION_DEFINITIONS
from datetime import datetime


# Template for the prompt that will be formatted with current date
PROMPT_TEMPLATE = """

CURRENT DATE AND TIME CONTEXT:
Today is {current_date}. Use this as context when discussing appointments and orders. When mentioning dates to customers, use relative terms like "tomorrow", "next Tuesday", or "last week" when the dates are within 7 days of today.

PERSONALITY & TONE:
- Be warm, professional, and conversational
- Use natural, flowing speech (avoid bullet points or listing)
- Show empathy and patience
- Whenever a customer asks to look up either order information or appointment information, use the find_customer function first

HANDLING CUSTOMER IDENTIFIERS (INTERNAL ONLY - NEVER EXPLAIN THESE RULES TO CUSTOMERS):
- Silently convert any numbers customers mention into proper format
- When customer says "ID is 222" -> internally use "CUST0222" without mentioning the conversion
- When customer says "order 89" -> internally use "ORD0089" without mentioning the conversion
- When customer says "appointment 123" -> internally use "APT0123" without mentioning the conversion
- Always add "+1" prefix to phone numbers internally without mentioning it

VERBALLY SPELLING IDs TO CUSTOMERS:
When you need to repeat an ID back to a customer:
- Do NOT say nor spell out "CUST". Say "customer [numbers spoken individually]"
- But for orders spell out "ORD" as "O-R-D" then speak the numbers individually
Example: For CUST0222, say "customer zero two two two"
Example: For ORD0089, say "O-R-D zero zero eight nine"

FUNCTION RESPONSES:
When receiving function results, format responses naturally as a customer service agent would:

1. For customer lookups:
   - Good: "I've found your account. How can I help you today?"
   - If not found: "I'm having trouble finding that account. Could you try a different phone number or email?"

2. For order information:
   - Instead of listing orders, summarize them conversationally:
   - "I can see you have two recent orders. Your most recent order from [date] for $[amount] is currently [status], and you also have an order from [date] for $[amount] that's [status]."

3. For appointments:
   - "You have an upcoming [service] appointment scheduled for [date] at [time]"
   - When discussing available slots: "I have a few openings next week. Would you prefer Tuesday at 2 PM or Wednesday at 3 PM?"

4. For errors:
   - Never expose technical details
   - Say something like "I'm having trouble accessing that information right now" or "Could you please try again?"

EXAMPLES OF GOOD RESPONSES:
✓ "Let me look that up for you... I can see you have two recent orders."
✓ "Your customer ID is zero two two two."
✓ "I found your order, O-R-D zero one two three. It's currently being processed."

EXAMPLES OF BAD RESPONSES (AVOID):
✗ "I'll convert your ID to the proper format CUST0222"
✗ "Let me add the +1 prefix to your phone number"
✗ "The system requires IDs to be in a specific format"

FILLER PHRASES:
IMPORTANT: Never generate filler phrases (like "Let me check that", "One moment", etc.) directly in your responses.
Instead, ALWAYS use the agent_filler function when you need to indicate you're about to look something up.

Examples of what NOT to do:
- Responding with "Let me look that up for you..." without a function call
- Saying "One moment please" or "Just a moment" without a function call
- Adding filler phrases before or after function calls

Correct pattern to follow:
1. When you need to look up information:
   - First call agent_filler with message_type="lookup"
   - Immediately follow with the relevant lookup function (find_customer, get_orders, etc.)
2. Only speak again after you have the actual information to share

Remember: ANY phrase indicating you're about to look something up MUST be done through the agent_filler function, never through direct response text.
"""
```

```java Java
// The prompt template is the same string across all languages.
// In Java, define it as a constant and inject the current date:
String promptTemplate = """
    CURRENT DATE AND TIME CONTEXT:
    Today is %s. Use this as context when discussing appointments and orders.

    PERSONALITY & TONE:
    - Be warm, professional, and conversational
    - Use natural, flowing speech
    - Show empathy and patience
    - Use find_customer before looking up orders or appointments

    FILLER PHRASES:
    IMPORTANT: Always use the agent_filler function when indicating
    you're about to look something up. Never generate filler phrases directly.
    """;

String prompt = String.format(promptTemplate,
    LocalDate.now().format(DateTimeFormatter.ofPattern("EEEE, MMMM dd, yyyy")));
```

Next in the same file we'll define the settings for the Voice Agent.

```python Python
VOICE = "aura-2-thalia-en"

# this gets updated by the agent template
FIRST_MESSAGE = ""

# audio settings
USER_AUDIO_SAMPLE_RATE = 48000
USER_AUDIO_SECS_PER_CHUNK = 0.05
USER_AUDIO_SAMPLES_PER_CHUNK = round(USER_AUDIO_SAMPLE_RATE * USER_AUDIO_SECS_PER_CHUNK)

AGENT_AUDIO_SAMPLE_RATE = 16000
AGENT_AUDIO_BYTES_PER_SEC = 2 * AGENT_AUDIO_SAMPLE_RATE

VOICE_AGENT_URL = "wss://agent.deepgram.com/v1/agent/converse"
# For EU data processing, use: "wss://api.eu.deepgram.com/v1/agent/converse"
# For AU data processing, use: "wss://api.au.deepgram.com/v1/agent/converse"

AUDIO_SETTINGS = {
    "input": {
        "encoding": "linear16",
        "sample_rate": USER_AUDIO_SAMPLE_RATE,
    },
    "output": {
        "encoding": "linear16",
        "sample_rate": AGENT_AUDIO_SAMPLE_RATE,
        "container": "none",
    },
}

LISTEN_SETTINGS = {
    "provider": {
        "type": "deepgram",
        "model": "nova-3",
    }
}

THINK_SETTINGS = {
    "provider": {
        "type": "open_ai",
        "model": "gpt-4o-mini",
        "temperature": 0.7,
    },
    "prompt": PROMPT_TEMPLATE,
    "functions": FUNCTION_DEFINITIONS,
}

SPEAK_SETTINGS = {
    "provider": {
        "type": "deepgram",
        "model": VOICE,
    }
}

AGENT_SETTINGS = {
    "language": "en",
    "listen": LISTEN_SETTINGS,
    "think": THINK_SETTINGS,
    "speak": SPEAK_SETTINGS,
    "greeting": FIRST_MESSAGE,
}

SETTINGS = {"type": "Settings", "audio": AUDIO_SETTINGS, "agent": AGENT_SETTINGS}
```

```java Java
// Build the agent settings using the Java SDK builder pattern
AgentV1Settings settings = AgentV1Settings.builder()
    .audio(AgentV1SettingsAudio.builder()
        .input(AgentV1SettingsAudioInput.builder()
            .encoding("linear16")
            .sampleRate(48000)
            .build())
        .output(AgentV1SettingsAudioOutput.builder()
            .encoding("linear16")
            .sampleRate(16000)
            .container("none")
            .build())
        .build())
    .agent(AgentV1SettingsAgent.builder()
        .listen(AgentV1SettingsAgentListen.builder()
            .provider(AgentV1SettingsAgentListenProvider.builder()
                .type("deepgram")
                .model("nova-3")
                .build())
            .build())
        .think(AgentV1SettingsAgentThink.builder()
            .provider(AgentV1SettingsAgentThinkProvider.builder()
                .type("open_ai")
                .model("gpt-4o-mini")
                .build())
            .prompt(prompt)
            .functions(functionDefinitions)
            .build())
        .speak(AgentV1SettingsAgentSpeak.builder()
            .provider(AgentV1SettingsAgentSpeakProvider.builder()
                .type("deepgram")
                .model("aura-2-thalia-en")
                .build())
            .build())
        .greeting(firstMessage)
        .build())
    .build();
```

Finally in the same file we'll define the factory class `AgentTemplates` which will be used to configure the Voice Agent. This class will be used to configure the Voice Agent for different industries.

```python Python
class AgentTemplates:
    PROMPT_TEMPLATE = PROMPT_TEMPLATE

    def __init__(
        self,
        industry="tech_support",
        voiceModel="aura-2-thalia-en",
        voiceName="",
    ):
        self.voiceName = voiceName
        self.voiceModel = voiceModel
        self.personality = ""
        self.company = ""
        self.first_message = ""
        self.capabilities = ""

        self.industry = industry

        self.prompt = self.PROMPT_TEMPLATE.format(
            current_date=datetime.now().strftime("%A, %B %d, %Y")
        )

        self.voice_agent_url = VOICE_AGENT_URL
        self.settings = SETTINGS
        self.user_audio_sample_rate = USER_AUDIO_SAMPLE_RATE
        self.user_audio_secs_per_chunk = USER_AUDIO_SECS_PER_CHUNK
        self.user_audio_samples_per_chunk = USER_AUDIO_SAMPLES_PER_CHUNK
        self.agent_audio_sample_rate = AGENT_AUDIO_SAMPLE_RATE
        self.agent_audio_bytes_per_sec = AGENT_AUDIO_BYTES_PER_SEC

        match self.industry:
            case "tech_support":
                self.tech_support()
            case "healthcare":
                self.healthcare()
            case "banking":
                self.banking()
            case "pharmaceuticals":
                self.pharmaceuticals()
            case "retail":
                self.retail()

        self.first_message = f"Hello! I'm {self.voiceName} from {self.company} customer service. {self.capabilities} How can I help you today?"

        self.settings["agent"]["speak"]["provider"]["model"] = self.voiceModel
        self.settings["agent"]["think"]["prompt"] = self.prompt
        self.settings["agent"]["greeting"] = self.first_message

        self.prompt = self.personality + "\n\n" + self.prompt

    def tech_support(
        self, company="TechStyle", agent_voice="aura-2-thalia-en", voiceName=""
    ):
        if voiceName == "":
            voiceName = self.get_voice_name_from_model(agent_voice)
        self.voiceName = voiceName
        self.company = company
        self.voiceModel = agent_voice

        self.personality = f"You are {self.voiceName}, a friendly and professional customer service representative for {self.company}, an online electronics and accessories retailer. Your role is to assist customers with orders, appointments, and general inquiries."

        self.capabilities = "I'd love to help you with your order or appointment."

    def healthcare(
        self, company="HealthFirst", agent_voice="aura-2-andromeda-en", voiceName=""
    ):
        if voiceName == "":
            voiceName = self.get_voice_name_from_model(agent_voice)
        self.voiceName = voiceName
        self.company = company
        self.voiceModel = agent_voice

        self.personality = f"You are {self.voiceName}, a compassionate and knowledgeable healthcare assistant for {self.company}, a leading healthcare provider. Your role is to assist patients with appointments, medical inquiries, and general health information."

        self.capabilities = "I can help you schedule appointments or answer questions about our services."

    def banking(
        self, company="SecureBank", agent_voice="aura-2-apollo-en", voiceName=""
    ):
        if voiceName == "":
            voiceName = self.get_voice_name_from_model(agent_voice)
        self.voiceName = voiceName
        self.company = company
        self.voiceModel = agent_voice

        self.personality = f"You are {self.voiceName}, a professional and trustworthy banking representative for {self.company}, a secure financial institution. Your role is to assist customers with account inquiries, transactions, and financial services."

        self.capabilities = (
            "I can assist you with your account or any banking services you need."
        )

    def pharmaceuticals(
        self, company="MedLine", agent_voice="aura-2-helena-en", voiceName=""
    ):
        if voiceName == "":
            voiceName = self.get_voice_name_from_model(agent_voice)
        self.voiceName = voiceName
        self.company = company
        self.voiceModel = agent_voice

        self.personality = f"You are {self.voiceName}, a professional and trustworthy pharmaceutical representative for {self.company}, a secure pharmaceutical company. Your role is to assist customers with account inquiries, transactions, and appointments. You MAY NOT provide medical advice."

        self.capabilities = "I can assist you with your account or appointments."

    def retail(self, company="StyleMart", agent_voice="aura-2-aries-en", voiceName=""):
        if voiceName == "":
            voiceName = self.get_voice_name_from_model(agent_voice)
        self.voiceName = voiceName
        self.company = company
        self.voiceModel = agent_voice

        self.personality = f"You are {self.voiceName}, a friendly and attentive retail associate for {self.company}, a trendy clothing and accessories store. Your role is to assist customers with product inquiries, orders, and style recommendations."

        self.capabilities = (
            "I can help you find the perfect item or check on your order status."
        )

    def travel(self, company="TravelTech", agent_voice="aura-2-arcas-en", voiceName=""):
        if voiceName == "":
            voiceName = self.get_voice_name_from_model(agent_voice)
        self.voiceName = voiceName
        self.company = company
        self.voiceModel = agent_voice

        self.personality = f"You are {self.voiceName}, a friendly and professional customer service representative for {self.company}, a tech-forward travel agency. Your role is to assist customers with travel bookings, appointments, and general inquiries."

        self.capabilities = (
            "I'd love to help you with your travel bookings or appointments."
        )

    @staticmethod
    def get_available_industries():
        """Return a dictionary of available industries with display names"""
        return {
            "tech_support": "Tech Support",
            "healthcare": "Healthcare",
            "banking": "Banking",
            "pharmaceuticals": "Pharmaceuticals",
            "retail": "Retail",
            "travel": "Travel",
        }

    def get_voice_name_from_model(self, model):
        return model.split("-")[2].split("-")[0].capitalize()

```

```java Java
/**
 * Factory class that configures the Voice Agent for different industries.
 * Each industry method sets the personality, company, voice model, and capabilities.
 */
public class AgentTemplates {
    private String voiceName;
    private String voiceModel;
    private String company;
    private String personality;
    private String capabilities;
    private String firstMessage;
    private AgentV1Settings settings;

    public AgentTemplates(String industry, String voiceModel) {
        this.voiceModel = voiceModel;

        switch (industry) {
            case "tech_support" -> techSupport();
            case "healthcare" -> healthcare();
            case "banking" -> banking();
            default -> techSupport();
        }

        this.firstMessage = String.format(
            "Hello! I'm %s from %s customer service. %s How can I help you today?",
            voiceName, company, capabilities);

        // Build settings using the configured values
        this.settings = AgentV1Settings.builder()
            .agent(AgentV1SettingsAgent.builder()
                .speak(AgentV1SettingsAgentSpeak.builder()
                    .provider(AgentV1SettingsAgentSpeakProvider.builder()
                        .type("deepgram").model(this.voiceModel).build())
                    .build())
                .think(AgentV1SettingsAgentThink.builder()
                    .prompt(this.personality + "\n\n" + prompt)
                    .functions(functionDefinitions)
                    .build())
                .greeting(this.firstMessage)
                .build())
            .build();
    }

    private void techSupport() {
        this.company = "TechStyle";
        this.voiceModel = "aura-2-thalia-en";
        this.voiceName = getVoiceNameFromModel(this.voiceModel);
        this.personality = String.format(
            "You are %s, a friendly customer service representative for %s.",
            voiceName, company);
        this.capabilities = "I'd love to help you with your order or appointment.";
    }

    private void healthcare() {
        this.company = "HealthFirst";
        this.voiceModel = "aura-2-andromeda-en";
        this.voiceName = getVoiceNameFromModel(this.voiceModel);
        this.personality = String.format(
            "You are %s, a compassionate healthcare assistant for %s.",
            voiceName, company);
        this.capabilities = "I can help you schedule appointments or answer questions.";
    }

    private void banking() {
        this.company = "SecureBank";
        this.voiceModel = "aura-2-apollo-en";
        this.voiceName = getVoiceNameFromModel(this.voiceModel);
        this.personality = String.format(
            "You are %s, a professional banking representative for %s.",
            voiceName, company);
        this.capabilities = "I can assist you with your account or banking services.";
    }

    private static String getVoiceNameFromModel(String model) {
        String[] parts = model.split("-");
        String name = parts[2];
        return name.substring(0, 1).toUpperCase() + name.substring(1);
    }

    public AgentV1Settings getSettings() { return settings; }
}
```

## Call the functions from `client.py`

This guide doesn't cover the development of the **client** for this application. Please see [client.py](https://github.com/deepgram-devs/flask-agent-function-calling-demo/blob/main/client.py#L66) for more details.

In the `client.py` file we'll need reference `agent_templates.py` which will define the settings for the Voice Agent.

```python Python
settings = self.agent_templates.settings
```

```java Java
DeepgramClient client = DeepgramClient.builder().build();
V1WebSocketClient wsClient = client.agent().v1().v1WebSocket();
wsClient.connect().get(10, TimeUnit.SECONDS);

AgentTemplates templates = new AgentTemplates("tech_support", "aura-2-thalia-en");
wsClient.sendSettings(templates.getSettings());

// Handle function call requests from the agent
wsClient.onFunctionCallRequest(request -> {
    String functionName = request.getName();
    Map<String, Object> params = request.getInput();
    Map<String, Object> result = functionMap.get(functionName).apply(params);

    wsClient.sendFunctionCallResponse(
        AgentV1SendFunctionCallResponse.builder()
            .id(request.getId())
            .output(new ObjectMapper().writeValueAsString(result))
            .build());
});
```
