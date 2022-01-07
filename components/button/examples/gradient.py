import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.Button(
            "Indigo cyan",
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
        ),
        dmc.Button(
            "Lime green",
            variant="gradient",
            gradient={"from": "teal", "to": "lime", "deg": 105},
        ),
        dmc.Button(
            "Teal blue",
            variant="gradient",
            gradient={"from": "teal", "to": "blue", "deg": 60},
        ),
        dmc.Button(
            "Orange red",
            variant="gradient",
            gradient={"from": "orange", "to": "red"},
        ),
        dmc.Button(
            "Grape pink",
            variant="gradient",
            gradient={"from": "grape", "to": "pink", "deg": 35},
        ),
    ]
)
