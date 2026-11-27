import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.Toggle(
            DashIconify(icon="tabler:bold", height=18),
            **{"aria-label": "Bold"},
        ),
        dmc.Toggle(
            DashIconify(icon="tabler:italic", height=18),
            **{"aria-label": "Italic"},
        ),
        dmc.Toggle(
            DashIconify(icon="tabler:underline", height=18),
            **{"aria-label": "Underline"},
        ),
    ]
)
