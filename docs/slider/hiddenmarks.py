from dash import Input, Output, callback
import dash_mantine_components as dmc

marks = [
    {"value": 0, "label": "0%"},
    {"value": 25, "hidden": True},
    {"value": 50, "label": "50%"},
    {"value": 75, "hidden": True},
    {"value": 100, "label": "100%"},
]

component = dmc.Stack(
    [
        dmc.Text(
            id="hidden-marks-slider-value",
            size="sm",
            children="Hidden marks allow you to snap to specific values "
            "without displaying them visually. Current value: 50",
        ),
        dmc.Slider(
            id="hidden-marks-slider",
            value=50,
            min=0,
            max=100,
            step=1,
            restrictToMarks=True,
            marks=marks,
        ),
    ],
)

@callback(
    Output("hidden-marks-slider-value", "children"),
    Input("hidden-marks-slider", "value"),
)
def update_value(value):
    return (
        "Hidden marks allow you to snap to specific values without displaying "
        f"them visually. Current value: {value}"
    )

