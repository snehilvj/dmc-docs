import dash_mantine_components as dmc

component = dmc.Group(
    justify="center",
    children=[
        dmc.HoverCard(
            width=280,
            shadow="md",
            interactive=True,
            position="bottom-end",
            offset=40,
            children=[
                dmc.HoverCardTarget(
                    dmc.Button("Interactive")
                ),
                dmc.HoverCardDropdown(
                    dmc.Text(
                        [
                            "Move the pointer diagonally to the ",
                            dmc.Anchor(
                                "link",
                                href="https://mantine.dev",
                                target="_blank",
                            ),
                            ". The dropdown stays open.",
                        ],
                        size="sm",
                    )
                ),
            ],
        ),
        dmc.HoverCard(
            width=280,
            shadow="md",
            position="bottom-end",
            offset=40,
            children=[
                dmc.HoverCardTarget(
                    dmc.Button("Not interactive", variant="default")
                ),
                dmc.HoverCardDropdown(
                    dmc.Text(
                        "Moving the pointer outside the target may close this dropdown.",
                        size="sm",
                    )
                ),
            ],
        ),
    ],
)