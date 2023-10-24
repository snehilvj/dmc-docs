import dash_mantine_components as dmc
from dash import html
from docs.scrollarea.text import text
from components.configurator import Configurator

TARGET_ID = "interactive-scrollarea"

target = html.Div(
    [
        dmc.Title("Charizard (Pokémon)", order=3),
        dmc.ScrollArea(
            h=250, w=350,
            children = dmc.Paper(dmc.Text(text), withBorder=True),
            id=TARGET_ID
        )
    ]
)

configurator = Configurator(target, TARGET_ID)

configurator.add_select("type", ["auto", "scroll", "always", "never", "hover"], "hover")
configurator.add_number_input("scrollbarSize", 10, **{"min": 2, "max": 20, "step": 2})
configurator.add_number_input("scrollHideDelay", 1000, **{"min": 0, "max": 4000, "step": 500})
configurator.add_switch("offsetScrollbars", False)

component = configurator.panel
