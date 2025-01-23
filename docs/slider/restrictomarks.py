import dash_mantine_components as dmc

component = dmc.Stack(
    [
        # Slider
        dmc.Slider(
            restrictToMarks=True,
            value=25,
            marks=[{"value": index * 25} for index in range(5)],
        ),
        # RangeSlider
        dmc.RangeSlider(
            restrictToMarks=True,
            value=[5, 15],
            marks=[
                {"value": 5},
                {"value": 15},
                {"value": 25},
                {"value": 35},
                {"value": 70},
                {"value": 80},
                {"value": 90},
            ],
        ),
    ]
)
