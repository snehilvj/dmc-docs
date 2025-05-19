---
name: DatePicker
description: Inline date, multiple dates and dates range picker
endpoint: /components/datepicker
package: dash_mantine_components
category: Date Pickers
---

.. toc::

> Looking for a date picker with an input field and a dropdown calendar? Try `DateInput` or `DatePickerInput`.

### Simple Example

This is a simple example of `DatePicker` with a callback. You can either use strings in format 'YYYY-MM-DD` or use the
date object from datetime library.

.. exec::docs.datepicker.simple

### Allow deselect
Set `allowDeselect` to allow user to deselect current selected date by clicking on it. `allowDeselect` is disregarded
when `type` prop is `range` or `multiple`. When date is deselected the value is None.


.. exec::docs.datepicker.allowdeselect

### Multiple dates
Set `type="multiple"` to allow user to pick multiple dates.  Note that value must be a list.


.. exec::docs.datepicker.multiple

### Dates range
Set `type="range"` to allow user to pick dates range. Note that value must be a list.


.. exec::docs.datepicker.range

### Single date in range
By default, it is not allowed to select single date as range – when user clicks the same date second time it is
deselected. To change this behavior set `allowSingleDateInRange=True` prop. `allowSingleDateInRange` is ignored 
when type prop is not range.


.. exec::docs.datepicker.rangesingledate

### Default date

Use `defaultDate` prop to set date value that will be used to determine which year should be displayed initially. For 
example to display 2015 February month set `defaultDate="2015-02-01"`. If value is not specified, then defaultDate will
use today's date. Day, minutes and seconds are ignored in provided date, only year and month data is used – you can 
specify any date value.


.. exec::docs.datepicker.defaultdate

### Level
Set `level` prop to configure initial level that will be displayed:

.. exec::docs.datepicker.level

### Hide outside dates
Set `hideOutsideDates=True` to remove all dates that do not belong to the current month:

.. exec::docs.datepicker.hideoutsidedates

### Display week numbers
Set `withWeekNumbers=True` to display week numbers:

.. exec::docs.datepicker.weeknumbers

### First day of week
Set `firstDayOfWeek` prop to configure first day of week. The prop accepts number from 0 to 6, where 0 is Sunday and 6
is Saturday. Default value is 1 – Monday. You can also configure this option for all components with `DatesProvider`.


.. exec::docs.datepicker.firstdayofweek

### Hide weekdays
Set `hideWeekdays=True` to hide weekdays names:

.. exec::docs.datepicker.hideweekdays

### Weekend days
Use `weekendDays` prop to configure weekend days. The prop accepts an array of numbers from 0 to 6, where 0 is
Sunday and 6 is Saturday. Default value is `[0, 6]` – Saturday and Sunday. You can also configure this option for
all components with DatesProvider.


.. exec::docs.datepicker.weekenddays

### Min and max date
Set `minDate` and `maxDate` props to define min and max dates. If previous/next page is not available then 
corresponding control will be disabled.


.. exec::docs.datepicker.minmax

