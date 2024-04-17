import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Group([dmc.Badge("Badge 1"), dmc.Badge("Badge 2")]),
        dmc.Space(h="xl"),
        dmc.Group([dmc.Badge("Badge 1"), dmc.Space(w="lg"), dmc.Badge("Badge 2")]),
        dmc.Space(h=30),
        dmc.Group([dmc.Badge("Badge 1"), dmc.Space(w=45), dmc.Badge("Badge 2")]),
    ]
)
