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


### ColorSchemeToggle Component
For apps using DMC versions ≥ 2.6, it is recommended to use the [ColorSchemeToggle](/components/colorschemetoggle)  component.
It automatically switches between light and dark themes and persists the user’s selection in localStorage.

Copy this app to run it locally. For a live demo, click the ColorSchemeToggle in the header of these docs.

> The toggle handles theme switching internally and does not require a Dash callback.

For more information, see the  [ColorSchemeToggle](/components/colorschemetoggle) documentation.

```python
import dash_mantine_components as dmc
from dash import Dash
from dash_iconify import DashIconify

app = Dash()

component = dmc.ColorSchemeToggle(
    lightIcon=DashIconify(icon="radix-icons:sun", width=20),
    darkIcon=DashIconify(icon="radix-icons:moon", width=20),
    color="yellow",
    size="lg",
    m="xl",
)

app.layout = dmc.MantineProvider(component)

if __name__ == "__main__":
    app.run(debug=True)

```


### Mantine Light and dark themes

Mantine sets the light and dark color schemes using the `data-mantine-color-scheme` attribute on the `<html>` element.
This allows it to apply global styles dynamically based on the theme.

If you are not using the `ColorSchemeToggle` component, you can switch themes by setting the `data-mantine-color-scheme` in a clientside callback.


### Custom Theme Switch

This example shows how to use the `Switch` component with icon labels to create a theme switch component.   The `Switch`
is set with `persistence=True` to retain the selected theme even after a browser refresh.

Use this approach if you are on DMC < 2.6.0 or want a custom control (such as `Switch`, `SegmentedControl`, or `Button` etc.) 
instead of the `ActionIcon` used by `ColorSchemeToggle`.

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
