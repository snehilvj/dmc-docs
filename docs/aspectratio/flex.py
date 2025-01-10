import dash_mantine_components as dmc
from dash import html

component = html.Div(
    dmc.AspectRatio(
        ratio=1,
        style={"flex": "0 0 100px"},
        children=[
            dmc.Image(
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-6.png",
                alt="Avatar",
            )
        ],
    ),
    style={"display": "flex"},
)