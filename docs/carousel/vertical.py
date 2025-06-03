import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(
            dmc.Center(f"Slide {i}", ta="center", bg="blue", c="white", h="100%")
        )
        for i in range(1, 7)
    ],
    id="carousel-vertical",
    orientation="vertical",
    withIndicators=True,
    height=200,
    emblaOptions={"loop": True},
)
