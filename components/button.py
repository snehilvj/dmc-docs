import dash_mantine_components as dmc
from dash import html

title = "Button"
doc = dmc.Button.__doc__

layout = html.Div(
    children=[
        dmc.Text("Interactive Demo", color="dimmed"),
        dmc.Space(h=10),
        dmc.Paper(
            withBorder=True,
            padding="md",
            children=[
                dmc.Grid(
                    align="stretch",
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Button("Settings", id="button-demo"),
                                    style={"height": 275},
                                )
                            ],
                            span=8,
                        ),
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Group(
                                        direction="column",
                                        grow=True,
                                        children=[
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Variant", size="sm"),
                                                    dmc.Select(
                                                        id="variant-button-demo",
                                                        value="filled",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "filled",
                                                                "outline",
                                                                "light",
                                                                "gradient",
                                                                "white",
                                                                "default",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Color", size="sm"),
                                                    dmc.Select(
                                                        id="color-button-demo",
                                                        value="blue",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "dark",
                                                                "gray",
                                                                "red",
                                                                "pink",
                                                                "grape",
                                                                "violet",
                                                                "indigo",
                                                                "blue",
                                                                "cyan",
                                                                "teal",
                                                                "green",
                                                                "lime",
                                                                "yellow",
                                                                "orange",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Radius", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="radius-button-demo",
                                                        value="sm",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": s,
                                                                "label": s,
                                                            }
                                                            for s in [
                                                                "xs",
                                                                "sm",
                                                                "md",
                                                                "lg",
                                                                "xl",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Size", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="size-button-demo",
                                                        value="sm",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": s,
                                                                "label": s,
                                                            }
                                                            for s in [
                                                                "xs",
                                                                "sm",
                                                                "md",
                                                                "lg",
                                                                "xl",
                                                            ]
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.SimpleGrid(
                                                cols=2,
                                                children=[
                                                    dmc.Switch(
                                                        label="Loading",
                                                        id="loading-button-demo",
                                                    ),
                                                    dmc.Switch(
                                                        label="Compact",
                                                        id="compact-button-demo",
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Children", size="sm"),
                                                    dmc.TextInput(
                                                        id="children-button-demo",
                                                        value="Settings",
                                                    ),
                                                ],
                                            ),
                                        ],
                                    )
                                )
                            ],
                            span=4,
                        ),
                    ],
                )
            ],
        ),
        dmc.Space(h=50),
        dmc.Text("With Gradient", color="dimmed"),
        dmc.Space(h=10),
        dmc.Group(
            children=[
                dmc.Button(
                    "Indigo cyan",
                    variant="gradient",
                    gradient={"from": "indigo", "to": "cyan"},
                ),
                dmc.Button(
                    "Lime green",
                    variant="gradient",
                    gradient={"from": "teal", "to": "lime", "deg": 105},
                ),
                dmc.Button(
                    "Teal blue",
                    variant="gradient",
                    gradient={"from": "teal", "to": "blue", "deg": 60},
                ),
                dmc.Button(
                    "Orange red",
                    variant="gradient",
                    gradient={"from": "orange", "to": "red"},
                ),
                dmc.Button(
                    "Grape pink",
                    variant="gradient",
                    gradient={"from": "grape", "to": "pink", "deg": 35},
                ),
            ]
        ),
    ]
)
