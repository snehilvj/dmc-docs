import dash_mantine_components as dmc

component = dmc.RingProgress(
    sections=[
        {"value": 40, "color": "yellow"},
    ],
    rootColor="red",
)
