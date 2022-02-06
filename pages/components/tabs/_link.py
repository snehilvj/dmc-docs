import dash_mantine_components as dmc
from dash import dcc

component = dmc.Group(
    [
        dmc.Text("Refer to", color="gray"),
        dcc.Link(
            "dmc.Tab",
            href="/components/tab",
            className="home-page-buttons",
        ),
        dmc.Text("for its properties.", color="gray"),
    ],
    style={"marginBottom": 10},
    spacing=4,
)
