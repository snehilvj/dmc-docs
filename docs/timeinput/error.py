import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.TimeInput(label="Enter Time:", style={"width": 100}, error=True),
        dmc.TimeInput(
            label="Enter Time:",
            style={"width": 150},
            error="Enter a valid time",
            withSeconds=True,
        ),
    ],
)
