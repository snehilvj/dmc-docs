import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Radio(label="Radio item")

configurator = Configurator(target)

configurator.add_segmented_control("labelPosition", ["right", "left"], "right")
configurator.add_text_input("label", "Radio item", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_switch("disabled", False)

component = configurator.panel
