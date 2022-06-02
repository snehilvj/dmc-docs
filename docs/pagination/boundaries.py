import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Text("1 boundary (default)"),
        dmc.Space(h=5),
        dmc.Pagination(total=20, boundaries=1, page=10),
        dmc.Space(h=25),

        dmc.Text("2 boundaries"),
        dmc.Space(h=5),
        dmc.Pagination(total=20, boundaries=2, page=10),
        dmc.Space(h=25),

        dmc.Text("3 boundaries"),
        dmc.Space(h=5),
        dmc.Pagination(total=20, boundaries=3, page=10),
    ]
)
