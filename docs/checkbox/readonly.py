
from dash import Input, Output, callback
import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Checkbox(
            id="read-only-checkbox",
            checked=True,
            readOnly=True,
            label="Read only checkbox",
        ),
        dmc.Button("Toggle from callback", id="toggle-read-only-checkbox", mt="md"),
    ]
)


@callback(
    Output("read-only-checkbox", "checked"),
    Input("toggle-read-only-checkbox", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_checkbox(n_clicks):
    return n_clicks % 2 == 0

