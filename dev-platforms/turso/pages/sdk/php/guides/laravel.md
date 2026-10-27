---
title: "Turso Quickstart (Laravel)"
source: https://docs.turso.tech/sdk/php/guides/laravel
path: sdk/php/guides/laravel
---

In this Laravel quickstart we will learn how to:

* Install the Turso Laravel adapter
* Configure Laravel to use Turso
* Create a model and migration
* Perform CRUD operations using Eloquent

**1. Retrieve database credentials**

You will need an existing database to continue. If you don't have one, [create one](/quickstart).

<Snippet />

> [!NOTE]
>
> You will want to store these as environment variables.

**2. Install**

Install the package to your Laravel project using Composer:

```console theme={null}
composer require turso/libsql-laravel
```

> [!NOTE]
>
> Make sure to enable FFI in your PHP configuration to use the Laravel adapter.

**3. Configure**

Choose your preferred setup and configure accordingly:

> **Local only**
>
> Update your `config/database.php`:
>
> ```php theme={null}
> return [
>     "default" => env("DB_CONNECTION", "libsql"),
>
>     "connections" => [
>         "libsql" => [
>             "driver" => "libsql",
>             "database" => database_path("database.db"),
>         ],
>         // ...
>     ],
> ];
> ```
>
> This will use a local SQLite file with the libSQL adapter.

> **Remote only**
>
> Update your `config/database.php`:
>
> ```php theme={null}
> return [
>     "default" => env("DB_CONNECTION", "libsql"),
>
>     "connections" => [
>         "libsql" => [
>             "driver" => "libsql",
>             "url" => env("TURSO_DATABASE_URL"),
>             "password" => env("TURSO_AUTH_TOKEN"),
>         ],
>         // ...
>     ],
> ];
> ```
>
> Then add to your `.env` file:
>
> ```
> DB_CONNECTION=libsql
> TURSO_DATABASE_URL=libsql://...
> TURSO_AUTH_TOKEN=...
> ```

> **Embedded Replicas**
>
> Update your `config/database.php`:
>
> ```php theme={null}
> return [
>     "default" => env("DB_CONNECTION", "libsql"),
>
>     "connections" => [
>         "libsql" => [
>             "driver" => "libsql",
>             "database" => database_path("database.db"),
>             "url" => env("TURSO_DATABASE_URL"),
>             "password" => env("TURSO_AUTH_TOKEN"),
>             "sync_interval" => env("TURSO_SYNC_INTERVAL", 300),
>         ],
>         // ...
>     ],
> ];
> ```
>
> Then add to your `.env` file:
>
> ```
> DB_CONNECTION=libsql
> TURSO_DATABASE_URL=libsql://...
> TURSO_AUTH_TOKEN=...
> TURSO_SYNC_INTERVAL=300
> ```
>
> > [!NOTE]
> >
> > The `sync_interval` is optional and defaults to 300 seconds (5 minutes).

**4. Create a model and migration**

Create a User model and migration:

```console theme={null}
php artisan make:model User -m
```

Update the migration file:

```php theme={null}
public function up()
{
    Schema::create('users', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->string('email')->unique();
        $table->timestamps();
    });
}
```

**5. Run migrations**

Apply the migration to create the users table:

```console theme={null}
php artisan migrate
```

**6. Execute CRUD operations**

Now you can perform CRUD operations using Eloquent:

```php Create theme={null}
use App\Models\User;

$user = User::create([
    'name' => 'John Doe',
    'email' => 'john@example.com',
]);
```

```php Read theme={null}
use App\Models\User;

// Fetch all users
$allUsers = User::all();

// Find a specific user by ID
$user = User::find(1);

// Filter users
$filteredUsers = User::where('name', 'John Doe')->get();
```

```php Update theme={null}
use App\Models\User;

// Update a single record
$user = User::find(1);
$user->name = 'Jane Doe';
$user->save();

// Update multiple records
User::where('name', 'John Doe')->update(['name' => 'Jane Doe']);
```

```php Delete theme={null}
use App\Models\User;

// Delete a single record
$user = User::find(1);
$user->delete();

// Delete multiple records
User::where('name', 'Jane Doe')->delete();
```
