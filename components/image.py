import dash_mantine_components as dmc
from dash import html

title = "Image"
doc = dmc.Image.__doc__

layout = html.Div(
    children=[
        dmc.Text("Simple", color="dimmed"),
        dmc.Space(h=10),
        dmc.Image(
            src="https://imgk.timesnownews.com/story/Delhi_Pollution.png?tr=w-600,h-450,fo-auto",
            caption="Funny Meme",
            style={"width": 400},
            withPlaceholder=True,
        ),
        dmc.Space(h=50),
        dmc.Text("With placeholder", color="dimmed"),
        dmc.Space(h=10),
        dmc.Image(
            src="",
            caption="Bad source",
            height=200,
            withPlaceholder=True,
        ),
    ]
)
