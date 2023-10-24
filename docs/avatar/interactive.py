import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.Avatar(src="/assets/avatar.jpeg")

configurator = Configurator(target)

configurator.add_slider("radius", "sm")
configurator.add_slider("size", "md")

component = configurator.panel
