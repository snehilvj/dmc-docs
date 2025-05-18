import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Chip("Awesome chip", checked=True)

configurator = Configurator(target, center_component=True)

configurator.add_segmented_control("variant", ["filled", "outline", "light"], "light")
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "lg")

component = configurator.panel
