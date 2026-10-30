import dash_mantine_components as dmc

from docs.scrollarea.text import text

component = dmc.Center(
    dmc.ScrollArea(
        h=200,
        w=350,
        startScrollPosition={ "y": 250},
        children=dmc.Paper(
            [dmc.Title("Charizard (Pokémon)", order=3), dmc.Text(text)], w=600
        ),
    ),
)
