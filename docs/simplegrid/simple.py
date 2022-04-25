import dash_mantine_components as dmc
from dash import html

from lib.configurator import create_configurator

controls = [
    {"property": "cols", "component": "NumberInput", "value": 3, "min": 1, "max": 6},
    {"property": "spacing", "component": "DemoSlider", "value": "md"},
]

style = {
    "backgroundColor": dmc.theme.DEFAULT_COLORS["indigo"][4],
    "textAlign": "center",
}

demo = dmc.SimpleGrid(
    cols=3,
    children=[
        html.Div("1", style=style),
        html.Div("2", style=style),
        html.Div("3", style=style),
        html.Div("4", style=style),
        html.Div("5", style=style),
    ],
)

component = create_configurator(demo, controls, center=False)
