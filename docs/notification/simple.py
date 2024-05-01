import dash_mantine_components as dmc
from dash import Output, Input, html, callback
from dash_iconify import DashIconify

"""
Add Notifications to your app layout.

app.layout = html.Div(
    [
        dmc.NotificationProvider(),
        html.Div(id="notifications-container"),
        dmc.Button("Show Notification", id="notify"),
    ]
)

"""

component = html.Div(
    [
        html.Div(id="notifications-container"),
        dmc.Button("Show Notification", id="notify"),
    ]
)


@callback(
    Output("notifications-container", "children"),
    Input("notify", "n_clicks"),
    prevent_initial_call=True,
)
def show(n_clicks):
    return dmc.Notification(
        title="Hey there!",
        id="simple-notify",
        action="show",
        message="Notifications in Dash, Awesome!",
        icon=DashIconify(icon="ic:round-celebration"),
    )
