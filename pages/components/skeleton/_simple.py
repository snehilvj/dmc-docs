import dash_mantine_components as dmc

component = dmc.Group(
    direction="column",
    grow=True,
    spacing="xs",
    children=[
        dmc.Skeleton(height=50, circle=True),
        dmc.Skeleton(height=8),
        dmc.Skeleton(height=8),
        dmc.Skeleton(height=8, width="70%"),
    ],
)
