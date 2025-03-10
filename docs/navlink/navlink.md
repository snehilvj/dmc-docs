---
name: NavLink
description: Use the Navlink component to create navigation link in the side navigation bars.
endpoint: /components/navlink
package: dash_mantine_components
category: Navigation
---

.. toc::

### Basic usage

You can use dmc.NavLink's `n_clicks` property in callbacks, or you can pass `href` to make it a link.

.. exec::docs.navlink.basic

### Active styles

Set `active` prop to add active styles to dmc.NavLink. You can customize active styles with `color` and `variant` properties.

.. exec::docs.navlink.active
    :code: false

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.NavLink(
    label="With right section",
    leftSection=DashIconify(icon="tabler:gauge"),
    active=True,
    variant="filled",
    color="orange",
    id="navlink-interactive",
    rightSection=DashIconify(icon="tabler-chevron-right"),
),
```

#### Using a callback to set active prop

This example demonstrates how to use a callback to set the active prop of the NavLinks when the user navigates to a different page. It uses the "Dash Pages" feature but can be adapted to any other page navigation system.

```python
# Create Navlinks (using dash.page_registry)
[
    dmc.NavLink(
        label=f"{page['name']}",
        href=page["relative_path"],
        id={"type": "navlink", "index": page["relative_path"]},
    )
    for page in page_registry.values()
]

# ...

# Callback (using the dcc.location provided by Dash Pages)
@app.callback(Output({"type": "navlink", "index": ALL}, "active"), Input("_pages_location", "pathname"))
def update_navlinks(pathname):
    return [control["id"]["index"] == pathname for control in callback_context.outputs_list]

```

### Nested NavLinks

To create nested links put dmc.NavLink as children of another dmc.NavLink.

.. exec::docs.navlink.nested

### Styles API

| Name        | Static selector              | Description                                  |
|:------------|:-----------------------------|:---------------------------------------------|
| root        | .mantine-NavLink-root        | Root element                                 |
| body        | .mantine-NavLink-body        | Contains label and description               |
| section     | .mantine-NavLink-section     | Left and right sections                      |
| label       | .mantine-NavLink-label       | NavLink label                                |
| description | .mantine-NavLink-description | Dimmed description displayed below the label |
| children    | .mantine-NavLink-children    | Wrapper around nested links                  |
| chevron     | .mantine-NavLink-chevron     | Default chevron icon                         |
| collapse    | .mantine-NavLink-collapse    | Nested links Collapse container              |

### Keyword Arguments

#### NavLink

.. kwargs::NavLink
