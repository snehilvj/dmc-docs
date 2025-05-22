import dash
import dash_mantine_components as dmc
from dash import Output, Input, html, callback_context as ctx, callback
from dash_iconify import DashIconify

component = html.Div(
    [
        html.Div(id="notifications-container2"),
        dmc.Group(
            [
                dmc.Button(
                    "Load Data",
                    id="show-notification",
                    n_clicks=0
                ),
                dmc.Button(
                    "Update",
                    id="update-notification",
                    n_clicks=0
                ),
            ],
        ),
    ],
)


@callback(
    Output("notifications-container2", "children"),
    Input("show-notification", "n_clicks"),
    Input("update-notification", "n_clicks"),
    prevent_initial_call=True,
)
def notify(nc1, nc2):
    button_id = ctx.triggered_id
    if nc1 > 0:
        if "show" in button_id:
            return dmc.Notification(
                id="my-notification",
                title="Process initiated",
                message="The process has started.",
                loading=True,
                color="orange",
                action="show",
                autoClose=False,
            )
    if nc2 > 0:
        if "update" in button_id:
            return dmc.Notification(
                id="my-notification",
                title="Data loaded",
                message="Notification closing in 2 seconds",
                color="green",
                loading=False,
                action="update",
                autoClose=2000,
                icon=DashIconify(icon="akar-icons:circle-check"),
            )
    return dash.no_update
