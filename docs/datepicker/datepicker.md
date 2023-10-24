---
name: DatePicker
description: Inline date, multiple dates and dates range picker. Helps you easily switch between different months, years along with locale support.
endpoint: /components/datapicker
package: dash_mantine_components
---

.. toc::

.. admonition::Note
    :color: yellow
    :icon: radix-icons:info-circled
    To include an Input field for the DatePicker, use DatePickerInput.  The DatePickerInput supports all props for DatePicker shown on this page.

### Simple Example

.. exec::docs.datepicker.simple




### Allow deselect
Set `allowDeselect` to allow user to deselect current selected date by clicking on it. `allowDeselect` is disregarded when type prop is range or multiple. When date is deselected the `value` will be None.


.. exec::docs.datepicker.deselect



### Multiple dates
Set type="multiple" to allow user to pick multiple dates.

.. exec::docs.datepicker.multiple


### Dates range
Set type="range" to allow user to pick dates range:

.. exec::docs.datepicker.range

### Disabled dates
Use the `disabledDates` prop to specify days that should be disabled.

.. exec::docs.datepicker.disabled_dates

### Single date in range
By default, it is not allowed to select single date as range – when user clicks the same date second time it is deselected. To change this behavior set `allowSingleDateInRange` prop. `allowSingleDateInRange` is ignored when `type` prop is not `range`.

.. exec::docs.datepicker.range_single

### Level
Set `level` prop to configure initial level that will be displayed.

.. exec::docs.datepicker.default_level

### Hide outside dates
Set `hideOutsideDates` prop to remove all dates that do not belong to the current month.

.. exec::docs.datepicker.hide_outside

### First day of week
Set `firstDayOfWeek` prop to configure first day of week. The prop accepts number from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is 1 – Monday. You can also configure this option for all components with DatesProvider.

.. exec::docs.datepicker.first_day_of_week

### Hide weekdays
Set `hideWeekdays` prop to hide weekdays names.

.. exec::docs.datepicker.hide_weekdays

### Weekend days
Use `weekendDays` prop to configure weekend days. The prop accepts an array of numbers from 0 to 6, where 0 is Sunday and 6 is Saturday. Default value is [0, 6] – Saturday and Sunday. You can also configure this option for all components with DatesProvider.

.. exec::docs.datepicker.weekend_days

### Min and max date
Set `minDate` and `maxDate` props to define min and max dates. If previous/next page is not available then corresponding control will be disabled.


.. exec::docs.datepicker.min_max


### Number of columns

Set `numberOfColumns` prop to define number of pickers that will be rendered side by side.

.. exec::docs.datepicker.amount

### Max level
Use the `maxLevel` prop to set the max level that user can go up to (decade, year, month), defaults to decade.

.. exec::docs.datepicker.max_level

### Size

.. exec::docs.datepicker.size
    :code: false

### Change year and months controls format
Use `yearsListFormat` and `monthsListFormat` props to change [dayjs](https://day.js.org/docs/en/display/format) format of year/month controls:

.. exec::docs.datepicker.year_month_controls

### Change label format
Use decadeLabelFormat, yearLabelFormat and monthLabelFormat props to change [dayjs](https://day.js.org/docs/en/display/format) format of decade/year label:


.. exec::docs.datepicker.label_format

### Localization

DatePickerInput component uses `dayjs` behind the scenes. So you can easily customize locale by including required locale data
and setting the `locale` prop. Make sure to include proper localization file from `dayjs` library.

Wrap the DatePickerInput with the DatesProvider.  See the DatesProvider component for more details.

```python
from dash import Dash

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/fr.min.js",
]

app = Dash(__name__, external_scripts=scripts)
```

.. exec::docs.datepicker.locale



### Keyword Arguments

#### DatePicker

.. kwargs::DatePicker
