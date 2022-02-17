import dash_mantine_components as dmc
from dash import html

from lib.interactive import MantineThemeColorSwatches, DemoSlider

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
                        dmc.Switch(
                            id="switch-demo",
                            label="I agree to sell my privacy.",
                            checked=True,
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        MantineThemeColorSwatches(id="color-switch-demo"),
                        DemoSlider(
                            id="radius-switch-demo", label="Radius", initial_value=5
                        ),
                        DemoSlider(
                            id="size-switch-demo", label="Size", initial_value=2
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="switch-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
