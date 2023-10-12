import dash_mantine_components as dmc

component = dmc.Popover(
    [
        dmc.PopoverTarget(dmc.Button("Toggle Popover")),
        dmc.PopoverDropdown(
            [
                dmc.TextInput(label="Name", placeholder="Name", size="xs"),
                dmc.TextInput(label="Email", placeholder="john@doe.com",size="xs", mt="xs")
            ]
        )

    ],
    width=300,
    position="bottom",
    withArrow=True,
    trapFocus=True,
    shadow="md",
    


)