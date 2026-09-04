---
title: "db inspect"
source: https://docs.turso.tech/cli/db/inspect
path: cli/db/inspect
---

You can inspect the usage of a database, including the total space used, rows read and written with the following command:

```bash theme={null}
turso db inspect <database-name>
```

## Flags

| Flag        | Description                                                          |
| ----------- | -------------------------------------------------------------------- |
| `--queries` | Show database query statistics.                                      |
| `--verbose` | Show detailed information, including the location and instance type. |

## Examples

### Top Queries

You can fetch the most executed, resource-intensive SQL statements that have been run against your database using the Turso CLI:

<CodeGroup>
  ```bash Command theme={null}
  turso db inspect <database-name> --queries
  ```

  ```bash Response theme={null}
  SELECT * FROM Orders WHERE Status = 'Pending';
  SELECT COUNT(*), CustomerID FROM Orders GROUP BY CustomerID HAVING COUNT(*) > 5;
  SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
  UPDATE Products SET Price = Price * 1.10 WHERE Category = 'Electronics';
  ```
</CodeGroup>
