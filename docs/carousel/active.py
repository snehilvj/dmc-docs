import dash_mantine_components as dmc
from dash import Input, Output, callback

component = dmc.Box(
    [
        dmc.Carousel(
            [
                dmc.CarouselSlide(
                    dmc.Center(f"Slide-{n+1}", bg="blue", c="white", p=60)
                )
                for n in range(6)
            ],
            id="carousel-active",
            loop=True,
            autoplay={
                "delay": 2000,
                "stopOnMouseEnter": True,
                "stopOnInteraction": False,
            },
        ),
        dmc.Pagination(id="pagination", total=6, value=1, withControls=False),
    ]
)


@callback(Output("pagination", "value"), Input("carousel-active", "active"))
def update(n):
    return n + 1
