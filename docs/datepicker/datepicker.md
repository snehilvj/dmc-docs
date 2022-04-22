---
name: DatePicker
section: Inputs & Buttons
head: Capture date inputs from user.
description: Best DatePicker and DateRangePicker components out there. Helps you easily switch between different months, years along with locale support.
component: DatePicker
---

##### Simple Example

This is a simple example of DatePicker tied to a callback. You can either use strings in a valid datetime format such
as `YYYY-MM-DD` or use the date object from datetime library.

.. exec-block::docs.datepicker.simple

##### Date formats

Use `format` property to change the format of the date displayed in the date picker. You can use any permutation from
the below table to achieve the desired date format. Note: This is not the format of the value you'll receive from the
date picker in a callback. That will always follow: `YYYY-MM-DD`.

| Format | Output           | Description                           |
|--------|------------------|---------------------------------------|
| YY     | 18               | Two-digit year                        |
| YYYY   | 2018             | Four-digit year                       |
| M      | 1-12             | The month: beginning at 1             |
| MM     | 01-12            | The month: 2-digits                   |
| MMM    | Jan-Dec          | The abbreviated month name            |
| MMMM   | January-December | The full month name                   |
| D      | 1-31             | The day of the month                  |
| DD     | 01-31            | The day of the month: 2-digits        |
| d      | 0-6              | The day of the week: with Sunday as 0 |
| dd     | Su-Sa            | The min name of the day of the week   |
| ddd    | Sun-Sat          | The short name of the day of the week |
| dddd   | Sunday-Saturday  | The name of the day of the week       |

##### Date Format Examples

.. exec-block::docs.datepicker.formats

##### Localization

DatePicker component uses dayjs behind the scenes. So you can easily customize locale by including required locale data
and setting the `locale` prop. Make sure to include proper localization file from dayjs library.

```python
from dash import Dash

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
]

app = Dash(__name__, external_scripts=scripts)
```

.. exec-block::docs.datepicker.locale

##### Clear and Overlay Mode

dmc.DatePicker is clearable by default. You can change this behaviour by setting the `clearable` prop to `False`.
dmc.DatePicker also supports opening date picker as an overlay instead of the normal popover mode. To enable that, set
the type `dropdownType` prop to `modal`.

.. exec-block::docs.datepicker.modal

##### Amount of months

You can display more than one month in date picker dropdown by setting the `amountOfMonths` prop to the desired value.

.. exec-block::docs.datepicker.amount

##### Error Display

You can convey errors in your date picker by setting the `error` prop. For instance, in the below example we try to
convey the user that it's a required field and the date can't be an odd date. Since it's a required field, we also
set `clearable=False`.

.. exec-block::docs.datepicker.errors
