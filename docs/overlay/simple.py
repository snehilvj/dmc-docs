
import dash_mantine_components as dmc
from dash import Dash, Input, Output, callback, html


component = dmc.Stack([
        dmc.AspectRatio(
            ratio=16/9,
            maw=400,
            mx="auto",
            pos="relative",
            children=[
                html.Img(
                    src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png",
                    alt="Demo",
                ),
                dmc.Overlay(
                    id="overlay-usage",
                    color="#000",
                    backgroundOpacity=0.85,
                    style={"display": "block"}  # Initially visible
                )
            ]
        ),
        dmc.Button(
            "Toggle overlay",
            id="overlay-toggle-button",
            mx="auto",
            mt="lg",
            n_clicks=0
        )
    ])


@callback(
    Output("overlay-usage", "style"),
    Input("overlay-toggle-button", "n_clicks")
)
def toggle_overlay(n_clicks):
    if n_clicks %2 == 0:
        return {"display": "block"}
    return {"display": "none"}

