
import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.Slider(
        min=2,
        max=30,
        step=1,
        value=10,
        scale={"function": "getScale"},
        labelAlwaysOn=True,
        label={"function": "valueLabelFormat"}
    ),
    dmc.RangeSlider(
        mt=50,
        min=2,
        max=30,
        step=1,
        value=[10, 20],
        scale={"function": "getScale"},
        labelAlwaysOn=True,
        label={"function": "valueLabelFormat"}
    )
])
