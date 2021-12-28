import dash_mantine_components as dmc
from dash import html

title = "Drawer"
doc = dmc.Drawer.__doc__

layout = html.Div(
    children=[
        dmc.Drawer(id="drawer-demo", padding="md", children=[]),
        dmc.Text("Interactive Demo", color="dimmed"),
        dmc.Space(h=10),
        dmc.Paper(
            withBorder=True,
            padding="md",
            children=[
                dmc.Grid(
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Button("Open Drawer", id="drawer-demo-button"),
                                    style={"height": 170},
                                )
                            ],
                            span=7,
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
                                                    dmc.Text("Title", size="sm"),
                                                    dmc.TextInput(
                                                        id="title-drawer-demo",
                                                        value="Register",
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Position", size="sm"),
                                                    dmc.Select(
                                                        id="position-drawer-demo",
                                                        value="left",
                                                        searchable=False,
                                                        clearable=False,
                                                        data=[
                                                            {
                                                                "label": val.title(),
                                                                "value": val,
                                                            }
                                                            for val in [
                                                                "left",
                                                                "right",
                                                                "top",
                                                                "bottom",
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
                                                        id="size-drawer-demo",
                                                        value="lg",
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
                                                label="No overlay",
                                                id="overlay-drawer-demo",
                                            ),
                                        ],
                                    )
                                )
                            ],
                            span=5,
                        ),
                    ],
                )
            ],
        ),
    ]
)
