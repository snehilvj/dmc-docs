import dash_mantine_components as dmc
from dash import Output, Input, callback


component = dmc.Box(
    [
        dmc.Chip("Awesome chip", checked=True, id="chip-state"),
        dmc.Text(id="chip-container"),
    ],
    p=20,
)


@callback(Output("chip-container", "children"), Input("chip-state", "checked"))
def checkbox(checked):
    return f"The chip is selected: {checked}"
