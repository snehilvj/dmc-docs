import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.TextInput(label="Your Email:", w=200, error=True),
        dmc.TextInput(label="Your Email:", w=200, error="Enter a valid email"),
    ],
)
