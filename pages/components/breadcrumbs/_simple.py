import dash_mantine_components as dmc
from dash import dcc

component = dmc.Breadcrumbs(
    separator="→",
    children=[
        dcc.Link("Home", href="/"),
        dcc.Link("Dash Mantine Components", href="/"),
        dcc.Link("Breadcrumbs", href="/components/breadcrumbs"),
    ]
)
