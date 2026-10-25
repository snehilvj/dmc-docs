import dash_mantine_components as dmc

component = dmc.Marquee(
    children=[
        dmc.Badge("Python", color="blue", variant="light", w=80),
        dmc.Badge("Plotly", color="indigo", variant="light", w=80),
        dmc.Badge("Dash", color="violet", variant="light", w=80),
        dmc.Badge("Mantine", color="orange", variant="light", w=80),
        dmc.Badge("React", color="teal", variant="light", w=80),
    ],
    gap="lg"
)