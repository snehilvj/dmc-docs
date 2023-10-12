import dash_mantine_components as dmc

component = dmc.Popover(
    [
        dmc.PopoverTarget(dmc.Button("Toggle Popover", w=200)),
        dmc.PopoverDropdown(
            dmc.Text("This popover has same width as target, it is useful when you are building input dropdowns")
        )
    ],
    width="target", position="bottom", withArrow=True, shadow="md",
)