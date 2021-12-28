import dash_mantine_components as dmc
from dash import html

title = "Badge"
doc = dmc.Badge.__doc__


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
                                    dmc.Badge("Badge", id="badge-demo"),
                                    style={"height": 240},
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
                                                        id="variant-badge-demo",
                                                        value="light",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "light",
                                                                "filled",
                                                                "outline",
                                                                "dot",
                                                                "gradient",
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
                                                        id="color-badge-demo",
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
                                                        id="radius-badge-demo",
                                                        value="xl",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": "xs",
                                                                "label": "xs",
                                                            },
                                                            {
                                                                "value": "sm",
                                                                "label": "sm",
                                                            },
                                                            {
                                                                "value": "md",
                                                                "label": "md",
                                                            },
                                                            {
                                                                "value": "lg",
                                                                "label": "lg",
                                                            },
                                                            {
                                                                "value": "xl",
                                                                "label": "xl",
                                                            },
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Size", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="size-badge-demo",
                                                        value="md",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": "xs",
                                                                "label": "xs",
                                                            },
                                                            {
                                                                "value": "sm",
                                                                "label": "sm",
                                                            },
                                                            {
                                                                "value": "md",
                                                                "label": "md",
                                                            },
                                                            {
                                                                "value": "lg",
                                                                "label": "lg",
                                                            },
                                                            {
                                                                "value": "xl",
                                                                "label": "xl",
                                                            },
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Children", size="sm"),
                                                    dmc.TextInput(
                                                        id="children-badge-demo",
                                                        value="Badge",
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
                dmc.Badge(
                    "Indigo cyan",
                    variant="gradient",
                    gradient={"from": "indigo", "to": "cyan"},
                ),
                dmc.Badge(
                    "Lime green",
                    variant="gradient",
                    gradient={"from": "teal", "to": "lime", "deg": 105},
                ),
                dmc.Badge(
                    "Teal blue",
                    variant="gradient",
                    gradient={"from": "teal", "to": "blue", "deg": 60},
                ),
                dmc.Badge(
                    "Orange red",
                    variant="gradient",
                    gradient={"from": "orange", "to": "red"},
                ),
                dmc.Badge(
                    "Grape pink",
                    variant="gradient",
                    gradient={"from": "grape", "to": "pink", "deg": 35},
                ),
            ]
        ),
    ]
)
