import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Slider(inverted=True, value=80),
        dmc.RangeSlider(inverted=True, value=[40, 60], mt="xl"),
    ]
)
