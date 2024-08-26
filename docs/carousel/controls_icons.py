import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Center(f"Slide {i}", ta="center", bg="blue", c="white", h="100%"))
        for i in range(1, 7)
    ],
    id="carousel-controls_icons",
    withIndicators=True,
    height=180,
    nextControlIcon= DashIconify(icon="flat-ui:settings", width=30),
    previousControlIcon="",
    loop=True,

)
