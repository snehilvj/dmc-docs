import dash_mantine_components as dmc

component = dmc.Flex(
    [
        "Here is some text with ",
        dmc.Popover(
            [
                dmc.PopoverTarget(dmc.Mark(" an inline popover ")),
                dmc.PopoverDropdown(" more info")
            ],
            middlewares={"flip": True, "shift": True, "inline": True}
        ),
        " and more text after."
    ],
    direction="row",
    gap="xs"
)
