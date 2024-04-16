import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-loader"

target = dmc.Center(dmc.Loader(id=TARGET_ID))

configurator = Configurator(target, TARGET_ID)

configurator.add_colorpicker("color", "red")
configurator.add_slider("size", "md")
configurator.add_segmented_control("variant", ["oval", "bars", "dots"], "oval")

component = configurator.panel
