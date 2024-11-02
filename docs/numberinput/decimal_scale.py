import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.NumberInput(
        label="You can enter only 2 digits after decimal point",
        placeholder="Do not enter more than 2 decimals",
        decimalScale=2,
        w=250,
        mb="md"
    ),
    dmc.NumberInput(
        label="Number input with decimal steps",
        value=0.05,
        decimalScale=2,
        min=-1,
        step=0.05,
        max=1,
        w=250,
        mt="md"
    )
])

