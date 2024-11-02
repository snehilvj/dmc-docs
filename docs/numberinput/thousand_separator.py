import dash_mantine_components as dmc

component = dmc.Stack([

    dmc.NumberInput(
        label="Thousands are separated with a comma",
        placeholder="Thousands are separated with a comma",
        thousandSeparator=",",
        value=1_000_000,
        w=400
    ),

    dmc.NumberInput(
        label="Thousands are separated with a space",
        placeholder="Thousands are separated with a space",
        thousandSeparator=" ",
        value=1_000_000,
        mt="md",
        w=400
    )
])

