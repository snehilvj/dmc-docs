import dash_mantine_components as dmc
from dash import html

title = "Checkbox"
doc = dmc.Checkbox.__doc__


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
                                    dmc.Checkbox(
                                        label="I agree to sell my privacy",
                                        id="checkbox-demo",
                                        checked=True,
                                    ),
                                    style={"height": 140},
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
                                                    dmc.Text("Color", size="sm"),
                                                    dmc.Select(
                                                        id="color-checkbox-demo",
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
                                                    dmc.Text("Size", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="size-checkbox-demo",
                                                        value="sm",
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
                                                    dmc.Text("Label", size="sm"),
                                                    dmc.TextInput(
                                                        id="label-checkbox-demo",
                                                        value="I agree to sell my privacy",
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
    ]
)
