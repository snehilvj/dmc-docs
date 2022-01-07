import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Checkbox(
            label="I agree to sell my privacy",
            size="xs",
            checked=True,
            style={"marginBottom": 10},  # no-prism
        ),
        dmc.Checkbox(
            label="I agree to sell my privacy",
            size="sm",
            checked=True,
            style={"marginBottom": 10},  # no-prism
        ),
        dmc.Checkbox(
            label="I agree to sell my privacy",
            size="md",
            checked=True,
            style={"marginBottom": 10},  # no-prism
        ),
        dmc.Checkbox(
            label="I agree to sell my privacy",
            size="lg",
            checked=True,
            style={"marginBottom": 10},  # no-prism
        ),
        dmc.Checkbox(
            label="I agree to sell my privacy",
            size="xl",
            checked=True,
            style={"marginBottom": 10},  # no-prism
        ),
    ]
)
