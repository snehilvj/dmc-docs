import dash_mantine_components as dmc
from dash import Input, Output, html, callback


component = dmc.Stack([
    dmc.DatePicker(
        id="date-picker-allow-deselect",
        allowDeselect=True
    ),
    dmc.Text(id="date-picker-out-allow-deselect"),

], align="center")


@callback(
    Output("date-picker-out-allow-deselect", "children"), Input("date-picker-allow-deselect", "value")
)
def update_output(d):
    return f"You selected {d}"