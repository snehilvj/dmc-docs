import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Group(
    [dmc.Button(val, variant="outline") for val in ["1", "2", "3"]],
    justify="flex-start",
)

configurator = Configurator(target)
configurator.add_select("justify", ["flex-start", "center", "flex-end", "space-around"], "center")
configurator.add_slider("gap", "md")
configurator.add_switch("grow", False)

component = configurator.panel
