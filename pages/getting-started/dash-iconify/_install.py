import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Prism("pip install dash-iconify", language="bash"),
        dmc.Space(h=10),
        dmc.Prism("poetry add dash-iconify", language="bash"),
    ]
)
