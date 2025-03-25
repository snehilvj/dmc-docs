---
name: DateInput
description: Free form date input
endpoint: /components/dateinput
package: dash_mantine_components
category: Date Pickers
---

.. toc::



### CSS Extensions

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   Date components require additional CSS styles.

The Date components require an additional CSS stylesheet.  See the [Getting Started](/getting-started) section for more information.

Be sure to include:
```python
app = Dash(external_stylesheets=[dmc.styles.DATES])
```
Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```


### DateInput props

DateInput supports most of the [DatePicker](/components/datepicker) props, read through DatePicker
documentation to learn about all component features that are not listed on this page.

### Simple Example

This is a simple example of DateInput tied to a callback. You can type a date or select from the DatePicker

.. exec::docs.dateinput.simple

### Value format

Use `format` property to change the format of the date displayed in the date input field.

.. exec::docs.dateinput.formats

Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label.


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

### Styles API


.. styles_api_text::

| Name                      | Static selector                              | Description                                                          |
|:--------------------------|:---------------------------------------------|:---------------------------------------------------------------------|
| wrapper                   | .mantine-DateInput-wrapper                   | Root element of the Input                                            |
| input                     | .mantine-DateInput-input                     | Input element                                                        |
| section                   | .mantine-DateInput-section                   | Left and right sections                                              |
| root                      | .mantine-DateInput-root                      | Root element                                                         |
| label                     | .mantine-DateInput-label                     | Label element                                                        |
| required                  | .mantine-DateInput-required                  | Required asterisk element, rendered inside label                     |
| description               | .mantine-DateInput-description               | Description element                                                  |
| error                     | .mantine-DateInput-error                     | Error element                                                        |
| calendarHeader            | .mantine-DateInput-calendarHeader            | Calendar header root element                                         |
| calendarHeaderControl     | .mantine-DateInput-calendarHeaderControl     | Previous/next calendar header controls                               |
| calendarHeaderControlIcon | .mantine-DateInput-calendarHeaderControlIcon | Icon of previous/next calendar header controls                       |
| calendarHeaderLevel       | .mantine-DateInput-calendarHeaderLevel       | Level control (changes levels when clicked, month -> year -> decade) |
| levelsGroup               | .mantine-DateInput-levelsGroup               | Group of decades levels                                              |
| yearsList                 | .mantine-DateInput-yearsList                 | Years list table element                                             |
| yearsListRow              | .mantine-DateInput-yearsListRow              | Years list row element                                               |
| yearsListCell             | .mantine-DateInput-yearsListCell             | Years list cell element                                              |
| yearsListControl          | .mantine-DateInput-yearsListControl          | Button used to pick months and years                                 |
| monthsList                | .mantine-DateInput-monthsList                | Years list table element                                             |
| monthsListRow             | .mantine-DateInput-monthsListRow             | Years list row element                                               |
| monthsListCell            | .mantine-DateInput-monthsListCell            | Years list cell element                                              |
| monthsListControl         | .mantine-DateInput-monthsListControl         | Button used to pick months and years                                 |
| monthThead                | .mantine-DateInput-monthThead                | thead element of month table                                         |
| monthRow                  | .mantine-DateInput-monthRow                  | tr element of month table                                            |
| monthTbody                | .mantine-DateInput-monthTbody                | tbody element of month table                                         |
| monthCell                 | .mantine-DateInput-monthCell                 | td element of month table                                            |
| month                     | .mantine-DateInput-month                     | Month table element                                                  |
| weekdaysRow               | .mantine-DateInput-weekdaysRow               | Weekdays tr element                                                  |
| weekday                   | .mantine-DateInput-weekday                   | Weekday th element                                                   |
| day                       | .mantine-DateInput-day                       | Month day control                                                    |

### Keyword Arguments

#### DateInput

.. kwargs::DateInput
