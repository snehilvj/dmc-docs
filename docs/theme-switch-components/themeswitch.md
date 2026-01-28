---
name: Theme Switch Components
description: Examples of components to switch between light and dark modes
endpoint: /theme-switch
package: dash_mantine_components
category: Theming
order: 10  # sets order in navbar section
---

.. toc::
.. llms_copy::Theme Switch Components


### New ColorSchemeToggle

For most apps, use the [ColorSchemeToggle](/color-scheme-toggle) component. It automatically toggles between light and
dark themes, persists the selection in localStorage.  The `pre_render_color_shcheme()` helper can be used to apply 
styles before the app renders to prevent flashes of the wrong theme.

The examples below show how to create a custom theme switch or implement one if you are using `dash-mantine-components` version < 2.6.0.




### Mantine Light and dark themes

Mantine sets the light and dark color schemes using the `data-mantine-color-scheme` attribute on the `<html>` element.
This allows it to apply global styles dynamically based on the theme.

To switch themes in a Dash app you can set the `data-mantine-color-scheme` in a clientside callback.


### Example 1 Theme Switch

This example shows how to use the `Switch` component with icon labels to create a theme switch component.   The `Switch`
is set with `persistence=True` to retain the selected theme even after a browser refresh.

This is the theme switch used in these docs.  Click on the switch in the header to change themes.

Here is a complete minimal example:

```python

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output,  clientside_callback


theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color= "var(--mantine-color-yellow-8)"),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color= "var(--mantine-color-yellow-6)"),
    id="color-scheme-switch",
    persistence=True,
    color="grey",
)

app = Dash()

app.layout = dmc.MantineProvider(
    [theme_toggle, dmc.Text("Your page content")],
)

clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-switch", "id"),
    Input("color-scheme-switch", "checked"),
)


if __name__ == "__main__":
    app.run(debug=True)

```


### Example 2 Theme Toggle

This example demonstrates how to toggle between light and dark modes using  `ActionIcon` as the theme switch component.
To see this live, see the theme toggle component in the header of the [Mantine documention](https://mantine.dev/getting-started/).

```python


import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output, clientside_callback

app=Dash()

theme_toggle = dmc.ActionIcon(
    [
        dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
        dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
    ],
    variant="transparent",
    color="yellow",
    id="color-scheme-toggle",
    size="lg",
)


component=dmc.Group([
    dmc.Text("Theme Switch Demo"),
    theme_toggle
])
app.layout = dmc.MantineProvider(component)


clientside_callback(
    """
    (n) => {
        document.documentElement.setAttribute(
            'data-mantine-color-scheme',
            (n % 2) ? 'dark' : 'light'
        );
        return window.dash_clientside.no_update      
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "n_clicks"),
)

if __name__ == "__main__":
    app.run(debug=True)


```