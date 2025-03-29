import dash_mantine_components as dmc
from dash import callback, Output, Input

positions = ['top-left', 'top-right', 'bottom-left', 'bottom-right', 'top-center', 'bottom-center']

component = dmc.Box(
    [
        dmc.Text("Display Notification at position:"),
        dmc.SegmentedControl( data=positions, value="top-right", id="notify-position"),
        dmc.Box(id="notifications-container3")
    ]
)

@callback(
    Output("notifications-container3", "children"),
    Input("notify-position", "value"),
    prevent_initial_call=True,
)
def notify(value):
    return dmc.Notification(
            title=f"Notification {value}",
            autoClose=True,
            action="show",
            message="Hello World",
            color="red",
            position=value

        )