import dash_mantine_components as dmc
from dash import html, Input, Output, callback


def make_carousel(id):
    return dmc.Carousel(
        loop=True,
        withIndicators=True,
        children=[
            dmc.CarouselSlide(
                dmc.Center(
                    slide,
                    bg="blue",
                    c="white",
                    p=60,
                )
            )
            for slide in ["Slide 1", "Slide 2", "Slide 3"]
        ],
        id=id,
    )


component = html.Div(
    [
        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.TabsTab("Tab one", value="1"),
                        dmc.TabsTab("Tab two", value="2"),
                    ]
                ),
            ],
            id="tabs-carousel-example",
            value="1",
        ),
        html.Div(id="tabs-carousel-content", style={"paddingTop": 10}),
    ]
)


@callback(
    Output("tabs-carousel-content", "children"), Input("tabs-carousel-example", "value")
)
def render_content(active):
    if active == "1":
        return [dmc.Text("Tab One selected", my=10), make_carousel("carousel-tab1")]
    else:
        return [dmc.Text("Tab Two selected", my=10), make_carousel("carousel-tab2")]
