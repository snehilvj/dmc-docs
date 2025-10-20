---
name: MonthPickerInput
description: Month, multiple months and months range picker input
endpoint: /components/monthpickerinput
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::MonthPickerInput



### Simple Example

.. exec::docs.monthpickerinput.simple

### Multiple dates

Set type="multiple" to allow user to pick multiple months.  Note that `value` is a list.

.. exec::docs.monthpickerinput.multiple

### Dates range

Set type="range" to allow user to pick dates range. Note that `value` is a list.

.. exec::docs.monthpickerinput.range

### Open picker in modal

By default, MonthPickerInput is rendered inside Popover. You can change that to Modal by setting dropdownType="modal"

.. exec::docs.monthpickerinput.modal

### Number of columns

.. exec::docs.monthpickerinput.columns

### Value format

Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label.

.. exec::docs.monthpickerinput.valueformat


### Clearable

Set `clearable=True` prop to display clear button in the right section. Note that if you set `rightSection` prop, clear button will not be displayed.

.. exec::docs.monthpickerinput.clearable


### With Icon

.. exec::docs.monthpickerinput.icon


### Min and Max Date

.. exec::docs.monthpickerinput.minmax


### CSS Extensions

As of DMC 1.2.0, Date component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.



### Styles API

.. styles_api_text::

#### MonthPickerInput selectors

| Selector                   | Static selector                                        | Description                                                           |
| ---------------------------| ------------------------------------------------------ | --------------------------------------------------------------------- |
| `wrapper`                  | `.mantine-MonthPickerInput-wrapper`                    | Root element of the Input                                              |
| `input`                    | `.mantine-MonthPickerInput-input`                      | Input element                                                         |
| `section`                  | `.mantine-MonthPickerInput-section`                    | Left and right sections                                                |
| `root`                     | `.mantine-MonthPickerInput-root`                       | Root element                                                          |
| `label`                    | `.mantine-MonthPickerInput-label`                      | Label element                                                         |
| `required`                 | `.mantine-MonthPickerInput-required`                   | Required asterisk element, rendered inside label                       |
| `description`              | `.mantine-MonthPickerInput-description`                | Description element                                                    |
| `error`                    | `.mantine-MonthPickerInput-error`                      | Error element                                                         |
| `calendarHeader`           | `.mantine-MonthPickerInput-calendarHeader`             | Calendar header root element                                           |
| `calendarHeaderControl`     | `.mantine-MonthPickerInput-calendarHeaderControl`      | Previous/next calendar header controls                                 |
| `calendarHeaderControlIcon` | `.mantine-MonthPickerInput-calendarHeaderControlIcon`  | Icon of previous/next calendar header controls                         |
| `calendarHeaderLevel`       | `.mantine-MonthPickerInput-calendarHeaderLevel`        | Level control (changes levels when clicked, month -> year -> decade)   |
| `levelsGroup`              | `.mantine-MonthPickerInput-levelsGroup`                | Group of decades levels                                                |
| `yearsList`                | `.mantine-MonthPickerInput-yearsList`                  | Years list table element                                               |
| `yearsListRow`             | `.mantine-MonthPickerInput-yearsListRow`               | Years list row element                                                 |
| `yearsListCell`            | `.mantine-MonthPickerInput-yearsListCell`              | Years list cell element                                                |
| `yearsListControl`         | `.mantine-MonthPickerInput-yearsListControl`           | Button used to pick months and years                                   |
| `monthsList`               | `.mantine-MonthPickerInput-monthsList`                 | Years list table element                                               |
| `monthsListRow`            | `.mantine-MonthPickerInput-monthsListRow`              | Years list row element                                                 |
| `monthsListCell`           | `.mantine-MonthPickerInput-monthsListCell`             | Years list cell element                                                |
| `monthsListControl`        | `.mantine-MonthPickerInput-monthsListControl`          | Button used to pick months and years                                   |
| `placeholder`              | `.mantine-MonthPickerInput-placeholder`                | Placeholder element                                                    |

#### MonthPickerInput data attributes

| Selector              | Attribute      | Condition                           | Value                              |
| --------------------- | -------------- | ----------------------------------- | ---------------------------------- |
| `calendarHeaderControl`| `data-direction`| –                                   | "previous" or "next" depending on the control type |
| `calendarHeaderControl`| `data-disabled`| Control is disabled for any reason  | –                                  |


### Keyword Arguments
.. style_props_text::

#### MonthPickerInput

.. kwargs::MonthPickerInput
