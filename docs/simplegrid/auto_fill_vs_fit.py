import dash_mantine_components as dmc
from dash import html

style = {
    "border": "1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Stack([
    # auto-fill: empty tracks are preserved, items do not stretch
    dmc.Text("auto-fill"),
    dmc.SimpleGrid(
        minColWidth="200px",
        autoFlow="auto-fill",
        children=[
            html.Div("1", style=style),
            html.Div("2", style=style),
            html.Div("3", style=style),
        ],
    ),

    # auto-fit: empty tracks are collapsed, items stretch to fill the row
    dmc.Text("auto-fit"),
    dmc.SimpleGrid(
        minColWidth="200px",
        autoFlow="auto-fit",
        children=[
            html.Div("1", style=style),
            html.Div("2", style=style),
            html.Div("3", style=style),
        ],
    ),
])