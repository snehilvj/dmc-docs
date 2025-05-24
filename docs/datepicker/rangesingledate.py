import dash_mantine_components as dmc
from dash import Input, Output, html, callback


component = dmc.Stack([
    dmc.DatePicker(
        id="date-picker-range-s",
        value=[],
        type="range",
        allowSingleDateInRange=True
    ),
    dmc.Text(id="date-picker-out-range-s"),

], align="center")


@callback(
    Output("date-picker-out-range-s", "children"), Input("date-picker-range-s", "value")
)
def update_output(d):
    return f"You selected {str(d)}"