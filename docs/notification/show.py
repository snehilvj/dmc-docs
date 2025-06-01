
import dash_mantine_components as dmc
from dash import Output, Input, html, callback, no_update
from dash_iconify import DashIconify


component = html.Div([
    # Place one NotificationContainer in app.layout)
    dmc.Button("Show Notification", id="notification-show")

])

@callback(
    Output("notification-container", "sendNotifications"),
    Input("notification-show", "n_clicks"),
    prevent_initial_call=True,
)
def show(n_clicks):
    if n_clicks is None:
        return no_update
    return [dict(
        title="Hey there!",
        id="show-notify",
        action="show",
        message="Notifications in Dash, Awesome!",
        icon=DashIconify(icon="ic:round-celebration"),
    )]
