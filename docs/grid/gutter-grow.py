import dash_mantine_components as dmc
from dash import html
from lib.configurator import Configurator

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
}

target = dmc.Grid(
    children=[
        dmc.GridCol(html.Div("1", style=style), span=4),
        dmc.GridCol(html.Div("2", style=style), span=4),
        dmc.GridCol(html.Div("3", style=style), span=4),
        dmc.GridCol(html.Div("4", style=style), span=4),
        dmc.GridCol(html.Div("5", style=style), span=4),
    ],
    gutter="md",
)

configurator = Configurator(target)
configurator.add_switch("grow", False)
configurator.add_slider("gutter", "md")

component = configurator.panel
