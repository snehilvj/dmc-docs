---
name: MantineProvider
description: Use MantineProvider component to enable dark theme in your app globally.
endpoint: /components/mantineprovider
package: dash_mantine_components
category: Theming
---

.. toc::

### Usage

Your app must be wrapped inside a MantineProvider, and it must be used only once.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    theme = {...},
    children={...}
)
```

### Color Scheme

Color Scheme is currently controlled using the prop `forceColorScheme`.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    theme = {...},
    children={...}
)
```

### Custom Colors

You can add custom colors using MantineProvider, other than the ones found in `dmc.DEFAULT_THEME['colors']`.
Use [this](https://omatsuri.app/color-shades-generator) tool to generate 10 shades of the color you like. Mantine's
styling system needs 10 shades for any color so that it can use the right one depending on the colorScheme.

You can also use the same color 10 times but using the tool will give you better results. You can add more than 10 values
as well but the extra values will not be used by Mantine.

.. exec::docs.mantineprovider.colors
    :code: false

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
        "colors": {
            "myColor": [                
              "#F2FFB6",
              "#DCF97E",
              "#C3E35B",
              "#AAC944",
              "#98BC20",
              "#86AC09",
              "#78A000",
              "#668B00",
              "#547200",
              "#455D00",                
            ]
        },
    },
    children=[dmc.Button("Custom Colors!", color="myColor")],
)
```

### Further Customization

You can further customize your theme such as theme colors, shadows, etc. Refer to
[mantine.dev](https://mantine.dev/theming/theme-object/) for more information.

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
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

app.layout = dmc.MantineProvider(
     forceColorScheme="light",
     theme={
         "primaryColor": "indigo",
         "fontFamily": "'Inter', sans-serif",
         "components": {
             "Button": {"defaultProps": {"fw": 400}},
             "Alert": {"styles": {"title": {"fontWeight": 500}}},
             "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
             "Badge": {"styles": {"root": {"fontWeight": 500}}},
             "Progress": {"styles": {"label": {"fontWeight": 500}}},
             "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
             "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
             "Table": {
                 "defaultProps": {
                     "highlightOnHover": True,
                     "withTableBorder": True,
                     "verticalSpacing": "sm",
                     "horizontalSpacing": "md",
                 }
             },
         },
     },
     children=[
         # content
     ],
 )
```

### Theme Switch

This minimal example shows how to toggle between light and dark modes.  It uses a `dmc.ActionIcon` for the theme switch,
component, similar to the theme switcher used in these docs.

```python

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output, State, callback, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

theme_toggle = dmc.ActionIcon(
    [
        dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
        dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
    ],
    variant="transparent",
    color="yellow",
    id="color-scheme-toggle",
    size="lg",
    ms="auto",
)

app = Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    [theme_toggle, dmc.Text("Your page content")],
    id="mantine-provider",
    forceColorScheme="light",
)


@callback(
    Output("mantine-provider", "forceColorScheme"),
    Input("color-scheme-toggle", "n_clicks"),
    State("mantine-provider", "forceColorScheme"),
    prevent_initial_call=True,
)
def switch_theme(_, theme):
    return "dark" if theme == "light" else "light"


if __name__ == "__main__":
    app.run(debug=True)
```

### Theme Switch with Clientside Callback

This example demonstrates how to use the `dmc.Switch` component with icons as labels to create a theme switcher.
A clientside callback is used to update the `data-mantine-color-scheme` attribute to either `'light'` or `'dark'`. 
Additionally, the `dmc.Switch` component is configured with `persistence=True`, ensuring that the selected theme is 
retained even after the browser is refreshed.

.. exec::docs.mantineprovider.themeswitch2

### Default theme

Default theme is available as `dmc.DEFAULT_THEME`. It includes all theme properties with default values. 
When you pass theme override to MantineProvider, it will be deeply merged with the default theme.

.. exec::docs.mantineprovider.theme
    :code: false

### Keyword Arguments

#### MantineProvider

.. kwargs::MantineProvider
