import dash_mantine_components as dmc
from dash import html
from components.configurator import Configurator

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

target = dmc.Grid(
    children=[
        dmc.Col(html.Div("1", style=style), span=4),
        dmc.Col(html.Div("2", style=style), span=4),
        dmc.Col(html.Div("3", style=style), span=4),
        dmc.Col(html.Div("4", style=style), span=4),
        dmc.Col(html.Div("5", style=style), span=4),
    ],
    gutter="md",
)

configurator = Configurator(target)
configurator.add_switch("grow", False)
configurator.add_slider("gutter", "md")

component = configurator.panel
