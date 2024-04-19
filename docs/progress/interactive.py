import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Progress(radius="sm", size="md", value=69)

configurator = Configurator(target)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "lg")
configurator.add_slider("radius", "sm")
configurator.add_number_input("value", 69, **{"min": 0, "max": 100, "step": 10})
configurator.add_switch("striped", False)
configurator.add_switch("animated", False)

component = configurator.panel
