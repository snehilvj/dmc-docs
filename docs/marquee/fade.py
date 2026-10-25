
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Box(
            [
                dmc.Text("Default fade (5%)", size="sm", mb="xs"),
                dmc.Marquee(
                    [
                        dmc.Badge("Python", color="blue", variant="light", w=80),
                        dmc.Badge("Plotly", color="indigo", variant="light", w=80),
                        dmc.Badge("Dash", color="violet", variant="light", w=80),
                        dmc.Badge("pandas", color="teal", variant="light", w=80),
                    ],
                    gap="lg",
                ),
            ]
        ),
        dmc.Box(
            [
                dmc.Text("Larger fade (15%)", size="sm", mb="xs"),
                dmc.Marquee(
                    [
                        dmc.Badge("Python", color="blue", variant="light", w=80),
                        dmc.Badge("Plotly", color="indigo", variant="light", w=80),
                        dmc.Badge("Dash", color="violet", variant="light", w=80),
                        dmc.Badge("pandas", color="teal", variant="light", w=80),
                    ],
                    gap="lg",
                    fadeEdgeSize="15%",
                ),
            ]
        ),
        dmc.Box(
            [
                dmc.Text("Custom fade color", size="sm", mb="xs"),
                dmc.Marquee(
                    [
                        dmc.Badge("Python", color="blue", variant="light", w=80),
                        dmc.Badge("Plotly", color="indigo", variant="light", w=80),
                        dmc.Badge("Dash", color="violet", variant="light", w=80),
                        dmc.Badge("pandas", color="teal", variant="light", w=80),
                    ],
                    gap="lg",
                    fadeEdgeColor="var(--mantine-color-red-light)",
                ),
            ]
        ),
        dmc.Box(
            [
                dmc.Text("No fade", size="sm", mb="xs"),
                dmc.Marquee(
                    [
                        dmc.Badge("Python", color="blue", variant="light", w=80),
                        dmc.Badge("Plotly", color="indigo", variant="light", w=80),
                        dmc.Badge("Dash", color="violet", variant="light", w=80),
                        dmc.Badge("pandas", color="teal", variant="light", w=80),
                    ],
                    gap="lg",
                    fadeEdges=False,
                ),
            ]
        ),
    ]
)
