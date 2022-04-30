---
name: ThemeIcon
section: Data Display
head: Render icon inside element with theme colors.
description: Use ThemeIcon component to render icon inside element with theme colors.
component: ThemeIcon
---

##### Usage

ThemeIcon can be customized by setting its variant, size, radius and color.

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ThemeIcon(
    size="xl",
    color="indigo",
    variant="filled",
    children=[DashIconify(icon="tabler:photo", width=25)]
)
```

.. exec::docs.themeicon.interactive
    :prism: false

##### Colors

ThemeIcon supports all colors from Mantine's theme colors.

.. exec::docs.themeicon.colors

##### Gradient Variant

To use gradient as ThemeIcon background:

* set `variant` prop to "gradient"
* set `gradient` prop to `{ "from": "color-from", "to": "color-to", "deg": 135}`, where

* `color-from` and `color-to` are colors from Mantine's theme colors.
* `deg` is linear gradient deg.

.. exec::docs.themeicon.gradient
