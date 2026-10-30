import dash_mantine_components as dmc
from dash_iconify import DashIconify

from utils.configurator import Configurator

target = dmc.Blockquote(
    "Life is like a box of chocolates - you never know what you are going to get",
    cite="- Forest Gump",
    icon=DashIconify(icon="mdi:gift-outline", width=26),
    color="green",
    iconSize=34,

)

configurator = Configurator(target)

configurator.add_colorpicker("color", "green")
configurator.add_number_slider("iconSize", 36, min=20, max=50 )
configurator.add_slider("radius", "lg")
component = configurator.panel
