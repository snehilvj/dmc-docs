import dash_mantine_components as dmc

component = dmc.Group(
    justify="center",
    children=[
        dmc.Tooltip(children=[dmc.Badge(color, color=color)], label=color, color=color)
        for color in [
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
    ],
)
