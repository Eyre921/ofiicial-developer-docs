---
title: "Build a coding agent"
source: https://docs.together.ai/docs/how-to-build-coding-agents
path: docs/how-to-build-coding-agents
---

Build a simple code editing agent from scratch in 400 lines of code.

I recently read a great [blog post](https://ampcode.com/how-to-build-an-agent) by Thorsten Ball on how simple it is to build coding agents and was inspired to make a python version guide here!

We'll create an LLM that can call tools that allow it to create, edit and read the contents of files and repos!

## Setup

First, let's import the necessary libraries. We'll be using the `together` library to interact with the Together AI API.

<CodeGroup>
  ```sh Shell theme={null}
  !pip install together
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()
  ```
</CodeGroup>

## Basic Chat Interaction

Let's start with a simple loop that takes user input, sends it to a language model (LLM) using the Together AI client, and prints the LLM's response. We'll maintain a `messages_history` to keep track of the conversation context.

<CodeGroup>
  ```python Python theme={null}
  def chat():
      while True:
          user_input = input("Enter something (type 'exit' to quit): ")
          if user_input.lower() == "exit":
              break
          messages_history.append({"role": "user", "content": user_input})
          print(f"You: {user_input}")
          # Process user_input here
          completion = client.chat.completions.create(
              model="Qwen/Qwen3.5-9B",
              reasoning={"enabled": False},
              messages=messages_history,
          )
          print(f"LLM: {completion.choices[0].message.content}")
          messages_history.append(
              {
                  "role": "assistant",
                  "content": completion.choices[0].message.content,
              }
          )


  chat()
  ```
</CodeGroup>

Usage:

```
You: Hey! I'm Zain! How are you?

LLM: Nice to meet you, Zain. I'm doing well, thanks for asking. I'm a large language model, so I don't have feelings or emotions like humans do, but I'm always happy to chat and help with any questions or topics you'd like to discuss. How about you? How's your day going?

You: Can you come up with any horse-related nicknames that make fun of my first name?

LLM: I can try to come up with some horse-related nicknames that poke fun at your name. Keep in mind that these are lighthearted and meant in a playful spirit.

Here are a few ideas:

1. Zain Stallion (a playful take on the idea of a strong, majestic horse)
2. Zainy McMane (a silly name that adds a fun twist to your name)
3. Zain the Reiner (a reference to the reining horse discipline, with a nod to your name)
4. Zainy Horseface (a goofy nickname that's sure to bring a smile)
5. Zain the Colt (a playful reference to a young, energetic horse)

Remember, these are just for fun, and I'm sure you're more than just a nickname!
```

## Tool use by LLMs

Tool use is pretty simple - we tell the model that it has access to certain tools and instruct it to use them when it feels it would help resolve a prompt. As Thorsten says:

To summarize, all there is to tools and tool use are two things:

1. You tell the model what tools are available
2. When the model wants to execute the tool, it tells you, you execute the tool and send the response up

To make (1) easier, the big model providers have built-in APIs to send tool definitions along.

To get the intuition behind `tool_use` you don't need to make any code changes - we can simply use the same `chat()` function above:

```
You: You are a weather expert. When I ask you about the weather in a given location, I want you to reply with `get_weather(<location_name>)`. I will then tell you what the weather in that location is. Understood?

LLM: You're reminding me of our previous agreement. Yes, I understand. When you ask about the weather in a location, I'll respond with `get_weather(<location_name>)`, and you'll provide the actual weather conditions. Let's get back to it.

You: Hey, what's the weather in Munich?

LLM: get_weather(Munich)

You: hot and humid, 28 degrees celcius

LLM: It sounds like Munich is experiencing a warm and muggy spell. I'll make a note of that. What's the weather like in Paris?
```

Pretty simple! We asked the model to use the `get_weather()` function if needed and it did. When it did we provided it information it wanted and it followed us by using that information to answer our original question!

This is all function calling/tool-use really is!

## Defining Tools for the Agent

To make this workflow of instructing the model to use tools and then running the functions it calls and sending it the response more convenient people have built scaffolding where we can pass in pre-specified tools to LLMs as follows:

<CodeGroup>
  ```python Python theme={null}
  # Let define a function that you would use to read a file


  def read_file(path: str) -> str:
      """
      Reads the content of a file and returns it as a string.

      Args:
          path: The relative path of a file in the working directory.

      Returns:
          The content of the file as a string.

      Raises:
          FileNotFoundError: If the specified file does not exist.
          PermissionError: If the user does not have permission to read the file.
      """
      try:
          with open(path, "r", encoding="utf-8") as file:
              content = file.read()
          return content
      except FileNotFoundError:
          raise FileNotFoundError(f"The file '{path}' was not found.")
      except PermissionError:
          raise PermissionError(f"You don't have permission to read '{path}'.")
      except Exception as e:
          raise Exception(f"An error occurred while reading '{path}': {str(e)}")


  read_file_schema = {
      "type": "function",
      "function": {
          "name": "read_file",
          "description": "The relative path of a file in the working directory.",
          "parameters": {
              "properties": {
                  "path": {
                      "description": "The relative path of a file in the working directory.",
                      "title": "Path",
                      "type": "string",
                  }
              },
              "type": "object",
          },
      },
  }
  ```
</CodeGroup>

Function schema:

```json theme={null}
{'type': 'function',
 'function': {'name': 'read_file',
  'description': 'The relative path of a file in the working directory.',
  'parameters': {'properties': {'path': {'description': 'The relative path of a file in the working directory.',
     'title': 'Path',
     'type': 'string'}},
   'type': 'object'}}}
```

We can now pass these function/tool into an LLM and if needed it will use it to read files!

Let's create a file first:

<CodeGroup>
  ```shell Shell theme={null}
  echo "my favourite colour is cyan sanguine" >> secret.txt
  ```
</CodeGroup>

Now let's see if the model can use the new `read_file` tool to discover the secret!

<CodeGroup>
  ```python Python theme={null}
  import os
  import json

  messages = [
      {
          "role": "system",
          "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
          "role": "user",
          "content": "Read the file secret.txt and reveal the secret!",
      },
  ]
  tools = [read_file_schema]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=messages,
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```
</CodeGroup>

This will output a tool call from the model:

```json theme={null}
[
  {
    "id": "call_kx9yu9ti0ejjabt7kexrsn1c",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"secret.txt\"}"
    },
    "index": 0
  }
]
```

## Calling Tools

Now we need to run the function that the model has asked for and feed the response back to the model, this can be done by simply checking if the model asked for a tool call and executing the corresponding function and sending the response to the model:

<CodeGroup>
  ```python Python theme={null}
  tool_calls = response.choices[0].message.tool_calls

  # check is a tool was called by the first model call
  if tool_calls:
      for tool_call in tool_calls:
          function_name = tool_call.function.name
          function_args = json.loads(tool_call.function.arguments)

          if function_name == "read_file":
              # manually call the function
              function_response = read_file(path=function_args.get("path"))

              # add the response to messages to be sent back to the model
              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )
      # re-call the model now with the response of the tool!
      function_enriched_response = client.chat.completions.create(
          model="Qwen/Qwen2.5-7B-Instruct-Turbo",
          messages=messages,
      )
      print(
          json.dumps(
              function_enriched_response.choices[0].message.model_dump(),
              indent=2,
          )
      )
  ```
</CodeGroup>

Output:

<CodeGroup>
  ```json Json theme={null}
  {
    "role": "assistant",
    "content": "The secret from the file secret.txt is \"my favourite colour is cyan sanguine\".",
    "tool_calls": []
  }
  ```
</CodeGroup>

Above, we simply did the following:

1. See if the model wanted us to use a tool.
2. If so, we used the tool for it.
3. We appended the output from the tool back into `messages` and called the model again to make sense of the function response.

Now let's make our coding agent more interesting by creating two more tools!

## More tools: `list_files` and `edit_file`

We'll want our coding agent to be able to see what files exist in a repo and also modify pre-existing files as well so we'll add two more tools:

### `list_files` Tool: Given a path to a repo, this tool lists the files in that repo.

<CodeGroup>
  ```python Python theme={null}
  def list_files(path="."):
      """
      Lists all files and directories in the specified path.

      Args:
          path (str): The relative path of a directory in the working directory.
                      Defaults to the current directory.

      Returns:
          str: A JSON string containing a list of files and directories.
      """
      result = []
      base_path = Path(path)

      if not base_path.exists():
          return json.dumps({"error": f"Path '{path}' does not exist"})

      for root, dirs, files in os.walk(path):
          root_path = Path(root)
          rel_root = (
              root_path.relative_to(base_path)
              if root_path != base_path
              else Path(".")
          )

          # Add directories with trailing slash
          for dir_name in dirs:
              rel_path = rel_root / dir_name
              if str(rel_path) != ".":
                  result.append(f"{rel_path}/")

          # Add files
          for file_name in files:
              rel_path = rel_root / file_name
              if str(rel_path) != ".":
                  result.append(str(rel_path))

      return json.dumps(result)


  list_files_schema = {
      "type": "function",
      "function": {
          "name": "list_files",
          "description": "List all files and directories in the specified path.",
          "parameters": {
              "type": "object",
              "properties": {
                  "path": {
                      "type": "string",
                      "description": "The relative path of a directory in the working directory. Defaults to current directory.",
                  }
              },
          },
      },
  }

  # Register the list_files function in the tools
  tools.append(list_files_schema)
  ```
</CodeGroup>

### `edit_file` Tool: Edit files by adding new content or replacing old content

<CodeGroup>
  ```python Python theme={null}
  def edit_file(path, old_str, new_str):
      """
      Edit a file by replacing all occurrences of old_str with new_str.
      If old_str is empty and the file doesn't exist, create a new file with new_str.

      Args:
          path (str): The relative path of the file to edit
          old_str (str): The string to replace
          new_str (str): The string to replace with

      Returns:
          str: "OK" if successful
      """

      if not path or old_str == new_str:
          raise ValueError("Invalid input parameters")

      try:
          with open(path, "r") as file:
              old_content = file.read()
      except FileNotFoundError:
          if old_str == "":
              # Create a new file if old_str is empty and file doesn't exist
              with open(path, "w") as file:
                  file.write(new_str)
              return "OK"
          else:
              raise FileNotFoundError(f"File not found: {path}")

      new_content = old_content.replace(old_str, new_str)

      if old_content == new_content and old_str != "":
          raise ValueError("old_str not found in file")

      with open(path, "w") as file:
          file.write(new_content)

      return "OK"


  # Define the function schema for the edit_file tool
  edit_file_schema = {
      "type": "function",
      "function": {
          "name": "edit_file",
          "description": "Edit a file by replacing all occurrences of a string with another string",
          "parameters": {
              "type": "object",
              "properties": {
                  "path": {
                      "type": "string",
                      "description": "The relative path of the file to edit",
                  },
                  "old_str": {
                      "type": "string",
                      "description": "The string to replace (empty string for new files)",
                  },
                  "new_str": {
                      "type": "string",
                      "description": "The string to replace with",
                  },
              },
              "required": ["path", "old_str", "new_str"],
          },
      },
  }

  # Update the tools list to include the edit_file function
  tools.append(edit_file_schema)
  ```
</CodeGroup>

## Incorporating Tools into the Coding Agent

Now we can add all three of these tools into the simple looping chat function we made and call it!

<CodeGroup>
  ```python Python theme={null}
  def chat():
      messages_history = []

      while True:
          user_input = input("You: ")
          if user_input.lower() in ["exit", "quit", "q"]:
              break

          messages_history.append({"role": "user", "content": user_input})

          response = client.chat.completions.create(
              model="Qwen/Qwen2.5-7B-Instruct-Turbo",
              messages=messages_history,
              tools=tools,
          )

          tool_calls = response.choices[0].message.tool_calls
          if tool_calls:
              for tool_call in tool_calls:
                  function_name = tool_call.function.name
                  function_args = json.loads(tool_call.function.arguments)

                  if function_name == "read_file":
                      print(f"Tool call: read_file")
                      function_response = read_file(
                          path=function_args.get("path")
                      )
                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )
                  elif function_name == "list_files":
                      print(f"Tool call: list_files")
                      function_response = list_files(
                          path=function_args.get("path", ".")
                      )

                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )
                  elif function_name == "edit_file":
                      print(f"Tool call: edit_file")
                      function_response = edit_file(
                          path=function_args.get("path"),
                          old_str=function_args.get("old_str"),
                          new_str=function_args.get("new_str"),
                      )
                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )

                  function_enriched_response = client.chat.completions.create(
                      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
                      messages=messages_history,
                  )

                  messages_history.append(
                      {
                          "role": "assistant",
                          "content": function_enriched_response.choices[
                              0
                          ].message.content,
                      }
                  )
                  print(
                      f"LLM: {function_enriched_response.choices[0].message.content}"
                  )
          else:
              messages_history.append(
                  {
                      "role": "assistant",
                      "content": response.choices[0].message.content,
                  }
              )
              print(f"LLM: {response.choices[0].message.content}")


  # start the chat
  chat()
  ```
</CodeGroup>

Output:

````
You: Create a congrats.py script that rot13-decodes the following string ‘Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!’ and prints it.

Tool call: edit_file

LLM: Sure, I'll create a `congrats.py` script that rot13-decodes the given string and prints it. Here's the script:

```python
def rot13_decode(s):
    result = ""
    for char in s:
        if "a" <= char <= "z":
            start = ord("a")
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        elif "A" <= char <= "Z":
            start = ord("A")
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        else:
            result += char
    return result


# The encoded string
encoded_string = "Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!"

# Decoding the string
decoded_string = rot13_decode(encoded_string)

# Printing the decoded string
print(decoded_string)
```
You can save this code in a file named `congrats.py` and run it to see the decoded message.
````

This code will give you a new python script: `congrats.py` which you can run!

<CodeGroup>
  ```shell Shell theme={null}
  python congrats.py
  ```
</CodeGroup>

Output:

```
Congratulations on building a code-editing agent!
```
