import dash_mantine_components as dmc

component = dmc.Group(
    direction="column",
    children=[
        dmc.Checkbox(label="I agree to sell my privacy", size="xs", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="sm", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="md", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="lg", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", size="xl", checked=True),
    ],
)
