---
name: TimeInput
description: Use the TimeInput component to capture time input from user.
endpoint: /components/timeinput
package: dash_mantine_components
category: Date Pickers
---

.. toc::

### Simple Example

This is a simple example of the TimeInput. You can enter a valid time string such as hh:mm:ss.

Use the  `withSeconds` prop to display seconds.

.. exec::docs.timeinput.simple

### TimePicker component
TimeInput component is based on the native `input[type="time"]` element and does not support most of advanced features
like choosing time format or custom dropdown with time select. If you need more features, use [TimePicker](/components/timepicker) 
component instead.

`TimeInput` features/limitations:

- Native `input[type="time"]` element
- Native browser controls for time selection on mobile devices
- Time format depends on the user's locale
- Only native dropdown with hours/minutes/seconds, does not work in Firefox
- Mobile Safari does not provide an option to select seconds


### Input Props

TimeInput supports all props from Input and InputWrapper components such as `radius`, `size`, `required`, etc.

.. exec::docs.timeinput.interactive
    :code: false

### With icon


.. exec::docs.timeinput.icon

### Invalid State And Error

You can display an error with a red border and add an error message.

.. exec::docs.timeinput.error

### Styles API

.. styles_api_text::


| Name        | Static selector                | Description                                      |
|:------------|:-------------------------------|:-------------------------------------------------|
| wrapper     | .mantine-TimeInput-wrapper     | Root element of the Input                        |
| input       | .mantine-TimeInput-input       | Input element                                    |
| section     | .mantine-TimeInput-section     | Left and right sections                          |
| root        | .mantine-TimeInput-root        | Root element                                     |
| label       | .mantine-TimeInput-label       | Label element                                    |
| required    | .mantine-TimeInput-required    | Required asterisk element, rendered inside label |
| description | .mantine-TimeInput-description | Description element                              |
| error       | .mantine-TimeInput-error       | Error element                                    |

### Keyword Arguments

#### TimeInput

.. kwargs::TimeInput
