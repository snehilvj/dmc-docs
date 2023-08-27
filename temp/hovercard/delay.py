import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.HoverCard(
            shadow="md",
            openDelay=1000,
            children=[
                dmc.HoverCardTarget(dmc.Button("1000ms open delay")),
                dmc.HoverCardDropdown(dmc.Text("Opened with 1000ms delay", size="sm")),
            ],
        ),
        dmc.HoverCard(
            shadow="md",
            closeDelay=1000,
            children=[
                dmc.HoverCardTarget(dmc.Button("1000ms close delay")),
                dmc.HoverCardDropdown(dmc.Text("Closed with 1000ms delay", size="sm")),
            ],
        ),
    ]
)
