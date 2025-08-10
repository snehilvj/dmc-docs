import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = html.Div(
    # Wrapper div is added for demonstration purposes only,
    # it is not required in real projects
    dmc.SimpleGrid(
        type="container",
        cols={"base": 1, "300px": 2, "500px": 5},
        spacing={"base": 10, "300px": "xl"},
        children=[
            html.Div("1", style=style),
            html.Div("2", style=style),
            html.Div("3", style=style),
            html.Div("4", style=style),
            html.Div("5", style=style),
        ],
        p="xs",
    ),
    style={"resize": "horizontal", "overflow": "hidden", "maxWidth": "100%"},
)
