import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Negative numbers are not allowed",
    placeholder="Do not enter negative numbers",
    allowNegative=False,
    w=300,
)
