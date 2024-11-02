import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.NumberInput(
        label="With prefix",
        placeholder="Dollars",
        prefix="$",
        value=100,
        w=250,
        mb="md"
    ),
    dmc.NumberInput(
        label="With suffix",
        placeholder="Percent",
        suffix="%",
        value=100,
        w=250,
        mt="md"
    ),
])

