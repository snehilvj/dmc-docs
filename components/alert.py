import dash_mantine_components as dmc
from dash import html

title = "Alert"
doc = dmc.Alert.__doc__


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
                                    dmc.Alert(
                                        "Something terrible happened! You made a mistake and there is no going back, your data was lost forever!",
                                        title="Bummer!",
                                        show=True,
                                        color="red",
                                        id="alert-demo",
                                    ),
                                    style={"height": 170},
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
                                                        id="color-alert-demo",
                                                        value="red",
                                                        searchable=False,
                                                        clearable=False,
                                                        style={"width": 185},
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
                                                    dmc.Text("Title", size="sm"),
                                                    dmc.TextInput(
                                                        id="title-alert-demo",
                                                        value="Bummer!",
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text("Children", size="sm"),
                                                    dmc.TextInput(
                                                        id="children-alert-demo",
                                                        value="Something terrible happened! You made a mistake and there is no going back, your data was lost forever!",
                                                    ),
                                                ],
                                            ),
                                            dmc.Switch(
                                                label="With close button",
                                                id="close-alert-demo",
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
        dmc.Text("Dismissable Alerts", color="dimmed"),
        dmc.Space(h=10),
        dmc.Alert(
            "Something terrible happened! You made a mistake and there is no going back, your data was lost forever! ",
            title="Bummer!",
            id="alert",
            color="violet",
            withCloseButton=True,
            show=True,
        ),
        dmc.Space(h=20),
        dmc.Button("Toggle alert", id="alert-button"),
    ]
)
