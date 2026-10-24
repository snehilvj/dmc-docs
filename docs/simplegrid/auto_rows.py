import dash_mantine_components as dmc
from dash import html

style = {
    "border": "1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.SimpleGrid(
    cols=3,
    autoRows="minmax(100px, auto)",
    children=[
        html.Div("1", style=style),
        html.Div("2", style=style),
        html.Div("3", style=style),
        html.Div("4", style=style),
        html.Div("5", style=style),
    ],
)

