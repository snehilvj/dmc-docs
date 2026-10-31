import random

from dash import callback, Input, Output
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Stack(
            [
                dmc.Text("200ms", size="sm", c="dimmed"),
                dmc.RollingNumber(id="rn-number-200", value=500, animationDuration=200, fz="28px"),
            ],
            gap="xs",
        ),
        dmc.Stack(
            [
                dmc.Text("600ms (default)", size="sm", c="dimmed"),
                dmc.RollingNumber(id="rn-number-600", value=500, animationDuration=600, fz="28px"),
            ],
            gap="xs",
        ),
        dmc.Stack(
            [
                dmc.Text("1200ms", size="sm", c="dimmed"),
                dmc.RollingNumber(id="rn-number-1200", value=500, animationDuration=1200, fz="28px"),
            ],
            gap="xs",
        ),
        dmc.Button("Random", id="rn-random-button", w=200),
    ]
)


@callback(
    Output("rn-number-200", "value"),
    Output("rn-number-600", "value"),
    Output("rn-number-1200", "value"),
    Input("rn-random-button", "n_clicks"),
    prevent_initial_call=True,
)
def update_value(n):
    value = random.randint(0, 999)
    return value, value, value