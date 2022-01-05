import dash_mantine_components as dmc

from lib.blocks import (
    Text,
    Heading,
    PageBlock,
    CodeBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "installation")

app.layout = PageBlock(
    title="Installation",
    children=[
        Text("You can install dash_mantine_components using pip or poetry."),
        Heading("Pip", id="pip"),
        dmc.Prism(
            code="pip install dash_mantine_components",
            language="markdown",
            style={"marginBottom": 40},
        ),
        Heading("Poetry", id="poetry"),
        dmc.Prism(
            code="poetry add dash_mantine_components",
            language="markdown",
            style={"marginBottom": 40},
        ),
        Heading("Basic Usage", id="basic-usage"),
        Text(
            "Using Dash Mantine Components is pretty much the same as using Dash Bootstrap Components or the official "
            "Dash components. You can get the below output by running the following code."
        ),
        CodeBlock(__file__, "example.py", app),
    ],
)
