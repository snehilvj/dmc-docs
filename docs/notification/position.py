import dash
import dash_mantine_components as dmc
from dash import callback, Output, Input

positions = ['top-left', 'top-right', 'bottom-left', 'bottom-right', 'top-center', 'bottom-center']

component =  dmc.RadioGroup(
    children=dmc.Group([dmc.Radio(p, value=p) for p in positions], my=10),
    label="Select Notification position",
    value=None,
    id="notification-position"
)

@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Input("notification-position", "value"),
    prevent_initial_call=True,
)
def notify(value):
    if value:
        return [dict(
            title=f"Notification {value}",
            autoClose=True,
            action="show",
            message="Hello World",
            color="red",
            position=value,
        )]
    return dash.no_update