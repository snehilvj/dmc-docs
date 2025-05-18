import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Avatar()

configurator = Configurator(target, center_component=True)

configurator.add_select("variant", ["filled", "light", "outline", "transparent", "white", "default"], "filled")
configurator.add_slider("radius", "sm")
configurator.add_slider("size", "md")

component = configurator.panel
