import dash_mantine_components as dmc

component = dmc.Progress(
    size="xl",
    sections=[
        {"value": 14, "color": "yellow", "label": "Docs", "tooltip": "Docs - 14GB"},
        {"value": 17, "color": "red", "label": "Apps", "tooltip": "Apps - 17GB"},
        {"value": 69, "color": "violet", "label": "Other", "tooltip": "Other - 69GB"},
    ],
)
