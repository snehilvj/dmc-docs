from dash import Dash, html, Output, Input
import dash_mantine_components as dmc
from utils import create_component_title

progress = html.Div(
    [
        create_component_title("Progress"),
        dmc.Progress(
            id="progress",
            value=69,
        ),
        dmc.Space(h=20),
        dmc.Button("Update Progress with random number", id="progress-button"),
        dmc.Space(h=30),
    ]
)
