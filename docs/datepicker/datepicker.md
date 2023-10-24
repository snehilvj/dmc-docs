---
name: DatePicker
description: Inline date, multiple dates and dates range picker. Helps you easily switch between different months, years along with locale support.
endpoint: /components/datepicker
package: dash_mantine_components
---

.. toc::

.. admonition::Note
    :color: yellow
    :icon: radix-icons:info-circled
    To include an Input field for the DatePicker, use DatePickerInput.

### Simple Example

.. exec::docs.datepicker.simple

### Allow deselect

Set `allowDeselect` to allow user to deselect current selected date by clicking on it. `allowDeselect` is disregarded when type prop is range or multiple. When date is deselected the `value` will be None.

```python
from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DatePicker(
    value=datetime.now().date(),
    allowDeselect=True,
)
```

### Multiple dates

.. exec::docs.datepicker.multiple

### Range of dates

.. exec::docs.datepicker.range

By default, it is not allowed to select single date as range – when user clicks the same date second time it is deselected.
To change this behavior set `allowSingleDateInRange` prop. `allowSingleDateInRange` is ignored when `type` prop is not `range`.

### Disabled dates

Use the `disabledDates` prop to specify days that should be disabled.

```python
from datetime import datetime, timedelta

import dash_mantine_components as dmc

today = datetime.now().date()

component = dmc.DatePicker(
    value=today,
    disabledDates=[today + timedelta(days=1), today + timedelta(days=3)],
)
```

### Weekend days

Use `weekendDays` prop to configure weekend days. The prop accepts an array of numbers from 0 to 6, where 0 is Sunday and 6 is Saturday.
Default value is [0, 6] – Saturday and Sunday. You can also configure this option for all components with DatesProvider.

```python
from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DatePicker(
    value=datetime.now().date(), weekendDays=[5, 6, 0], firstDayOfWeek=0
)
```

### Min and max date

Set `minDate` and `maxDate` props to define min and max dates. If previous/next page is not available then corresponding control will be disabled.

```python
from datetime import date

import dash_mantine_components as dmc

component = dmc.DatePicker(
    minDate=date(2023, 8, 1),
    maxDate=date(2023, 8, 15),
    value="2023-08-11",
)
```

### Localization

For information on setting locale, have a look at the [DatesProvider](/components/datesprovider) component.

### Keyword Arguments

#### DatePicker

.. kwargs::DatePicker
