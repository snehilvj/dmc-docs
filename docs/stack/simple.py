import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Button("1", variant="outline"),
        dmc.Button("2", variant="outline"),
        dmc.Button("3", variant="outline"),
    ],
    align="center",
    gap="xl",
)
