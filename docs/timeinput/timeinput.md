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

### Input Props

TimeInput supports all props from Input and InputWrapper components such as `radius`, `size`, `required`, etc.

.. exec::docs.timeinput.interactive
    :code: false

### Invalid State And Error

You can display an error with a red border and add an error message.

.. exec::docs.timeinput.error

### Styles API

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
