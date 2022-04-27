---
name: Getting Started
section: Getting Started
head: Installation instructions and basic usage.
description: Install dash-mantine-components using pip, poetry, or conda.
---

##### PyPI

You can install `dash-mantine-components` from PyPI via pip or poetry.

```bash
pip install dash-mantine-components
```

```bash
poetry add dash-mantine-components
```

##### Anaconda

You can also install `dash-mantine-components` with conda through the conda-forge channel.

```bash
conda install -c conda-forge dash-mantine-components
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
code for some inspiration.

While going through this documentation, you will come across interactive demos meant to show an overview as well as the overall effect of different combinations of a component's props.

.. exec-block::docs.getting-started.interactive
    :prism: false

Note that this documentation has some additional styling applied to it. So when you actually use these components, they 
might look a bit different. You can check out [MantineProvider]("/components/mantineprovider) for more details on
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
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
    },
    styles={"Button": {"root": {"fontWeight": 400}}},
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[dmc.Button("Settings")],
)

if __name__ == "__main__":
    app.run_server()
```

##### Gallery

For some components you will also find a dedicated section showcasing some ready-made components along with their
source code. Any [contributions](https://github.com/snehilvj/dash-mantine-components) to this section or docs in 
general is highly appreciated.
