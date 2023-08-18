import dash_mantine_components as dmc

component = dmc.Progress(
    size="xl",
    sections=[
        {"value": 40, "color": "cyan"},
        {"value": 20, "color": "blue"},
        {"value": 15, "color": "indigo"},
    ],
)
