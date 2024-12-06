import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-burger"

target = dmc.Center(dmc.Burger(size="md", lineSize=2, id=TARGET_ID))

configurator = Configurator(target, TARGET_ID)

configurator.add_slider("size", "md")
configurator.add_number_slider("lineSize",2, min=1, max=10)

component = configurator.panel
