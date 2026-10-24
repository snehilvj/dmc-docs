import dash_mantine_components as dmc

from docs.scrollarea.text import text
from lib.configurator import Configurator

target = dmc.ScrollArea(
    h=250,
    w=350,
    type="always",
    scrollbars="y",
    children=dmc.Paper([dmc.Title("Charizard (Pokémon)", order=3), dmc.Text(text)]),
)

configurator = Configurator(target, center_component=True)
configurator.add_segmented_control("verticalScrollbarPosition", ["right", "left"], "right")
configurator.add_switch("offsetScrollbars", False)

component = configurator.panel
