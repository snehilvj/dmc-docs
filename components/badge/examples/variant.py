import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Badge("Default light badge"),
        dmc.Badge("Dot badge", variant="dot"),
        dmc.Badge("Outline badge", variant="outline"),
        dmc.Badge("Filled badge", variant="filled"),
    ]
)
