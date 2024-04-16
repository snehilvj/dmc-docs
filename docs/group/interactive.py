import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Group(
    [dmc.Button(val, variant="outline") for val in ["1", "2", "3"]],
    justify="flex-start",
)

configurator = Configurator(target)
configurator.add_select("position", ["left", "right", "center", "apart"], "left")
configurator.add_slider("spacing", "md")
configurator.add_switch("grow", False)

component = configurator.panel
