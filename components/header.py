import dash_mantine_components as dmc
from dash import html

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
                dmc.Anchor(
                    "GitHub",
                    color="dark",
                    variant="link",
                    size="xl",
                    href="https://github.com/snehilvj/dash-mantine-components",
                ),
            ],
        )
    ],
)
