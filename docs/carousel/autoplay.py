import dash
import dash_mantine_components as dmc
from dash import html, callback, Input, Output

component = html.Div([
    dmc.Button("start", id="carousel-autoplay-btn", variant="outline", color="black", n_clicks=0),
    dmc.Carousel(
        [
            dmc.CarouselSlide(dmc.Center("Slide-1", bg="blue", c="white", p=60)),
            dmc.CarouselSlide(dmc.Center("Slide-2", bg="blue", c="white", p=60)),
            dmc.CarouselSlide(dmc.Center("Slide-3", bg="blue", c="white", p=60)),
        ],
        id="carousel-autoplay",
        mt="sm",
        loop=True,
        autoplay=False,  # Default delay is 4000ms
    )
])

@callback(
    Output("carousel-autoplay", "autoplay"),
    Input("carousel-autoplay-btn", "n_clicks")
)
def start(n):
    if n > 0:
        return True
    return dash.no_update