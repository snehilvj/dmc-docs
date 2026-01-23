import dash_mantine_components as dmc
from dash import html

style = {
    "height": 100,
    "border": "1px solid var(--mantine-color-blue-outline)",
    "marginTop": 20,
    "marginBottom": 20,
}

component = html.Div(
    children=[
        dmc.Container("Default container", style=style),
        dmc.Container(
            "xs container with xs horizontal padding", size="xs", px="xs", style=style
        ),
        dmc.Container(
            "200px container with 0px horizontal padding", size=200, px=0, style=style
        ),
    ]
)
