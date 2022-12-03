import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Burger(),
        dmc.Burger(color="red"),
        dmc.Burger(color="green"),
    ]
)
