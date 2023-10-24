import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-switch"

target = dmc.Center(dmc.Switch(label="I agree to sell my privacy", checked=True, id=TARGET_ID))

configurator = Configurator(target, TARGET_ID)

configurator.add_segmented_control("labelPosition", ["right", "left"], "right")
configurator.add_text_input(
    "label", "I agree to sell my privacy", **{"placeholder": "Label"}
)
configurator.add_text_input("description", "", **{"placeholder": "Description"})
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "lg")
configurator.add_colorpicker("color", "indigo")
configurator.add_switch("disabled", False)

component = configurator.panel
