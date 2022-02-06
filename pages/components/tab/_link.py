import dash_mantine_components as dmc
from dash import dcc

component = dmc.Group(
    [
        dmc.Text("Refer to", color="gray"),
        dcc.Link(
            "dmc.Tabs",
            href="/components/tabs",
            className="home-page-buttons",
        ),
        dmc.Text("to use tabs in your dash app.", color="gray"),
    ],
    style={"marginBottom": 10},
    spacing=4,
)
