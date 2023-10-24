import dash_mantine_components as dmc

data = ["Dash", "Mantine", "Bootstrap", "Core"]

component = dmc.Stack(
    [
        dmc.Text("No transition"),
        dmc.SegmentedControl(data=data, transitionDuration=0),
        dmc.Text("500ms linear transition"),
        dmc.SegmentedControl(
            data=data, transitionDuration=500, transitionTimingFunction="linear"
        ),
    ],
    align="flex-start",
)
