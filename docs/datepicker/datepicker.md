---
name: DatePicker
description: Date, multiple dates and dates range picker input. Helps you easily switch between different months, years along with locale support.
endpoint: /components/datepicker
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
app = Dash(external_stylesheets=dmc.styles.DATES)
```
Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```


### Simple Example

This is a simple example of DatePicker tied to a callback. You can either use strings in a valid datetime format such
as `YYYY-MM-DD` or use the date object from datetime library.

.. exec::docs.datepicker.simple

### Multiple dates

Set type="multiple" to allow user to pick multiple dates.  Note that `value` is a list.

.. exec::docs.datepicker.multiple

### Dates range

Set type="range" to allow user to pick dates range. Note that `value` is a list.

.. exec::docs.datepicker.range

### Open picker in modal

By default, DatePicker is rendered inside Popover. You can change that to Modal by setting dropdownType="modal"

.. exec::docs.datepicker.modal

### Number of columns

.. exec::docs.datepicker.columns

### Value format

Use `format` property to change the format of the date displayed in the date input field.

.. exec::docs.datepicker.formats

Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label.

### Clearable

Set `clearable=True` prop to display clear button in the right section. Note that if you set `rightSection` prop, clear button will not be displayed.

.. exec::docs.datepicker.clearable

### Error Display

You can convey errors in your date picker by setting the `error` prop. For instance, in the below example we try to
convey the user that it's a required field and the date can't be an odd date. Since it's a required field, we also
set `clearable=False`.

.. exec::docs.datepicker.errors

### Localization

For information on setting locale, have a look at the [DatesProvider](/components/datesprovider) component.

### Styles API

| Name                      | Static selector                                    | Description                                                          |
|:--------------------------|:---------------------------------------------------|:---------------------------------------------------------------------|
| wrapper                   | .mantine-DatePickerInput-wrapper                   | Root element of the Input                                            |
| input                     | .mantine-DatePickerInput-input                     | Input element                                                        |
| section                   | .mantine-DatePickerInput-section                   | Left and right sections                                              |
| root                      | .mantine-DatePickerInput-root                      | Root element                                                         |
| label                     | .mantine-DatePickerInput-label                     | Label element                                                        |
| required                  | .mantine-DatePickerInput-required                  | Required asterisk element, rendered inside label                     |
| description               | .mantine-DatePickerInput-description               | Description element                                                  |
| error                     | .mantine-DatePickerInput-error                     | Error element                                                        |
| calendarHeader            | .mantine-DatePickerInput-calendarHeader            | Calendar header root element                                         |
| calendarHeaderControl     | .mantine-DatePickerInput-calendarHeaderControl     | Previous/next calendar header controls                               |
| calendarHeaderControlIcon | .mantine-DatePickerInput-calendarHeaderControlIcon | Icon of previous/next calendar header controls                       |
| calendarHeaderLevel       | .mantine-DatePickerInput-calendarHeaderLevel       | Level control (changes levels when clicked, month -> year -> decade) |
| levelsGroup               | .mantine-DatePickerInput-levelsGroup               | Group of decades levels                                              |
| yearsList                 | .mantine-DatePickerInput-yearsList                 | Years list table element                                             |
| yearsListRow              | .mantine-DatePickerInput-yearsListRow              | Years list row element                                               |
| yearsListCell             | .mantine-DatePickerInput-yearsListCell             | Years list cell element                                              |
| yearsListControl          | .mantine-DatePickerInput-yearsListControl          | Button used to pick months and years                                 |
| monthsList                | .mantine-DatePickerInput-monthsList                | Years list table element                                             |
| monthsListRow             | .mantine-DatePickerInput-monthsListRow             | Years list row element                                               |
| monthsListCell            | .mantine-DatePickerInput-monthsListCell            | Years list cell element                                              |
| monthsListControl         | .mantine-DatePickerInput-monthsListControl         | Button used to pick months and years                                 |
| monthThead                | .mantine-DatePickerInput-monthThead                | thead element of month table                                         |
| monthRow                  | .mantine-DatePickerInput-monthRow                  | tr element of month table                                            |
| monthTbody                | .mantine-DatePickerInput-monthTbody                | tbody element of month table                                         |
| monthCell                 | .mantine-DatePickerInput-monthCell                 | td element of month table                                            |
| month                     | .mantine-DatePickerInput-month                     | Month table element                                                  |
| weekdaysRow               | .mantine-DatePickerInput-weekdaysRow               | Weekdays tr element                                                  |
| weekday                   | .mantine-DatePickerInput-weekday                   | Weekday th element                                                   |
| day                       | .mantine-DatePickerInput-day                       | Month day control                                                    |
| placeholder               | .mantine-DatePickerInput-placeholder               | Placeholder element                                                  |

### Keyword Arguments

#### DatePicker

.. kwargs::DatePicker
