---
name: NumberInput
description: Use NumberInput to provide a field for entering numbers in your app with ability to set min, max and step.
endpoint: /components/numberinput
package: dash_mantine_components
---

.. toc::

### Simple Example

.. exec::docs.numberinput.simple

### Increment/decrement on hold

Set `stepHoldDelay` and `stepHoldInterval` props to define behavior when increment/decrement controls are clicked and 
held.

.. exec::docs.numberinput.hold

### Decimal steps

To use decimal steps set following props:
* `step` - decimal number, e.g. 0.05
* `precision` - amount of significant digits

.. exec::docs.numberinput.decimal

### With Icon

You can use DashIconify to add icon to the NumberInput.

.. exec::docs.numberinput.icon

### Styles API

| Name         | Static selector                   | Description                                                               |
|:-------------|:----------------------------------|:--------------------------------------------------------------------------|
| wrapper      | .mantine-NumberInput-wrapper      | Root Input element                                                        |
| icon         | .mantine-NumberInput-icon         | Input icon wrapper on the left side of the input, controlled by icon prop |
| input        | .mantine-NumberInput-input        | Main input element                                                        |
| rightSection | .mantine-NumberInput-rightSection | Right section with up and down controls                                   |
| root         | .mantine-NumberInput-root         | Root element                                                              |
| label        | .mantine-NumberInput-label        | Label element styles, defined by label prop                               |
| error        | .mantine-NumberInput-error        | Error element styles, defined by error prop                               |
| description  | .mantine-NumberInput-description  | Description element styles, defined by description prop                   |
| required     | .mantine-NumberInput-required     | Required asterisk element styles, defined by required prop                |
| control      | .mantine-NumberInput-control      | Shared up and down controls styles                                        |
| controlUp    | .mantine-NumberInput-controlUp    | Up control styles                                                         |
| controlDown  | .mantine-NumberInput-controlDown  | Down control styles                                                       |

### Keyword Arguments

#### NumberInput

.. kwargs::NumberInput
