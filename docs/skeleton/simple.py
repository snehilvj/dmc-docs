import dash_mantine_components as dmc

component = dmc.Stack(
    gap="xs",
    children=[
        dmc.Skeleton(h=50, circle=True),
        dmc.Skeleton(h=8),
        dmc.Skeleton(h=8),
        dmc.Skeleton(h=8, w="70%"),
    ],
)
