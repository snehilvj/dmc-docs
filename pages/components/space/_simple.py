import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Group([dmc.Badge("Badge 1"), dmc.Badge("Badge 2")]),
        dmc.Group([dmc.Badge("Badge 1"), dmc.Space(w="sm"), dmc.Badge("Badge 2")]),
        dmc.Group([dmc.Badge("Badge 1"), dmc.Space(w="xl"), dmc.Badge("Badge 2")]),
    ]
)
