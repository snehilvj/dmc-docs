import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.TimeInput(label="Enter Time:", w=100, error=True),
        dmc.TimeInput(
            label="Enter Time:",
            w=150,
            error="Enter a valid time",
            withSeconds=True,
        ),
    ],
)
