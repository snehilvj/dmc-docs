import dash_mantine_components as dmc

component = dmc.Slider(
    restrictToMarks=True,
    value=25,
    marks=[
        {"value": 25, "label": "25%"},
        {"value": 50, "label": "50%"},
        {"value": 75, "label": "75%"},
        {"value": 85, "label": "85%"},
        {"value": 95, "label": "95%"},
    ],
    m=30,
)
