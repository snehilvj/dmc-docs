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

### Mantine Light and dark themes

Mantine sets the light and dark color schemes using the `data-mantine-color-scheme` attribute on the `<html>` element.
This allows it to apply global styles dynamically based on the theme.

To switch themes in a Dash app you can set the `data-mantine-color-scheme` in a clientside callback.

### Example 1 Theme Toggle

This example demonstrates how to toggle between light and dark modes using  `ActionIcon` as the theme switch component.

.. exec::docs.theme-switch-components.themeswitch

### Example 2 Theme Switch

This example shows how to use the `Switch` component with icon labels to create a theme switch component.   The `Switch`
is set with `persistence=True` to retain the selected theme even after a browser refresh.

This is the theme switch used in these docs.  Click on the switch in the header to change themes.

Here is a complete minimal example:

```python

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output,  clientside_callback


theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][8]),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][6]),
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