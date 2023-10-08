import dash_mantine_components as dmc
from dash import html

from docs.scrollarea.text import text


component = html.Div(
    [
        dmc.Title("Charizard (Pokémon)", order=3),
        dmc.ScrollArea(
            h=250, w=350,
            children = dmc.Paper(dmc.Text(text), withBorder=True, w=600),
        )
    ]
)
