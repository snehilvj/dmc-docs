import dash_mantine_components as dmc

component = dmc.Group(
    grow=True,
    direction="column",
    children=[
        dmc.Divider(variant="solid"),
        dmc.Divider(variant="dashed"),
        dmc.Divider(variant="dotted"),
    ],
)
