---
name: ThemeIcon
description: Use ThemeIcon component to render icon inside element with theme colors.
endpoint: /components/themeicon
package: dash_mantine_components
category: Data Display
---

.. toc::

### Usage

ThemeIcon can be customized by setting its variant, size, radius and color.

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ThemeIcon(
    size="xl",
    color="indigo",
    variant="filled",
    children=DashIconify(icon="tabler:photo", width=25)
)
```

.. exec::docs.themeicon.interactive
    :code: false

### Colors

ThemeIcon supports all colors from Mantine's theme colors.

.. exec::docs.themeicon.colors

### Gradient Variant

To use gradient as ThemeIcon background:

* set `variant` prop to "gradient"
* set `gradient` prop to `{ "from": "color-from", "to": "color-to", "deg": 135}`, where

* `color-from` and `color-to` are colors from Mantine's theme colors.
* `deg` is linear gradient deg.

.. exec::docs.themeicon.gradient

### Styles API

| Name        | Static selector         | Description                                      |
|:------------|:------------------------|:-------------------------------------------------|
| root        | .mantine-ThemeIcon-root | Root element                                     |

### Keyword Arguments

#### ThemeIcon

.. kwargs::ThemeIcon
