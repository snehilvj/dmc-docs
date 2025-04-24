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

#### Wrap Your App with MantineProvider
DMC components require `dmc.MantineProvider` to apply theming and styles.

#### React 18 is Required with Dash 2.x
- Dash 2.x: Set REACT_VERSION=18.2.0 before running your app.

```python
# required only with dash 2.x
import dash
dash._dash_renderer._set_react_version("18.2.0")
```


#### Adding Optional Stylesheets required with DMC < 1.2.0 

Starting in DMC 1.2.0, all necessary stylesheets are bundled automatically. You no longer need to manually add styles for specific components.  
For details on including optional stylesheets in older versions, see our [migration guide](/migration).

### Documentation

This entire documentation has been created almost entirely using Dash Mantine Components. You can check out the source
code in the [dcm-docs GitHub](https://github.com/snehilvj/dmc-docs) for some inspiration.

While going through this documentation, you will come across interactive demos meant to show an overview as well as the overall effect of different combinations of a component's props.

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


