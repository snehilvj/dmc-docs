import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.Stack(
    [
        dmc.Button("1", variant="outline"),
        dmc.Button("2", variant="outline"),
        dmc.Button("3", variant="outline"),
    ],
    style={"height": 200},
    align="flex-start",
    justify="center",
)

configurator = Configurator(target)

configurator.add_select(
    "align", ["stretch", "center", "flex-end", "flex-start"], "flex-start"
)
configurator.add_select(
    "justify",
    ["space-between", "space-around", "center", "flex-end", "flex-start"],
    "center",
)
configurator.add_slider("spacing", "sm")


component = configurator.panel
