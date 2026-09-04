---
title: "SQLAlchemy + Turso"
source: https://docs.turso.tech/sdk/python/orm/sqlalchemy
path: sdk/python/orm/sqlalchemy
---

Configure SQLAlchemy to work with your Turso database

<img alt="SQLAlchemy Quickstart" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)

<Steps>
  <Step title="Install the libSQL dialect for SQLAlchemy">
    ```bash theme={null}
    pip install sqlalchemy-libsql
    ```
  </Step>

  <Step title="Retrieve database credentials">
    <Snippet />
  </Step>

  <Step title="Create database models">
    ```python models.py theme={null}
    from sqlalchemy import String
    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy.orm import Mapped
    from sqlalchemy.orm import mapped_column

    class Base(DeclarativeBase):
        pass

    class Foo(Base):
        __tablename__ = "foo"
        id: Mapped[str] = mapped_column(primary_key=True)
        bar: Mapped[str] = mapped_column(String(100))
        def __repr__(self) -> str:
            return f"Item(id={self.id!r}, bar={self.bar!r})"

    ```
  </Step>

  <Step title="Create engine">
    <AccordionGroup>
      <Accordion title="Embedded Replicas">
        ```python theme={null}
        from dotenv import load_dotenv
        from sqlalchemy import create_engine

        TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
        TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

        engine = create_engine(
             "sqlite+libsql:///embedded.db",
             connect_args={
                 "auth_token": TURSO_AUTH_TOKEN,
                 "sync_url": TURSO_DATABASE_URL,
             },
        )
        ```
      </Accordion>

      <Accordion title="Remote only">
        ```python theme={null}
        from dotenv import load_dotenv
        from sqlalchemy import create_engine

        TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
        TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

        engine = create_engine(
            f"sqlite+{TURSO_DATABASE_URL}?secure=true",
            connect_args={
                "auth_token": TURSO_AUTH_TOKEN,
            },
        )
        ```
      </Accordion>

      <Accordion title="Memory Only">
        ```python theme={null}
        from sqlalchemy import create_engine

        engine = create_engine("sqlite+libsql://")
        ```
      </Accordion>

      <Accordion title="Local only">
        ```python theme={null}
        from sqlalchemy import create_engine

        engine = create_engine("sqlite+libsql:///local.db")
        ```
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Query">
    ```py app.py theme={null}
    from sqlalchemy.orm import Session
    from sqlalchemy import select
    from models import Foo

    @app.route("/", methods=(["GET"]))
    def home():
        session = Session(engine)

        # get & print foos
        stmt = select(Foo)

        for item in session.scalars(stmt):
            print(item)

    ```
  </Step>
</Steps>
