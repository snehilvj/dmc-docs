import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

component = html.Div(
    [
        dmc.Button("Open Modal", id="modal-demo-button"),
        dmc.Modal(
            title="New Modal",
            id="modal",
            children=[
                dmc.Text("I am in a modal component."),
                dmc.Space(h=20),
                dmc.Group(
                    [
                        dmc.Button("Submit", id="modal-submit-button"),
                        dmc.Button(
                            "Close",
                            color="red",
                            variant="outline",
                            id="modal-close-button",
                        ),
                    ],
                    position="right",
                ),
            ],
        ),
    ]
)


@callback(
    Output("modal", "opened"),
    Input("modal-demo-button", "n_clicks"),
    Input("modal-close-button", "n_clicks"),
    Input("modal-submit-button", "n_clicks"),
    State("modal", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, nc2, nc3, opened):
    return not opened
