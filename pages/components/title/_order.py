import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [dmc.Title(f"This is h{order} title", order=order) for order in range(1, 7)]
)
