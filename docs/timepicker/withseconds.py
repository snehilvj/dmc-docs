import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.Group(
    gap=50,
    children=[
        dmc.TimePicker(label="Enter a time", withSeconds=True, id="timepicker-seconds"),
        dmc.Text(id="out-timepicker-seconds")
    ],
)

@callback(
    Output("out-timepicker-seconds", "children"),
    Input("timepicker-seconds", "value")
)
def update(value):
    return f"You entered: {value}"