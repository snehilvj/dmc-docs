import random
from dash import callback, Input, Output, State
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.RollingNumber(
            id="rolling-number2",
            value=99.99,
            prefix="$ ",
            suffix=" USD",
            decimalScale=2,
            fixedDecimalScale=True,
            thousandSeparator=True,
            fz="32px",
        ),
        dmc.Group(
            [
                dmc.Button("+10.50", id="rn-add-amount"),
                dmc.Button("-10.50", id="rn-subtract-amount"),
                dmc.Button("Random", id="rn-random-amount"),
            ],
            mt="md",
        ),
    ]
)


@callback(
    Output("rolling-number2", "value"),
    Input("rn-add-amount", "n_clicks"),
    Input("rn-subtract-amount", "n_clicks"),
    Input("rn-random-amount", "n_clicks"),
    State("rolling-number2", "value"),
    prevent_initial_call=True,
)
def update_value(add, subtract, random_click, value):
    from dash import ctx

    if ctx.triggered_id == "rn-add-amount":
        return round(value + 10.5, 2)
    if ctx.triggered_id == "rn-subtract-amount":
        return round(value - 10.5, 2)
    return round(random.random() * 10000, 2)