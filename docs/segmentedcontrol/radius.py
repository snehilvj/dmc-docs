import dash_mantine_components as dmc

data = ["Dash", "Mantine", "Bootstrap", "Core"]

component = dmc.Stack(
    [dmc.SegmentedControl(data=data, radius=x) for x in [0, "md", "lg", 20]],
    align="flex-start",
)
