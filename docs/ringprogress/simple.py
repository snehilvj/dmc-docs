import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.RingProgress(
            sections=[
                {"value": 40, "color": "cyan"},
                {"value": 15, "color": "orange"},
                {"value": 15, "color": "grape"},
            ]
        ),
        dmc.RingProgress(
            sections=[
                {"value": 40, "color": "#68b5e8"},
                {"value": 15, "color": "#6888e8"},
                {"value": 15, "color": "#8468e8"},
            ]
        ),
    ]
)
