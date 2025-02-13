import dash_mantine_components as dmc


component = dmc.RadioCard(
    withBorder=True,
    p="md",
    checked=True,
    children=[
        dmc.Center([
            dmc.RadioIndicator(),
            dmc.Text("RadioCard", size="xl", pl="sm"),
        ], inline=True),
    ]
)

