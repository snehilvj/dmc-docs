import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Badge(1, size="xs", circle=True),
        dmc.Badge(7, size="sm", circle=True),
        dmc.Badge(9, size="md", circle=True),
        dmc.Badge(3, size="lg", circle=True),
        dmc.Badge(8, size="xl", circle=True),
    ]
)
