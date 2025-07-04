---
name: Plotly figure templates
description: How to style Plotly figures with a Mantine theme.
endpoint: /components/figure-templates
package: dash_mantine_components
category: Theming
order: 11  # sets order in navbar section
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
from my_figure_templates import add_figure_templates

# Register custom templates
add_figure_templates()
```

In the [Help Center](https://github.com/snehilvj/dmc-docs/tree/main/help_center/theme_switch_figure_templates_custom) you'll find a complete minimal example of a custom figure template with a green primary color.

### Using a Theme Switcher

To update the figure when switching themes, you need to change the Plotly template in a callback.


> For more information on adding a theme switcher to your app, check the [Theme Switch Component](/theme-switch) section.

The example below uses this app's  theme switch component in the callback.  Try it out by clicking the **theme switch** in the header!

See a complete minimal example in the [Help Center](https://github.com/snehilvj/dmc-docs/tree/main/help_center/theme_switch_figure_templates_simple)

.. exec::docs.figuretemplates.theme_switch

For better performance, you can update the figure template using [Partial Property Updates.](https://dash.plotly.com/partial-properties)

Here is the callback updated to use `Patch` to change the figure template.  Note that when using `Patch` you must use the template
object rather than just the string name.  

```python

from dash import  Input, Output, callback, Patch
import plotly.io as pio


@callback(
    Output("figure-templates-bar", "figure"),
    Input("docs-color-scheme-switch", "checked"),
)
def update_figure(switch_on):
    # template must be template object rather than just the template string name
    template = pio.templates["mantine_dark"] if switch_on else pio.templates["mantine_light"]
    patched_fig = Patch()
    patched_fig["layout"]["template"] = template
    return patched_fig
```

### Updating multiple figures

To update multiple figure when switching themes, you can use [Pattern Matching Callbacks.](https://dash.plotly.com/pattern-matching-callbacks)
 
The example below uses this app's  theme switch component in the callback.  Try it out by clicking the **theme switch** in the header!

See a complete minimal example in the [Help Center](https://github.com/snehilvj/dmc-docs/tree/main/help_center/theme_switch_figure_templates)

.. exec::docs.figuretemplates.multiple_figures

