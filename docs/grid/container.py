import dash_mantine_components as dmc
from dash import html

style = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "textAlign": "center",
}

component = html.Div(
    dmc.Grid(
        children=[
            dmc.GridCol(html.Div("1", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(html.Div("2", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(html.Div("3", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(html.Div("4", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(html.Div("5", style=style), span={"base": 12, "md": 6, "lg": 3}),
        ],
        gutter="xl",
        type="container",
        breakpoints={
            "xs": "100px",
            "sm": "200px",
            "md": "300px",
            "lg": "400px",
            "xl": "500px",
        },
    ),
    style={"resize": 'horizontal', "overflow": 'hidden', "maxWidth": '100%', "margin": 24 },
)
