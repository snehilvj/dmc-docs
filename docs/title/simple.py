import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Title(f"This is h1 title", order=1),
        dmc.Title(f"This is h2 title", order=2),
        dmc.Title(f"This is h3 title", order=3),
        dmc.Title(f"This is h4 title", order=4),
        dmc.Title(f"This is h5 title", order=5),
        dmc.Title(f"This is h6 title", order=6),
    ]
)
