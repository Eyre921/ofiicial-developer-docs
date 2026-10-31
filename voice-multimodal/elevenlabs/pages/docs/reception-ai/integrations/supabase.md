---
title: "Supabase"
source: https://elevenlabs.io/docs/reception-ai/integrations/supabase.md
path: docs/reception-ai/integrations/supabase
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Supabase

Your receptionist can save details from a call to a Supabase table and look up a caller by phone number, through Supabase's REST API. The setup below uses your project's public key with row-level security, so the receptionist can only do what you allow.

> **Warning**
>
> Never put the `service_role` or secret key in a webhook tool. Those keys bypass row-level security
> and give full access to your database.

## Before you start

In the Supabase dashboard, open **Project Settings** → **API Keys** and copy the **publishable** key, or the legacy **anon** key. Your project URL is `https://PROJECT_REF.supabase.co`.

## Prepare the database

Run this in the **SQL Editor**. It creates a table your receptionist can only insert into, and a function that returns one customer by exact phone number. The function assumes an existing `customers` table with `name`, `plan`, `notes`, and `phone` columns, so adjust the names to your schema.

Callers can't use the function to list customers: it returns nothing unless the exact phone number is known.

```sql
create table callback_requests (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  caller_name text not null,
  phone text not null,
  reason text not null
);

alter table callback_requests enable row level security;

create policy "Receptionist can add callback requests"
  on callback_requests for insert to anon
  with check (true);

create function find_customer_by_phone(phone text)
returns table (name text, plan text, notes text)
language sql stable security definer set search_path = public
as $$
  select c.name, c.plan, c.notes from customers c where c.phone = find_customer_by_phone.phone limit 1;
$$;

revoke execute on function find_customer_by_phone from public;
grant execute on function find_customer_by_phone to anon;
```

## Create the tools

For both tools, go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and add these request headers:

| Header          | Value                                                                   |
| --------------- | ----------------------------------------------------------------------- |
| `apikey`        | Your publishable or anon key                                            |
| `Authorization` | `Bearer ` followed by the anon key. Leave it out for a publishable key. |

### Save a callback request

| Field                | Value                                                                  |
| -------------------- | ---------------------------------------------------------------------- |
| **Name**             | `save_callback_request`                                                |
| **Description**      | "Save a callback request whenever you promise the caller a follow-up." |
| **Method**           | POST                                                                   |
| **URL**              | `https://PROJECT_REF.supabase.co/rest/v1/callback_requests`            |
| **Body Parameters**  | `caller_name`, `phone`, and `reason` (all strings, required)           |
| **Assign to agents** | **Receptionist**                                                       |

### Look up a customer

| Field                | Value                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| **Name**             | `find_customer`                                                                                        |
| **Description**      | "Look up the caller's account by phone number. Use it when a caller asks about their plan or account." |
| **Method**           | POST                                                                                                   |
| **URL**              | `https://PROJECT_REF.supabase.co/rest/v1/rpc/find_customer_by_phone`                                   |
| **Body Parameters**  | `phone` (string, required): "The caller's phone number in E.164 format, for example +14155550123."     |
| **Assign to agents** | **Receptionist**                                                                                       |

Select **Enable** on each tool, then [test your receptionist](/docs/reception-ai/receptionist/testing) with a callback request. The row appears in **Table Editor**.

## Troubleshooting

| Problem                                      | What to check                                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------------------ |
| `new row violates row-level security policy` | The insert policy must target the `anon` role.                                       |
| `Could not find the function`                | The body parameter must be named exactly like the function's argument, here `phone`. |
| 401 `Invalid API key`                        | With a publishable key, remove the `Authorization` header.                           |
| Customers aren't found                       | Store phone numbers in E.164 format, the same format your receptionist sends.        |
