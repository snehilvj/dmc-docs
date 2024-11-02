import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Custom decimal separator",
    decimalSeparator=",",
    value=20.234,
    w=250,
)
