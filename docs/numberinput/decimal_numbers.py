import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="Decimal numbers are not allowed",
    placeholder="Do not enter decimal numbers",
    allowDecimal=False,
    w=250,
)
