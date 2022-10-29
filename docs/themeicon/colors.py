import dash_mantine_components as dmc
from dash_iconify import DashIconify

colors = [
    "gray",
    "red",
    "pink",
    "grape",
    "violet",
    "indigo",
    "blue",
    "lime",
    "yellow",
    "orange",
]

component = dmc.Stack(
    spacing="xs",
    children=[
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(icon="tabler:photo", width=20),
                    variant=variant,
                    color=color,
                )
                for color in colors
            ],
            position="center",
        )
        for variant in ["outline", "light", "filled"]
    ],
)
