---
name: Button
description: DMC alternative to html.Button.
endpoint: /components/button
package: dash_mantine_components
category: Buttons
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

You can add icons in your button with leftSection and rightSection props. Dash Iconify is recommended.

.. exec::docs.button.icons

### Loading State

Starting with dash version 2.9.2, you can use duplicate callback outputs. Here's an example that lets you easily show
loading state and at the same time, disable the button.

.. exec::docs.button.loading

### Loader Props

You can customize [Loader](/components/loader) with `loaderProps` prop, it accepts all props that Loader component has:

.. exec::docs.button.loader-props

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

### Compact Size

.. exec::docs.button.compact

### Full Width Button

Pass `fullWidth=True` for a full width button.

.. exec::docs.button.full

### Button Group

.. exec::docs.button.group

### Styles API

| Name    | Static selector         | Description                                                 |
|:--------|:------------------------|:------------------------------------------------------------|
| root    | .mantine-Button-root    | Root element                                                |
| loader  | .mantine-Button-loader  | Loader component, displayed only when `loading` prop is set |
| section | .mantine-Button-section | Left and right sections of the button                       |
| inner   | .mantine-Button-inner   | Contains all other elements, child of the `root` element    |
| label   | .mantine-Button-label   | Button children                                             |

### Keyword Arguments

#### Button

.. kwargs::Button

#### ButtonGroup

.. kwargs::ButtonGroup
