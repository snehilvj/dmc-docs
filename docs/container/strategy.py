import dash_mantine_components as dmc
from dash import html


component = dmc.Container(
    [
        dmc.Box("Main Content", bg="var(--mantine-color-indigo-light)", h=50),
        html.Div(
            [
                "Breakout",
                html.Div(
                    "Container inside breakout",
                    style={
                        "backgroundColor": "var(--mantine-color-indigo-filled)",
                        "color": "white",
                        "height": 50,
                    },
                    **{"data-container": ""}
                ),
            ],
            style={
                "backgroundColor": "var(--mantine-color-indigo-light)",
                "marginTop": 16,
            },
            **{"data-breakout": ""}
        ),
    ],
    size=500,
    strategy="grid",
)
