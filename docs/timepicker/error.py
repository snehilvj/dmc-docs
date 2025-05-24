import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.TimePicker(label="Enter Time:", w=100, error=True),
        dmc.TimePicker(
            label="Enter Time:",
            w=150,
            error="Enter a valid time",
            withSeconds=True,
        ),
    ],
)
