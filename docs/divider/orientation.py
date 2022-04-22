import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Badge("Badge 1"),
        dmc.Divider(orientation="vertical", style={"height": 20}),
        dmc.Badge("Badge 2"),
        dmc.Divider(orientation="vertical", style={"height": 20}),
        dmc.Badge("Badge 3"),
    ]
)