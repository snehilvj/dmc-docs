import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import Configurator

target = dmc.Alert(
    icon=DashIconify(icon="radix-icons:cross-circled"),
    title="Bummer",
    children="Something terrible happened! You made a mistake and there is no going back, your data was lost forever!",
)

configurator = Configurator(target)

configurator.add_colorpicker("color", "red")
configurator.add_switch("withCloseButton", False)
configurator.add_select(
    "variant",
    ["light", "filled", "outline", "transparent", "white", "default"],
    "light",
)
configurator.add_slider("radius", "sm")

component = configurator.panel
