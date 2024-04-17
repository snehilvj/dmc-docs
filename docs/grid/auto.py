import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(html.Div("span=auto", style=style), span="auto"),
        dmc.GridCol(html.Div("span=6", style=style), span=6),
        dmc.GridCol(html.Div("span=auto", style=style), span="auto"),
    ],
    gutter="xl",
)
