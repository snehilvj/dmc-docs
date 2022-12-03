---
name: Button
section: Buttons
head: Render button or link with button styles from mantine theme.
description: DMC alternative to html <button>.
component: Button
---

##### Interactive Demo

.. exec::docs.button.interactive
    :prism: false

##### Variants

Button supports the following variants: default, subtle, gradient, filled, light, outline etc.

.. exec::docs.button.variant

##### Icons Support

You can add icons in your button with leftIcon and rightIcon props. Dash Iconify is recommended.

.. exec::docs.button.icons

##### Colors

Change the color of the button by choosing from one of the theme colors.

.. exec::docs.button.colors

You can play more with the colors and variants in the interactive demo at the top.

##### With Gradient

To use gradient as Button background:

* set `variant` prop to "gradient"
* set `gradient` prop to `{ "from": "color-from", "to": "color-to", "deg": 135}`, where

* `color-from` and `color-to` are colors from Mantine's theme colors.
* `deg` is linear gradient deg.

.. exec::docs.button.gradient

##### Radius and Size

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

##### Full Width Button

Pass `fullWidth=True` for a full width button.

.. exec::docs.button.full
