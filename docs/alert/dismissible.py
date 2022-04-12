import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

component = html.Div(
    [
        dmc.Alert(
            "Something terrible happened! You made a mistake and there is no going back, your data was lost forever! ",
            title="Bummer!",
            id="alert",
            color="red",
            withCloseButton=True,
        ),
        dmc.Space(h=20),
        dmc.Button("Toggle alert", id="alert-button"),
    ]
)


@callback(
    Output("alert", "hide"),
    Input("alert-button", "n_clicks"),
    State("alert", "hide"),
    prevent_initial_call=True,
)
def alert(n_clicks, hide):
    return not hide
