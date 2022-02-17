import dash_mantine_components as dmc
from dash import html

from lib.interactive import DemoSelect, DemoSlider, DemoSegmentedControl

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    [
                        dmc.Group(
                            children=[
                                dmc.Button(val, variant="outline", fullWidth=True)
                                for val in ["1", "2", "3"]
                            ],
                            id="group-demo",
                            style={"flex": 1},
                        )
                    ],
                    style={"flex": 1, "paddingRight": 20},
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    grow=True,
                    children=[
                        DemoSelect(
                            id="position-group-demo",
                            value="left",
                            label="Position",
                            data=[
                                "left",
                                "center",
                                "right",
                                "apart",
                            ],
                        ),
                        DemoSegmentedControl(
                            id="direction-group-demo",
                            label="Direction",
                            values=["row", "column"],
                            initial_value="row",
                        ),
                        DemoSlider(
                            label="Spacing", id="spacing-group-demo", initial_value=3
                        ),
                        dmc.Switch(
                            label="Grow",
                            id="grow-group-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "", id="group-code-output", language="python", style={"marginTop": 30}
        ),
    ]
)
