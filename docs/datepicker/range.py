import dash_mantine_components as dmc
from dash import Input, Output, html, callback


component = dmc.Stack([
    dmc.DatePicker(
        id="date-picker-range",
        value=[],
        type="range"
    ),
    dmc.Text(id="date-picker-out-range"),

], align="center")


@callback(
    Output("date-picker-out-range", "children"), Input("date-picker-range", "value")
)
def update_output(d):
    return f"You selected {str(d)}"