import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-rating"

target = dmc.Group(dmc.Rating(defaultValue=2, count=5, id=TARGET_ID), position="center")

configurator = Configurator(target, TARGET_ID)

configurator.add_colorpicker("color", "yellow")
configurator.add_slider("size", "sm")
configurator.add_number_input("count",5, **{"min": 1, "max":15})
configurator.add_number_input("value",2, **{"min": 1, "max":15})
configurator.add_switch("highlightSelectedOnly", False)

component = configurator.panel
