---
title: "Set up and deploy a webhook"
source: https://docs.stripe.com/webhooks/quickstart.md
path: webhooks/quickstart
---

# Set up and deploy a webhook

Learn how to set up and deploy a webhook to listen to events from Stripe.

# Interactive webhook endpoint builder 

Learn how to set up and deploy a webhook endpoint to listen to events from Stripe. Use a webhook endpoint for post-payment commerce events such as sending custom email receipts, fulfilling orders, or updating your database. Your webhook endpoint is the app you build and host. Stripe notifies it with a [thin event](https://docs.stripe.com/events/how-events-work.md#thin-events) when something happens, and if you need more information, you fetch the full event or the associated object.

Test these steps in a sandbox before implementing them in live mode.

1. Build the server

~~~
npm install
~~~

2. Run the server

~~~
npm start
~~~
1. Run the server

~~~
go run server.go
~~~
1. Build the server

~~~
pip3 install -r requirements.txt
~~~

2. Run the server

~~~
export FLASK_APP=server.py
python3 -m flask run --port=4242
~~~

1. Build the server

~~~
bundle install
~~~

2. Run the server

~~~
ruby server.rb -o 0.0.0.0
~~~

1. Build the server

~~~
composer install
~~~

2. Run the server

~~~
php -S 127.0.0.1:4242
~~~
1. Build the server

~~~
dotnet restore
~~~

2. Run the server

~~~
dotnet run
~~~
1. Build the server

~~~
mvn package
~~~

2. Run the server

~~~
java -cp target/sample-jar-with-dependencies.jar com.stripe.sample.Server
~~~

~~~
stripe listen --forward-thin-to localhost:4242/public/webhook.php --thin-events "*"
~~~

~~~
stripe listen --forward-thin-to localhost:4242/webhook --thin-events "*"
~~~
### Install the Stripe Node library

Install the package and import it in your code. Alternatively, if you’re starting from scratch and need a package.json file, download the project files using the Download link in the code editor.

#### npm

Install the library:

```bash
npm install --save stripe
```

#### GitHub

Or download the stripe-node library source code directly [from GitHub](https://github.com/stripe/stripe-node).

### Install the Stripe Ruby library

Install the Stripe ruby gem and require it in your code. Alternatively, if you’re starting from scratch and need a Gemfile, download the project files using the link in the code editor.

#### Terminal

Install the gem:

```bash
gem install stripe
```

#### Bundler

Add this line to your Gemfile:

```bash
gem 'stripe'
```

#### GitHub

Or download the stripe-ruby gem source code directly [from GitHub](https://github.com/stripe/stripe-ruby).

### Install the Stripe Java library

Add the dependency to your build and import the library. Alternatively, if you’re starting from scratch and need a sample pom.xml file (for Maven), download the project files using the link in the code editor.

#### Maven

Add the following dependency to your POM and replace {VERSION} with the version number you want to use.

```bash
<dependency>\n<groupId>com.stripe</groupId>\n<artifactId>stripe-java</artifactId>\n<version>{VERSION}</version>\n</dependency>
```

#### Gradle

Add the dependency to your build.gradle file and replace {VERSION} with the version number you want to use.

```bash
implementation "com.stripe:stripe-java:{VERSION}"
```

#### GitHub

Download the JAR directly [from GitHub](https://github.com/stripe/stripe-java/releases/latest).

### Install the Stripe Python package

Install the Stripe package and import it in your code. Alternatively, if you’re starting from scratch and need a requirements.txt file, download the project files using the link in the code editor.

#### pip

Install the package through pip:

```bash
pip3 install stripe
```

#### GitHub

Download the stripe-python library source code directly [from GitHub](https://github.com/stripe/stripe-python).

### Install the Stripe PHP library

Install the library with composer and initialize with your secret API key. Alternatively, if you’re starting from scratch and need a composer.json file, download the files using the link in the code editor.

#### Composer

Install the library:

```bash
composer require stripe/stripe-php
```

#### GitHub

Or download the stripe-php library source code directly [from GitHub](https://github.com/stripe/stripe-php).

### Set up your server

Add the dependency to your build and import the library. Alternatively, if you’re starting from scratch and need a go.mod file, download the project files using the link in the code editor.

#### Go

Make sure to initialize with Go Modules:

```bash
go get -u github.com/stripe/stripe-go/v87
```

#### GitHub

Or download the stripe-go module source code directly [from GitHub](https://github.com/stripe/stripe-go).

### Install the Stripe.net library

Install the package with .NET or NuGet. Alternatively, if you’re starting from scratch, download the files which contains a configured .csproj file.

#### dotnet

Install the library:

```bash
dotnet add package Stripe.net
```

#### NuGet

Install the library:

```bash
Install-Package Stripe.net
```

#### GitHub

Or download the Stripe.net library source code directly [from GitHub](https://github.com/stripe/stripe-dotnet).

### Install the Stripe libraries

Install the packages and import them in your code. Alternatively, if you’re starting from scratch and need a `package.json` file, download the project files using the link in the code editor.

Install the libraries:

```bash
npm install --save stripe @stripe/stripe-js next
```

### Create a webhook endpoint to receive event notifications

[Event destinations](https://docs.stripe.com/event-destinations/overview.md) are Stripe objects that send events to your webhook endpoint. Add a route to your app that accepts unauthenticated POST requests. Make sure your app’s publicly accessible, then register it with Stripe. Event types for API v1 resources start with `v1.`, such as `v1.payment_intent.succeeded` and `v1.payment_method.attached`. To receive  [API v2](https://docs.stripe.com/api-v2-overview.md) notifications, set `event_payload` to `thin` when you [create an event destination](https://docs.stripe.com/api/v2/core/event-destinations.md).

### Read the event notification

Stripe sends an [event notification](https://docs.stripe.com/events/how-events-work.md#thin-events) in the request body. Thin event notifications contain references to the resource that changed (such as `id`, `type`, and `related_object`), not the resource itself. This means that thin event payloads stay the same size and shape no matter which API version you use. Use a [Stripe SDK](https://docs.stripe.com/sdks.md) to parse the request body and verify the request signature.

### Handle the event

Check the [event_type](https://docs.stripe.com/api/v2/core/events/event-types.md) to understand what happened. Set up event destinations to handle logically related groups of events single events if some actions require special handling.

### Fetch the related object

A notification tells you which object changed, not what it contains. Call `fetchRelatedObject` to retrieve the current version of the object from the Stripe API using the API version configured for your client, which defaults to the version pinned by your SDK. Learn how to [set the API version](https://docs.stripe.com/sdks/set-version.md). You can also retrieve the object yourself with the `related_object.id` value and the API v1 resource method, such as `retrieve` on PaymentIntent. Because you fetch the object after the event happens, you always read its latest state. In both sandbox and live mode, use a [restricted API key](https://docs.stripe.com/keys.md#create-restricted-api-key) with **Payment Intents: Read**, **Payment Methods: Read**, and **Events: Read** permissions.

### Retrieve the full event

This step is optional. You only need to retrieve the full event if you need data that the notification and the related object don’t provide, such as `changes`, which lists the attributes that changed. Set `FETCH_FULL_EVENT=true`, then call `fetchEvent` to retrieve the complete [event](https://docs.stripe.com/api/v2/core/events.md) from the Events v2 API. Each retrieval is an additional API call.

### Return a 200 response

[Send a successful 200 response](https://docs.stripe.com/webhooks.md#handle-events-asynchronously) to Stripe as quickly as possible because Stripe retries the event if a response isn’t sent within a reasonable time. Write any long-running processes as code that can run asynchronously outside the webhook endpoint. Fetching the related object and the full event adds API calls to your handler. If those calls make your handler slow, queue the notification and process it outside the request.

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at `http://localhost:4242/webhook`.

```bash
npm start
```

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at `http://localhost:4242/webhook`.

```bash
ruby server.rb
```

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at `http://localhost:4242/webhook`.

```bash
python3 -m flask --app server run --port=4242
```

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at `http://localhost:4242/public/webhook.php`.

```bash
php -S 127.0.0.1:4242
```

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at `http://localhost:4242/webhook`.

```bash
dotnet run
```

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at `http://localhost:4242/webhook`.

```bash
go run server.go
```

### Run the server

Set the `STRIPE_WEBHOOK_SECRET` environment variable to your event destination’s signing secret. Find this secret in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, or from the CLI output when you run `stripe listen`. Build and run your server to test the endpoint at http://localhost:4242/webhook.

```bash
java -cp target/sample-jar-with-dependencies.jar com.stripe.sample.Server
```

### Download the CLI

Use the Stripe CLI to test your webhook locally. [Download the CLI](https://docs.stripe.com/cli.md) and log in to the same Stripe account as the restricted sandbox API key configured in your server. Alternatively, use a service like ngrok to make your local endpoint publicly accessible.

```bash
stripe login
```

### Forward events to your webhook

Set up [event forwarding](https://docs.stripe.com/webhooks.md#local-listener) with the CLI to send thin events in a sandbox to your local webhook endpoint. Use `--forward-thin-to` for thin events, and `--thin-events` to select which event types to forward.

```bash
stripe listen --forward-thin-to localhost:4242/webhook --thin-events "*"
```

The listener prints a `whsec_` signing secret. In the terminal where you run the server, export that value as `STRIPE_WEBHOOK_SECRET`, then restart the server before triggering an event.

```bash
export STRIPE_WEBHOOK_SECRET=whsec_...
```

### Forward events to your webhook

Set up [event forwarding](https://docs.stripe.com/webhooks.md#local-listener) with the CLI to send thin events in a sandbox to your local webhook endpoint. Use `--forward-thin-to` for thin events, and `--thin-events` to select which event types to forward.

```bash
stripe listen --forward-thin-to localhost:4242/public/webhook.php --thin-events "*"
```

The listener prints a `whsec_` signing secret. In the terminal where you run the server, export that value as `STRIPE_WEBHOOK_SECRET`, then restart the server before triggering an event.

```bash
export STRIPE_WEBHOOK_SECRET=whsec_...
```

### Simulate events

Use the CLI to [simulate specific events](https://docs.stripe.com/cli/trigger) that test your webhook application logic. Trigger the API v1 event, and Stripe delivers the matching `v1.` thin event to your thin event destination.

```bash
stripe trigger payment_intent.succeeded
```

### Secure your webhook

Verify every request to prevent fake payloads from triggering work in your backend, and use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) to configure network access.

### Add the endpoint signing secret

Each event destination has a unique signing secret, which you can find in the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench. If you’re testing locally with the Stripe CLI, you can also get the signing secret from the CLI output using the command `stripe listen`.

### Read the request signature

Each request from Stripe contains a `Stripe-Signature` header. Store a reference to this header value for later use.

### Verify the request

Pass the raw request body, the `Stripe-Signature` header, and the signing secret to the Stripe library to verify the request and parse it into an event notification. Alternatively, you can [manually verify](https://docs.stripe.com/webhooks.md?verify=verify-manually#verify-manually) the signature without using the Stripe library.

### Handle errors

Checking for errors helps catch improperly configured webhooks or malformed requests from non-Stripe services. Common errors include using the signing secret of a different event destination, passing a parsed representation (for example, JSON) of the request body, or reading the wrong request header.

### Test the endpoint

Test your secured endpoint by using the Stripe CLI, which sends the proper signature header in each test event.

// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
// Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
// To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
// your thin event destination's unique secret.
//
// If you are testing with the CLI, find the secret by running 'stripe listen'.
// If you're using a destination defined with the API or Dashboard, look in
// your webhook settings at https://dashboard.stripe.com/webhooks.
//
// Don't include webhook secrets in code.
const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;
const express = require('express');
const app = express();
app.post('/webhook', express.raw({type: 'application/json'}), async (request, response) => {
  let notification;
  // Get the signature sent by Stripe
  const signature = request.headers['stripe-signature'];
  try {
    // Verify the signature and parse the thin event notification
    notification = stripe.parseEventNotification(
      request.body,
      signature,
      endpointSecret
    );
  } catch (err) {
    console.log(`Webhook signature verification failed.`, err.message);
    return response.sendStatus(400);
  }
  try {
    // Handle the event notification by matching its type property.
    // The notification identifies the related object, but doesn't contain it.
    // Matching on type also identifies events that are represented by
    // UnknownEventNotification because this SDK version doesn't include their class.
    switch (notification.type) {
      case 'v1.payment_intent.succeeded': {
        // Fetch the current version of the related object
        const paymentIntent = await notification.fetchRelatedObject();
        console.log(`PaymentIntent for ${paymentIntent.amount} was successful!`);
        // Then define and call a method to handle the successful payment intent.
        // handlePaymentIntentSucceeded(paymentIntent);
        // Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
        // need data that the notification and related object don't provide.
        if (process.env.FETCH_FULL_EVENT === 'true') {
          const event = await notification.fetchEvent();
          console.log(`Retrieved event ${event.id}.`);
        }
        break;
      }
      case 'v1.payment_method.attached': {
        const paymentMethod = await notification.fetchRelatedObject();
        // Then define and call a method to handle the successful attachment of a PaymentMethod.
        // handlePaymentMethodAttached(paymentMethod);
        break;
      }
      default:
        // Unexpected event type
        console.log(`Unhandled event type ${notification.type}.`);
    }
  } catch (err) {
    console.log(`Webhook handler failed.`, err.message);
    return response.sendStatus(500);
  }
  // Return a 200 response to acknowledge receipt of the event
  response.send();
app.listen(4242, () => console.log('Running on port 4242'));
{
  "name": "stripe-sample",
  "version": "1.0.0",
  "description": "A sample Stripe implementation",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "author": "stripe-samples",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1",
    "stripe": "^23.0.0"
  }
}
{
  "name": "stripe-sample",
  "version": "0.1.0",
  "dependencies": {
    "@stripe/react-stripe-js": "^3.7.0",
    "@stripe/stripe-js": "^7.3.0",
    "express": "^4.17.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "^3.4.0",
    "stripe": "23.0.0"
  },
  "devDependencies": {
    "concurrently": "4.1.2"
  },
  "homepage": "http://localhost:3000/checkout",
  "proxy": "http://localhost:4242",
  "scripts": {
    "start-client": "react-scripts start",
    "start-server": "node server.js",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "start": "concurrently \"npm run start-client\" \"npm run start-server\""
  },
  "eslintConfig": {
    "extends": "react-app"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
require 'stripe'
\# This is a public sample test API key.
# Don't submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
\# Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')
\# To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
# your thin event destination's unique secret.
#
# If you are testing with the CLI, find the secret by running 'stripe listen'.
# If you're using a destination defined with the API or Dashboard, look in
# your webhook settings at https://dashboard.stripe.com/webhooks.
#
# Don't include webhook secrets in code.
endpoint_secret = ENV['STRIPE_WEBHOOK_SECRET']
post '/webhook' do
  payload = request.body.read
  notification = nil
  signature = request.env['HTTP_STRIPE_SIGNATURE']
  begin
    \# Verify the signature and parse the thin event notification
    notification = client.parse_event_notification(
      payload, signature, endpoint_secret
    )
  rescue Stripe::SignatureVerificationError => e
    puts "Webhook signature verification failed. #{e.message}"
    status 400
    return
  end
  \# Handle the event notification by matching its type attribute.
  # The notification identifies the related object, but doesn't contain it.
  # Matching on type also identifies events that are represented by
  # UnknownEventNotification because this SDK version has no class for them.
  case notification.type
  when 'v1.payment_intent.succeeded'
    \# Fetch the current version of the related object
    payment_intent = notification.fetch_related_object
    puts "Payment for #{payment_intent.amount} succeeded."
    # Then define and call a method to handle the successful payment intent.
    # handle_payment_intent_succeeded(payment_intent)
    \# Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
    # need data that the notification and related object don't provide.
    if ENV['FETCH_FULL_EVENT'] == 'true'
      event = notification.fetch_event
      puts "Retrieved event #{event.id}."
    end
  when 'v1.payment_method.attached'
    payment_method = notification.fetch_related_object
    \# Then define and call a method to handle the successful attachment of a PaymentMethod.
    # handle_payment_method_attached(payment_method)
  else
    puts "Unhandled event type: #{notification.type}"
  end
  status 200
import stripe
\# This is a public sample test API key.
# Don't submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
\# Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
client = stripe.StripeClient('<<YOUR_SECRET_KEY>>')
\# To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
# your thin event destination's unique secret.
#
# If you are testing with the CLI, find the secret by running 'stripe listen'.
# If you're using a destination defined with the API or Dashboard, look in
# your webhook settings at https://dashboard.stripe.com/webhooks.
#
# Don't include webhook secrets in code.
endpoint_secret = os.environ.get('STRIPE_WEBHOOK_SECRET')
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
    sig_header = request.headers.get('stripe-signature')
    try:
        \# Verify the signature and parse the thin event notification
        notification = client.parse_event_notification(
            payload, sig_header, endpoint_secret
        )
    except stripe.SignatureVerificationError as e:
        print('Webhook signature verification failed.' + str(e))
        return jsonify(success=False), 400
    \# Handle the event notification by matching its type attribute.
    # The notification identifies the related object, but doesn't contain it.
    # Matching on type also identifies events that are represented by
    # UnknownEventNotification because this SDK version has no class for them.
    if notification.type == 'v1.payment_intent.succeeded':
        \# Fetch the current version of the related object
        payment_intent = notification.fetch_related_object()
        print('Payment for {} succeeded'.format(payment_intent.amount))
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
        \# Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
        # need data that the notification and related object don't provide.
        if os.environ.get('FETCH_FULL_EVENT') == 'true':
            event = notification.fetch_event()
            print('Retrieved event {}'.format(event.id))
    elif notification.type == 'v1.payment_method.attached':
        payment_method = notification.fetch_related_object()
        \# Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(notification.type))
    return jsonify(success=True)
certifi==2026.1.4
chardet==5.2.0
click==8.3.1
Flask==3.1.2
idna==3.11
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
requests==2.32.5
stripe==16.0.0
toml==0.10.2
Werkzeug==3.1.5
$stripe = new \Stripe\StripeClient($stripeSecretKey);
// To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
// your thin event destination's unique secret.
//
// If you are testing with the CLI, find the secret by running 'stripe listen'.
// If you're using a destination defined with the API or Dashboard, look in
// your webhook settings at https://dashboard.stripe.com/webhooks.
//
// Don't include webhook secrets in code.
$endpoint_secret = getenv('STRIPE_WEBHOOK_SECRET');
$payload = @file_get_contents('php://input');
$notification = null;
$sig_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];
try {
  // Verify the signature and parse the thin event notification
  $notification = $stripe->parseEventNotification(
    $payload, $sig_header, $endpoint_secret
  );
} catch(\Stripe\Exception\SignatureVerificationException $e) {
  // Invalid signature
  echo 'Webhook error while validating signature.';
  http_response_code(400);
  exit();
}
  // Handle the event notification by matching its type property.
  // The notification identifies the related object, but doesn't contain it.
  // Matching on type also identifies events that are represented by
  // UnknownEventNotification because this SDK version doesn't include their class.
switch ($notification->type) {
  case 'v1.payment_intent.succeeded':
    // Fetch the current version of the related object
    $paymentIntent = $notification->fetchRelatedObject();
    // Then define and call a method to handle the successful payment intent.
    // handlePaymentIntentSucceeded($paymentIntent);
    // Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
    // need data that the notification and related object don't provide.
    if (getenv('FETCH_FULL_EVENT') === 'true') {
      $event = $notification->fetchEvent();
      error_log('Retrieved event ' . $event->id);
    }
    break;
  case 'v1.payment_method.attached':
    $paymentMethod = $notification->fetchRelatedObject();
    // Then define and call a method to handle the successful attachment of a PaymentMethod.
    // handlePaymentMethodAttached($paymentMethod);
    break;
  default:
    // Unexpected event type
    error_log('Received unknown event type ' . $notification->type);
}
http_response_code(200);
// Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
$stripeSecretKey = '<<YOUR_SECRET_KEY>>';
      // This is a public sample test API key.
      // Don't submit any personally identifiable information in requests made with this key.
      // Sign in to see your own test API key embedded in code samples.
      // Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
      // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
      services.AddSingleton(new StripeClient("<<YOUR_SECRET_KEY>>"));
  [Route("webhook")]
  [ApiController]
  public class WebhookController : Controller
        // To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
        // your thin event destination's unique secret.
        //
        // If you are testing with the CLI, find the secret by running 'stripe listen'.
        // If you're using a destination defined with the API or Dashboard, look in
        // your webhook settings at https://dashboard.stripe.com/webhooks.
        //
        // Don't include webhook secrets in code.
        var endpointSecret = Environment.GetEnvironmentVariable("STRIPE_WEBHOOK_SECRET");
            var signatureHeader = Request.Headers["Stripe-Signature"];
            // Verify the signature and parse the thin event notification
            var notification = client.ParseEventNotification(
                    json, signatureHeader, endpointSecret);
            // Handle the event notification by matching its class.
            // The notification identifies the related object, but doesn't contain it.
            // Events without a generated class in this SDK version are represented by
            // UnknownEventNotification. To handle them, add a branch that checks
            // the event-name string in the Type property.
            if (notification is V1PaymentIntentSucceededEventNotification paymentIntentNotification)
            {
                // Fetch the current version of the related object
                var paymentIntent = await paymentIntentNotification.FetchRelatedObjectAsync();
                Console.WriteLine("A successful payment for {0} was made.", paymentIntent.Amount);
                // Then define and call a method to handle the successful payment intent.
                // handlePaymentIntentSucceeded(paymentIntent);
                // Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
                // need data that the notification and related object don't provide.
                if (Environment.GetEnvironmentVariable("FETCH_FULL_EVENT") == "true")
                {
                    var stripeEvent = await paymentIntentNotification.FetchEventAsync();
                    Console.WriteLine("Retrieved event {0}.", stripeEvent.Id);
                }
            }
            else if (notification is V1PaymentMethodAttachedEventNotification paymentMethodNotification)
            {
                var paymentMethod = await paymentMethodNotification.FetchRelatedObjectAsync();
                // Then define and call a method to handle the successful attachment of a PaymentMethod.
                // handlePaymentMethodAttached(paymentMethod);
            }
            else
            {
                // Unexpected event type
                Console.WriteLine("Unhandled event type: {0}", notification.Type);
            }
            return Ok();
        catch (StripeException e)
        {
            Console.WriteLine("Error: {0}", e.Message);
            return BadRequest();
        }
  "github.com/stripe/stripe-go/v87"
  // This is a public sample test API key.
  // Don't submit any personally identifiable information in requests made with this key.
  // Sign in to see your own test API key embedded in code samples.
  // Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  sc = stripe.NewClient("<<YOUR_SECRET_KEY>>")
  http.HandleFunc("/webhook", handleWebhook)
  // To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
  // your thin event destination's unique secret.
  //
  // If you are testing with the CLI, find the secret by running 'stripe listen'.
  // If you're using a destination defined with the API or Dashboard, look in
  // your webhook settings at https://dashboard.stripe.com/webhooks.
  //
  // Don't include webhook secrets in code.
  endpointSecret := os.Getenv("STRIPE_WEBHOOK_SECRET")
  signatureHeader := req.Header.Get("Stripe-Signature")
  // Verify the signature and parse the thin event notification
  notification, err := sc.ParseEventNotification(payload, signatureHeader, endpointSecret)
  if err != nil {
    fmt.Fprintf(os.Stderr, "Webhook signature verification failed. %v\n", err)
    w.WriteHeader(http.StatusBadRequest) // Return a 400 error on a bad signature
    return
  }
  // Handle the event notification by switching on its concrete Go type.
  // The notification identifies the related object, but doesn't contain it.
  // Events without a generated type in this SDK version are represented by
  // *stripe.UnknownEventNotification. To handle them, add a case that checks
  // the event-name string returned by GetEventNotification().Type.
  switch evt := notification.(type) {
  case *stripe.V1PaymentIntentSucceededEventNotification:
    // Fetch the current version of the related object
    paymentIntent, err := evt.FetchRelatedObject(context.TODO())
    if err != nil {
      fmt.Fprintf(os.Stderr, "Error fetching related object: %v\n", err)
      w.WriteHeader(http.StatusInternalServerError)
      return
    }
    log.Printf("Successful payment for %d.", paymentIntent.Amount)
    // Then define and call a func to handle the successful payment intent.
    // handlePaymentIntentSucceeded(paymentIntent)
    // Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
    // need data that the notification and related object don't provide.
    if os.Getenv("FETCH_FULL_EVENT") == "true" {
      event, err := evt.FetchEvent(context.TODO())
      if err != nil {
        fmt.Fprintf(os.Stderr, "Error fetching event: %v\n", err)
        w.WriteHeader(http.StatusInternalServerError)
        return
      }
      log.Printf("Retrieved event %s.", event.ID)
    }
  case *stripe.V1PaymentMethodAttachedEventNotification:
    paymentMethod, err := evt.FetchRelatedObject(context.TODO())
    if err != nil {
      fmt.Fprintf(os.Stderr, "Error fetching related object: %v\n", err)
      w.WriteHeader(http.StatusInternalServerError)
      return
    }
    _ = paymentMethod
    // Then define and call a func to handle the successful attachment of a PaymentMethod.
    // handlePaymentMethodAttached(paymentMethod)
  default:
    fmt.Fprintf(os.Stderr, "Unhandled event type: %s\n", evt.GetEventNotification().Type)
  }
  w.WriteHeader(http.StatusOK)
require github.com/stripe/stripe-go/v87 v87.0.0
        // This is a public sample test API key.
        // Don't submit any personally identifiable information in requests made with this key.
        // Sign in to see your own test API key embedded in code samples.
        // Before testing, use a sandbox secret key from the Stripe account used by the Stripe CLI.
        // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
        StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");
        // To run this example, set an environment variable STRIPE_WEBHOOK_SECRET to
        // your thin event destination's unique secret.
        //
        // If you are testing with the CLI, find the secret by running 'stripe listen'.
        // If you're using a destination defined with the API or Dashboard, look in
        // your webhook settings at https://dashboard.stripe.com/webhooks.
        //
        // Don't include webhook secrets in code.
        String endpointSecret = System.getenv("STRIPE_WEBHOOK_SECRET");
        post("/webhook", (request, response) -> {
            String payload = request.body();
            EventNotification notification = null;
            String sigHeader = request.headers("Stripe-Signature");
            try {
                // Verify the signature and parse the thin event notification
                notification = client.parseEventNotification(
                    payload, sigHeader, endpointSecret
                );
            } catch (StripeException e) {
                // Invalid signature
                System.out.println("Webhook error while validating signature.");
                response.status(400);
                return "";
            }
            // Handle the event notification by matching its class.
            // The notification identifies the related object, but doesn't contain it.
            // Events without a generated class in this SDK version are represented by
            // UnknownEventNotification. To handle them, add a branch that checks
            // the event-name string returned by getType().
            if (notification instanceof V1PaymentIntentSucceededEventNotification) {
                V1PaymentIntentSucceededEventNotification paymentIntentNotification =
                    (V1PaymentIntentSucceededEventNotification) notification;
                // Fetch the current version of the related object
                PaymentIntent paymentIntent = paymentIntentNotification.fetchRelatedObject();
                System.out.println("Payment for " + paymentIntent.getAmount() + " succeeded.");
                // Then define and call a method to handle the successful payment intent.
                // handlePaymentIntentSucceeded(paymentIntent);
                // Optional: set FETCH_FULL_EVENT=true to retrieve the full event when you
                // need data that the notification and related object don't provide.
                if ("true".equals(System.getenv("FETCH_FULL_EVENT"))) {
                    V1PaymentIntentSucceededEvent event = paymentIntentNotification.fetchEvent();
                    System.out.println("Retrieved event " + event.getId());
                }
            } else if (notification instanceof V1PaymentMethodAttachedEventNotification) {
                PaymentMethod paymentMethod =
                    ((V1PaymentMethodAttachedEventNotification) notification).fetchRelatedObject();
                // Then define and call a method to handle the successful attachment of a PaymentMethod.
                // handlePaymentMethodAttached(paymentMethod);
            } else {
                System.out.println("Unhandled event type: " + notification.getType());
            }
            response.status(200);
            return "";
## Next steps

#### [Secure your webhooks](https://docs.stripe.com/events/set-up-events.md#signature-checking)

Secure your webhook endpoint by allowing only verified events from Stripe.

#### [Going live](https://docs.stripe.com/events/set-up-events.md#deploy-event-handler)

Learn how to deploy your webhook endpoint to production and handle events at scale by only sending the specific events you need.

#### [Thin event types](https://docs.stripe.com/api/v2/core/events/event-types.md)

See every event type you can subscribe to with a thin event destination.

#### [Best practices](https://docs.stripe.com/events/manage-webhook-endpoints.md#best-practices)

Understand best practices for maintaining your endpoint, such as managing retries or duplicate events.

#### [Stripe CLI](https://docs.stripe.com/cli.md)

The Stripe CLI has several commands that can help test your Stripe application beyond webhooks.

