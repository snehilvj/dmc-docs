---
name: DateTimePicker
description: Capture datetime from the user
endpoint: /components/datetimepicker
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::DateTimePicker



### DatePicker props
`DateTimePicker` supports most of the `DatePicker` props, read through `DatePicker` documentation to learn about all component features that are not listed on this page.

### Simple Example

.. exec::docs.datetimepicker.simple

### With Seconds


.. exec::docs.datetimepicker.seconds

### Presets

Use `presets` prop to add custom date presets. Presets are displayed next to the calendar:

.. exec::docs.datetimepicker.presets

### TimePicker props
You can pass props down to the underlying `TimePicker` component with `timePickerProps` prop. Example of enabling 
dropdown and setting 12h format for time picker:

.. exec::docs.datetimepicker.time-picker-props

### Value format

Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label.

.. exec::docs.datetimepicker.valueformat

### Disabled state

.. exec::docs.datetimepicker.disabled


### Input props

.. exec::docs.datetimepicker.interactive
   :code:  false


### Clearable

Set `clearable=True` prop to display clear button in the right section. Note that if you set `rightSection` prop, clear button will not be displayed.

.. exec::docs.datetimepicker.clearable


### Open picker in modal

By default, `DateTimePicker` is rendered inside `Popover`. You can change that to `Modal` by setting `dropdownType="modal"`

.. exec::docs.datetimepicker.modal




### CSS Extensions

As of DMC 1.2.0, Date component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.




### Styles API

.. styles_api_text::

#### DateTimePicker selectors

| Selector                    | Static selector                               | Description                                                 |
|-----------------------------|-----------------------------------------------|-------------------------------------------------------------|
| wrapper                     | .mantine-DateTimePicker-wrapper               | Root element of the Input                                   |
| input                       | .mantine-DateTimePicker-input                 | Input element                                               |
| section                     | .mantine-DateTimePicker-section               | Left and right sections                                     |
| root                        | .mantine-DateTimePicker-root                  | Root element                                                |
| label                       | .mantine-DateTimePicker-label                 | Label element                                               |
| required                    | .mantine-DateTimePicker-required              | Required asterisk element, rendered inside label            |
| description                 | .mantine-DateTimePicker-description           | Description element                                         |
| error                       | .mantine-DateTimePicker-error                 | Error element                                               |
| calendarHeader              | .mantine-DateTimePicker-calendarHeader        | Calendar header root element                                |
| calendarHeaderControl       | .mantine-DateTimePicker-calendarHeaderControl | Previous/next calendar header controls                      |
| calendarHeaderControlIcon   | .mantine-DateTimePicker-calendarHeaderControlIcon | Icon of previous/next calendar header controls           |
| calendarHeaderLevel         | .mantine-DateTimePicker-calendarHeaderLevel   | Level control (changes levels when clicked, month -> year -> decade) |
| levelsGroup                 | .mantine-DateTimePicker-levelsGroup           | Group of months levels                                      |
| yearsList                   | .mantine-DateTimePicker-yearsList             | Years list table element                                    |
| yearsListRow                | .mantine-DateTimePicker-yearsListRow          | Years list row element                                      |
| yearsListCell               | .mantine-DateTimePicker-yearsListCell         | Years list cell element                                     |
| yearsListControl            | .mantine-DateTimePicker-yearsListControl      | Button used to pick months and years                        |
| monthsList                  | .mantine-DateTimePicker-monthsList            | Months list table element                                   |
| monthsListRow               | .mantine-DateTimePicker-monthsListRow         | Months list row element                                     |
| monthsListCell              | .mantine-DateTimePicker-monthsListCell        | Months list cell element                                    |
| monthsListControl           | .mantine-DateTimePicker-monthsListControl     | Button used to pick months and years                        |
| monthThead                  | .mantine-DateTimePicker-monthThead            | thead element of month table                                |
| monthRow                    | .mantine-DateTimePicker-monthRow              | tr element of month table                                   |
| monthTbody                  | .mantine-DateTimePicker-monthTbody            | tbody element of month table                                |
| monthCell                   | .mantine-DateTimePicker-monthCell             | td element of month table                                   |
| month                       | .mantine-DateTimePicker-month                 | Month table element                                         |
| weekdaysRow                 | .mantine-DateTimePicker-weekdaysRow           | Weekdays tr element                                         |
| weekday                     | .mantine-DateTimePicker-weekday               | Weekday th element                                          |
| day                         | .mantine-DateTimePicker-day                   | Month day control                                           |
| timeWrapper                 | .mantine-DateTimePicker-timeWrapper           | Wrapper around time input and submit button                 |
| timeInput                   | .mantine-DateTimePicker-timeInput             | TimeInput                                                   |
| submitButton                | .mantine-DateTimePicker-submitButton          | Submit button                                               |

#### DateTimePicker data attributes

| Selector              | Attribute          | Condition                                                | Value                                        |
|-----------------------|--------------------|----------------------------------------------------------|----------------------------------------------|
| calendarHeaderControl  | data-direction     | –                                                        | "previous" or "next" depending on the control type |
| calendarHeaderControl  | data-disabled      | Control is disabled for any reason                        | –                                            |
| monthCell             | data-with-spacing  | `withCellSpacing` prop is set                             | –                                            |
| day                   | data-today         | Date is the same as `new Date()`                          | –                                            |
| day                   | data-hidden        | Day is outside of current month and `hideOutsideDates` is set | –                                         |
| day                   | data-disabled      | Day disabled by one of the props (`excludeDate`, `getDayProps`, etc.) | –                                      |
| day                   | data-weekend       | Day is weekend                                            | –                                            |
| day                   | data-outside       | Day is outside of the current month                       | –                                            |
| day                   | data-selected      | Day is selected                                           | –                                            |
| day                   | data-in-range      | Day is in range selection                                 | –                                            |
| day                   | data-first-in-range| Day is first in range selection                           | –                                            |
| day                   | data-last-in-range | Day is last in range selection                            | –                                            |



### Keyword Arguments
.. style_props_text::

#### DateTimePicker

.. kwargs::DateTimePicker
