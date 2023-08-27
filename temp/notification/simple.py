import dash_mantine_components as dmc
from dash import Output, Input, html, callback
from dash_iconify import DashIconify

"""
Wrap your layout inside a NotificationsProvider for your app.

app.layout = dmc.NotificationsProvider(
    html.Div(
        [
            html.Div(id="notifications-container"),
            dmc.Button("Show Notification", id="notify"),
        ]
    )
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
