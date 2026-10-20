---
title: "Connect your users to Pinecone"
source: https://docs.pinecone.io/integrations/build-integration/connect-your-users-to-pinecone
path: integrations/build-integration/connect-your-users-to-pinecone
---

Embed a Connect to Pinecone flow in your app or notebook so users can sign in, choose a project, and receive an API key without leaving your integration.

Add a **Connect to Pinecone** flow to your app, website, or [Colab](https://colab.google/) notebook so your users can get a Pinecone API key without leaving your integration. In the flow, users sign up for or log in to Pinecone, select or create an organization and project, and generate an API key. The API key is then shown to the user to copy, or sent directly to your page, app, or notebook.

You can add the flow in two ways:

* [Add a Connect popup](#add-a-connect-popup) that opens from your own button or link.
* [Embed the Connect widget](#embed-the-connect-widget), a drop-in component with the same functionality.

Both require an integration ID, so start by [creating one](#create-an-integration-id).

> [!NOTE]
>
> Only [organization owners](/admin/organizations/manage-organization-members) can add or manage integrations.

## Create an integration ID

Create a unique `integrationId` to use with the **Connect to Pinecone** popup and widget:

**1. Open the Integrations tab**

On the [**Integrations**](https://app.pinecone.io/organizations/-/settings/integrations) tab in the Pinecone console, click **Create Integration**.

> [!NOTE]
>
> The **Integrations** tab doesn't appear until your organization has an integration. To create your first one, go to the [**Create integration**](https://app.pinecone.io/organizations/-/settings/integrations?create=true) form directly.

**2. Fill out the form**

In the **Create integration** form, fill out these fields:

* **Integration name**: A name for your integration.
* **URL Slug**: Your `integrationId`. Enter a human-readable string that uniquely identifies your integration and that may appear in URLs. The URL slug is public and can't be changed.
* **Logo**: A logo for your integration.
* **Return mechanism**: How the generated API key is returned:
  * **Web Message**: Your application receives the API key through a web message, and only the allowed origins you list below receive it. Select this option if you use the [`@pinecone-database/connect` library](#javascript).
  * **Copy/Paste**: The API key appears in the success message, and users copy and paste it into your application.
* **Allowed origin**: If you selected **Web Message**, list the URL origins where your integration is hosted. An [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) is the part of a URL that specifies the protocol, hostname, and port.

**3. Create the integration**

Click **Create**.

After you create your integration, [attribute usage to your integration](/integrations/build-integration/attribute-usage-to-your-integration).

> [!NOTE]
>
> Anyone can create an integration. To apply to become an official Pinecone partner, see [Integration ecosystem](/integrations/build-integration/integration-ecosystem).

## Add a Connect popup

After you [create your `integrationId`](#create-an-integration-id), you can open the **Connect to Pinecone** popup from your own button or link. You can use the JavaScript library or the script. The library is the most common method. Use the script when you can't build with a custom library, such as in a content management system (CMS).

**1. Load the library or script**

Install the [`@pinecone-database/connect` library](https://www.npmjs.com/package/@pinecone-database/connect), or load the script in your page's `<head>`:

```shell JavaScript library theme={null}
npm i -S @pinecone-database/connect
```

```html JavaScript script theme={null}
<script src="https://connect.pinecone.io/embed.js"></script>
```

**2. Create the popup**

Call the `ConnectPopup` function. It takes one required configuration option:

* `integrationId`: The URL slug of your integration. If you don't pass `integrationId`, the popup doesn't render.

When the user completes the flow, the `onConnect` callback receives the API key. The function returns an object with an `open` function that opens the popup.

```javascript JavaScript library theme={null}
import { ConnectPopup } from '@pinecone-database/connect'

const popup = ConnectPopup({
  onConnect: (key) => console.log("API Key:", key),
  integrationId: 'myApp'
});
```

```html JavaScript script theme={null}
<script>
  const pineconePopup = ConnectPopup({
    onConnect: (key) => console.log(key),
    onCancel: () => console.log("Cancelled"),
    integrationId: 'myApp'
  });
</script>
```

**3. Open the popup from your button or link**

Call `open` when the user clicks your button or link:

```javascript JavaScript library theme={null}
document.getElementById('connectButton').addEventListener('click', () => {
  popup.open();
});
```

```html JavaScript script theme={null}
<button onclick="pineconePopup.open()">Connect to Pinecone</button>
```

## Embed the Connect widget

The **Connect** widget is a drop-in component with the same functionality as the popup. After you [create your `integrationId`](#create-an-integration-id), you can embed it in two ways:

* Use the [JavaScript](#javascript) library (`@pinecone-database/connect`) or script to render the widget in apps and websites.
* Use the [Colab](#colab) library (`pinecone-notebooks`) to render the widget in Colab notebooks with Python.

### JavaScript

To embed the widget in your app or website, use the [`@pinecone-database/connect` library](https://www.npmjs.com/package/@pinecone-database/connect) or, if you can't use the library, the script.

**1. Load the library or script**

Install the library, or load the script in your page's `<head>`:

```shell JavaScript library theme={null}
npm i -S @pinecone-database/connect
```

```html JavaScript script theme={null}
<script src="https://connect.pinecone.io/embed.js"></script>
```

**2. Add a container for the widget**

Add the HTML element where the widget renders:

```html HTML theme={null}
<div id="connect-widget"></div>
```

**3. Render the widget**

Call the `connectToPinecone` function. It takes two required configuration options:

* `integrationId`: The URL slug of your integration. If you don't pass `integrationId`, the widget doesn't render.
* `container`: The HTML element where the widget renders.

When the user completes the flow, the function calls your callback with the Pinecone API key. If you use the script, place the inline `<script>` in the page body after the container element, so the container exists when `connectToPinecone` runs.

```javascript JavaScript library theme={null}
import { connectToPinecone } from '@pinecone-database/connect'

const setupPinecone = (apiKey) => { /* Set up a Pinecone client using the API key */ }

connectToPinecone(
  setupPinecone,
  {
    integrationId: 'myApp',
    container: document.getElementById('connect-widget')
  }
)
```

```html JavaScript script theme={null}
<script>
  connectToPinecone(
    (apiKey) => { /* Set up a Pinecone client using the API key */ },
    {
      integrationId: 'myApp',
      container: document.getElementById('connect-widget'),
    }
  );
</script>
```

### Colab

To embed the widget in a Colab notebook, use the [`pinecone-notebooks` Python library](https://pypi.org/project/pinecone-notebooks/#description).

**1. Install the libraries**

```shell theme={null}
pip install -qU pinecone-notebooks pinecone
```

**2. Render the widget**

Call `Authenticate` to render the widget, so the user can log in and generate an API key:

```python theme={null}
from pinecone_notebooks.colab import Authenticate

Authenticate()
```

**3. Use the API key**

After the user completes the flow, the API key is available in the `PINECONE_API_KEY` environment variable. Use it to initialize the Pinecone client:

```python theme={null}
import os
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
```

> [!TIP]
>
> To see this flow in practice, open the [example notebook](https://colab.research.google.com/drive/1VZ-REFRbleJG4tfJ3waFIrSveqrYQnNx?usp=sharing).

## Manage generated API keys

Your users can [manage the API keys](/admin/projects/manage-api-keys) generated by your integration in the Pinecone console.
