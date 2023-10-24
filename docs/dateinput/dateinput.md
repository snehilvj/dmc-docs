---
name: DateInput
description: Free date input
endpoint: /components/dateinput
package: dash_mantine_components
---

.. toc::


### DateInput props
DateInput supports all props from DatePicker, read through its documentation to learn about all component features that are not listed on this page.



### Simple Example

This is a simple example of DateInput tied to a callback. You can type a date or select from the DatePicker

.. exec::docs.dateinput.simple

### Value formats

Use `format` property to change the format of the date displayed in the date input field. You can use any permutation from
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

### Value Format 

.. exec::docs.dateinput.formats

### With Time

Include time in `valueFormat` to allow hours, minutes and seconds to be entered.

.. exec::docs.dateinput.time

### Clearable

Set clearable prop to allow removing value from the input. Input will be cleared if user selects the same date in dropdown or clears input value.

When `clearable=True`, a clear button in the right section is displayed. Note that if you set rightSection prop, clear button will not be displayed.

.. exec::docs.dateinput.clearable

### Min and max date
Set `minDate` and `maxDate` props to define min and max dates. If date that is after `maxDate` or before `minDate` is entered, then it will be considered invalid and input value will be reverted to last known valid date value.

.. exec::docs.dateinput.minmax

### Input props

.. exec::docs.dateinput.interactive
   :code: false




### Keyword Arguments

#### DateInput

.. kwargs::DateInput
