import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-badge"

target = dmc.Center(dmc.Badge("Badge", id=TARGET_ID))

configurator = Configurator(target, TARGET_ID, "Badge")

configurator.add_select(
    "variant", ["light", "filled", "outline", "dot", "gradient"], "light"
)
configurator.add_colorpicker("color", "blue")
configurator.add_slider("size", "md")
configurator.add_slider("radius", "xl")

component = configurator.panel
