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
                        dmc.Button(
                            "Settings",
                            id="button-demo",
                            variant="filled",
                            color="blue",
                            radius="sm",
                            size="sm",
                            loading=False,
                            compact=False,
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSelect(
                            id="variant-button-demo",
                            value="filled",
                            label="Variant",
                            data=[
                                "filled",
                                "outline",
                                "light",
                                "gradient",
                                "white",
                                "default",
                            ],
                        ),
                        MantineThemeColorSwatches(id="color-button-demo"),
                        DemoSlider(
                            id="radius-button-demo", label="Radius", initial_value=2
                        ),
                        DemoSlider(
                            id="size-button-demo", label="Size", initial_value=2
                        ),
                        dmc.TextInput(
                            id="children-button-demo",
                            value="Settings",
                            label="Children",
                        ),
                        dmc.Switch(
                            label="Compact",
                            id="compact-button-demo",
                            checked=False,
                        ),
                        dmc.Switch(
                            label="Loading",
                            id="loading-button-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="button-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
