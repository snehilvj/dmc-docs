import dash_mantine_components as dmc

component = dmc.Navbar(
    p="md",
    width={"base": 300},
    height=500,
    children=[
        dmc.Anchor("Link1", href="#"),
        dmc.Anchor("Link2", href="#"),
        dmc.Anchor("Link3", href="#"),
        dmc.Anchor("Link4", href="#"),
    ],
)
