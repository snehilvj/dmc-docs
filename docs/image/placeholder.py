import dash_mantine_components as dmc

component = dmc.Group(
    justify="space-apart",
    children=[
        dmc.Image(w=200, h=100, alt="Without placeholder"),
        dmc.Image(
            w=200,
            h=100,
            fallbackSrc="https://placehold.co/600x400?text=Placeholder",
        ),
    ],
)
