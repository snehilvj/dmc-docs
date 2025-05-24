import dash_mantine_components as dmc
from dash import Input, Output, callback, no_update

component = dmc.Paper(
    [
        dmc.Select(
            label="Set initial slide",
            data=[str(i) for i in range(6)],
            value="0",
            id="carousel-input",
            mb=10,
        ),
        dmc.Carousel(
            [
                dmc.CarouselSlide(
                    dmc.Center(
                        f"Slide {i}", ta="center", bg="blue", c="white", h="100%"
                    )
                )
                for i in range(6)
            ],
            id="carousel-initial",
            height=200,
            emblaOptions = {"loop": True, "align": "start"},
        ),
    ]
)


@callback(
    Output("carousel-initial", "initialSlide"),
    Input("carousel-input", "value"),
)
def go_to_slide(value):
    return int(value)
