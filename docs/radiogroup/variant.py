import dash_mantine_components as dmc


component = dmc.Stack(
    [
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i, variant="filled") for i in ["USA", "Canada", "France"]],
                my=10,
            ),
            value="USA",
            label="Variant - filled",
        ),
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i, variant="outline") for i in ["USA", "Canada", "France"]],
                my=10,
            ),
            value="USA",
            label="Variant - outline",
        ),
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i, variant="light") for i in ["USA", "Canada", "France"]],
                my=10,
            ),
            value="USA",
            label="Variant - light",
        ),
    ]
)