import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(
            dmc.Center(f"Slide {i}", ta="center", bg="blue", c="white", h="100%")
        )
        for i in range(1, 7)
    ],
    id="carousel-drag-free",
    withIndicators=True,
    height=200,
    slideGap="md",
    emblaOptions = {"loop": True, "align": "start", "dragFree": True},
)
