import dash_mantine_components as dmc

component = dmc.Anchor(
    "A link with pink to yellow gradient",
    href="#text-props",
    variant="gradient",
    gradient={"from": "pink", "to": "yellow"},
    fw=500,
    fz="lg",
)
