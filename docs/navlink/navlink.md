---
name: NavLink
description: A Navlink component.
endpoint: /components/navlink
package: dash_mantine_components
category: Navigation
---

.. toc::
.. llms_copy::NavLink

### Basic usage

Use `NavLink`'s `n_clicks` property in callbacks, or you can set `href` to make it a link.

.. exec::docs.navlink.basic

### Active styles

Set `active` prop to add active styles to `NavLink`. You can customize active styles with `color` and `variant` properties.

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

### Setting Active prop based on URL

The `active` prop in `NavLink` controls whether a link is highlighted as active. It can be set manually (`True`/`False`)
or automatically based on the current URL.  


`active` can be set dynamically without using dash callbacks:  
- `"exact"` → Active when the current pathname matches `href` path
- `"exact-with-search`→ Active when the current pathname matches `href` path and query strings
- `"partial"` → Active when the current pathname starts with `href` (includes subpages)
- `"children"` → Parent link active when any child link is active


Example:
- User on `/page-1/subject-1` → The second and third links are active (since `"partial"` includes subpages).  
- User on `/page-1` → Only the second link is active.  


```python
html.Div([
    dmc.NavLink(label="Home", href="/home", active="exact"),
    dmc.NavLink(label="Page 1", href="/page-1", active="partial"),
    dmc.NavLink(label="Subject 1", href="/page-1/subject-1", active="exact"),
])
```
See a complete example in Multi-Page App Example with Active Links section.  


### Setting active prop in a callback

Use a callback to set `active` prop if you are using dash-mantine-components<1.0.0

This example demonstrates how to use a callback to set the `active` prop of the `NavLink` when the user navigates to a different page. It uses the "Dash Pages" feature but can be adapted to any other page navigation system.

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


### Multi-Page App Example with Active Links


This example uses [Dash Pages](https://dash.plotly.com/urls) to create a simple multi-page app. For simplicity, all
pages are defined in a single file instead of separate folders.

It demonstrates `active="exact-with-search"` with query strings and shows how `active="children"` keeps a parent link
active when a child route is selected.


.. image::/assets/dmc-navlink-active.png
    :w: 500px


```python
import dash
import dash_mantine_components as dmc

app = dash.Dash(use_pages=True, pages_folder="")


def reports_layout(type=None, **kwargs):
    return dmc.Box(f"{type} Report ")

dash.register_page("home", path="/", layout=dmc.Box("Home"))
dash.register_page("reports", path="/reports", layout=reports_layout)
dash.register_page("settings", path="/settings", layout=dmc.Box("Settings"))


nav = dmc.Box([
    dmc.NavLink(label="Home", href="/", active="exact"),
    dmc.NavLink(
        label="Reports",
        active="children",
        childrenOffset=28,
        children=[
            dmc.NavLink(
                label="Sales",
                href="/reports?type=Sales",
                active="exact-with-search",
            ),
            dmc.NavLink(
                label="Inventory",
                href="/reports?type=Inventory",
                active="exact-with-search",
            ),
        ],
    ),
    dmc.NavLink(label="Settings", href="/settings", active="exact"),
])

app.layout = dmc.MantineProvider(
    dmc.AppShell(
        [
            dmc.AppShellNavbar(nav),
            dmc.AppShellMain(dash.page_container),
        ],
        padding="xl",
        navbar={"width": 300},
    )
)

if __name__ == "__main__":
    app.run(debug=True)


```

### Styles API

.. styles_api_text::

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
.. style_props_text::

#### NavLink

.. kwargs::NavLink
