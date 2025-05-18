import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import Configurator

target = dmc.ThemeIcon(children=DashIconify(icon="tabler:photo", width=20))

configurator = Configurator(target, center_component=True)

configurator.add_segmented_control("variant", ["filled", "light", "outline"], "filled")
configurator.add_slider("size", "md")
configurator.add_slider("radius", "sm")
configurator.add_colorpicker("color", "indigo")

component = configurator.panel
