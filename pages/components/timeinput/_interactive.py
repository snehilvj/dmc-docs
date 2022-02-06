import dash_mantine_components as dmc
from dash import html

from lib.interactive import DemoSelect, DemoSlider

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
                        dmc.TimeInput(
                            id="timeinput-demo",
                            label="Start Time",
                            description="This is a description.",
                            variant="default",
                            radius="sm",
                            size="sm",
                            withSeconds=False,
                            disabled=False,
                            required=True,
                            style={"width": 150}
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSelect(
                            id="variant-timeinput-demo",
                            value="default",
                            label="Variant",
                            data=["default", "filled", "unstyled", "headless"],
                        ),
                        DemoSlider(
                            id="radius-timeinput-demo", label="Radius", initial_value=2
                        ),
                        DemoSlider(
                            id="size-timeinput-demo", label="Size", initial_value=2
                        ),
                        dmc.Switch(
                            label="With Seconds",
                            id="seconds-timeinput-demo",
                            checked=False,
                        ),
                        dmc.Switch(
                            label="Disabled",
                            id="disabled-timeinput-demo",
                            checked=False,
                        ),
                        dmc.Switch(
                            label="Required",
                            id="required-timeinput-demo",
                            checked=True,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="timeinput-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
