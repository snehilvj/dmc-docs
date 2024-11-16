import dash_mantine_components as dmc


component = dmc.Stack(
    [
        dmc.Slider(value=60, disabled=True),
        dmc.RangeSlider(
            mt="xl",
            mb="xl",
            value=[25, 75],
            disabled=True,
            marks=[
                {"value": 0, "label": "xs"},
                {"value": 25, "label": "sm"},
                {"value": 50, "label": "md"},
                {"value": 75, "label": "lg"},
                {"value": 100, "label": "xl"},
            ],
        ),
    ]
)
