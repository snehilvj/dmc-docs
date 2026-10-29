import dash_mantine_components as dmc


component = dmc.Marquee(
    children=[
        dmc.Badge("Python", color="red", variant="light", w=80),
        dmc.Badge("Plotly", color="blue", variant="light", w=80),
        dmc.Badge("Dash", color="violet", variant="light", w=80),
        dmc.Badge("Mantine", color="yellow", variant="light", w=80),
        dmc.Badge("React", color="teal", variant="light", w=80),
    ],
    pauseOnHover=True,
)