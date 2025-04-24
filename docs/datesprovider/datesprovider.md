---
name: DatesProvider
description: DatesProvider component lets you set various settings that are shared across all date components.
endpoint: /components/datesprovider
package: dash_mantine_components
category: Date Pickers
---

.. toc::


### CSS Extensions

As of DMC 1.2.0, `Date` component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.




### Usage

The DatesProvider component lets you set various settings that are shared across all date components. DatesProvider supports the following settings:

- `locale` – dayjs locale, note that you also need to import corresponding locale module from dayjs. Default value is en.
- `firstDayOfWeek` – number from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is 1 – Monday.
- `weekendDays` – an array of numbers from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is [0, 6] – Saturday and Sunday.

### Locale

DatePicker component uses [dayjs](https://day.js.org) behind the scenes. So you can easily customize locale by including
required locale data and setting the `locale`. Make sure to include proper localization file from dayjs library.

```python
from dash import Dash
import dash_mantine_components as dmc

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
]

app = Dash(__name__, external_scripts=scripts)
```

.. exec::docs.datesprovider.simple

### Keyword Arguments

#### DatesProvider

.. kwargs::DatesProvider
