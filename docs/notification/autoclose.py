from dash import Input, Output, callback, no_update
import dash_mantine_components as dmc

component = dmc.Group(
    justify="center",
    children=[
        dmc.Button("Closes in 4 seconds", id="default-close-btn", n_clicks=0),
        dmc.Button("Closes in 500ms", id="short-close-btn", n_clicks=0),
        dmc.Button("Never closes automatically", id="no-autoclose-btn", n_clicks=0),
      #  dmc.NotificationsContainer(id="notification-container"),
    ]
)


@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Input("default-close-btn", "n_clicks"),
    prevent_initial_call=True
)
def short_notification(n):
    if n > 0:
        return [{
            "action": "show",
            "message": "I will close in 4 seconds (the default auto close)",

        }]
    return no_update

@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Input("short-close-btn", "n_clicks"),
    prevent_initial_call=True
)
def short_notification(n):
    if n > 0:
        return [{
            "action": "show",
            "message": "I will close in 500ms",
            "autoClose": 500,
        }]
    return no_update


@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Input("no-autoclose-btn", "n_clicks"),
    prevent_initial_call=True
)
def sticky_notification(n):
    if n > 0:
        return [{
            "action": "show",
            "title": "I will never close",
            "message": "unless you click X",
            "color": "blue",
            "autoClose": False,
            "style": {"marginBottom": 20}
        }]
    return no_update
