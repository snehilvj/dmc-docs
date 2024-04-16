import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-checkbox"

target = dmc.Center(
    dmc.Checkbox(label="I agree to sell my privacy.", checked=True, id=TARGET_ID)
)

configurator = Configurator(target, TARGET_ID)

configurator.add_segmented_control("labelPosition", ["left", "right"], "right")
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")

component = configurator.panel
