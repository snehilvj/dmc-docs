import dash_mantine_components as dmc

component = dmc.Group(
    justify="center",
    children=[
        dmc.HoverCard(
            width=280,
            shadow="md",
            events={"focus": False},
            children=[
                dmc.HoverCardTarget(dmc.Button("Hover only")),
                dmc.HoverCardDropdown(
                    dmc.Text(
                        "Focusing the target does not open this dropdown",
                        size="sm",
                    )
                ),
            ],
        ),
        dmc.HoverCard(
            width=280,
            shadow="md",
            events={"touch": True},
            children=[
                dmc.HoverCardTarget(dmc.Button("Hover, focus and touch")),
                dmc.HoverCardDropdown(
                    dmc.Text(
                        "This dropdown is also opened by a tap on touch devices",
                        size="sm",
                    )
                ),
            ],
        ),
    ],
)