import dash_mantine_components as dmc

component = dmc.Slider(
    value=79,
    marks=[
        {"value": 20, "label": "20%"},
        {"value": 50, "label": "50%"},
        {"value": 80, "label": "80%"},
    ],
    size=2,
    classNames={
        "track": "dmc-slider-track",
        "mark": "dmc-slider-mark",
        "markLabel": "dmc-slider-markLabel",
        "thumb": "dmc-slider-thumb",
    },
)
