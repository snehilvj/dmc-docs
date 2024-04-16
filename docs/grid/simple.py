import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(html.Div("1", style=style), span=4),
        dmc.GridCol(html.Div("2", style=style), span=4),
        dmc.GridCol(html.Div("3", style=style), span=4),
    ],
    gutter="xl",
)
