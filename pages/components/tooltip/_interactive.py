import dash_mantine_components as dmc
from dash import html, callback, Output, Input

from lib.interactive import (
    DemoSelect,
    MantineThemeColorSwatches,
    DemoSlider,
    DemoSegmentedControl,
)

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
                        dmc.Tooltip(
                            label="Tooltip",
                            id="tooltip-demo",
                            withArrow=True,
                            children=[
                                dmc.Button(
                                    "Tooltip",
                                    variant="outline",
                                    size="xl",
                                )
                            ],
                        )
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        MantineThemeColorSwatches(
                            id="color-tooltip-demo", value="#25262b"
                        ),
                        DemoSlider(
                            id="radius-tooltip-demo", label="Radius", initial_value=2
                        ),
                        DemoSelect(
                            id="position-tooltip-demo",
                            value="top",
                            label="Position",
                            data=[
                                "top",
                                "left",
                                "right",
                                "bottom",
                            ],
                        ),
                        DemoSegmentedControl(
                            id="placement-tooltip-demo",
                            label="Placement",
                            values=["Start", "Center", "End"],
                            initial_value="center",
                        ),
                        dmc.Switch(
                            label="With Arrow",
                            id="arrow-tooltip-demo",
                            checked=True,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="tooltip-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)


@callback(Output("tooltip-demo", "opened"), Input("tooltip-code-output", "children"))
def opened(children):
    # time.sleep(2)
    return True
