---
title: "Developer quickstart"
source: https://developers.notion.com/guides/get-started/quick-start
path: guides/get-started/quick-start
---

Build your first Notion connection with a hands-on tutorial.

## Why start with an internal connection?

We recommend starting with an [internal connection](/guides/get-started/internal-connections). Internal connections let you focus on building with the API right away — you just need an API token to get started. There's no OAuth flow to implement and no listing process to worry about. Everything stays within your workspace.

If you later need your connection to work across multiple workspaces, you can always create a [public connection](/guides/get-started/public-connections) and re-wire your code to use OAuth.

If you only need a token for a user-owned script or CLI workflow, a [personal access token](/guides/get-started/personal-access-tokens) may be faster. This quickstart uses an internal connection because it demonstrates a team-owned automation with explicit page sharing.

In this guide, we're going to build an internal Notion connection that creates a new database in your workspace via a web form.

<Frame>
  <img />
</Frame>

## What to know before you start

Before diving in, here are a few essential things to keep in mind when working with the Notion API:

* **Versioning:** Every request must include a `Notion-Version` header. See [Versioning](/reference/versioning) for the latest version.
* **Rate limits:** The API allows an average of 3 requests per second. If you exceed a rate limit, you'll receive a `429` or `529` response with a `Retry-After` header. See [Request limits](/reference/request-limits).
* **Error handling:** API errors return structured JSON with a `code` and `message`. See [Status codes](/reference/status-codes) for the full list.
* **Pagination:** List endpoints return paginated results. Use `start_cursor` and `has_more` to iterate through pages. See the [API introduction](/reference/intro) for details.
* **Token security:** Never store your API secret in source code or version control. Use environment variables or a secret manager. See [Best practices for handling API keys](/guides/get-started/handling-api-keys).

## What you will build

This guide will demonstrate how to build an HTML form that will [create a new Notion database](/reference/create-a-database) when submitted.

By the end of this guide, we'll have a functional app that looks like this:

<Frame>
  <img />
</Frame>

The completed [sample code](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/web-form-with-express) includes additional examples beyond what's covered in this guide, including forms to:

* [Add a new page](/reference/post-page) to the database
* [Add content](/reference/patch-block-children) to the new page
* [Add a comment](/reference/create-a-comment) to the page content

### Requirements

To follow along with this guide, you will need:

