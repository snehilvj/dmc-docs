import dash_mantine_components as dmc

component = dmc.Center(
    [
        dmc.Tooltip(
            label="⌘ + K",
            closeDelay=1000,
            children=[dmc.Button("Search", variant="outline")],
        )
    ]
)
