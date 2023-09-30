import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Number input with custom separators",
    value=0.05,
    precision=2,
    decimalSeparator=",",
    thousandsSeparator=".",
    style={"width": 250},
)
