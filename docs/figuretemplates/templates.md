---
name: Plotly figure templates
description: How to style Plotly figures with a Mantine theme.
endpoint: /components/figure-templates
package: dash_mantine_components
category: Theming
---

.. toc::

---

### Plotly Figure Template Basics

Plotly figure templates allow you to style your figures globally or per-figure. Templates include pre-defined color schemes, font styles, and layout configurations.

For more details, refer to the [Plotly templates documentation](https://plotly.com/python/templates/).

Below is an example using Plotly's built-in `plotly_white` and `plotly_dark` templates.  This is the same figure
styled for a light and dark theme.


.. exec::docs.figuretemplates.plotly_figure_templates


### Mantine-Themed Plotly Templates

To make Plotly figures consistent with Mantine's default theme, Dash Mantine Components provides two custom Plotly templates:

- **`mantine_light`**: Based on `plotly_white` and styled with Mantine's light theme.  
- **`mantine_dark`**: Based on `plotly_dark` and styled with Mantine's dark theme.  

These templates are created and registered using the `add_figure_templates` function. They include:  
- Color palettes from Mantine’s theme.  
- Fonts (`Inter` by default).  
- Background and grid colors that match Mantine’s styles.  


.. exec::docs.figuretemplates.mantine_figure_templates


### Setting a Default Template
You can globally set either `mantine_light` or `mantine_dark` as the default Plotly template. This ensures all figures
use the specified template unless explicitly overridden.

```python
import dash_mantine_components as dmc

# Set "mantine_dark" as the default template
dmc.add_figure_templates(default="mantine_dark")
```


### Modifying Existing Plotly Templates
The `mantine_light` and `mantine_dark` templates can be customized like any other Plotly template. Refer to the
[Plotly templates documentation](https://plotly.com/python/templates/) for more info and examples.

```python
import plotly.io as pio
import plotly.express as px
import dash_mantine_components as dmc

dmc.add_figure_templates()

# Access the registered Mantine light template
template = pio.templates["mantine_light"]

# Reduce the margins in the template
template.layout.margin = dict(l=20, r=20, t=20, b=20)

fig = px.scatter(px.data.gapminder(), x="gdpPercap", y="lifeExp", template="mantine_light")



```

### Customizing `add_figure_templates` Function
The `add_figure_templates` function is available starting in DMC version 0.15.1.
If you are using an earlier version, or if you are using a custom Mantine theme, you can include your own `add_figure_templates` implementation in your project.

Example Project Structure:
```bash
my_project/  
├── app.py  
├── my_figure_templates.py  
```

In `my_figure_templates.py`:

Copy the `add_figure_templates` code from the [Dash Mantine Components GitHub](https://github.com/snehilvj/dash-mantine-components/blob/master/dash_mantine_components/figure_templates.py) 
repository and modify it to fit your project's requirements.

In `app.py`:
```python
from .my_figure_templates import add_figure_templates
import dash_mantine_components as dmc

# Register custom templates
add_figure_templates()
```


### Using a Theme Switcher

To update the figure when switching themes, you need to change the Plotly template in a callback.

The `MantineProvider` has a `forceColorScheme` prop that switches between light and dark themes. For more information on
adding a theme switcher to your app, check the [MantineProvider documentation](/components/mantineprovider).

This example uses this app's  `MantineProvider` in the callback.  Try it out by clicking the **theme icon** in the header!

.. exec::docs.figuretemplates.theme_switch
    :code: false


```python

import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, callback, _dash_renderer
import plotly.express as px
_dash_renderer._set_react_version("18.2.0")

df = px.data.gapminder()
dff = df[df.year == 2007]

dmc.add_figure_templates()

app= Dash(external_stylesheets=dmc.styles.ALL)

# also need to add your own theme switch component and callbacks
app.layout = dmc.MantineProvider(
    dcc.Graph(id="figure-templates-bar"),
    forceColorScheme="light",
    id="mantine-provider"
)

@callback(
    Output("figure-templates-bar", "figure"),
    Input("mantine-provider", "forceColorScheme"),
)
def update_figure(theme):
   return px.bar(dff, x="continent", y="pop", title="Population by Continent", template=f"mantine_{theme}")


if __name__ == "__main__":
    app.run(debug=True)
```

For better performance, you can update the figure template using [Partial Property Updates](https://dash.plotly.com/partial-properties)

Here is the same app update to use `Patch` to update the figure.  Note that when using `Patch` you must use the template
object rather than just the string name.  For example, instead of using "mantine_light" use
```
pio.templates["mantine_light"]
```

```python

import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, callback, _dash_renderer, Patch
import plotly.express as px
import plotly.io as pio
_dash_renderer._set_react_version("18.2.0")

df = px.data.gapminder()
dff = df[df.year == 2007]

dmc.add_figure_templates()

app= Dash(external_stylesheets=dmc.styles.ALL)

# also need to add your own theme switch component and callbacks
app.layout = dmc.MantineProvider(
    dcc.Graph(
        id="figure-templates-bar",
        figure= px.bar(dff, x="continent", y="pop", title="Population by Continent")
    ),
    forceColorScheme="light",
    id="mantine-provider"
)

@callback(
    Output("figure-templates-bar", "figure"),
    Input("mantine-provider", "forceColorScheme"),
)
def update_figure(theme):
    # template must be template object rather than just the template string name
    template = pio.templates["mantine_light"] if theme == "light" else pio.templates["mantine_dark"]
    patched_fig = Patch()
    patched_fig["layout"]["template"] = template
    return patched_fig

if __name__ == "__main__":
    app.run(debug=True)

```

### Updating multiple figures

To update multiple figure when switching themes, you can use [Pattern Matching Callbacks](https://dash.plotly.com/pattern-matching-callbacks)
 
We use the doc's theme switch component.  Try it out by clicking the theme icon in the header!


.. exec::docs.figuretemplates.multiple_figures
    :code: false


```python

import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, State, callback, _dash_renderer, Patch, ALL
import plotly.express as px
import plotly.io as pio
_dash_renderer._set_react_version("18.2.0")

dmc.add_figure_templates(default="mantine_dark")

df = px.data.gapminder()


line_fig = px.line(
    df.query("1952 <= year <= 1982 & continent != 'Asia'"),
    x="year",
    y="gdpPercap",
    color="continent",
    line_group="country"
)

dff = df[df.year == 2007]
scatter_fig = px.scatter(
    dff,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    log_x=True,
    size_max=60,
    title=f"2007 GDP per Capita vs Life Expectancy, Sized by Population ",
)


avg_lifeExp = (dff["lifeExp"] * dff["pop"]).sum() / dff["pop"].sum()
map_fig = px.choropleth(
    dff,
    locations="iso_alpha",
    color="lifeExp",
    title="%.0f World Average Life Expectancy was %.1f years" % (2007, avg_lifeExp),
)

bar_fig = px.bar(dff, x="continent", y="pop", title="Population by Continent")

graphs = dmc.Grid(
    [
        dmc.GridCol(dcc.Graph(figure=bar_fig, id={"index": "bar"}), span={"base": 12, "md":6}),
        dmc.GridCol(dcc.Graph(figure=scatter_fig, id={"index": "scatter"}), span={"base": 12, "md":6}),
        dmc.GridCol(dcc.Graph(figure=line_fig, id={"index": "line"}), span={"base": 12, "md":6}),
        dmc.GridCol(dcc.Graph(figure=map_fig, id={"index": "map"}), span={"base": 12, "md":6}),
    ],
    gutter="xl",
)

sample_controls = dmc.Box([
    dmc.Button("sample button"),
    dmc.Button("sample red button", color="red"),
    dmc.Button("sample yellow button", color="yellow"),
    dmc.Slider(value=25, my="lg"),
], w=600)


app= Dash(external_stylesheets=dmc.styles.ALL)

# also need to add a theme switch component and callbacks
app.layout = dmc.MantineProvider(
    [sample_controls, graphs],
    forceColorScheme="dark",
    id="mantine-provider"
)

@callback(
    Output({"index": ALL}, "figure"),
    Input("mantine-provider", "forceColorScheme"),
    State({"index": ALL}, "id"),
)
def update_figure(theme, ids):
    # template must be template object rather than just the template string name
    template = pio.templates["mantine_light"] if theme == "light" else pio.templates["mantine_dark"]
    patched_figures = []
    for i in ids:
        patched_fig = Patch()
        patched_fig["layout"]["template"] = template
        patched_figures.append(patched_fig)

    return patched_figures

if __name__ == "__main__":
    app.run(debug=True)
```



