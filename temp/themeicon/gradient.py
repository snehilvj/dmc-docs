import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    children=[
        dmc.ThemeIcon(
            DashIconify(icon="tabler:photo", width=20),
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
            size="lg",
        ),
        dmc.ThemeIcon(
            DashIconify(icon="tabler:photo", width=20),
            variant="gradient",
            gradient={"from": "teal", "to": "lime", "deg": 105},
            size="lg",
        ),
        dmc.ThemeIcon(
            DashIconify(icon="tabler:photo", width=20),
            variant="gradient",
            gradient={"from": "teal", "to": "blue", "deg": 60},
            size="lg",
        ),
        dmc.ThemeIcon(
            DashIconify(icon="tabler:photo", width=20),
            variant="gradient",
            gradient={"from": "orange", "to": "red"},
            size="lg",
        ),
        dmc.ThemeIcon(
            DashIconify(icon="tabler:photo", width=20),
            variant="gradient",
            gradient={"from": "grape", "to": "pink", "deg": 35},
            size="lg",
        ),
    ]
)
