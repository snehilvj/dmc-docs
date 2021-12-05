from dash import html
import dash_mantine_components as dmc
from utils import create_component_title

notifications = html.Div(
    [
        create_component_title("Notifications"),
        dmc.NotificationsProvider(
            dmc.NotificationHandler(id="handler"), autoClose=False, position="top-right"
        ),
        dmc.Group(
            [
                dmc.Button("Show notifications", id="show"),
                dmc.Button("Update notifications", id="update"),
                dmc.Button("Hide notifications", id="hide"),
            ]
        ),
        dmc.Space(h=30),
    ]
)
