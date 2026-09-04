---
title: "Connect to Turso using Dart"
source: https://docs.turso.tech/connect/dart
path: connect/dart
---

<Steps>
  <Step title="Install">
    Add the turso\_dart package to your `pubspec.yaml`:

    ```yaml theme={null}
    dependencies:
      turso_dart:
    ```

    Then run:

    ```bash theme={null}
    dart pub get
    ```
  </Step>

  <Step title="Connect">
    Create a client connection. You can connect to an in-memory database or a local file:

    ```dart theme={null}
    import 'package:turso_dart/turso_dart.dart';

    // In memory
    final client = TursoClient.memory();

    // Or local file
    final client = TursoClient.local('/path/to/local.db');

    await client.connect();
    ```
  </Step>

  <Step title="Create table">
    Create a table for customers:

    ```dart theme={null}
    await client.execute(
      "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT)"
    );
    ```
  </Step>

  <Step title="Insert data">
    Insert some data into the customers table:

    ```dart theme={null}
    await client.query("INSERT INTO customers(name) VALUES ('John Doe')");
    await client.query("INSERT INTO customers(name) VALUES ('Jane Smith')");
    ```
  </Step>

  <Step title="Query data">
    Query all customers from the table:

    ```dart theme={null}
    final result = await client.query("SELECT * FROM customers");
    print(result);
    ```
  </Step>

  <Step title="Prepared statements">
    Use prepared statements for better performance and security:

    ```dart theme={null}
    final statement = await client.prepare("SELECT * FROM customers WHERE id = ?");
    final result = await statement.query(positional: [1]);
    print(result);
    ```
  </Step>
</Steps>
