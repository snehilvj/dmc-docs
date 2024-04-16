import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Alert(
            "This alert will dismiss itself after 3 seconds! ",
            title="Auto Dismissing Alert!",
            id="alert-auto",
            color="violet",
            duration=3000,
        ),
        dmc.Button("Show alert", id="alert-auto-button", mt=20),
    ]
)


@callback(
    Output("alert-auto", "hide"),
    Input("alert-auto-button", "n_clicks"),
    prevent_initial_call=True,
)
def alert_auto(n_clicks):
    return False
