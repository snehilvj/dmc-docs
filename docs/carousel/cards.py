import dash_mantine_components as dmc
from dash import html

data = [
    {
        "image": "https://images.unsplash.com/photo-1508193638397-1c4234db14d8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
        "title": "Best forests to visit in North America",
        "category": "NATURE",
    },
    {
        "image": "https://images.unsplash.com/photo-1559494007-9f5847c49d94?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
        "title": "Hawaii beaches review: better than you think",
        "category": "BEACH",
    },
    {
        "image": "https://images.unsplash.com/photo-1608481337062-4093bf3ed404?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
        "title": "Mountains at night: 12 best locations to enjoy the view",
        "category": "NATURE",
    },
    {
        "image": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
        "title": "Best places to visit this winter",
        "category": "TOURISM",
    },
    {
        "image": "https://images.unsplash.com/photo-1582721478779-0ae163c05a60?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
        "title": "Active volcanos reviews: travel at your own risk",
        "category": "NATURE",
    },
]


def make_card(image, title, category):
    return dmc.Paper(
        [
            html.Div(
                [
                    dmc.Text(category, c="white", opacity=0.7, fw=700),
                    dmc.Title(title, lh=1.2, order=3, mt="xs", fw=900, c="white"),
                ]
            ),
            dmc.Button("Read Article", variant="white", color="dark"),
        ],
        shadow="md",
        p="xl",
        radius="md",
        style={
            "backgroundImage": f"url({image})",
            "height": 440,
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "space-between",
            "alignItems": "flex-start",
            "backgroundSize": "cover",
            "backgroundPosition": "center",
        },
    )


component = dmc.Carousel(
    [dmc.CarouselSlide(make_card(d["image"], d["title"], d["category"])) for d in data],
    id="carousel-cards",
    w=400,
    emblaOptions={"loop": True, "align": "start"},
)
