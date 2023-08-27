import dash_mantine_components as dmc
from dash import callback, html, Output, Input

component = html.Div(
    [
        dmc.Slider(
            id="slider-callback",
            value=26,
            marks=[
                {"value": 20, "label": "20%"},
                {"value": 50, "label": "50%"},
                {"value": 80, "label": "80%"},
            ],
            mb=35,
        ),
        dmc.Text(id="slider-output"),
    ]
)


@callback(Output("slider-output", "children"), Input("slider-callback", "value"))
def update_value(value):
    return f"You have selected: {value}"
