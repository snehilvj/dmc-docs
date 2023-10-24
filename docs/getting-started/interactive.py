import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "getting-started-button-interactive"

target = dmc.Center(dmc.Button("Settings", id=TARGET_ID))

configurator = Configurator(target, TARGET_ID)

configurator.add_select(
    "variant",
    ["link", "filled", "outline", "light", "gradient", "subtle", "default"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_switch("loading", False)

component = configurator.panel
