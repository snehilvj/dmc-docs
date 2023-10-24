---
name: Getting Started
endpoint: /getting-started
description: Install dash-mantine-components using pip, poetry, or conda.
dmc: false
---

.. toc::

##### PyPI

You can install `dash-mantine-components` from PyPI via pip or poetry.

```bash
pip install dash-mantine-components
```

```bash
poetry add dash-mantine-components
```

##### Simple Usage

Using Dash Mantine Components is pretty much the same as using Dash Bootstrap Components or the official Dash 
components.

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash(__name__)

app.layout = dmc.Alert(
    "Hi from Dash Mantine Components. You can create some great looking dashboards using me!",
    title="Welcome!",
    color="violet",
)

if __name__ == "__main__":
    app.run_server()
```

##### Documentation

This entire documentation has been created almost entirely using Dash Mantine Components. You can check out the source
code [here](https://github.com/snehilvj/dmc-docs) for some inspiration.

While going through this documentation, you will come across interactive demos meant to show an overview as well as the overall effect of different combinations of a component's props.

.. exec::docs.getting-started.interactive
   :code: false

Note that this documentation has some additional styling applied to it. So when you actually use these components, they 
might look a bit different. You can check out [MantineProvider](/components/mantineprovider) for more details on
theming and customizations.

Here's how you can add the same styling to your apps:

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash(
    __name__,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "components": {
            "Button": {"styles": {"root": {"fontWeight": 400}}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[dmc.Button("Settings")],
)

if __name__ == "__main__":
    app.run_server()
```
