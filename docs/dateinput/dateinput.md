---
name: DateInput
description: Free form date input
endpoint: /components/dateinput
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::DateInput


### DateInput props

DateInput supports most of the [DatePicker](/components/datepicker) props, read through DatePicker
documentation to learn about all component features that are not listed on this page.

### Simple Example

This is a simple example of DateInput tied to a callback. You can type a date or select from the DatePicker

.. exec::docs.dateinput.simple

### Value format


Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label displayed in the input field.

.. exec::docs.dateinput.formats


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


### CSS Extensions

As of DMC 1.2.0, Date component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.



### Styles API


.. styles_api_text::

#### DateInput selectors

| Selector                  | Static selector                                | Description                                                        |
| ------------------------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| wrapper                   | `.mantine-DateInput-wrapper`                   | Root element of the Input                                          |
| input                     | `.mantine-DateInput-input`                     | Input element                                                      |
| section                   | `.mantine-DateInput-section`                   | Left and right sections                                            |
| root                      | `.mantine-DateInput-root`                      | Root element                                                       |
| label                     | `.mantine-DateInput-label`                     | Label element                                                      |
| required                  | `.mantine-DateInput-required`                  | Required asterisk element, rendered inside label                   |
| description               | `.mantine-DateInput-description`               | Description element                                                |
| error                     | `.mantine-DateInput-error`                     | Error element                                                      |
| calendarHeader            | `.mantine-DateInput-calendarHeader`            | Calendar header root element                                       |
| calendarHeaderControl     | `.mantine-DateInput-calendarHeaderControl`     | Previous/next calendar header controls                             |
| calendarHeaderControlIcon | `.mantine-DateInput-calendarHeaderControlIcon` | Icon of previous/next calendar header controls                     |
| calendarHeaderLevel       | `.mantine-DateInput-calendarHeaderLevel`       | Level control (changes levels when clicked, month → year → decade) |
| levelsGroup               | `.mantine-DateInput-levelsGroup`               | Group of months levels                                             |
| yearsList                 | `.mantine-DateInput-yearsList`                 | Years list table element                                           |
| yearsListRow              | `.mantine-DateInput-yearsListRow`              | Years list row element                                             |
| yearsListCell             | `.mantine-DateInput-yearsListCell`             | Years list cell element                                            |
| yearsListControl          | `.mantine-DateInput-yearsListControl`          | Button used to pick months and years                               |
| monthsList                | `.mantine-DateInput-monthsList`                | Months list table element                                          |
| monthsListRow             | `.mantine-DateInput-monthsListRow`             | Months list row element                                            |
| monthsListCell            | `.mantine-DateInput-monthsListCell`            | Months list cell element                                           |
| monthsListControl         | `.mantine-DateInput-monthsListControl`         | Button used to pick months and years                               |
| monthThead                | `.mantine-DateInput-monthThead`                | `thead` element of month table                                     |
| monthRow                  | `.mantine-DateInput-monthRow`                  | `tr` element of month table                                        |
| monthTbody                | `.mantine-DateInput-monthTbody`                | `tbody` element of month table                                     |
| monthCell                 | `.mantine-DateInput-monthCell`                 | `td` element of month table                                        |
| month                     | `.mantine-DateInput-month`                     | Month table element                                                |
| weekdaysRow               | `.mantine-DateInput-weekdaysRow`               | Weekdays `tr` element                                              |
| weekday                   | `.mantine-DateInput-weekday`                   | Weekday `th` element                                               |
| day                       | `.mantine-DateInput-day`                       | Month day control                                                  |
| weekNumber                | `.mantine-DateInput-weekNumber`                | Week number `td` element                                           |
| datePickerRoot            | `.mantine-DateInput-datePickerRoot`            | Date picker root element, contains calendar and presets            |
| presetsList               | `.mantine-DateInput-presetsList`               | Presets wrapper element                                            |
| presetButton              | `.mantine-DateInput-presetButton`              | Preset button                                                      |



#### DateInput data attributes

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

#### DateInput

.. kwargs::DateInput
