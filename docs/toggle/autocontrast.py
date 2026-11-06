import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.Toggle(
            DashIconify(icon="tabler:bold", height=18),
            active=True,
            variant="filled",
            color="lime.4",
            **{"aria-label": "Bold"},
        ),
        dmc.Toggle(
            DashIconify(icon="tabler:bold", height=18),
            active=True,
            variant="filled",
            autoContrast=True,
            color="lime.4",
            **{"aria-label": "Bold"},
        ),

    ]
)
