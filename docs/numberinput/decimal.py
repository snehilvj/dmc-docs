import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Number input with decimal steps",
    value=0.05,
    decimalScale=2,
    min=-1,
    step=0.05,
    max=1,
    style={"width": 250},
)
