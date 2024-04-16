import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Highlight(
    "Highlight this, definitely this and also this!", highlight="this"
)

configurator = Configurator(target)
configurator.add_colorpicker("highlightColor", "lime")

component = configurator.panel
