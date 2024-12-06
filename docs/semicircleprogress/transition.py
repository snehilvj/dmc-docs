
import random
import dash_mantine_components as dmc
from dash import Input, Output, callback

component = dmc.Box([
    dmc.SemiCircleProgress(value=30, transitionDuration=250, label="30%", id="semi-circle-progress"),
    dmc.Button("Set random value", mt="md", ml=22, id="semi-circle-progress-btn"),

])

@callback(
    Output("semi-circle-progress", "value"),
    Output("semi-circle-progress", "label"),
    Input("semi-circle-progress-btn", "n_clicks")
)
def update(n):
    number = random.randint(1, 100)
    return number, f"{number}%"

