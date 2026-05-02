---
name: Getting Started
endpoint: /getting-started
description: Build feature-rich, accessible Dash apps faster than ever! Dash Mantine Components includes over 100 customizable components based on the React Mantine library, with consistent styling, theming, and full support for light and dark mode.
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

#### Version information

Dash Mantine Components v2 is built on Mantine v8. When referring to the upstream Mantine documentation, please use
[Mantine v8](https://v8.mantine.dev/).  Avoid the Mantine v9 documentation, as it includes breaking changes that are
not compatible with DMC v2.



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

Using older versions of dash or DMC?  See our [Migration Guide](/migration) for more information.

### Questions?

Please ask on the [dash community forum](https://community.plotly.com/), or join our [Discord.](https://discord.gg/KuJkh4Pyq5)




