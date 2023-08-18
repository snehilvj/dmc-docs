import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Button("Default button"),
        dmc.Button("Subtle button", variant="subtle"),
        dmc.Button("Gradient button", variant="gradient"),
        dmc.Button("Filled button", variant="filled"),
        dmc.Button("Light button", variant="light"),
        dmc.Button("Outline button", variant="outline"),
    ]
)
