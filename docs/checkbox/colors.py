import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.Checkbox(label="I agree to sell my privacy", color="green", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", color="blue", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", color="red", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", color="orange", checked=True),
        dmc.Checkbox(label="I agree to sell my privacy", color="pink", checked=True),
    ],
)
