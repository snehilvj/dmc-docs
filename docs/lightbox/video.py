from dash import callback, Input, Output
import dash_mantine_components as dmc

video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
image_url = "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images"

slides = [
    {
        "type": "video",
        "src": video_url,
        "poster": f"{image_url}/bg-2.png",
        "caption": "Play this video, then navigate to the next slide – it pauses automatically",
        "autoPlay": True,
    },
    {
        "src": f"{image_url}/bg-1.png",
        "caption": "Image slide",
    },
    {
        "type": "video",
        "src": video_url,
        "poster": f"{image_url}/bg-4.png",
        "caption": "Another video - autoPlay is False",
    },
    {
        "src": f"{image_url}/bg-3.png",
        "caption": "Another image",
    },
]

component = dmc.Box([
    dmc.Lightbox(
        id="lightbox-video",
        opened=False,
        slides=slides,
        withThumbnails=True,
    ),
    dmc.Button("Open lightbox with videos", id="open-lightbox-video"),
])


@callback(
    Output("lightbox-video", "opened"),
    Input("open-lightbox-video", "n_clicks"),
    prevent_initial_call=True,
)
def open_lightbox(n):
    return True