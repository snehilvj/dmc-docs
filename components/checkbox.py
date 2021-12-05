import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

checkbox = html.Div(
    [
        create_component_title("Checkbox"),
        dmc.Checkbox(label="This is a checkbox. Do you agree?"),
        dmc.Space(h=30),
    ]
)
