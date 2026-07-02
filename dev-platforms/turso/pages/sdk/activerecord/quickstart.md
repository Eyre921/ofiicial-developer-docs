---
title: "Turso Quickstart (ActiveRecord)"
source: https://docs.turso.tech/sdk/activerecord/quickstart
path: sdk/activerecord/quickstart
---

Get started with Turso and ActiveRecord in a few simple steps.

<Snippet />

In this Ruby quickstart we will learn how to:

* Retrieve database credentials
* Install the libSQL ActiveRecord gem
* Connect to a local or remote Turso database
* Define and create models
* Perform basic CRUD operations
* Execute raw SQL queries
* Work with migrations

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet />
  </Step>

  <Step title="Install">
    In your Ruby project, add the following gems to your Gemfile:

    ```ruby theme={null}
    gem 'libsql_activerecord'
    gem 'activerecord'
    ```

    Then run:

    ```bash theme={null}
    bundle install
    ```
  </Step>

  <Step title="Connect">
    Create a Ruby file (e.g., `database.rb`) to set up the database connection:

    <AccordionGroup>
      <Accordion title="Embedded Replicas">
        ```rb theme={null}
        require 'libsql_activerecord'
        require 'active_record'

        ActiveRecord::Base.establish_connection(
          adapter: 'libsql',
          url: ENV['TURSO_DATABASE_URL'],
          auth_token: ENV['TURSO_AUTH_TOKEN'],
          path: 'path/to/local/replica.db'
        )
        ```
      </Accordion>

      <Accordion title="Local only">
        ```rb theme={null}
        require 'libsql_activerecord'
        require 'active_record'

        ActiveRecord::Base.establish_connection(
          adapter: 'libsql',
          path: 'path/to/local.db'
        )
        ```
      </Accordion>

      <Accordion title="Remote only">
        ```rb theme={null}
        require 'libsql_activerecord'
        require 'active_record'

        ActiveRecord::Base.establish_connection(
          adapter: 'libsql',
          url: ENV['TURSO_DATABASE_URL'],
          auth_token: ENV['TURSO_AUTH_TOKEN']
        )
        ```
      </Accordion>

      <Accordion title="In-memory">
        ```rb theme={null}
        require 'libsql_activerecord'
        require 'active_record'

        ActiveRecord::Base.establish_connection(adapter: 'libsql')
        ```
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Define models">
    Create model files for your database tables. For example, `product.rb`:

    ```rb theme={null}
    class Product < ActiveRecord::Base
      validates :name, presence: true
    end
    ```
  </Step>

  <Step title="Create and execute a migration">
    Create a migration file (e.g., `001_create_products.rb`):

    ```rb theme={null}
    class CreateProducts < ActiveRecord::Migration[8.0]
      def change
        create_table :products do |t|
          t.string :name
          t.text :description
          t.timestamps
        end
      end
    end
    ```

    Execute the migration:

    ```rb theme={null}
    require_relative 'database'
    require_relative '001_create_products'

    CreateProducts.migrate(:up)
    ```
  </Step>

  <Step title="Execute">
    Perform some basic CRUD operations:

    <CodeGroup>
      ```rb Create theme={null}
      product = Product.create(name: 'Book', description: 'A book about books')
      ```

      ```rb Read theme={null}
      all_products = Product.all
      first_product = Product.first
      found_product = Product.find_by(name: 'Book')
      ```

      ```rb Update theme={null}
      product.update(description: 'An updated description')
      ```

      ```rb Delete theme={null}
      product.destroy
      ```

      ```rb Raw SQL theme={null}
      results = ActiveRecord::Base.connection.execute("SELECT * FROM products WHERE name LIKE '%Book%'")

      results.each do |row|
        puts row.inspect
      end
      ```
    </CodeGroup>
  </Step>

  <Step title="Work with associations">
    Define associations in your models:

    ```ruby theme={null}
    class Author < ActiveRecord::Base
      has_many :books
    end

    class Book < ActiveRecord::Base
      belongs_to :author
    end
    ```

    Use associations in your code:

    ```ruby theme={null}
    author = Author.create(name: 'Jane Doe')
    book = author.books.create(title: 'My First Book')

    puts author.books.count # => 1
    puts book.author.name # => "Jane Doe"
    ```
  </Step>
</Steps>
