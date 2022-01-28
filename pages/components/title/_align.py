import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Title("This is a title", align=align, order=3)
        for align in ["left", "right", "center"]
    ]
)
