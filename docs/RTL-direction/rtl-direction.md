---
name: Right-to-left direction
endpoint: /rtl
description: All Mantine components support right-to-left direction out of the box. You can preview how components work with RTL direction by clicking direction control in the top right corner.
package: dash_mantine_components
category: Styling
order: 10  # sets order in navbar section
---

.. toc::
.. llms_copy::Right-to-left direction

### DirectionProvider

`DirectionProvider` component is used to set direction for all components inside it. It is required to wrap your 
application with `DirectionProvider` if you are planning to either use RTL direction or change direction dynamically.

```python
app.layout=dmc.DirectionProvider(
    dmc.MantineProvider(
        # your layout
    ),
    direction="rtl",  # or "ltr"
    id="direction-provider"
)
```

The `direction` prop sets the `dir` attribute on the root element of your application, the `html` element.

### RTL direction toggle

You can change the text direction by updating the `direction` prop in a callback.

Here is a minimal example of a RTL direction toggle, similar to the one used in the DMC documentation:

```python

import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify

app = Dash()

layout = dmc.Stack([
    dmc.Group([
        dmc.Title("RTL Direction demo", order=3),
        dmc.ActionIcon(
            DashIconify(icon="tabler:text-direction-rtl", width=18),
            id="rtl-toggle",
            variant="outline",
        ),
    ], justify="space-between"),
    dmc.Slider(value=25, labelAlwaysOn=True, mt="xl"),
], m="lg")

app.layout = dmc.DirectionProvider(
    dmc.MantineProvider(layout),
    id="direction-provider",
    direction="ltr"
)

@callback(
    Output("rtl-toggle", "children"),
    Output("direction-provider", "direction"),
    Input("rtl-toggle", "n_clicks"),
    State("direction-provider", "direction")
)
def toggle_direction(n, d):
    if n is None:
        raise PreventUpdate

    new_dir = "ltr" if d == "rtl" else "rtl"
    return DashIconify(icon=f"tabler:text-direction-{d}", width=18), new_dir


if __name__ == "__main__":
    app.run(debug=True)

```

