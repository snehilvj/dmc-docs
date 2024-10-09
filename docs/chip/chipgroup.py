import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Group(
            dmc.ChipGroup(
                [
                    dmc.Chip("Single chip", value="a"),
                    dmc.Chip("Can be selected", value="b"),
                    dmc.Chip("At a time", value="c"),
                ],
                multiple=False,
            ),
            justify="center",
            mb="sm",
        ),
        dmc.Group(
            dmc.ChipGroup(
                [
                    dmc.Chip("Multiple chips", value="a"),
                    dmc.Chip("Can be selected", value="b"),
                    dmc.Chip("At a time", value="c"),
                ],
                multiple=True,
            ),
            justify="center",
        ),
    ]
)
