---
name: Getting Started
endpoint: /getting-started
description: Dash Mantine Components (DMC) integrates the Mantine UI library with Dash, making it easy to create modern, responsive, and highly customizable applications—right out of the box.
dmc: false
---

.. toc::


### Installation

```bash
pip install dash-mantine-components
```

```bash
poetry add dash-mantine-components
```

### Basic Usage

.. exec::docs.getting-started.hello_world
   :code: false

Be sure to wrap your app layout in the `dmc.MantineProvider`


```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash()

app.layout = dmc.MantineProvider(
    dmc.Alert(
       "Welcome to Dash Mantine Components",
       title="Hello!",
       color="violet",
    )
)

if __name__ == "__main__":
    app.run(debug=True)
```


### Important Notes 


#### Wrap the app.layout with `MantineProvider`
Required to enable theming and styles for all DMC components.

#### Using Dash 2.x?
You must set React to version 18.2.0:
```python
# required for dash 2.x
import dash
dash._dash_renderer._set_react_version("18.2.0")
```

#### DMC < 1.2.0 Requires additional stylesheets

From DMC 1.2.0 on, styles are bundled—no need to add them manually. Still on an older version? Check the [migration guide](/migration)
for info on how to add the stylesheets.

### Documentation

This documentation site is built almost entirely with Dash Mantine Components.
You can explore the source code on the [dcm-docs GitHub](https://github.com/snehilvj/dmc-docs)  for ideas and inspiration.

Throughout the docs, you’ll find interactive demos that highlight how different props and combinations affect each component in real time.

.. exec::docs.getting-started.interactive
   :code: false

Note that this documentation has some additional styling applied to it. So when you actually use these components, they 
might look a bit different. You can check out [MantineProvider theme object](/theme-object) for more details on
theming and customizations.

Here's how you can add the same styling to your apps:

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash()

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

### Questions?

Please ask on the [dash community forum](https://community.plotly.com/), or join our [Discord.](https://discord.gg/KuJkh4Pyq5)




