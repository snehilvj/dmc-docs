import dash_mantine_components as dmc

component = dmc.Popover(
    width=200,
    position="bottom",
    clickOutsideEvents=["mouseup", "touchend"],
    children=[
        dmc.PopoverTarget(
            dmc.Button("Toggle popover", id="toggle-btn")
        ),
        dmc.PopoverDropdown(
            dmc.Text(
                "Popover will be closed with mouseup and touchend events",
                size="xs"
            )
        )
    ]
)