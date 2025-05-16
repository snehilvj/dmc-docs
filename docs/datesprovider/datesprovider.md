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
- `consistentWeeks` – boolean, if true every month will have 6 weeks. Default value is false.



### Locale

DatePicker component uses [dayjs](https://day.js.org) behind the scenes. So you can easily customize locale by including
required locale data and setting the `locale`. Make sure to include proper localization file from dayjs library.

 - [dayjs internationalization](https://day.js.org/docs/en/i18n/i18n)
 - [Loading locale in the browser](https://day.js.org/docs/en/installation/browser#cdn-resource)
 - [Supported locales](https://github.com/iamkun/dayjs/tree/dev/src/locale)

```python
from dash import Dash
import dash_mantine_components as dmc

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",      # dayjs  
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/fr.min.js",  # french locale
]

app = Dash(external_scripts=scripts)
```

.. exec::docs.datesprovider.simple


### Consistent weeks
If you want to avoid layout shifts, set `consistentWeeks=True` in `DatesProvider` settings. This will make sure that 
every month has 6 weeks, even if outside days are not in the same month.


.. exec::docs.datesprovider.consistentweeks



### Keyword Arguments

#### DatesProvider

.. kwargs::DatesProvider
