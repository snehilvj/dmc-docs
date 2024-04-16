import dash_mantine_components as dmc

code = "import collections"

component = dmc.Group(
    children=[
        dmc.Code(code, color=color) for color in ["red", "blue", "green", "pink"]
    ],
)
