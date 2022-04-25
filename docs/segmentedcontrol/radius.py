import dash_mantine_components as dmc

data = ["Dash", "Mantine", "Bootstrap", "Core"]

component = dmc.Group(
    direction="column",
    children=[dmc.SegmentedControl(data=data, radius=x) for x in [0, "md", "lg", 20]],
)
