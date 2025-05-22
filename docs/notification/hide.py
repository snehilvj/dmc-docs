
import dash_mantine_components as dmc
from dash import Output, Input, html, ctx, callback, no_update

component = html.Div(
    [
        dmc.NotificationContainer(id="notification-container"),
        dmc.Group(
            [
                dmc.Button(
                    "Show",
                    id="notifications-show",
                    n_clicks=0
                ),
                dmc.Button(
                    "Hide",
                    id="notifications-hide",
                    n_clicks=0
                ),
            ],
        ),
    ],
)


@callback(
    Output("notification-container", "sendNotifications", allow_duplicate=True),
    Output("notification-container", "hideNotifications"),
    Input("notifications-show", "n_clicks"),
    Input("notifications-hide", "n_clicks"),
    prevent_initial_call=True,
)
def notify(n1, n2):
    button_id = ctx.triggered_id
    if n1 > 0:
        if "show" in button_id:
            return [dict(
                id="show-hide",
                action="show",
                message="Notification Message",
                color="Red",
                autoClose=False,
            )], no_update
    if n2 > 0:
        if "hide" in button_id:
            return no_update, ["show-hide"]
    return no_update
