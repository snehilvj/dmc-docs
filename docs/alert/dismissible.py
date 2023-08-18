import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

component = html.Div(
    [
        dmc.Alert(
            "Something terrible happened! You made a mistake and there is no going back, your data was lost forever! ",
            title="Bummer!",
            id="alert-dismiss",
            color="red",
            withCloseButton=True,
        ),
        dmc.Button("Toggle alert", id="alert-button", mt=20),
    ]
)


@callback(
    Output("alert-dismiss", "hide"),
    Input("alert-button", "n_clicks"),
    State("alert-dismiss", "hide"),
    prevent_initial_call=True,
)
def alert(n_clicks, hide):
    return not hide
