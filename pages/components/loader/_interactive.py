import dash_mantine_components as dmc
from dash import html

from lib.interactive import DemoSelect, MantineThemeColorSwatches, DemoSlider

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
                        dmc.Loader(
                            id="loader-demo",
                            variant="oval",
                            color="blue",
                            size="md",
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSelect(
                            id="variant-loader-demo",
                            value="oval",
                            label="Variant",
                            data=[
                                "oval",
                                "bars",
                                "dots",
                            ],
                        ),
                        MantineThemeColorSwatches(id="color-loader-demo"),
                        DemoSlider(
                            id="size-loader-demo", label="Size", initial_value=3
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="loader-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
