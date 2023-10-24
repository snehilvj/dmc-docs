---
name: Button
description: DMC alternative to html.Button.
endpoint: /components/button
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.button.interactive
    :code: false

### Variant

.. exec::docs.button.variant

#### Gradient Variant

To use gradient as Button background:

* set `variant` prop to "gradient"
* set `gradient` prop to `{ 'from': 'color-from', 'to': 'color-to', 'deg': 135}`, where

  * `color-from` and `color-to` are colors from Mantine's theme colors.
  * `deg` is linear gradient deg.

.. exec::docs.button.gradient

### Icons Support

You can add icons in your button with leftIcon and rightIcon props. Dash Iconify is recommended.

.. exec::docs.button.icons

### Loading State

Starting with dash version 2.9.2, you can use duplicate callback outputs. Here's an example that lets you easily show
loading state and at the same time, disable the button.

.. exec::docs.button.loading

### Colors

```python
import dash_mantine_components as dmc

dmc.Button("Settings", color="red")
```

.. exec::docs.button.colors
    :code: false

### Radius and Size

Button's radius and size can be customized by setting `radius` and `size` props. Both props have predefined values:
xs, sm, md, lg, xl. Alternatively, you can use a number to set radius, size in px.

```python
import dash_mantine_components as dmc

dmc.Group(
    [
        dmc.Button("Connect to Database", size="sm"),
        dmc.Button("Notify", radius="xl"),
        dmc.Button("Settings", size=20),
    ]
)
```

### Full Width Button

Pass `fullWidth=True` for a full width button.

.. exec::docs.button.full

### Button Group

.. exec::docs.button.group

### Styles API

| Name         | Static selector              | Description                          |
|:-------------|:-----------------------------|:-------------------------------------|
| root         | .mantine-Button-root         | Root button element                  |
| icon         | .mantine-Button-icon         | Shared icon styles                   |
| leftIcon     | .mantine-Button-leftIcon     | Left icon                            |
| rightIcon    | .mantine-Button-rightIcon    | Right icon                           |
| centerLoader | .mantine-Button-centerLoader | Center loader                        |
| inner        | .mantine-Button-inner        | Contains label, left and right icons |
| label        | .mantine-Button-label        | Contains button children             |

### Keyword Arguments

#### Button

.. kwargs::Button

#### ButtonGroup

.. kwargs::ButtonGroup
