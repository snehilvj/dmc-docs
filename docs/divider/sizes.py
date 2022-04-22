import dash_mantine_components as dmc

component = dmc.Group(
    grow=True,
    direction="column",
    children=[
        dmc.Divider(size="xs"),
        dmc.Divider(size="sm"),
        dmc.Divider(size="md"),
        dmc.Divider(size="lg"),
        dmc.Divider(size="xl"),
        dmc.Divider(size=10),
    ],
)
