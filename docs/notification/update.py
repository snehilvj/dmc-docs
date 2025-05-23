
import dash_mantine_components as dmc
from dash import Output, Input, html, ctx, callback, no_update
from dash_iconify import DashIconify

component = html.Div(
    [
        dmc.Group(
            [
                dmc.Button(
                    "Load Data",
                    id="show-notifications",
                    n_clicks=0
                ),
                dmc.Button(
                    "Update",
                    id="update-notifications",
                    n_clicks=0
                ),
            ],
        ),
    ],
)


@callback(
    Output("notification-container", "sendNotifications",  allow_duplicate=True,),
    Input("show-notifications", "n_clicks"),
    Input("update-notifications", "n_clicks"),
    prevent_initial_call=True,
)
def notify(n1, n2):
    button_id = ctx.triggered_id
    if n1 and n1 > 0:
        if "show" in button_id:
            return [dict(
                id="my-load-notification",
                title="Process initiated",
                message="The process has started.",
                loading=True,
                color="orange",
                action="show",
                autoClose=False,
            )]
    if n2 and n2 > 0:
        if "update" in button_id:
            return [dict(
                id="my-load-notification",
                title="Data loaded",
                message="Notification closing in 2 seconds",
                color="green",
                loading=False,
                action="update",
                autoClose=2000,
                icon=DashIconify(icon="akar-icons:circle-check"),
            )]
    return no_update
