import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-avatar"

target = dmc.Center(
    dmc.Avatar( id=TARGET_ID)
)

configurator = Configurator(target, TARGET_ID, "Avatar")

configurator.add_select("variant", ["filled", "light", "outline", "transparent", "white", "default"], "filled")
configurator.add_slider("radius", "sm")
configurator.add_slider("size", "md")

component = configurator.panel
