import dash_mantine_components as dmc

component = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Center(f"Slide {i}", bg="blue", c="white", h="100%"))
        for i in range(1, 7)
    ],
    id="carousel-size",
    withIndicators=True,
    height=200,
    slideSize="33.3333%",
    slideGap="md",
    emblaOptions = {"loop": True, "align": "start", "slidesToScroll": 3},
)
