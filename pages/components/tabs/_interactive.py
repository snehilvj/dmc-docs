import dash_mantine_components as dmc
from dash import html

from lib.interactive import (
    DemoSelect,
    MantineThemeColorSwatches,
    DemoSlider,
    DemoSegmentedControl,
)

component = html.Div(
    [
        dmc.Center(
            style={"display": "flex"},
            children=[
                dmc.Tabs(
                    [
                        dmc.Tab("Gallery tab content", label="Gallery"),
                        dmc.Tab("Messages tab content", label="Messages"),
                        dmc.Tab("Settings tab content", label="Settings"),
                    ],
                    tabPadding="sm",
                    id="tabs-demo",
                    style={"flex": 1, "marginRight": 30},
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        MantineThemeColorSwatches(id="color-tabs-demo"),
                        DemoSegmentedControl(
                            id="variant-tabs-demo",
                            label="Variant",
                            values=["Default", "Outline", "Pills"],
                            initial_value="default",
                        ),
                        DemoSlider(
                            id="padding-tabs-demo", label="Padding", initial_value=2
                        ),
                        DemoSegmentedControl(
                            id="orientation-tabs-demo",
                            label="Orientation",
                            values=["Horizontal", "Vertical"],
                            initial_value="horizontal",
                        ),
                        DemoSelect(
                            id="position-tabs-demo",
                            value="left",
                            label="Position",
                            data=[
                                "left",
                                "right",
                                "center",
                                "apart",
                            ],
                        ),
                        dmc.Switch(
                            label="Grow",
                            id="grow-tabs-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="tabs-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
