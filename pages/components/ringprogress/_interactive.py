import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        html.Div(
            style={"display": "flex"},
            children=[
                dmc.Center(
                    style={"flex": 1},
                    children=[
                        dmc.RingProgress(
                            id="ringprogress-demo",
                            size=120,
                            thickness=12,
                            roundCaps=False,
                            sections=[
                                {"value": 40, "color": "red"},
                                {"value": 15, "color": "yellow"},
                                {"value": 15, "color": "violet"},
                            ],
                        ),
                    ],
                ),
                dmc.Group(
                    style={"width": 200},
                    direction="column",
                    align="flex-start",
                    children=[
                        dmc.NumberInput(
                            id="size-ringprogress-demo",
                            value=120,
                            label="Size",
                        ),
                        dmc.NumberInput(
                            id="thickness-ringprogress-demo",
                            value=12,
                            label="Thickness",
                        ),
                        dmc.Switch(
                            label="Rounded Caps",
                            id="caps-ringprogress-demo",
                            checked=False,
                        ),
                    ],
                ),
            ],
        ),
        dmc.Prism(
            "",
            id="ringprogress-code-output",
            language="python",
            style={"marginTop": 30},
        ),
    ]
)
