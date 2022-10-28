import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

component = html.Div(
    [
        dmc.Modal(title="Size: lg", id="modal-size-lg", size="lg"),
        dmc.Modal(title="Size: 378px", id="modal-size-378", size=378),
        dmc.Modal(title="Size: 55%", id="modal-size-55", size="55%"),
        dmc.Modal(title="Size: full", id="modal-size-full", fullScreen=True),
        dmc.Group(
            [
                dmc.Button("lg", id="lg-modal-button"),
                dmc.Button("378px", id="378-modal-button"),
                dmc.Button("55%", id="55-modal-button"),
                dmc.Button("full", id="full-modal-button"),
            ]
        ),
    ]
)


def toggle_modal(n_clicks, opened):
    return not opened


for size in ["lg", "378", "55", "full"]:
    callback(
        Output(f"modal-size-{size}", "opened"),
        Input(f"{size}-modal-button", "n_clicks"),
        State(f"modal-size-{size}", "opened"),
        prevent_initial_call=True,
    )(toggle_modal)
