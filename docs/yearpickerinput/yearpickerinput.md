---
name: YearPickerInput
description: Year, multiple years and years range picker input
endpoint: /components/yearpickerinput
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::YearPickerInput




### Simple Example

.. exec::docs.yearpickerinput.simple

### Multiple dates

Set type="multiple" to allow user to pick multiple months.  Note that `value` is a list.

.. exec::docs.yearpickerinput.multiple

### Dates range

Set type="range" to allow user to pick dates range. Note that `value` is a list.

.. exec::docs.yearpickerinput.range

### Presets
Use the `presets` prop to add custom year presets. Presets are displayed next to the calendar:

.. exec::docs.yearpickerinput.presets

To use `presets` with `type="range"`, define the value as a tuple of two dates:

.. exec::docs.yearpickerinput.presets_range

### Open picker in modal

By default, YearPickerInput is rendered inside Popover. You can change that to Modal by setting dropdownType="modal"

.. exec::docs.yearpickerinput.modal

### Number of columns

.. exec::docs.yearpickerinput.columns

### Value format

Use `valueFormat` property to change the format of the date displayed in the date input field.

.. exec::docs.yearpickerinput.valueformat

Use `valueFormat` prop to change [dayjs format](https://day.js.org/docs/en/display/format) of value label.



### Value formatter
`valueFormatter` is a more powerful alternative to the `valueFormat` prop. It allows formatting the value label with a
custom function. The function is the same for all component types (default, multiple and range) – you need to perform
additional checks inside the function to handle different types.

Example of using a custom formatter function with `type="multiple"`:


.. functions_as_props::  


.. exec::docs.yearpickerinput.valueformatter
    :code: false

.. sourcetabs::docs/yearpickerinput/valueformatter.py, assets/examples-js/format-dates-selected.js
    :defaultExpanded: true
    :withExpandedButton: true

### Clearable

Set `clearable=True` prop to display clear button in the right section. Note that if you set `rightSection` prop, clear button will not be displayed.

.. exec::docs.yearpickerinput.clearable


### Clear section mode
The `clearSectionMode` prop determines how the `clear` button and `rightSection` are rendered:

- 'both' (default) – render both the `clear` button and `rightSection`
- 'rightSection' – render only the user-supplied `rightSection`, ignore `clear` button
- 'clear' – render only the `clear` button, ignore `rightSection`


.. exec::docs.yearpickerinput.clear_section_mode


### With Icon

.. exec::docs.yearpickerinput.icon

### Min and Max date

.. exec::docs.yearpickerinput.minmax


### CSS Extensions

As of DMC 1.2.0, Date component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.

### Styles API

.. styles_api_text::

#### YearPickerInput selectors

| Selector                   | Static selector                                      | Description                                                           |
| ---------------------------| ---------------------------------------------------- | --------------------------------------------------------------------- |
| `wrapper`                  | `.mantine-YearPickerInput-wrapper`                   | Root element of the Input                                              |
| `input`                    | `.mantine-YearPickerInput-input`                     | Input element                                                         |
| `section`                  | `.mantine-YearPickerInput-section`                   | Left and right sections                                                |
| `root`                     | `.mantine-YearPickerInput-root`                      | Root element                                                          |
| `label`                    | `.mantine-YearPickerInput-label`                     | Label element                                                         |
| `required`                 | `.mantine-YearPickerInput-required`                  | Required asterisk element, rendered inside label                       |
| `description`              | `.mantine-YearPickerInput-description`               | Description element                                                    |
| `error`                    | `.mantine-YearPickerInput-error`                     | Error element                                                         |
| `calendarHeader`           | `.mantine-YearPickerInput-calendarHeader`            | Calendar header root element                                           |
| `calendarHeaderControl`     | `.mantine-YearPickerInput-calendarHeaderControl`     | Previous/next calendar header controls                                 |
| `calendarHeaderControlIcon` | `.mantine-YearPickerInput-calendarHeaderControlIcon` | Icon of previous/next calendar header controls                         |
| `calendarHeaderLevel`       | `.mantine-YearPickerInput-calendarHeaderLevel`       | Level control (changes levels when clicked, month -> year -> decade)   |
| `levelsGroup`              | `.mantine-YearPickerInput-levelsGroup`               | Group of decades levels                                                |
| `yearsList`                | `.mantine-YearPickerInput-yearsList`                 | Years list table element                                               |
| `yearsListRow`             | `.mantine-YearPickerInput-yearsListRow`              | Years list row element                                                 |
| `yearsListCell`            | `.mantine-YearPickerInput-yearsListCell`             | Years list cell element                                                |
| `yearsListControl`         | `.mantine-YearPickerInput-yearsListControl`          | Button used to pick months and years                                   |
| `placeholder`              | `.mantine-YearPickerInput-placeholder`               | Placeholder element                                                    |

#### YearPickerInput data attributes

| Selector              | Attribute      | Condition                           | Value                              |
| --------------------- | -------------- | ----------------------------------- | ---------------------------------- |
| `calendarHeaderControl`| `data-direction`| –                                   | "previous" or "next" depending on the control type |
| `calendarHeaderControl`| `data-disabled`| Control is disabled for any reason  | –                                  |


### Keyword Arguments
.. style_props_text::

#### YearPickerInput

.. kwargs::YearPickerInput
