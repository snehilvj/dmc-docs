import dash_mantine_components as dmc
from dash import Output, Input, State, callback, ALL, ctx, html


images = [
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png",
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-2.png",
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-3.png",
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-4.png",
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-5.png",
]

slides = [{"src": src} for src in images]

component = dmc.Box(
    [
        dmc.Lightbox(
            id="lightbox-usage",
            opened=False,
            slides=slides,
            currentIndex=0,
        ),
        dmc.SimpleGrid(
            cols=3,
            children=[
                html.Div(
                    dmc.Image(src=src, radius="md"),
                    style={"cursor": "pointer"},
                    id={"type": "lightbox-image-usage", "index": i},
                )
                for i, src in enumerate(images)
            ],
        ),
    ]
)



@callback(
    Output("lightbox-usage", "opened"),
    Output("lightbox-usage", "currentIndex"),
    Input({"type": "lightbox-image-usage", "index": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def open_lightbox(_):
    index = ctx.triggered_id["index"]
    return True, index