import dash_mantine_components as dmc

from utils.configurator import Configurator

target = dmc.Toggle("B")

configurator = Configurator(target, center_component=True)

configurator.add_select(
    "variant",
    ["filled", "light"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("autoContrast", False)
configurator.add_switch("disabled", False)

component = configurator.panel
