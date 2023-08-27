import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.Col(html.Div("span=auto", style=style), span="auto"),
        dmc.Col(html.Div("span=6", style=style), span=6),
        dmc.Col(html.Div("span=auto", style=style), span="auto"),
    ],
    gutter="xl",
)
