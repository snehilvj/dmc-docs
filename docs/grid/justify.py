import dash_mantine_components as dmc
from components.configurator import Configurator

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
    "margin": 2,
}

target = dmc.Grid(
    children=[
        dmc.Col("1", style=style, span=3),
        dmc.Col("2", style={**style, "minHeight": 80}, span=3),
        dmc.Col("3", style={**style, "minHeight": 120}, span=3),
    ],
)

configurator = Configurator(target)
configurator.add_select(
    "justify",
    ["space-between", "space-around", "center", "flex-end", "flex-start"],
    "flex-start",
)
configurator.add_select(
    "align", ["stretch", "center", "flex-end", "flex-start"], "stretch"
)
configurator.add_switch("grow", False)
configurator.add_slider("gutter", "md")

component = configurator.panel
