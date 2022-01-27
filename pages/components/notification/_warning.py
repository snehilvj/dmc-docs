import dash_mantine_components as dmc
from dash import dcc
from dash_iconify import DashIconify

component = dmc.Alert(
    [
        dmc.Group(
            spacing="xs",
            children=[
                "In order to show notifications in your apps, you need to wrap your layout inside a "
                "NotificationsProvider.",
                dcc.Link(
                    DashIconify(icon="akar-icons:link-out", style={"marginBottom": -2}),
                    href="/components/notifications-provider",
                    className="home-page-buttons",
                ),
            ],
        )
    ],
    color="yellow",
)
