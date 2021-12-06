import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

switch = html.Div(
    [
        create_component_title("Switch"),
        dmc.Switch(label="This is a switch.", checked=True),
        dmc.Space(h=30),
    ]
)
