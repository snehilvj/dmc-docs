import dash_mantine_components as dmc

# fmt: off # no-prism
colors = [
    "dark",
    "gray",
    "red",
    "pink",
    "grape",
    "violet",
    "indigo",
    "blue",
    "cyan",
    "teal",
    "green",
    "lime",
    "yellow",
    "orange",
]
# fmt: on # no-prism

component = dmc.Group(
    direction="column",
    spacing="xl",
    children=[
        dmc.Group(
            [dmc.Badge(color, variant=variant, color=color) for color in colors],
            position="center",
        )
        for variant in ["light", "outline", "filled", "dot"]
    ],
)
