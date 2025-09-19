import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Button("Settings")

configurator = Configurator(target, center_component=True)

configurator.add_select(
    "variant",
    ["filled", "outline", "light", "gradient", "subtle", "default", "transparent", "white"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("loading", False)
configurator.add_switch("disabled", False)

component = configurator.panel
