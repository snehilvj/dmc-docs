import dash_mantine_components as dmc
from dash import html, Output, Input, callback


component = html.Div(
    [
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i) for i in ["USA", "Canada", "France"]]
            ),
            value="USA",
            label="Size Example - small",
            size="sm",
            mt=10,
        ),
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i) for i in ["USA", "Canada", "France"]]
            ),
            value="USA",
            label="Size Example - large",
            size="lg",
            mt=30,
        ),
    ]
)
