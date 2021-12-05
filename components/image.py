from dash import html
import dash_mantine_components as dmc
from utils import create_component_title

image = html.Div(
    [
        create_component_title("Image"),
        dmc.Image(
            src="https://imgk.timesnownews.com/story/Delhi_Pollution.png?tr=w-600,h-450,fo-auto",
            caption="Funny Meme",
            style={"width": 400},
            withPlaceholder=True,
        ),
        dmc.Space(h=30),
    ]
)
