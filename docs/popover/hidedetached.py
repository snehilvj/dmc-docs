import dash_mantine_components as dmc


component = dmc.Box(
    style={"border": "1px solid var(--mantine-color-dimmed)", "overflow": "auto"},
    p="xl",
    w=400,
    h=200,
    children=[
        dmc.Box(
            w=1000,
            h=400,
            children=dmc.Group(
                [
                    dmc.Popover(
                        opened=True,
                        width="target",
                        position="bottom",
                        closeOnClickOutside=False,
                        children=[
                            dmc.PopoverTarget(
                                dmc.Button("Toggle popover")
                            ),
                            dmc.PopoverDropdown("This popover dropdown is hidden when detached"),
                        ],
                    ),
                    dmc.Popover(
                        opened=True,
                        width="target",
                        position="bottom",
                        closeOnClickOutside=False,
                        hideDetached=False,
                        children=[
                            dmc.PopoverTarget(
                                dmc.Button("Toggle popover")
                            ),
                            dmc.PopoverDropdown("This popover dropdown is visible when detached"),
                        ],
                    ),
                ]
            ),
        )
    ]
)
