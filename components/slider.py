import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

slider = html.Div(
    [
        create_component_title("Slider"),
        dmc.Slider(
            id="slider",
            min=0,
            max=100,
            marks=[
                {"value": 20, "label": "20%"},
                {"value": 50, "label": "50%"},
                {"value": 80, "label": "80%"},
            ],
        ),
        dmc.Space(h=20),
        dmc.Group(
            [
                dmc.Text(id="slider-output"),
                dmc.Text(id="slider-drag-output"),
            ]
        ),
        dmc.Space(h=30),
    ]
)
