import dash_mantine_components as dmc
from dash import html, dcc


header = html.Div(
    style={"margin": "20px 0"},
    children=[
        dmc.Group(
            position="apart",
            children=[
                dmc.Text(
                    "Dash Mantine Components",
                    variant="gradient",
                    style={"fontSize": 40},
                    gradient={"from": "indigo", "to": "cyan", "deg": 45},
                ),
                dcc.Link(
                    [html.I(className="bi bi-github", style={"fontSize": 25})],
                    href="https://github.com/snehilvj/dash-mantine-components",
                    target="_blank",
                ),
            ],
        )
    ],
)
