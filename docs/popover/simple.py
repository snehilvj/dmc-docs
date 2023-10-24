import dash_mantine_components as dmc

component = dmc.Popover(
    [
        dmc.PopoverTarget(dmc.Button("Toggle Popover")),
        dmc.PopoverDropdown(dmc.Text("This popover is opened on button click"))

    ],
    width=200, position="bottom", withArrow=True, shadow="md",
)