import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Text("Standard size", size="sm"),
        dmc.Slider(value=40, label=None),
        dmc.Text("Thumb size number", size="sm", mt="xl"),
        dmc.Slider(value=40, thumbSize=50),
    ]
)
