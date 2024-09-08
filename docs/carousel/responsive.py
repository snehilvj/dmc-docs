import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(
            dmc.Center(f"Slide {i}", ta="center", bg="blue", c="white", h="100%")
        )
        for i in range(1, 7)
    ],
    id="carousel-responsive",
    withIndicators=True,
    height=200,
    slideSize={"base": "100%", "sm": "50%", "md": "33.333333%"},
    slideGap={"base": 0, "sm": "md"},
    loop=True,
    align="start",
)
