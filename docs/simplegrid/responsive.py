import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.SimpleGrid(
    cols={"base": 1, "sm": 2, "lg": 5},
    spacing={"base": 10, "sm": "xl"},
    verticalSpacing={"base": "md", "sm": "xl"},
    children=[
        html.Div("1", style=style),
        html.Div("2", style=style),
        html.Div("3", style=style),
        html.Div("4", style=style),
        html.Div("5", style=style),
    ],
)
