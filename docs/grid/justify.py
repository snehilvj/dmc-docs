import dash_mantine_components as dmc
from lib.configurator import Configurator

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
    "margin": 2,
}

target = dmc.Grid(
    children=[
        dmc.GridCol("1", style=style, span=3),
        dmc.GridCol("2", style={**style, "minHeight": 80}, span=3),
        dmc.GridCol("3", style={**style, "minHeight": 120}, span=3),
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
