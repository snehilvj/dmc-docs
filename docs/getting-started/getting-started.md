---
name: Getting Started
endpoint: /getting-started
description: Dash Mantine Components (DMC) integrates the Mantine UI library with Dash, making it easy to create modern, responsive, and highly customizable applications—right out of the box.
dmc: false
order: 1  # sets order in section and in search
---

.. toc::
.. llms_copy::Getting Started


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


#### Wrap the layout with `MantineProvider`

```python
app.layout = dmc.MantineProvider(
   # your content
)
```

The `MantineProvider` is a core wrapper component that handles global styles, themes, and settings for all child components.

It’s required to:

- Enable component styling and theming (e.g., colors, fonts, spacing)

- Apply dark/light mode

- Customize default props across the app

- Register custom themes or override styles

#### Using Dash 2.x?
You must set React to version 18.2.0:
```python
# required for dash 2.x
import dash
dash._dash_renderer._set_react_version("18.2.0")
```

#### Using DMC < 1.2.0?

If you are using DMC < 1.2.0 it is required to include additional stylesheets for certain components. See the
[migration guide](/migration) for more information.

### Documentation

This documentation site is built almost entirely with Dash Mantine Components.
You can explore the source code on the [dcm-docs GitHub](https://github.com/snehilvj/dmc-docs)  for ideas and inspiration.

Throughout the docs, you’ll find interactive demos that highlight how different props and combinations affect each component in real time.

.. exec::docs.getting-started.interactive
   :code: false

Note that this documentation has some additional styling applied to it. So when you actually use these components, they 
might look a bit different. You can check out [MantineProvider theme object](/theme-object) for more details on
theming and customizations and to see the [theme used in these docs.](/theme-object#usage-in-dmc-docs)


### Next Steps

Please read the [Mantine API Overview](/mantine-api) section before starting development to learn about all of the
available theming and styling features.

### Questions?

Please ask on the [dash community forum](https://community.plotly.com/), or join our [Discord.](https://discord.gg/KuJkh4Pyq5)




