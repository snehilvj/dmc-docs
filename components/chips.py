import dash_mantine_components as dmc
from dash import html

title = "Chips"
doc = dmc.Chips.__doc__

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
                                    dmc.Chips(
                                        id="chips-demo",
                                        data=[
                                            {"value": "react", "label": "React"},
                                            {"value": "ng", "label": "Angular"},
                                            {"value": "svelte", "label": "Svelte"},
                                            {"value": "vue", "label": "Vue"},
                                        ],
                                        value="react",
                                    ),
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
                                                    dmc.Text("Color", size="sm"),
                                                    dmc.Select(
                                                        id="color-chips-demo",
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
                                                    dmc.Text("Variant", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="variant-chips-demo",
                                                        value="outline",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": "outline",
                                                                "label": "Outline",
                                                            },
                                                            {
                                                                "value": "filled",
                                                                "label": "Filled",
                                                            },
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Radius", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="radius-chips-demo",
                                                        value="xl",
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
                                                    dmc.Text("Spacing", size="sm"),
                                                    dmc.SegmentedControl(
                                                        id="spacing-chips-demo",
                                                        value="xs",
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
                                                        id="size-chips-demo",
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
                                            dmc.Switch(
                                                label="Multiple",
                                                id="multiple-chips-demo",
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
