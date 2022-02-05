import dash_mantine_components as dmc
from dash import html

from lib.interactive import DemoSlider

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1, "padding": "0 100px"},
                    children=[
                        dmc.Paper(
                            children=[
                                dmc.Text(
                                    "Paper is the most basic ui component. Use it to create cards, dropdowns, "
                                    "modals and other components that require background with shadow "
                                )
                            ],
                            id="paper-demo",
                            radius="sm",
                            padding="lg",
                            shadow="sm",
                            withBorder=False,
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSlider(
                            id="radius-paper-demo", label="Radius", initial_value=2
                        ),
                        DemoSlider(
                            id="padding-paper-demo", label="Padding", initial_value=4
                        ),
                        DemoSlider(
                            id="shadow-paper-demo", label="Shadow", initial_value=2
                        ),
                        dmc.Switch(
                            label="With Border",
                            id="border-paper-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="paper-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
