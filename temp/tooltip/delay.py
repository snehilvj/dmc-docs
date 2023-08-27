import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Tooltip(
            dmc.Button("Delay Open - 500ms", variant="outline"),
            label="Opened after 500ms",
            openDelay=500,
        ),
        dmc.Tooltip(
            dmc.Button("Delay Close - 500ms", variant="outline"),
            label="Closed after 500ms",
            closeDelay=500,
        ),
    ]
)
