import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Number input with custom separators",
    value=1001500.05,
    decimalScale=2,
    decimalSeparator=",",
    thousandSeparator=".",
    w=250,
)
