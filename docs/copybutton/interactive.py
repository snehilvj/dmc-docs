import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.CopyButton("Copy", copiedChildren="Copied")

configurator = Configurator(target, center_component=True)

configurator.add_select(
    "variant",
    ["filled", "outline", "light",  "subtle", "default", "transparent", "white"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_colorpicker("copiedColor", "red")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")


component = configurator.panel
