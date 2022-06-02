import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Text("1 sibling (default), active page number=10, grow=True to fill content: "),
        dmc.Space(h=5),
        dmc.Pagination(total=20, grow=True, siblings=1, page=10),
        dmc.Space(h=25),

        dmc.Text("2 siblings, active page number = 15, grow=default (False), positioned center: ", align='center'),
        dmc.Space(h=5),
        dmc.Pagination(total=20, siblings=2, page=15, position='center'),
        dmc.Space(h=25),

        dmc.Text("3 siblings, position to the right: ", align='right'),
        dmc.Space(h=5),
        dmc.Pagination(total=20, siblings=3, page=10, position='right'),
    ]
)
