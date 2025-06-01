import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.Group(
    gap=50,
    children=[
        dmc.TimePicker(
            label="Enter a time",
            debounce=True,
            id="timepicker-debounce"
        ),
        dmc.Text(id="out-timepicker-debounce")
    ],
)

@callback(
    Output("out-timepicker-debounce", "children"),
    Input("timepicker-debounce", "value")
)
def update(value):
    return f"You entered: {value}"