from dash import callback, Input, Output
import dash_mantine_components as dmc

slides = [
    {
        "src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png"
    },
    {
        "type": "custom",
        "render": {"function": "renderCustomSlide"},
        "renderThumb": {"function": "renderCustomThumb"},
        "caption": "Custom slide with render function",
    },
    {
        "type": "custom",
        "render": {"function": "renderYouTube"},
        "renderThumb": {"function": "renderYouTubeThumb"},
        "caption": "Embedded YouTube video",
    },
    {
        "src": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-3.png"
    },
]

component = dmc.Box([
    dmc.Lightbox(
        id="lightbox-custom",
        opened=False,
        slides=slides,
        withThumbnails=True,
    ),
    dmc.Button("Open lightbox with custom slides", id="open-lightbox-custom"),
])


@callback(
    Output("lightbox-custom", "opened"),
    Input("open-lightbox-custom", "n_clicks"),
    prevent_initial_call=True,
)
def open_lightbox(n):
    return True




