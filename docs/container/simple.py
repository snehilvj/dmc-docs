import dash_mantine_components as dmc
from dash import html

style = {
    "height": 100,
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
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
