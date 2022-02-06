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
                            "Input Props",
                            id="timeinput-demo",
                            label="My label",
                            description="My description",
                            error="error",
                            variant="default",
                            radius="sm",
                            size="sm",
                            withSeconds=False,
                            disabled=False,
                            required=True,
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        dmc.TextInput(
                            id="label-timeinput-demo",
                            value="My label",
                            label="Label",
                        ),
                        dmc.TextInput(
                            id="description-timeinput-demo",
                            value="My description",
                            label="Description",
                        ),
                        dmc.TextInput(
                            id="error-timeinput-demo",
                            value=None,
                            label="Error",
                        ),
                        DemoSelect(
                            id="variant-timeinput-demo",
                            value="filled",
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
                            label="With seconds",
                            id="withseconds-timeinput-demo",
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
