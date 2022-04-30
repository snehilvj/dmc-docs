import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Tooltip(
            dmc.Button("Default arrow", variant="outline"),
            label="Default arrow",
            withArrow=True,
            opened=True,
        ),
        dmc.Tooltip(
            dmc.Button("With size", variant="outline"),
            label="Arrow with size",
            withArrow=True,
            arrowSize=3,
            opened=True,
        ),
    ],
    style={"marginTop": 25},
)
