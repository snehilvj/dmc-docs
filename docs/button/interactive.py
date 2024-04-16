import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "button-interactive"

target = dmc.Center(dmc.Button("Settings", id=TARGET_ID))

configurator = Configurator(target, TARGET_ID)

configurator.add_select(
    "variant",
    ["link", "filled", "outline", "light", "gradient", "subtle", "default"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("loading", False)
configurator.add_switch("disabled", False)

component = configurator.panel
