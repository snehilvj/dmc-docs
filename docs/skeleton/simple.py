import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Skeleton(height=50,  circle=True, mb="xl"),
        dmc.Skeleton(height=8, radius="xl"),
        dmc.Skeleton(height=8, my=6),
        dmc.Skeleton(height=8, w="70%", radius="xl"),
    ],
)
