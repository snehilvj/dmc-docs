import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Text("No Marks"),
        dmc.Slider(value=59),
        dmc.Text("Marks but no label", style={"marginTop": 15}),
        dmc.Slider(
            value=69,
            marks=[{"value": 20}, {"value": 50}, {"value": 80}],
            style={"marginBottom": 15},
        ),
        dmc.Text("Marks with label"),
        dmc.Slider(
            value=79,
            marks=[
                {"value": 20, "label": "20%"},
                {"value": 50, "label": "50%"},
                {"value": 80, "label": "80%"},
            ],
        ),
    ]
)
