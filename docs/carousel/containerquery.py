import dash_mantine_components as dmc
from dash import html

component = html.Div(
    # Wrapper div is added for demonstration purposes only,
    #  It is not required in real projects
    dmc.Carousel(
        [
            dmc.CarouselSlide(dmc.Center("Slide-1", bg="blue", c="white", p=60)),
            dmc.CarouselSlide(dmc.Center("Slide-2", bg="blue", c="white", p=60)),
            dmc.CarouselSlide(dmc.Center("Slide-3", bg="blue", c="white", p=60)),
        ],
        id="carousel-container",
        type="container",
        slideSize = {"base": '100%', '300px': '50%', '500px': '33.333333%'},
        slideGap = {"base": 0, '300px': 'md', '500px': 'lg'},
        emblaOptions = {"loop": True, "align": "start"},
    ),
    style={
        "resize": 'horizontal',
        "overflow": 'hidden',
        "maxWidth": '100%',
        "minWidth": 250,
        "padding": 10,
      }
)
