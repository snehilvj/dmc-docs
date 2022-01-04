import dash_mantine_components as dmc
from dash import html

title = "Notifications"
doc = dmc.NotificationsProvider.__doc__ + "\n\n\n" + dmc.NotificationHandler.__doc__

layout = html.Div(
    children=[
        dmc.Text("Simple", color="dimmed"),
        dmc.Space(h=10),
        dmc.NotificationsProvider(
            dmc.NotificationHandler(id="notifications-demo-handler"),
            autoClose=False,
            position="top-right",
        ),
        dmc.Group(
            [
                dmc.Button("Show notifications", id="show-notifications-demo"),
                dmc.Button("Update notifications", id="update-notifications-demo"),
                dmc.Button("Hide notifications", id="hide-notifications-demo"),
            ]
        ),
    ]
)
