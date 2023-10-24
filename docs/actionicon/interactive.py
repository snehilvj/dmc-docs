import dash_mantine_components as dmc
from dash_iconify import DashIconify

from components.configurator import Configurator

TARGET_ID = "actionicon-interactive"
target = dmc.Center(
    dmc.ActionIcon(DashIconify(icon="clarity:settings-line", width=20), id=TARGET_ID)
)

configurator = Configurator(target, TARGET_ID)

configurator.add_select(
    "variant",
    ["filled", "outline", "light", "subtle", "default", "transparent"],
    "filled",
)
configurator.add_colorpicker("color", "orange")
configurator.add_slider("size", "lg")
configurator.add_slider("radius", "sm")
configurator.add_switch("loading", False)
configurator.add_switch("disabled", False)

component = configurator.panel
