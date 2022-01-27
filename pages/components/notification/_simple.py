import dash_mantine_components as dmc
from dash import Output, Input, html
from dash import callback  # no-prism
from dash_iconify import DashIconify

layout = dmc.NotificationsProvider(
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
def n_clicks(n_clicks):
    return dmc.Notification(
        title="Hey there!",
        id="simple-notify",
        action="show",
        message="Notifications in Dash, Awesome!",
        icon=[DashIconify(icon="ic:round-celebration")],
    )
