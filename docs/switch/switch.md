---
name: Switch
description: Use the Switch component to capture boolean input from user.
endpoint: /components/switch
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.switch.interactive
    :code: false

### Radius and Size

Set the radius and size of the Switch component using the `radius` and `size` prop respectively.

```python
import dash_mantine_components as dmc

dmc.Switch(
    size="lg",
    radius="sm",
    label="Enable this option",
    checked=True
)
```

### Callbacks

Use the property `checked` to use dmc.Switch in callbacks.

.. exec::docs.switch.callback

### Inner Labels

```python
import dash_mantine_components as dmc

dmc.Switch(
    label="I agree to sell my privacy",
    onLabel="ON",
    offLabel="OFF"
)
```

.. exec::docs.switch.label
    :code: false

### Icon Labels

You can also add icons in the switch labels.

.. exec::docs.switch.icons

### Thumb Icon

.. exec::docs.switch.thumb

### Styles API

| Name         | Static selector              | Description                             |
|:-------------|:-----------------------------|:----------------------------------------|
| root         | .mantine-Switch-root         | Root element                            |
| input        | .mantine-Switch-input        | Checkbox input                          |
| labelWrapper | .mantine-Switch-labelWrapper | Include label and description component |
| body         | .mantine-Switch-body         | Container Of Switch                     |
| track        | .mantine-Switch-track        | Track                                   |
| thumb        | .mantine-Switch-thumb        | Thumb of Switch                         |
| trackLabel   | .mantine-Switch-trackLabel   | onLabel and offLabel                    |
| error        | .mantine-Switch-error        | Error message                           |
| description  | .mantine-Switch-description  | Description                             |
| label        | .mantine-Switch-label        | Label                                   |

### Keyword Arguments

#### Switch

.. kwargs::Switch
