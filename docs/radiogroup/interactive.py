import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-radio"

target = dmc.Center(dmc.Radio(label="Radio item", id=TARGET_ID))

configurator = Configurator(target, target_id=TARGET_ID)

configurator.add_segmented_control("labelPosition", ["right", "left"], "right")
configurator.add_text_input("label", "Radio item", **{"placeholder": "Label"})
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_switch("disabled", False)

component = configurator.panel
