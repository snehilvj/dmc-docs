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

component = dmc.Group(
    direction="column",
    spacing="xs",
    position="center",
    children=[
        dmc.Group(
            [
                dmc.ActionIcon(
                    DashIconify(icon="icomoon-free:sun"),
                    variant=variant,
                    color=color,
                )
                for color in colors
            ],
            position="center",
        )
        for variant in ["transparent", "outline", "light", "filled"]
    ],
)
