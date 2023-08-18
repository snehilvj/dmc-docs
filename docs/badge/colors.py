import dash_mantine_components as dmc

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
            [dmc.Badge(color, variant=variant, color=color) for color in colors],
            position="center",
        )
        for variant in ["light", "outline", "filled", "dot"]
    ],
)
