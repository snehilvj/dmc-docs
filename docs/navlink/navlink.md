---
name: NavLink
description: A Navlink component.
endpoint: /components/navlink
package: dash_mantine_components
category: Navigation
---

.. toc::

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

*New in dash-mantine-components > = 1.0.0*  

Now, `active` can be set dynamically:  
- `"exact"` → Active when the current pathname matches `href`.  
- `"partial"` → Active when the current pathname starts with `href` (includes subpages).  

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
Here's a minimal multi-page app example using Pages. It demonstrates how `active="exact"` and `active="partial"`
automatically apply active styles based on the current URL

```python
import dash
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, html
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL, use_pages=True, pages_folder="")

dash.register_page("home", path="/", layout=html.Div("I'm home"))
dash.register_page("page1", path="/page-1", layout=html.Div("Info about page 1 subjects"))
dash.register_page("page1s1", path="/page-1/sub-1", layout=html.Div("page 1 subject 1"))
dash.register_page("page1s2", path="/page-1/sub-2", layout=html.Div("page 1 subject 2"))

component = dmc.Box([
    dmc.NavLink(label="home", href="/", active='exact'),
    dmc.NavLink(
            label="Page 1",
            childrenOffset=28,
            href="/page-1",
            active='partial',
            children=[
                dmc.NavLink(label="Subject 1", href="/page-1/sub-1", active="exact"),
                dmc.NavLink(label="Subject 2", href="/page-1/sub-2", active="exact"),
            ],
    ),
    dmc.Divider(mb="lg"),
    dash.page_container
])


app.layout = dmc.MantineProvider([component])

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

#### NavLink

.. kwargs::NavLink
