import dash_mantine_components as dmc
from dash import html

from lib.configurator import create_configurator

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

controls = [
    {"property": "grow", "component": "Switch", "checked": False},
    {"property": "gutter", "component": "DemoSlider", "value": "md"},
]

demo = dmc.Grid(
    children=[
        dmc.Col(html.Div("1", style=style), span=4),
        dmc.Col(html.Div("2", style=style), span=4),
        dmc.Col(html.Div("3", style=style), span=4),
        dmc.Col(html.Div("4", style=style), span=4),
        dmc.Col(html.Div("5", style=style), span=4),
    ],
    gutter="md",
)

component = create_configurator(demo, controls, center=False)
