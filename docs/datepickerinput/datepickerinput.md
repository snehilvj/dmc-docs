---
name: DatePickerInput
description: Date, multiple dates and dates range picker input. Helps you easily switch between different months, years along with locale support.
endpoint: /components/datepickerinput
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::DatePickerInput

### Simple Example

This is a simple example of `DatePickerInput` tied to a callback. You can either use strings in a valid datetime format such
as `YYYY-MM-DD` or use the date object from datetime library.

> If you would like to enable the user to type a date manually into the input field, please use the `DateInput` component

.. exec::docs.datepickerinput.simple

### Multiple dates

Set type="multiple" to allow user to pick multiple dates.  Note that `value` is a list.

.. exec::docs.datepickerinput.multiple

### Dates range

Set type="range" to allow user to pick dates range. Note that `value` is a list.

.. exec::docs.datepickerinput.range

### Presets

Use `presets` prop to add custom date presets. Presets are displayed next to the calendar:

.. exec::docs.datepickerinput.presets

To use `presets` with `type="range"`, define value a tuple of two dates:

.. exec::docs.datepickerinput.presetsrange

### Open picker in modal

By default, `DatePickerInput` is rendered inside `Popover`. You can change that to `Modal` by setting `dropdownType="modal"`

.. exec::docs.datepickerinput.modal

### Number of columns

.. exec::docs.datepickerinput.columns

### Value format

Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label.

.. exec::docs.datepickerinput.formats


### Clearable

Set `clearable=True` prop to display clear button in the right section. Note that if you set `rightSection` prop, clear button will not be displayed.

.. exec::docs.datepickerinput.clearable

### Error Display

You can convey errors in your date picker by setting the `error` prop. For instance, in the below example we try to
convey the user that it's a required field and the date can't be an odd date. Since it's a required field, we also
set `clearable=False`.

.. exec::docs.datepickerinput.errors

### Localization

For information on setting locale, have a look at the [DatesProvider](/components/datesprovider) component.


### CSS Extensions

As of DMC 1.2.0, Date component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.

### Styles API

.. styles_api_text::


#### DatePickerInput selectors

| Selector                  | Static selector                                      | Description                                                        |
| ------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------ |
| wrapper                   | `.mantine-DatePickerInput-wrapper`                   | Root element of the Input                                          |
| input                     | `.mantine-DatePickerInput-input`                     | Input element                                                      |
| section                   | `.mantine-DatePickerInput-section`                   | Left and right sections                                            |
| root                      | `.mantine-DatePickerInput-root`                      | Root element                                                       |
| label                     | `.mantine-DatePickerInput-label`                     | Label element                                                      |
| required                  | `.mantine-DatePickerInput-required`                  | Required asterisk element, rendered inside label                   |
| description               | `.mantine-DatePickerInput-description`               | Description element                                                |
| error                     | `.mantine-DatePickerInput-error`                     | Error element                                                      |
| calendarHeader            | `.mantine-DatePickerInput-calendarHeader`            | Calendar header root element                                       |
| calendarHeaderControl     | `.mantine-DatePickerInput-calendarHeaderControl`     | Previous/next calendar header controls                             |
| calendarHeaderControlIcon | `.mantine-DatePickerInput-calendarHeaderControlIcon` | Icon of previous/next calendar header controls                     |
| calendarHeaderLevel       | `.mantine-DatePickerInput-calendarHeaderLevel`       | Level control (changes levels when clicked, month → year → decade) |
| levelsGroup               | `.mantine-DatePickerInput-levelsGroup`               | Group of months levels                                             |
| yearsList                 | `.mantine-DatePickerInput-yearsList`                 | Years list table element                                           |
| yearsListRow              | `.mantine-DatePickerInput-yearsListRow`              | Years list row element                                             |
| yearsListCell             | `.mantine-DatePickerInput-yearsListCell`             | Years list cell element                                            |
| yearsListControl          | `.mantine-DatePickerInput-yearsListControl`          | Button used to pick months and years                               |
| monthsList                | `.mantine-DatePickerInput-monthsList`                | Months list table element                                          |
| monthsListRow             | `.mantine-DatePickerInput-monthsListRow`             | Months list row element                                            |
| monthsListCell            | `.mantine-DatePickerInput-monthsListCell`            | Months list cell element                                           |
| monthsListControl         | `.mantine-DatePickerInput-monthsListControl`         | Button used to pick months and years                               |
| monthThead                | `.mantine-DatePickerInput-monthThead`                | `thead` element of month table                                     |
| monthRow                  | `.mantine-DatePickerInput-monthRow`                  | `tr` element of month table                                        |
| monthTbody                | `.mantine-DatePickerInput-monthTbody`                | `tbody` element of month table                                     |
| monthCell                 | `.mantine-DatePickerInput-monthCell`                 | `td` element of month table                                        |
| month                     | `.mantine-DatePickerInput-month`                     | Month table element                                                |
| weekdaysRow               | `.mantine-DatePickerInput-weekdaysRow`               | Weekdays `tr` element                                              |
| weekday                   | `.mantine-DatePickerInput-weekday`                   | Weekday `th` element                                               |
| day                       | `.mantine-DatePickerInput-day`                       | Month day control                                                  |
| weekNumber                | `.mantine-DatePickerInput-weekNumber`                | Week number `td` element                                           |
| datePickerRoot            | `.mantine-DatePickerInput-datePickerRoot`            | Date picker root element, contains calendar and presets            |
| presetsList               | `.mantine-DatePickerInput-presetsList`               | Presets wrapper element                                            |
| presetButton              | `.mantine-DatePickerInput-presetButton`              | Preset button                                                      |
| placeholder               | `.mantine-DatePickerInput-placeholder`               | Placeholder element                                                |



#### DatePickerInput data attributes

| Selector              | Attribute             | Condition                                                             | Value                                                  |
| --------------------- | --------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
| calendarHeaderControl | `data-direction`      | –                                                                     | `"previous"` or `"next"` depending on the control type |
| calendarHeaderControl | `data-disabled`       | Control is disabled for any reason                                    | –                                                      |
| monthCell             | `data-with-spacing`   | `withCellSpacing` prop is set                                         | –                                                      |
| day                   | `data-today`          | Date is the same as `new Date()`                                      | –                                                      |
| day                   | `data-hidden`         | Day is outside of current month and `hideOutsideDates` is set         | –                                                      |
| day                   | `data-disabled`       | Day disabled by one of the props (`excludeDate`, `getDayProps`, etc.) | –                                                      |
| day                   | `data-weekend`        | Day is weekend                                                        | –                                                      |
| day                   | `data-outside`        | Day is outside of the current month                                   | –                                                      |
| day                   | `data-selected`       | Day is selected                                                       | –                                                      |
| day                   | `data-in-range`       | Day is in range selection                                             | –                                                      |
| day                   | `data-first-in-range` | Day is first in range selection                                       | –                                                      |
| day                   | `data-last-in-range`  | Day is last in range selection                                        | –                                                      |


### Keyword Arguments
.. style_props_text::

#### DatePickerInput

.. kwargs::DatePickerInput
