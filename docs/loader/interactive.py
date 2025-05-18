import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Loader()

configurator = Configurator(target, center_component=True)

configurator.add_colorpicker("color", "red")
configurator.add_slider("size", "md")
configurator.add_segmented_control("type", ["oval", "bars", "dots"], "oval")

component = configurator.panel
