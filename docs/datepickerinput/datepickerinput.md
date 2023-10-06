---
name: DatePickerInput
description: Date, multiple dates and dates range picker input. Helps you easily switch between different months, years along with locale support.
endpoint: /components/datepickerinput
package: dash_mantine_components
---

.. toc::

### Simple Example

This is a simple example of DatePickerInput tied to a callback. You can either use strings in a valid datetime format such
as `YYYY-MM-DD` or use the date object from datetime library.

.. exec::docs.datepickerinput.simple

### Multiple dates

Set type="multiple" to allow user to pick multiple dates.  Note that `value` is a list.

.. exec::docs.datepickerinput.multiple

### Dates range

Set type="range" to allow user to pick dates range. Note that `value` is a list.

.. exec::docs.datepickerinput.range

### Open picker in modal

By default, DatePicker is rendered inside Popover. You can change that to Modal by setting dropdownType="modal"

.. exec::docs.datepickerinput.modal

### Value formats

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

### Value Format Examples

.. exec::docs.datepickerinput.formats

### Clearable

Set clearable=True prop to display clear button in the right section. Note that if you set rightSection prop, clear button will not be displayed.

.. exec::docs.datepickerinput.clearable

### Error Display

You can convey errors in your date picker by setting the `error` prop. For instance, in the below example we try to
convey the user that it's a required field and the date can't be an odd date. Since it's a required field, we also
set `clearable=False`.

.. exec::docs.datepickerinput.errors

### Localization

For information on setting locale, have a look at the [DatesProvider](/components/datesprovider) component.

### Keyword Arguments

#### DatePickerInput

.. kwargs::DatePickerInput
