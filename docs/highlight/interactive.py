import dash_mantine_components as dmc

from utils.configurator import Configurator

target = dmc.Highlight(
    "Highlight this, definitely this and also this!", highlight="this"
)

configurator = Configurator(target)
configurator.add_colorpicker("color", "lime")

component = configurator.panel
