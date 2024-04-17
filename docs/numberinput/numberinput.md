---
name: NumberInput
description: Use NumberInput to provide a field for entering numbers in your app with ability to set min, max and step.
endpoint: /components/numberinput
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.numberinput.interactive
    :code: false

### Simple Example

.. exec::docs.numberinput.simple

### Increment/decrement on hold

Set `stepHoldDelay` and `stepHoldInterval` props to define behavior when increment/decrement controls are clicked and 
held.

.. exec::docs.numberinput.hold

### Decimal steps

To use decimal steps set following props:
* `step` - decimal number, e.g. 0.05
* `decimalScale` - amount of significant digits

.. exec::docs.numberinput.decimal

### With Icon

You can use DashIconify to add icon to the NumberInput.

.. exec::docs.numberinput.icon

### Decimal/Thousands separator

To change the separators set decimalSeparator and thousandsSeparator props:

.. exec::docs.numberinput.separator

### Remove controls

Controls are not rendered in these cases:

- `hideControls` prop is set to `True`
- Input is disabled
- `variant` prop is set to "unstyled"

.. exec::docs.numberinput.controls

### Styles API

| Name        | Static selector                  | Description                                      |
|:------------|:---------------------------------|:-------------------------------------------------|
| wrapper     | .mantine-NumberInput-wrapper     | Root element of the Input                        |
| input       | .mantine-NumberInput-input       | Input element                                    |
| section     | .mantine-NumberInput-section     | Left and right sections                          |
| root        | .mantine-NumberInput-root        | Root element                                     |
| label       | .mantine-NumberInput-label       | Label element                                    |
| required    | .mantine-NumberInput-required    | Required asterisk element, rendered inside label |
| description | .mantine-NumberInput-description | Description element                              |
| error       | .mantine-NumberInput-error       | Error element                                    |
| controls    | .mantine-NumberInput-controls    | Increment and decrement buttons wrapper          |
| control     | .mantine-NumberInput-control     | Increment and decrement buttons                  |

### Keyword Arguments

#### NumberInput

.. kwargs::NumberInput
