import dash_mantine_components as dmc

component = dmc.Aside(
    p="md",
    width={"base": 300},
    height=500,
    fixed=True,
    position={"right": 0, "top": 400},
    children=[
        dmc.Text("Link1"),
        dmc.Text("Link2"),
        dmc.Text("Link3"),
        dmc.Text("Link4"),
    ],
)
