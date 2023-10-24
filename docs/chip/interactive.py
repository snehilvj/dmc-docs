import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-chip"

target = dmc.Center(
    dmc.Chip("Dash Mantine Components", variant="outline", id=TARGET_ID)
)

configurator = Configurator(target, TARGET_ID)

configurator.add_colorpicker("color", "indigo")
configurator.add_select("variant", ["outline", "filled"], "outline")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "xl")

component = configurator.panel
