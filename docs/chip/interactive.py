import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-Chip"

target = dmc.Center(
    dmc.Chip("Awesome chip", checked=True, id=TARGET_ID)
)

configurator = Configurator(target, TARGET_ID, "Chip")

configurator.add_segmented_control("variant", ["filled", "outline", "light"], "light")
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "lg")

component = configurator.panel
