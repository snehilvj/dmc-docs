import dash_mantine_components as dmc
from dash import Output, Input, html, callback_context as ctx, no_update, callback

component = html.Div(
    [
        html.Div(id="caveat-container"),
        dmc.Group(
            children=[
                dmc.Button(
                    "Better way",
                    id="better-notification",
                ),
                dmc.Button(
                    "Normal way",
                    id="normal-notification",
                ),
            ],
        ),
    ],
)


@callback(
    Output("caveat-container", "children"),
    Input("better-notification", "n_clicks"),
    Input("normal-notification", "n_clicks"),
    prevent_initial_call=True,
)
def notify(nc1, nc2):
    if not ctx.triggered:
        return no_update
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if "better" in button_id:
            return dmc.Notification(
                id="better-notify",
                title="Better way",
                message=["You will be able to open this notification multiple times."],
                action="show",
            )
        else:
            return dmc.Notification(
                id="normal-notify",
                title="Normal way",
                message="This won't come up again until you refresh the app or create another notification.",
                action="show",
            )
