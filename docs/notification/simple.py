import dash
import dash_mantine_components as dmc
from dash import Output, Input, html, callback
from dash_iconify import DashIconify


component = html.Div([
    dmc.Button("Show Notification", id="notify"),
    html.Div(id="notifications-container")
])

@callback(
    Output("notifications-container", "children"),
    Input("notify", "n_clicks"),
    prevent_initial_call=True,
)
def show(n_clicks):
    if n_clicks is None:
        return dash.no_update
    return dmc.Notification(
        title="Hey there!",
        id="simple-notify",
        action="show",
        message="Notifications in Dash, Awesome!",
        icon=DashIconify(icon="ic:round-celebration"),
    )
