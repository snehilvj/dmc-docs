---
name: Getting Started
endpoint: /getting-started
description: Install dash-mantine-components using pip, poetry, or conda.
dmc: false
---

.. toc::

### PyPI

You can install `dash-mantine-components` from PyPI via pip or poetry.

```bash
pip install dash-mantine-components
```

```bash
poetry add dash-mantine-components
```

### Simple Usage

Using Dash Mantine Components is pretty much the same as using Dash Bootstrap Components or the official Dash 
components. 

.. admonition::Don't Forget MantineProvider!
   :icon: radix-icons:info-circled
   :color: red

   It's required that you wrap your app layout with a dmc.MantineProvider.

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   Some components require additional CSS styles.

.. admonition::React 18 with Dash 2.x Issue
   :icon: radix-icons:info-circled
   :color: red

   Dash Mantine Components is based on REACT 18. You must set the env variable REACT_VERSION=18.2.0 before
   starting  the app when using dash 2.x.


Dash 3.0 now uses react 18 by default.  If your app uses dash>=3.0 it is no longer necessary to set the React version:
```python
# not needed with dash>=3.0
_dash_renderer._set_react_version("18.2.0")
```

    

```python
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer

# not needed with dash >3.0.0
_dash_renderer._set_react_version("18.2.0")

# additional styles
app = Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    dmc.Alert(
       "Hi from Dash Mantine Components. You can create some great looking dashboards using me!",
       title="Welcome!",
       color="violet",
    )
)

if __name__ == "__main__":
    app.run(debug=True)
```

### CSS Extensions

Most of the necessary styling is already included with `dash-mantine-components`. However, for certain components like
`DatePicker`, `Carousel`, or `CodeHighlight`, you need to add their specific CSS files separately. You can also include 
all optional CSS stylesheets at once by using `dmc.styles.ALL`.

Starting from version 0.14.4, `dash-mantine-components` provides `dmc.styles` variables to ensure that the correct 
stylesheet version is used, matching the version of the library you have installed.

To include stylesheets in your Dash app, you can do something like this:

```python
from dash import Dash
import dash_mantine_components as dmc

# below covers all the stylesheets, you can pick as per your need.
stylesheets = [
    dmc.styles.DATES,
    dmc.styles.CODE_HIGHLIGHT,
    dmc.styles.CHARTS,
    dmc.styles.CAROUSEL,
    dmc.styles.NOTIFICATIONS,
    dmc.styles.NPROGRESS,
]
app = Dash(__name__, external_stylesheets=stylesheets)
```

Or, if you want to include all optional stylesheets:

```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```

If you need to add other external stylesheets along with these, you can do it like this:

```python
app = Dash(external_stylesheets=[dbc.icons.FONT_AWESOME] + dmc.styles.ALL)
```


Note - to find the correct stylesheet link, you can print it out like this:
```
print(dmc.styles.DATES)
```
This will give you a link like:
```
https://unpkg.com/@mantine/dates@7.11.0/styles.css
```


### Documentation

This entire documentation has been created almost entirely using Dash Mantine Components. You can check out the source
code in the [dcm-docs GitHub](https://github.com/snehilvj/dmc-docs) for some inspiration.

While going through this documentation, you will come across interactive demos meant to show an overview as well as the overall effect of different combinations of a component's props.

.. exec::docs.getting-started.interactive
   :code: false

Note that this documentation has some additional styling applied to it. So when you actually use these components, they 
might look a bit different. You can check out [MantineProvider](/components/mantineprovider) for more details on
theming and customizations.

Here's how you can add the same styling to your apps:

```python
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
     forceColorScheme="light",
     theme={
         "primaryColor": "indigo",
         "fontFamily": "'Inter', sans-serif",
         "components": {
             "Button": {"defaultProps": {"fw": 400}},
             "Alert": {"styles": {"title": {"fontWeight": 500}}},
             "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
             "Badge": {"styles": {"root": {"fontWeight": 500}}},
             "Progress": {"styles": {"label": {"fontWeight": 500}}},
             "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
             "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
             "Table": {
                 "defaultProps": {
                     "highlightOnHover": True,
                     "withTableBorder": True,
                     "verticalSpacing": "sm",
                     "horizontalSpacing": "md",
                 }
             },
         },
     },
     children=[
         # content
     ],
 )

if __name__ == "__main__":
    app.run(debug=True)
```

### Next Steps

Please read the [Mantine API Overview](/mantine-api) section Theming section before starting development to learn about all of the
available theming and styling features.


