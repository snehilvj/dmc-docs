import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.Group(
    gap=50,
    children=[
        dmc.TimePicker(label="Enter a time", id="timepicker-usage"),
        dmc.Text(id="out-timepicker")
    ],
)

@callback(
    Output("out-timepicker", "children"),
    Input("timepicker-usage", "value")
)
def update(value):
    return f"You entered: {value}"