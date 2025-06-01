import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.Group(
    gap=50,
    children=[
        dmc.TimePicker(label="Enter a time", format="12h", id="timepicker-12"),
        dmc.Text(id="out-timepicker-12")
    ],
)

@callback(
    Output("out-timepicker-12", "children"),
    Input("timepicker-12", "value")
)
def update(value):
    return f"You entered: {value}"