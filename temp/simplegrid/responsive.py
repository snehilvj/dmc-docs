import dash_mantine_components as dmc
from dash import html


style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

component = dmc.SimpleGrid(
    cols=4,
    spacing="lg",
    breakpoints=[
        {"maxWidth": 980, "cols": 3, "spacing": "md"},
        {"maxWidth": 755, "cols": 2, "spacing": "sm"},
        {"maxWidth": 600, "cols": 1, "spacing": "sm"},
    ],
    children=[
        html.Div("1", style=style),
        html.Div("2", style=style),
        html.Div("3", style=style),
        html.Div("4", style=style),
        html.Div("5", style=style),
    ],
)
