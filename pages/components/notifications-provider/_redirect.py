from dash import dcc
import dash_mantine_components as dmc

component = dmc.Group(
    spacing=5,
    children=[
        "For more information:",
        dcc.Link(
            "Notification",
            href="/components/notification",
            className="home-page-buttons",
        ),
    ],
)
