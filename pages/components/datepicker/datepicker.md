DatePicker | Capture date input from user.

### Simple Example

This is a simple example of DatePicker tied to a callback. You can either use strings in a valid datetime format such
as `YYYY-MM-DD` or use the date object from datetime library.

> example:components/datepicker/_simple.py

### Date formats

Use `format` property to change the format of the date displayed in the date picker. You can use any permutation from
the below table to achieve the desired date format. Note: This is not the format of the value you'll receive from the
date picker in a callback. That will always follow: `YYYY-MM-DD`.

> dmc:components/datepicker/_table.py

### Date Format Examples

> dmc:components/datepicker/_formats.py

### Clear and Overlay Mode

dmc.DatePicker is clearable by default. You can change this behaviour by setting the `clearable` prop to `False`.
dmc.DatePicker also supports opening date picker as an overlay instead of the normal popover mode. To enable that, set
the type `dropdownType` prop to `modal`.

> example:components/datepicker/_dropdown_type.py

### Amount of months

You can display more than one months in date picker dropdown by setting the `amountOfMonths` prop to the desired value.

> example:components/datepicker/_amount.py

### Error Display

You can convey errors in your date picker by setting the `error` prop. For instance, in the below example we try to
convey the user that it's a required field and the date can't be an odd date. Since it's a required field, we also
set `clearable=False`.

> example:components/datepicker/_errors.py

> apidoc:DatePicker