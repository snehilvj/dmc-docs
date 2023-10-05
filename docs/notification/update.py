import dash_mantine_components as dmc
from dash import Output, Input, html, callback_context as ctx, no_update, callback
from dash_iconify import DashIconify

component = html.Div(
    [
        html.Div(id="notify-container"),
        dmc.Group(
            children=[
                dmc.Button(
                    "Load Data",
                    id="show-notification",
                ),
                dmc.Button(
                    "Update",
                    id="update-notification",
                ),
            ],
        ),
    ],
)


@callback(
    Output("notify-container", "children"),
    Input("show-notification", "n_clicks"),
    Input("update-notification", "n_clicks"),
    prevent_initial_call=True,
)
def notify(nc1, nc2):
    if not ctx.triggered:
        return no_update
    else:
        button_id = ctx.triggered_id
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
        else:
            return dmc.Notification(
                id="my-notification",
                title="Data loaded",
                message="The process has started.",
                color="green",
                action="update",
                icon=DashIconify(icon="akar-icons:circle-check"),
            )
