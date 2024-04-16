import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Number input with custom separators",
    value=0.05,
    decimalScale=2,
    decimalSeparator=",",
    thousandSeparator=".",
    style={"width": 250},
)
