import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.TimeInput(label="Enter Time:", error=True),
        dmc.TimeInput(label="Enter Time:", error="Please enter a valid time"),
    ],
    style={"width": 200},
    direction="column",
    grow=False,
)
