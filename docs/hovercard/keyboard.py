import dash_mantine_components as dmc

component = dmc.Group(
    justify="center",
    children=[
        dmc.Button("Press Tab to move focus", variant="default"),
        dmc.HoverCard(
            width=280,
            shadow="md",
            children=[
                dmc.HoverCardTarget(
                    dmc.Button("Hover or focus me")
                ),
                dmc.HoverCardDropdown(
                    dmc.Text(
                        "The dropdown opens when the target is hovered or focused with the keyboard. Press Escape to close it.",
                        size="sm",
                    )
                ),
            ],
        ),
    ],
)