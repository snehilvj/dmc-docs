import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Burger(size="md", lineSize=2)

configurator = Configurator(target, center_component=True)

configurator.add_slider("size", "md")
configurator.add_number_slider("lineSize",2, min=1, max=10)

component = configurator.panel
