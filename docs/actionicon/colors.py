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
    gap="xs",
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
            justify="center",
        )
        for variant in ["subtle", "filled", "outline", "light" "transparent"]
    ],
)
