import dash_mantine_components as dmc

component = dmc.Slider(
    startPointValue=0,
    updatemode="drag",
    min=-100,
    max=100,
    value=40,
    marks=[
        {"value": -100, "label": "-100"},
        {"value": -50, "label": "-50"},
        {"value": 0, "label": "0"},
        {"value": 50, "label": "50"},
        {"value": 100, "label": "100"},
    ],
)