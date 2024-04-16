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

component = dmc.Group(
    [dmc.Button(color.title(), color=color) for color in colors],
)
