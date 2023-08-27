import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Step on hold",
    description="Step the value when clicking and holding the arrows",
    stepHoldDelay=500,
    stepHoldInterval=100,
    value=0,
    style={"width": 250},
)
