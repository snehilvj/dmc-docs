import dash_mantine_components as dmc
from dash import html, dcc

from utils import components

header = dmc.Affix(
    children=[
        dmc.Paper(
            [
                dmc.Container(
                    [
                        dmc.Container(
                            [
                                dmc.Group(
                                    position="apart",
                                    children=[
                                        dmc.Anchor(
                                            "Dash Mantine Components",
                                            variant="gradient",
                                            size="xl",
                                            href="/",
                                            gradient={
                                                "from": "indigo",
                                                "to": "cyan",
                                                "deg": 45,
                                            },
                                        ),
                                        dmc.Group(
                                            [
                                                dmc.Select(
                                                    id="component-select",
                                                    placeholder="Search for component",
                                                    style={"width": 300},
                                                    data=[
                                                        {
                                                            "label": label,
                                                            "value": label.lower(),
                                                        }
                                                        for label in components
                                                    ],
                                                ),
                                                dcc.Link(
                                                    [
                                                        html.I(
                                                            className="bi bi-github",
                                                            style={
                                                                "fontSize": 25,
                                                                "color": "#1c7ed6",
                                                            },
                                                        )
                                                    ],
                                                    href="https://github.com/snehilvj/dash-mantine-components",
                                                    target="_blank",
                                                ),
                                            ]
                                        ),
                                    ],
                                )
                            ],
                            style={"paddingTop": 20},
                            size="lg",
                        )
                    ],
                    fluid=True,
                    style={"height": 75},
                )
            ],
            shadow="md",
        ),
    ],
    position={"top": 0, "left": 0},
    style={"width": "100vw"},
)
