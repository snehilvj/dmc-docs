from dash import callback, Input, Output, no_update
import dash_mantine_components as dmc

component = dmc.Group(
    justify="center",
    children=[
        dmc.Button("Show 10 notifications", id="show-btn", n_clicks=0),
        dmc.Button("Clean queue", id="clean-queue-btn", variant="default", n_clicks=0),
        dmc.Button("Clean all", id="clean-all-btn", variant="outline", color="red", n_clicks=0),
    ]
)


@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Input("show-btn", "n_clicks"),
    prevent_initial_call=True
)
def show_notifications(n):
    return [
        {
            "action": "show",
            "title": f"Notification {i + 1}",
            "message": "Most notifications are added to queue",
            "autoClose": False,
        }
        for i in range(10)
    ]


@callback(
    Output("notification-container", "cleanQueue"),
    Input("clean-queue-btn", "n_clicks"),
    prevent_initial_call=True
)
def clean_queue(n):
    if n > 0:
        return True
    return no_update


@callback(
    Output("notification-container", "clean"),
    Input("clean-all-btn", "n_clicks"),
    prevent_initial_call=True
)
def clean_all(n):
    if n > 0:
        return True
    return no_update
