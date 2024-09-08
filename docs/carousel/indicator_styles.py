import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Center(f"Slide {i}", bg="blue", c="white", h="100%"))
        for i in range(1, 4)
    ],
    id="carousel-indicator-styles",
    withIndicators=True,
    height=200,
    loop=True,
    classNames={"indicator": "dmc-indicator"},
)
