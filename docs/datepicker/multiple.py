import dash_mantine_components as dmc
from dash import Input, Output, html, callback


component = dmc.Stack([
    dmc.DatePicker(
        id="date-picker-multiple",
        value=[],
        type="multiple"
    ),
    dmc.Text(id="date-picker-out-multiple"),

], align="center")


@callback(
    Output("date-picker-out-multiple", "children"), Input("date-picker-multiple", "value")
)
def update_output(d):
    return f"You selected {str(d)}"