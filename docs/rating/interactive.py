import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Rating(value=2, count=5)

configurator = Configurator(target, center_component=True)

configurator.add_colorpicker("color", "yellow")
configurator.add_slider("size", "sm")
configurator.add_number_input("count", 5, **{"min": 1, "max": 15})
configurator.add_number_input("value", 2, **{"min": 1, "max": 15})
configurator.add_switch("highlightSelectedOnly", False)

component = configurator.panel
