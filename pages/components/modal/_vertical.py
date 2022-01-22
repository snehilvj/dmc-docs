import dash_mantine_components as dmc
from dash import callback  # no-prism
from dash import html, Output, Input, State

component = html.Div(
    [
        dmc.Modal(
            title="Centered Modal",
            id="modal-centered",
            centered=True,
            children=[dmc.Text("This is a vertically centered modal.")],
        ),
        dmc.Button("Open modal", id="modal-centered-button"),
    ]
)


@callback(
    Output("modal-centered", "opened"),
    Input("modal-centered-button", "n_clicks"),
    State("modal-centered", "opened"),
    prevent_initial_call=True,
)
def toggle_modal(n_clicks, opened):
    return not opened
