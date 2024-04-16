import dash_mantine_components as dmc

component = dmc.AppShellAside(
    p="md",
    w={"base": 300},
    h=500,
    top=400,
    right=0,
    children=[
        dmc.Text("Link1"),
        dmc.Text("Link2"),
        dmc.Text("Link3"),
        dmc.Text("Link4"),
    ],
)
