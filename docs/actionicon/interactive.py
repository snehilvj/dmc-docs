import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import Configurator

target = dmc.ActionIcon(DashIconify(icon="clarity:settings-line", width=20))

configurator = Configurator(target, center_component=True)

configurator.add_select(
    "variant",
    ["filled", "outline", "light", "subtle", "default", "transparent", "white", "gradient"],
    "filled",
)
configurator.add_colorpicker("color", "orange")
configurator.add_slider("size", "lg")
configurator.add_slider("radius", "sm")
configurator.add_switch("loading", False)
configurator.add_switch("disabled", False)

component = configurator.panel
