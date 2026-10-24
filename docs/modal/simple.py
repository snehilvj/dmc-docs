import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Button("Open Modal", id="modal-demo-button", n_clicks=0),
        dmc.Modal(
            title="New Modal",
            id="modal-simple",
            children=dmc.Text("I am in a modal component."),                      ),
    ]
)


@callback(
    Output("modal-simple", "opened"),
    Input("modal-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def modal_demo(n):
    if n > 0:
        return True
