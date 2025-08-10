import dash_mantine_components as dmc
from lib.configurator import Configurator

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

target = dmc.Grid(
    children=[
        dmc.GridCol(dmc.Box("1", style=style), span=4),
        dmc.GridCol(dmc.Box("2", style=style), span=4),
        dmc.GridCol(dmc.Box("3", style=style), span=4),
        dmc.GridCol(dmc.Box("4", style=style), span=4),
        dmc.GridCol(dmc.Box("5", style=style), span=4),
    ],
    gutter="md",
)

configurator = Configurator(target)
configurator.add_switch("grow", False)
configurator.add_slider("gutter", "md")

component = configurator.panel
