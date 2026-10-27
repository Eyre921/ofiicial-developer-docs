---
title: "Drift + Turso / LibSQL"
source: https://docs.turso.tech/sdk/flutter/integrations/drift
path: sdk/flutter/integrations/drift
---

Configure `drift` to work with `libsql_dart`

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)

**1. Add packages to your project**

```bash theme={null}
flutter pub add drift_libsql drift drift_flutter dev:build_runner dev:drift_dev
```

**2. Retrieve database credentials**

<Snippet />

**3. Create a table schema**

```dart theme={null}
class TaskTable extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get title => text()();
  TextColumn get description => text()();
  BoolColumn get completed => boolean()();
}
```

**4. Create db class**

```dart theme={null}
@DriftDatabase(tables: [TaskTable])
class AppDatabase extends _$AppDatabase {
  AppDatabase(super.e);

  @override
  int get schemaVersion => 1;
}
```

**5. Run build runner**

```bash theme={null}
dart run build_runner build
```

**6. Create the db**

```dart theme={null}
final db = AppDatabase(DriftLibsqlDatabase(
    "${dir.path}/replica.db",
    syncUrl: url,
    authToken: token,
    readYourWrites: true,
    syncIntervalSeconds: 3,
  ));
```

**7. Perform SQL operations**

```dart theme={null}
await db.into(db.taskTable).insert(TaskTableCompanion.insert(
	title: task.title,
	description: task.description,
	completed: task.completed));
```
