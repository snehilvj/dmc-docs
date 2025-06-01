import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Badge("Badge")

configurator = Configurator(target, center_component=True)

configurator.add_select(
    "variant", ["light", "filled", "outline", "dot", "gradient"], "light"
)
configurator.add_colorpicker("color", "blue")
configurator.add_slider("size", "md")
configurator.add_slider("radius", "xl")

component = configurator.panel