* A [Notion account](https://www.notion.so/signup).
* To be a [Workspace Owner](https://www.notion.so/help/add-members-admins-guests-and-groups) in the workspace you're using. You can create a new workspace for testing purposes otherwise.
* Knowledge of HTML and JavaScript. We'll use [Express.js](https://expressjs.com/) for a server, as well.
* [npm and Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed locally to use the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) and [Express.js](https://expressjs.com/)

<Note>
  **SDK usage is recommended, but not required**

  The [sample code](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/web-form-with-express) shown below uses the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) to make public API requests.

  Using the Notion SDK for JavaScript is not required to build a Notion connection, but many JavaScript developers prefer it due to its ease of use.
</Note>

## Create your connection in Notion

The first step is to create a new internal connection in Notion's <a href={developerConnectionsUrl}>Developer portal</a>.

<Steps>
  <Step>
    In the **Build** section of the sidebar, select **Internal connections**, then click **Create a new connection**.
  </Step>

  <Step>
    Enter the connection name and select the workspace where the connection can be installed.
  </Step>
</Steps>

### Get your access token

API requests require an installation access token to be successfully authenticated. Visit the `Configuration` tab to get your connection's installation access token.

<Frame>
  <img alt="" />
</Frame>

<Info>
  **Never share your installation access token!**

  Any value used to authenticate API requests should always be kept private. Use environment variables and avoid committing sensitive data to your version control history.

  If you do accidentally expose it, remember to refresh your installation access token.

  [Learn more: Best practices for handling API keys](/guides/get-started/handling-api-keys)
</Info>

### Give your connection page permissions

The database that we're about to create will be added to a parent Notion page in your workspace. For your connection to interact with the page, it needs explicit permission to read/write to that specific Notion page.

To give the connection permission, you will need to:

<Steps>
  <Step>
    Pick (or create) a Notion page.
  </Step>

  <Step>
    Click on the `...` More menu in the top-right corner of the page.
  </Step>

  <Step>
    Scroll down to `+ Add Connections`.
  </Step>

  <Step>
    Search for your connection and select it.
  </Step>

  <Step>
    Confirm the connection can access the page and all of its child pages.

    <Frame>
      <img />
    </Frame>
  </Step>
</Steps>

Your connection can now make API requests related to this Notion page and any of its children.

To learn more about how internal connection permissions work — including the bot identity model — see the [Internal connections](/guides/get-started/internal-connections) guide.

<Warning>
  **Double-check your page access**

  If your API requests are failing, confirm you have given the connection permission to the page you are trying to update. This is a common cause of API request errors.
</Warning>

## Setting up the demo locally

In this example, we'll have three key files:

* `index.html`, which will contain our client-side HTML.
* `client.js`, which will contain our client-side JavaScript code.
* `server.js`, which will contain our server-side JavaScript code. This file contains all the endpoints to make requests to Notion's public API, as well as to serve the `index.html` file. ([More on that below.](#step-3-importing-the-notion-sdk-serverjs))

All of the sample code is available in [GitHub](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/web-form-with-express).

<Note>
  **Various examples are available**

  This connection includes frontend code, but connections can be server-side only, as well. See more examples of different connection use cases in [GitHub](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript).
</Note>

### Clone demo repo

To run this project locally, clone the repo and install its dependencies ([Express.js](https://expressjs.com/en/starter/installing.html), [dotenv](https://www.npmjs.com/package/dotenv), and [Notion's SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)):

```bash Shell theme={null}
# Clone this repository locally
git clone https://github.com/makenotion/notion-cookbook.git

# Switch into this project
cd notion-cookbook/examples/javascript/web-form-with-express/

# Install the dependencies
npm install
```

### Environment variables

In your `.env` file, add the following variables:

```bash .env theme={null}
NOTION_KEY=<your-notion-api-key>
NOTION_PAGE_ID=<parent-page-id>
```

Add the access token you retrieved in the [Get your access token](#get-your-access-token) step to `NOTION_KEY`, as well as a page ID (`NOTION_PAGE_ID`) for the page that you gave the connection permission to update.

<Check>
  **How database IDs work**

  When using the API to [create a database](/reference/create-a-database), the parent of a database must be a Notion page or a [wiki](https://www.notion.so/help/wikis-and-verified-pages) database. To get the ID of the page, locate the 32-character string at the end of the page's URL.

  <Frame>
    <img alt="The page ID is highlighted." />
  </Frame>
</Check>

As a best practice, add `.env` to your `.gitignore` file to ensure you don't accidentally share these values.

### Running the project locally

To run this project locally, you will need to enter the following command in your terminal:

<CodeGroup>
  ```bash Shell theme={null}
  npm start
  ```
</CodeGroup>

Once the server is running, open [http://localhost:8000](http://localhost:8000) in your browser. Next, let's look at how our database form works.

## Creating a new database

### Step 1 - Build the form

In our `index.html` file, we need a form for the user to create a new database and an area for the API response to be displayed. This is how the user will initiate a Notion API request.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

The corresponding [HTML elements](https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/web-form-with-express/views/index.html#L40) related to creating a database are shown below:

<CodeGroup>
  ```html HTML expandable theme={null}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      ...
  <!-- Import the webpage's stylesheet -->
      <link rel="stylesheet" href="/style.css" />

  <!-- Import the webpage's client-side javascript file -->
      <script src="/client.js" defer></script>
    </head>
    <body>
      ...
        <table>
          ...
          <tr>
            <td>
              <h3>1. Create a new database</h3>
  <!-- Form to create a database -->
              <form id="databaseForm">
                <label for="dbName">Database name</label>
                <input type="text" id="dbName" />
                <input type="submit" />
              </form>
            </td>
  <!-- Empty table cell to append the API response to -->
            <td id="dbResponse"></td>
          </tr>
          ...
        </table>
      </main>
      ...
    </body>
  </html>
  ```
</CodeGroup>

In terms of what's rendered in the `<body>`, notice the `<form>` element and an empty table cell with the ID `dbResponse`. The latter is where we'll append the Notion API response information.

The database form includes two inputs:

* A text input for the database name
* A submit input to submit the form

Also of note: the `client.js` file is included in the document's `<head>` tag, which allows us to apply client-side JavaScript to interact with these HTML elements.

### Step 2 - Handle the submission

In `client.js`, we can write a function to describe what should happen when the database form is submitted. In short, we want to make a request to `server.js` to then make an API request to Notion. The actual Notion API request will happen server-side to avoid exposing our API secret in the client. (In other words, it's more secure!)

<CodeGroup>
  ```jsx JSX expandable theme={null}
  // Assign the database form to a variable for later use
  const dbForm = document.getElementById("databaseForm");
  // Assign the empty table cell to a variable for later use
  const dbResponseEl = document.getElementById("dbResponse");

  // Add a submit handler to the form
  dbForm.onsubmit = async function (event) {
    event.preventDefault()

  // Get the database name from the form
    const dbName = event.target.dbName.value
    const body = JSON.stringify({ dbName })

  // Make a request to /databases endpoint in server.js
    const newDBResponse = await fetch("/databases", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body,
    })
    const newDBData = await newDBResponse.json()

  // Pass the new database info and the empty table cell
  // to a function that will append it.
    appendApiResponse(newDBData, dbResponseEl)
  }
  ```
</CodeGroup>

In this code block, we select the form element using its ID attribute with `getElementbyId()`.

Next, we attach an async function to the `onsubmit` event that will make a request to our local server's `/databases` endpoint. (This endpoint will be described below in our `server.js` code.) The function is asynchronous because we need to wait for a response from our server before proceeding.

The response is then appended to our `index.html` document. ([More on this below.](#step-5-displaying-the-response-indexhtml))

### Step 3 - Set up the Notion SDK

Let's start by looking at our `server.js` file without the Notion-related endpoints:

<CodeGroup>
  ```javascript JavaScript expandable theme={null}
  require("dotenv").config();
  const express = require("express");
  const app = express();

  // Notion SDK for JavaScript
  const { Client } = require("@notionhq/client");
  const notion = new Client({ auth: process.env.NOTION_KEY });

  // <http://expressjs.com/en/starter/static-files.html>
  app.use(express.static("public"));

  // <http://expressjs.com/en/starter/basic-routing.html>
  app.get("/", function(request, response) {
    response.sendFile(__dirname + "/views/index.html");
  });

  // listen for requests
  const listener = app.listen(process.env.PORT, function() {
    console.log("Your app is listening on port " + listener.address().port);
  });
  ```
</CodeGroup>

This Express.js code will listen for requests to `/` (e.g., `localhost:<port>/`) and respond with the `index.html` file. That's how the app knows to render our `index.html` code when the server is started.

To use the SDK, we import it at the top of `server.js`. We also initialize a new Notion Client instance and set the `auth` option to the Notion API secret already set in the environment variables:

<CodeGroup>
  ```jsx JSX theme={null}
  const { Client } = require("@notionhq/client");
  const notion = new Client({ auth: process.env.NOTION_KEY });
  ```
</CodeGroup>

We can now make requests to Notion's API in this file without having to worry about authentication again.

<Note>
  The SDK automatically sets the `Notion-Version` header on every request, so you don't need to include it manually. If you're making requests without the SDK, you'll need to set this header yourself. See [Versioning](/reference/versioning) for details.
</Note>

### Step 4 - Send the API request

Staying in `server.js`, we can add the following code that will be invoked when the database form makes a POST request to `/databases`:

<CodeGroup>
  ```jsx TypeScript expandable theme={null}
  app.post("/databases", async function (request, response) {
    const pageId = process.env.NOTION_PAGE_ID;
    const title = request.body.dbName;

    try {
  // Notion API request!
      const newDb = await notion.databases.create({
        parent: {
          type: "page_id",
          page_id: pageId,
        },
        title: [
          {
            type: "text",
            text: {
              content: title,
            },
          },
        ],
        properties: {
          Name: {
            title: {},
          },
        },
      });
      response.json({ message: "success!", data: newDb });
    } catch (error) {
      response.json({ message: "error", error });
    }
  });
  ```
</CodeGroup>

`app.post()` indicates this endpoint is for POST requests, and the first argument (`"/databases"`) indicates this function corresponds to requests made to the `/databases` path, as we did in our client-side code above.

Next, we can actually interact with the Notion API.

To create a new database, we'll use the [Create a database](/reference/create-a-database) endpoint:

<CodeGroup>
  ```jsx TypeScript theme={null}
  await notion.databases.create({...options})
  ```
</CodeGroup>

To use this endpoint, we need to pass the parent page ID in the body parameters. This page ID is the one already set in the environment variables. The page ID **must** be included in this request.

<CodeGroup>
  ```jsx TypeScript theme={null}
  const pageId = process.env.NOTION_PAGE_ID;
  ...
  try {
    const newDb = await notion.databases.create({
      parent: {
        type: "page_id",
        page_id: pageId,
      },
      ...
  ```
</CodeGroup>

(Note: Environment variables can only be accessed in `server.js` , not `client.js`.)

In this example, the title of the database should also be set. The title was provided in the form the user submitted, which we can access from the request's body (`request.body.dbName`).

<CodeGroup>
  ```jsx TypeScript theme={null}
  const pageId = process.env.NOTION_PAGE_ID;
  const title = request.body.dbName; // Get the user's title

  try {
    const newDb = await notion.databases.create({
      parent: {...},
      title: [
        {
          type: "text",
          text: {
            content: title, // Include the user's title in the request
          },
        },
      ],
      // ...
  ```
</CodeGroup>

Finally, we need to describe the [database's properties](/reference/property-object). The properties represent the columns in a database (or the "schema", depending on which terminology you prefer.)

In this case, our database will have just one column called "Name", which will represent the page names of its child pages:

<CodeGroup>
  ```jsx TypeScript theme={null}
  try {
      const newDb = await notion.databases.create({
        parent: {...},
        title: [...],
        properties: {
          Name: {
            title: {},
          },
        },
      })
  ...
  ```
</CodeGroup>

Finally, assuming the request works, we can return the response from Notion's API back to our original fetch request in `client.js`:

<CodeGroup>
  ```jsx JavaScript theme={null}
  ...
  response.json({ message: "success!", data: newDb });
  ```
</CodeGroup>

If it doesn't work, we'll return whatever error message we get from Notion's API:

<CodeGroup>
  ```jsx JavaScript theme={null}
  try {
  ...
  } catch (error) {
    response.json({ message: "error", error });
  }
  ```
</CodeGroup>

Now that we have our new database, the response can be added to the HTML document via the client-side JavaScript (`client.js`).

### Step 5 - Display the response

Let's first look at an example of the object the `/databases` endpoint responds with, which includes the database object that gets returned from the Notion API when we create a new database:

<CodeGroup>
  ```json Response expandable theme={null}
  {
    message: "success!",
    data: { // from Notion
      object: "database",
      id: "e604f78c-4145-4444-b7d5-1adea4fa5d08",
      cover: null,
      icon: null,
      created_time: "2023-07-18T20:56:00.000Z",
      created_by: { object: "user", id: "44b170f0-16ac-47cf-aaaa-8f2eab66hhhh" },
      last_edited_by: {
        object: "user",
        id: "44b170f0-16ac-47cf-gggg-8f2eab6rrrra",
      },
      last_edited_time: "2023-07-18T20:56:00.000Z",
      title: [
        {
          type: "text",
          text: [Object],
          annotations: [Object],
          plain_text: "test db",
          href: null,
        },
      ],
      description: [],
      is_inline: false,
      properties: {
        Name: { id: "title", name: "Name", type: "title", title: {} },
      },
      parent: {
        type: "page_id",
        page_id: "e7261079-9d30-4313-9999-14b29880gggg",
      },
      url: "<https://www.notion.so/e604f78c414548c6b7d51adea4fadddd>",
      public_url: null,
      archived: false,
      in_trash: false
    },
  }
  ```
</CodeGroup>

The most important information here (for our purposes) is the database ID (`data.id`). The ID will be required to make API requests to the [Create a page](/reference/post-page) endpoint, which is the next form in our completed demo's UI.

Knowing this JSON structure, let's now look at how `appendApiResponse()` works:

<CodeGroup>
  ```jsx JSX expandable theme={null}
  const dbForm = document.getElementById("databaseForm");
  // Empty table cell where we'll display the API response
  const dbResponse = document.getElementById("dbResponse");
  ...

  // Appends the API response to the UI
  const appendApiResponse = function (apiResponse, el) {
    // Add success message to UI
    const newParagraphSuccessMsg = document.createElement("p")
    newParagraphSuccessMsg.innerHTML = "Result: " + apiResponse.message
    el.appendChild(newParagraphSuccessMsg)

    // See browser console for more information if there's an error
    if (apiResponse.message === "error") return

    // Add ID of Notion item (db, page, comment) to UI
    const newParagraphId = document.createElement("p")
    newParagraphId.innerHTML = "ID: " + apiResponse.data.id
    el.appendChild(newParagraphId)

    // Add URL of Notion item (db, page) to UI
    if (apiResponse.data.url) {
      const newAnchorTag = document.createElement("a")
      newAnchorTag.setAttribute("href", apiResponse.data.url)
      newAnchorTag.innerText = apiResponse.data.url
      el.appendChild(newAnchorTag)
    }
  }
  ```
</CodeGroup>

`appendApiResponse(res, form)` accepts two parameters: the response (shown above) and the HTML element where we will append the response — in this case, an empty table cell next to the database form.

In this function, we first add a paragraph element to show the response message (i.e., whether it was a success or the error).

<CodeGroup>
  ```jsx JSX theme={null}
  const newParagraphSuccessMsg = document.createElement("p")
  newParagraphSuccessMsg.innerHTML = "Result: " + apiResponse.message
  el.appendChild(newParagraphSuccessMsg)
  ```
</CodeGroup>

Then, we do the same with the database ID after confirming the response was not an error:

<CodeGroup>
  ```jsx JSX theme={null}
  if (apiResponse.message === "error") return

  // Add ID of database and data source to UI
  const newParagraphId = document.createElement("p")
  newParagraphId.innerHTML = "Database ID: " + \
    apiResponse.data.id + "; Data Source ID" + apiResponse.data.data_sources[0].id
  el.appendChild(newParagraphId)
  ```
</CodeGroup>

Finally, if the response has a URL, we display that too with an anchor (`<a>`) tag. This allows the user to visit the database directly in Notion.

<CodeGroup>
  ```jsx JSX theme={null}
  if (apiResponse.data.url) {
    const newAnchorTag = document.createElement("a")
    newAnchorTag.setAttribute("href", apiResponse.data.url)
    newAnchorTag.innerText = apiResponse.data.url
    el.appendChild(newAnchorTag)
  }
  ```
</CodeGroup>

(Note: This function will be reused by other forms. Not all responses have a `url` property, which is why we check for it.)

Once this is done, our HTML document is updated and the form submission is officially complete.

## Testing the feature

Let's see the final results of testing this new feature:

<Frame>
  <img />
</Frame>

The database form is submitted and the response from Notion's API is appended to our UI. We can click the link to visit the new database in Notion and confirm it worked as expected.

As a next step, the new database ID can be copy and pasted into the page form below it to create a new page in the database. We can also use the page ID that the page form returns to add content to the page or comment on it using the block and comment forms.

We won't cover the code for page, blocks, or comment forms here, but the code is all included in the [source code](https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/web-form-with-express/views/index.html) for reference. It works the same as the database example.

As a next step, you could also try adding a feature to [retrieve all existing pages](/reference/query-a-data-source) in the database, or [retrieve block children](/reference/get-block-children) (i.e., page content) for an existing page.

## Wrapping up

This guide demonstrated how to use Notion's public API (via the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)) to build an internal connection. With this demo app, users can programmatically create a new database in their Notion workspace by filling out a form in the app UI and making a request to Notion's public API — the [Create a database](/reference/create-a-database) endpoint.

As a reminder, this example includes client-side code to allow for user interactions via a GUI (graphical user interface). Notion connections do not require a UI, however. What you build is completely up to you!

To see examples of server-side-only connections, test out the sample apps in the SDK's [GitHub repo](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript).

## Next steps

<CardGroup>
  <Card title="Internal connections" icon="lock" href="/guides/get-started/internal-connections">
    Learn how internal connection permissions and authentication work.
  </Card>

  <Card title="Public connections" icon="globe" href="/guides/get-started/public-connections">
    Expand to multiple workspaces with OAuth 2.0.
  </Card>

  <Card title="Authorization" icon="key" href="/guides/get-started/authorization">
    Implement the full OAuth flow for public connections.
  </Card>

  <Card title="API reference" icon="https://mintcdn.com/notion-demo/7WdlNb9IZkRhGCcR/icons/nds/curlyBraces.svg?fit=max&auto=format&n=7WdlNb9IZkRhGCcR&q=85&s=46f7a8b4a34544f9b03002e4ecc35ad5" href="/reference/intro" />

  <Card title="JavaScript client" icon="js" href="https://github.com/makenotion/notion-sdk-js" />

  <Card title="Postman collection" icon="box" href="https://www.postman.com/notionhq/notion-s-api-workspace/collection/52041987-03f70d8f-b6e5-4306-805c-f95f7cdf05b9" />

  <Card title="TypeScript starter template" icon="code" href="https://github.com/makenotion/notion-sdk-typescript-starter" />

  <Card title="Slack developer community" icon="slack" href="https://join.slack.com/t/notiondevs/shared_invite/zt-3u9oid9q8-HLUBmMVWYK~g9HFo4U4raA" />
</CardGroup>
