import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.Group(
    gap=50,
    children=[
        dmc.TimePicker(
            label="Enter a time",
            debounce=1000,
            id="timepicker-debounce-ms"
        ),
        dmc.Text(id="out-timepicker-debounce-ms")
    ],
)

@callback(
    Output("out-timepicker-debounce-ms", "children"),
    Input("timepicker-debounce-ms", "value")
)
def update(value):
    return f"You entered: {value}"