### Disabled dates
To disable specific dates use `disabledDates' prop. The prop accepts a list of dates in the string format of YYYY-MM-DD

.. exec::docs.datepicker.disabledates

### Number of columns
Set `numberOfColumns` prop to define number of pickers that will be rendered side by side:

.. exec::docs.datepicker.numberofcolumns

### Max level

.. exec::docs.datepicker.maxlevel

### Change year and months controls format
Use `yearsListFormat` and `monthsListFormat` props to change [dayjs](https://day.js.org/docs/en/display/format) format of year/month controls:

.. exec::docs.datepicker.yearmonformat

### Change label format
Use `decadeLabelFormat`, `yearLabelFormat` and `monthLabelFormat` props to change  [dayjs](https://day.js.org/docs/en/display/format)
format of decade/year label:


.. exec::docs.datepicker.labelformat

### CSS Extensions

As of DMC 1.2.0, Date component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.

### Migrating from DMC <= 0.14?

The `DatePicker` from 0.14 was renamed to `DatePickerInput` so it aligns with the upstream Mantine library.


### Localization

For information on setting locale, have a look at the [DatesProvider](/components/datesprovider) component.

### Styles API

.. styles_api_text::


#### DatePicker Selectors

| Selector                  | Static selector                                 | Description                                    |
| ------------------------- | ----------------------------------------------- | ---------------------------------------------- |
| calendarHeader            | `.mantine-DatePicker-calendarHeader`            | Calendar header root element                   |
| calendarHeaderControl     | `.mantine-DatePicker-calendarHeaderControl`     | Previous/next calendar header controls         |
| calendarHeaderControlIcon | `.mantine-DatePicker-calendarHeaderControlIcon` | Icon of previous/next calendar header controls |
| calendarHeaderLevel       | `.mantine-DatePicker-calendarHeaderLevel`       | Level control (month → year → decade)          |
| levelsGroup               | `.mantine-DatePicker-levelsGroup`               | Group of months levels                         |
| yearsList                 | `.mantine-DatePicker-yearsList`                 | Years list table element                       |
| yearsListRow              | `.mantine-DatePicker-yearsListRow`              | Years list row element                         |
| yearsListCell             | `.mantine-DatePicker-yearsListCell`             | Years list cell element                        |
| yearsListControl          | `.mantine-DatePicker-yearsListControl`          | Button used to pick months and years           |
| monthsList                | `.mantine-DatePicker-monthsList`                | Months list table element                      |
| monthsListRow             | `.mantine-DatePicker-monthsListRow`             | Months list row element                        |
| monthsListCell            | `.mantine-DatePicker-monthsListCell`            | Months list cell element                       |
| monthsListControl         | `.mantine-DatePicker-monthsListControl`         | Button used to pick months and years           |
| monthThead                | `.mantine-DatePicker-monthThead`                | Thead element of month table                   |
| monthRow                  | `.mantine-DatePicker-monthRow`                  | TR element of month table                      |
| monthTbody                | `.mantine-DatePicker-monthTbody`                | Tbody element of month table                   |
| monthCell                 | `.mantine-DatePicker-monthCell`                 | TD element of month table                      |
| month                     | `.mantine-DatePicker-month`                     | Month table element                            |
| weekdaysRow               | `.mantine-DatePicker-weekdaysRow`               | Weekdays TR element                            |
| weekday                   | `.mantine-DatePicker-weekday`                   | Weekday TH element                             |
| day                       | `.mantine-DatePicker-day`                       | Month day control                              |
| weekNumber                | `.mantine-DatePicker-weekNumber`                | Week number TD element                         |



#### DatePicker Data Attributes

| Selector              | Attribute             | Condition                                    | Value                    |
| --------------------- | --------------------- | -------------------------------------------- | ------------------------ |
| calendarHeaderControl | `data-direction`      | –                                            | `"previous"` or `"next"` |
| calendarHeaderControl | `data-disabled`       | Control is disabled                          | –                        |
| monthCell             | `data-with-spacing`   | `withCellSpacing` prop is set                | –                        |
| day                   | `data-today`          | Date is today (`new Date()`)                 | –                        |
| day                   | `data-hidden`         | Outside current month and `hideOutsideDates` | –                        |
| day                   | `data-disabled`       | Disabled by props (e.g., `excludeDate`)      | –                        |
| day                   | `data-weekend`        | Day is weekend                               | –                        |
| day                   | `data-outside`        | Day is outside of current month              | –                        |
| day                   | `data-selected`       | Day is selected                              | –                        |
| day                   | `data-in-range`       | Day is in selected range                     | –                        |
| day                   | `data-first-in-range` | First day in selected range                  | –                        |
| day                   | `data-last-in-range`  | Last day in selected range                   | –                        |


### Keyword Arguments

#### DatePicker

.. kwargs::DatePicker

