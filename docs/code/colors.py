import dash_mantine_components as dmc

code = "from collections import defaultdict"

component = dmc.Group(
    direction="column",
    children=[
        dmc.Code(code, color=color) for color in ["red", "blue", "green", "pink"]
    ],
)
