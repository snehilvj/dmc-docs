---
name: Switch
description: Use the Switch component to capture boolean input from user.
endpoint: /components/switch
package: dash_mantine_components
category: Inputs
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

| Name         | Static selector              | Description                                     |
|:-------------|:-----------------------------|:------------------------------------------------|
| root         | .mantine-Switch-root         | Root element                                    |
| track        | .mantine-Switch-track        | Switch track, contains `thumb` and `trackLabel` |
| trackLabel   | .mantine-Switch-trackLabel   | Label displayed inside `track`                  |
| thumb        | .mantine-Switch-thumb        | Thumb displayed inside `track`                  |
| input        | .mantine-Switch-input        | Input element, hidden by default                |
| body         | .mantine-Switch-body         | Input body, contains all other elements         |
| labelWrapper | .mantine-Switch-labelWrapper | Contains `label`, `description` and `error`     |
| label        | .mantine-Switch-label        | Label element                                   |
| description  | .mantine-Switch-description  | Description displayed below the label           |
| error        | .mantine-Switch-error        | Error message displayed below the label         |

### Keyword Arguments

#### Switch

.. kwargs::Switch
