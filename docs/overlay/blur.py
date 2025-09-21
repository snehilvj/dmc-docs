
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
                    id="overlay-blur",
                    color="#000",
                    backgroundOpacity=0.35,
                    blur=0
                )
            ]
        ),
        dmc.Text("Set Blur:"),
        dmc.Slider(
           id="overlay-blur-slider",
            min=0, max=15, value=5
        )
    ])


@callback(
    Output("overlay-blur", "blur"),
    Input("overlay-blur-slider", "value")
)
def toggle_overlay(v):
    return v


