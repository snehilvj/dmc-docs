import dash_mantine_components as dmc

component = dmc.AppShellNavbar(
    p="md",
    w={"base": 300},
    h=500,
    children=[
        dmc.Anchor("Link1", href="#"),
        dmc.Anchor("Link2", href="#"),
        dmc.Anchor("Link3", href="#"),
        dmc.Anchor("Link4", href="#"),
    ],
)
