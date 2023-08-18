---
name: MantineProvider
description: Use MantineProvider component to enable dark theme in your app globally.
endpoint: /components/mantineprovider
package: dash_mantine_components
---

.. toc::

### Dark Theme

All mantine components support dark color scheme natively without any additional steps. To use dark color scheme wrap
your application in MantineProvider and specify colorScheme.

.. exec::docs.mantineprovider.dark

### Global Styles

theme.colors.dark[7] shade is considered to be the body background color and theme.colors.dark[0] shade as text color
with dark color scheme. You can create these styles on your own or add them by setting withGlobalStyles prop on 
MantineProvider, which includes them by default.

```python
import dash_mantine_components as dmc

component = dmc.MantineProvider(withGlobalStyles=True, theme={"colorScheme": "dark"})
```

### Custom Colors

You can add custom colors using MantineProvider, other than the ones found in dmc.theme.DEFAULT_COLORS.
Use [this](https://omatsuri.app/color-shades-generator) tool to generate 10 shades of the color you like. Mantine's
styling system needs 10 shades for any color so that it can use the right one depending on the colorScheme.

You can also use the same color 10 times but using the tool will give you better results.

.. exec::docs.mantineprovider.colors

### Further Customization

You can further customize your theme such as theme colors, shadows, etc. Refer to
[mantine.dev](https://mantine.dev/theming/theme-object/) for more information.

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
        "colorScheme": "dark",
        # add your colors
        "colors": {
            "deepBlue": ["#E9EDFC", "#C1CCF6", "#99ABF0" "..."], # 10 color elements
        },
        "shadows": {
            # other shadows (xs, sm, lg) will be merged from default theme
            "md": "1px 1px 3px rgba(0,0,0,.25)",
            "xl": "5px 5px 3px rgba(0,0,0,.25)",
        },
        "headings": {
            "fontFamily": "Roboto, sans-serif",
            "sizes": {
                "h1": {"fontSize": 30},
            },
        },
    },
    children=[
        # dash/dmc components here
    ],
)
```

### Usage in DMC docs

MantineProvider is used to customize theme for these docs as well. The theming is more or less inline with below.

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash(
    __name__,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "components": {
            "Button": {"styles": {"root": {"fontWeight": 400}}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[...],
)

if __name__ == "__main__":
    app.run_server()
```

### Keyword Arguments

#### MantineProvider

.. kwargs::MantineProvider
