import dash_mantine_components as dmc
from dash import callback, html, Output, Input

component = html.Div(
    [
        dmc.RangeSlider(
            id="range-slider-callback",
            value=[26, 50],
            marks=[
                {"value": 20, "label": "20%"},
                {"value": 50, "label": "50%"},
                {"value": 80, "label": "80%"},
            ],
            mb=35,
        ),
        dmc.Text(id="range-slider-output"),
    ]
)


@callback(
    Output("range-slider-output", "children"), Input("range-slider-callback", "value")
)
def update_value(value):
    return f"You have selected: [{value[0]}, {value[1]}]"
