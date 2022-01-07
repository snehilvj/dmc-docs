import dash_mantine_components as dmc
from dash import html

from lib.blocks import (
    Text,
    Heading,
    PageBlock,
    CodeBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "installation")

app.layout = PageBlock(
    title="Installation",
    children=[
        ComponentDescription(
            "You can install dash-mantine-components using pip or poetry."
        ),
        Heading("Pip", id="pip"),
        dmc.Prism(
            code="pip install dash-mantine-components",
            language="markdown",
            style={"marginBottom": 40},
        ),
        Heading("Poetry", id="poetry"),
        dmc.Prism(
            code="poetry add dash-mantine-components",
            language="markdown",
            style={"marginBottom": 40},
        ),
        Heading("Basic Usage", id="basic-usage"),
        Text(
            "Using Dash Mantine Components is pretty much the same as using Dash Bootstrap Components or the official "
            "Dash components. You can get the below output by running the following code."
        ),
        CodeBlock(__file__, "example.py", app),
        Heading("Raise Issue", id="raise-issue"),
        Text(
            "If you find any issues with any components or the documentation, please create an issue."
        ),
        dmc.Group(
            [
                html.A(
                    [
                        dmc.Button(
                            [
                                html.I(
                                    className="bi bi-box-arrow-up-right",
                                    style={"marginRight": 10},
                                ),
                                "Create Issue on Dash Mantine Components",
                            ],
                            variant="outline",
                            color="dark",
                        ),
                    ],
                    href="https://github.com/snehilvj/dash-mantine-components/issues/new",
                ),
                html.A(
                    [
                        dmc.Button(
                            [
                                html.I(
                                    className="bi bi-file-earmark-text-fill",
                                    style={"marginRight": 10},
                                ),
                                "Create Issue on Docs",
                            ],
                            variant="outline",
                            color="dark",
                        ),
                    ],
                    href="https://github.com/snehilvj/dmc-demo/issues/new",
                ),
            ]
        ),
        dmc.Space(h=20),
        Heading("Support", id="support"),
        Text(
            "Now that you are here anyway, please consider giving **dash-mantine-components** a star on GitHub."
        ),
        html.A(
            [
                dmc.Button(
                    [
                        html.I(className="bi bi-star-fill", style={"marginRight": 10}),
                        "Star Dash Mantine Components on GitHub",
                    ],
                    variant="outline",
                ),
            ],
            href="https://github.com/snehilvj/dash-mantine-components",
        ),
        dmc.Space(h=50),
    ],
)
