---
name: DatesProvider
description: DatesProvider component lets you set various settings that are shared across all date components.
endpoint: /components/datesprovider
package: dash_mantine_components
---

.. toc::

### Usage

The DatesProvider component lets you set various settings that are shared across all date components. DatesProvider supports the following settings:

- `locale` – dayjs locale, note that you also need to import corresponding locale module from dayjs. Default value is en.
- `firstDayOfWeek` – number from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is 1 – Monday.
- `weekendDays` – an array of numbers from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is [0, 6] – Saturday and Sunday.

### Locale

.. exec::docs.datesprovider.simple

### Keyword Arguments

#### DatesProvider

.. kwargs::DatesProvider
