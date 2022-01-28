import dash_mantine_components as dmc
from dash import html

component = dmc.Container(
    padding=200, children=[html.Div(style={"border": "1px solid", "height": 200})]
)
