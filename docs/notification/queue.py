
from dash import Output, Input, callback, ctx, no_update
import dash_mantine_components as dmc

component = dmc.Button("Show 10 notifications", id="notify-btn", n_clicks=0),


@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Input("notify-btn", "n_clicks"),
    prevent_initial_call=True
)
def queue_notifications(n):
    if n > 0:
        return [
            {
                "action": "show",
                "title": f"Notification {i + 1}",
                "message": "Most notifications are added to queue",
                "autoClose": 3000,
                "withCloseButton": True,
            }
            for i in range(10)
        ]
    return no_update

