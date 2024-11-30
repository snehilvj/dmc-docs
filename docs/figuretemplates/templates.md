---
name: Plotly figure templates
description: How to style Plotly figures with a Mantine theme.
endpoint: /components/figure-templates
package: dash_mantine_components
category: Theming
---

.. toc::

### With Theme Switcher

When the theme changes, it's necessary to update the figure templates in a callback.  This example uses the `MantineProvider`
`forceColorScheme` prop as the Input of the callback.


.. exec::docs.figuretemplates.simple
    :code: false


```python
import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, callback
import plotly.express as px

df = px.data.gapminder()
dff = df[df.year == 2007]

# creates and adds the "mantine_light" and "mantine_dark" plotly figure templates
dmc.add_figure_templates()

app= Dash()

app.layout = dmc.MantineProvider(
    dcc.Graph(id="figure-templates-histogram"),
    id="mantine-provider"
)

@callback(
    Output("figure-templates-histogram", "figure"),
    Input("mantine-provider", "forceColorScheme"),
)
def update_figure(theme):
    return px.histogram(dff, x='lifeExp', title='2007 Life Expectancy', template=f"mantine_{theme}")

if __name__ == "__main__":
    app.run(debug=True)
```

### add_figure_templates()


You can set the default figure template to either "mantine_dark" or "mantine_light"

```python
dmc.add_figure_templates(default="mantine_dark")
```

### Updating figure templates

To make global changes to the figures, you can update the figure templates.

The following is just an image so we don't change all the figures in the docs:

```python
import plotly.io as pio

dmc.add_figure_templates()

mantine_dark = pio.templates[("mantine_dark")]
# change the paper background color for all figures using the "mantine_dark" theme
mantine_dark.layout.paper_bgcolor="#3b3b3b" # dark.6

```

### Updating multipe figures

