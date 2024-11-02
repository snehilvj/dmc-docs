import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Always show 2 digits after decimal point",
    placeholder="Do not enter more than 2",
    decimalScale=2,
    fixedDecimalScale=True,
    value=2.2,
    w=250,
)
