import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.Progress(radius="sm", size="md", value=69)

configurator = Configurator(target)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_number_input("value", 69, **{"min": 0, "max": 100, "step": 10})
configurator.add_switch("striped", False)
configurator.add_switch("animate", False)

component = configurator.panel
