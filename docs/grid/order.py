import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(html.Div("2", style=style), span=3, order={"base": 2, "sm": 1, "lg": 3}),
        dmc.GridCol(html.Div("3", style=style), span=3, order={"base": 3, "sm": 2, "lg": 2}),
        dmc.GridCol(html.Div("1", style=style), span=3, order={"base": 1, "sm": 3, "lg": 1}),
    ],
)
