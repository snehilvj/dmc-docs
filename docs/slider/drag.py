import dash_mantine_components as dmc
from dash import callback, html, Output, Input

component = html.Div(
    [
        dmc.Slider(
            id="drag-slider",
            value=26,
            updatemode="drag",
            marks=[
                {"value": 20, "label": "20%"},
                {"value": 50, "label": "50%"},
                {"value": 80, "label": "80%"},
            ],
        ),
        dmc.Space(h=35),
        dmc.Text(id="drag-output"),
    ]
)


@callback(Output("drag-output", "children"), Input("drag-slider", "value"))
def update_value(value):
    return f"You have selected: {value}"
