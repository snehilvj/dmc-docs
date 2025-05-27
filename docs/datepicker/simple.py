import dash_mantine_components as dmc
from dash import Input, Output, html, callback


component = dmc.Stack([
    dmc.DatePicker(id="date-picker"),
    dmc.Text(id="selected-date-picker", mt=10),
], align="center")


@callback(
    Output("selected-date-picker", "children"), Input("date-picker", "value")
)
def update_output(d):
    return f"You selected {d}"
