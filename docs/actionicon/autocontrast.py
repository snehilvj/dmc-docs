import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.Group(
    [
        dmc.ActionIcon(
            children=DashIconify(icon="tabler:heart", width=18, height=18),
            color="lime.3"
        ),
        dmc.ActionIcon(
            children=DashIconify(icon="tabler:heart", width=18, height=18),
            color="lime.3",
            autoContrast=True
        ),
    ]
)