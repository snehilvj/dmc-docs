import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

title = html.Div(
    [
        create_component_title("Title"),
        dmc.Title("This is h1 title", order=1),
        dmc.Title("This is h2 title", order=2),
        dmc.Title("This is h3 title", order=3),
        dmc.Title("This is h4 title", order=4),
        dmc.Title("This is h5 title", order=5),
        dmc.Title("This is h6 title", order=6),
        dmc.Space(h=30),
    ]
)
