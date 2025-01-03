---
name: Theme Switch Components
description: Examples of components to switch between light and dark modes
endpoint: /theme-switch
package: dash_mantine_components
category: Theming
order: 10  # sets order in navbar section
---

.. toc::

### Example 1

This simple example demonstrates how to toggle between light and dark modes using a `ActionIcon` as the theme switch.
It's similar to the theme switcher used in the Mantine documentation.

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

### Example 2: Theme Switch with Clientside Callback  

This example shows how to use the `Switch` component with icon labels to create a theme switcher. A clientside 
callback updates the `data-mantine-color-scheme` attribute to `'light'` or `'dark'`.  The `Switch` is set with 
`persistence=True` to retain the selected theme even after a browser refresh.

.. exec::docs.theme-switch-components.themeswitch2
