import dash_mantine_components as dmc

marks = [
    {"value": 20, "label": "20%"},
    {"value": 50, "label": "50%"},
    {"value": 80, "label": "80%"},
]

component = dmc.Group(
    [
        dmc.Slider(
            orientation="vertical",
            value=45,
            marks=marks,
        ),
        dmc.RangeSlider(
            orientation="vertical",
            value=[25, 65],
            marks=marks,
        ),
    ],
    gap=60,
)