import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.Col(html.Div("content width", style=style), span="content"),
        dmc.Col(html.Div("2", style=style), span=6),
    ],
    gutter="xl",
)
