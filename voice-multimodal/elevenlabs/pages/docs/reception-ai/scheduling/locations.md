---
title: "Locations"
source: https://elevenlabs.io/docs/reception-ai/scheduling/locations.md
path: docs/reception-ai/scheduling/locations
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Locations

Locations represent the places your business operates. Each location has its own address, opening hours, staff, assets, services, and products. Your receptionist asks callers which location they want, and customers can filter by location on the booking page.

## Adding a location

Go to **Business** → **Overview**, open **Locations**, and select **Add location**.

| Field                               | Description                                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| **Name**                            | Internal name for the location                                               |
| **Display name**                    | The name customers see on the booking page and hear from the receptionist    |
| **Address**                         | The street address                                                           |
| **Notes**                           | Extra details for the receptionist, such as parking or entrance instructions |
| **Active (available for bookings)** | Turn off to stop taking bookings at this location                            |

## What each location controls

Each location's settings have tabs for:

* **Hours**: the location's opening hours. See [Hours and booking rules](/docs/reception-ai/scheduling/hours-and-booking-rules).
* **Staff**: who works at this location.
* **Assets**: rooms and equipment at this location.
* **Services**: services offered here. Services not assigned to any location are available everywhere.
* **Products**: products sold here, including per-location stock when [orders](/docs/reception-ai/features/orders) are enabled.

Closures and the overlapping-appointment limit are also set per location.

## Plan limits

| Plan    | Active locations |
| ------- | ---------------- |
| Trial   | 20               |
| Basic   | 1                |
| Plus    | 1                |
| Premium | 20               |

If you downgrade to a plan with fewer locations, locations over the limit are deactivated. Upgrade to reactivate them.
