import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.TextInput(
            label="Your Email:",
            style={"width": 150},
            error=True
        ),
        dmc.TextInput(
            label="Your Email:",
            style={"width": 150},
            error="Enter a valid email",
        ),
    ],
    direction="center",
)
