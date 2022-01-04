import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.Badge(
            "Indigo cyan",
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
        ),
        dmc.Badge(
            "Lime green",
            variant="gradient",
            gradient={"from": "teal", "to": "lime", "deg": 105},
        ),
        dmc.Badge(
            "Teal blue",
            variant="gradient",
            gradient={"from": "teal", "to": "blue", "deg": 60},
        ),
        dmc.Badge(
            "Orange red",
            variant="gradient",
            gradient={"from": "orange", "to": "red"},
        ),
        dmc.Badge(
            "Grape pink",
            variant="gradient",
            gradient={"from": "grape", "to": "pink", "deg": 35},
        ),
    ]
)
