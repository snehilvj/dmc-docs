import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Center(f"Slide {i}", bg="blue", c="white", h="100%"))
        for i in range(1, 4)
    ],
    id="carousel-show-controls-on-hover",
    height=200,
    classNames={"controls": "dmc-controls", "root": "dmc-root"},
)
