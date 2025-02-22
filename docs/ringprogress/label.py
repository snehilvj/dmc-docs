import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.RingProgress(
            id="ring-progress-label",
            sections=[{"value": 33, "color": "indigo"}],
            label=dmc.Text("33%", c="indigo", ta="center"),
        ),
        dmc.RingProgress(
            id="ring-progress-label2",
            sections=[
                {"value": 25, "color": "indigo"},
                {"value": 15, "color": "orange"},
            ],
            label=dmc.Text("App data usage", size="xs", ta="center"),
        ),
        dmc.RingProgress(
            id="ring-progress-label3",
            sections=[{"value": 60, "color": "green"}, {"value": 5, "color": "yellow"}],
            label=dmc.Center(
                dmc.ActionIcon(
                    color="teal",
                    variant="light",
                    radius="xl",
                    size="xl",
                    children=DashIconify(icon="tabler:check", height=40),
                )
            ),
        ),
    ]
)
