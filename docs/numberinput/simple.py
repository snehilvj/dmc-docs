import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Your weight in kg",
    description="From 0 to infinity, in steps of 5",
    value=5,
    min=0,
    step=5,
    w=250,
)
