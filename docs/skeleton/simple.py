import dash_mantine_components as dmc

component = dmc.Stack(
    gap=0,
    children=[
        dmc.Skeleton(h=50, mb="xl"),
        dmc.Skeleton(h=8, radius="xl"),
        dmc.Skeleton(h=8, my=6),
        dmc.Skeleton(h=8, w="70%", radius="xl"),
    ],
)
