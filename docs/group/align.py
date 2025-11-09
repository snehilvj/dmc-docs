import dash_mantine_components as dmc
from lib.configurator import Configurator

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
    "margin": 2,
    "width": 100
}

target = dmc.Grid(
    children=[
        dmc.Box("1", style=style),
        dmc.Box("2", style={**style, "minHeight": 80}),
        dmc.Box("3", style={**style, "minHeight": 120}),
    ],
)

configurator = Configurator(target)

configurator.add_select(
    "align", ["stretch", "center", "flex-end", "flex-start"], "center"
)

component = configurator.panel
