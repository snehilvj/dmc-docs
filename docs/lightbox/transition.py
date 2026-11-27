from dash import html, callback, Input, Output
import dash_mantine_components as dmc

slides = [
    {"src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png"},
    {"src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-2.png"},
    {"src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-3.png"},
    {"src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-4.png"},
    {"src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-5.png"},
]

component = dmc.Box([
    dmc.Lightbox(
        id="lightbox-transition",
        opened=False,
        slides=slides,
        currentIndex=0,
        withSlideTransition=True,
        withThumbnails=True,
    ),
    dmc.Button("Open lightbox with slide transition", id="open-lightbox-transition"),
])



@callback(
    Output("lightbox-transition", "opened"),
    Input("open-lightbox-transition", "n_clicks"),
    prevent_initial_call=True,
)
def open_lightbox(n):
    return True