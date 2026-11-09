from dash import callback, Input, Output, State, ctx
import random
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.RollingNumber(id="rolling-number", value=1234, fz="36px"),
        dmc.Group(
            [
                dmc.Button("Increment", id="rn-increment"),
                dmc.Button("Decrement", id="rn-decrement"),
                dmc.Button("Random", id="rn-random"),
            ],
            mt="md",
        ),
    ]
)


@callback(
    Output("rolling-number", "value"),
    Input("rn-increment", "n_clicks"),
    Input("rn-decrement", "n_clicks"),
    Input("rn-random", "n_clicks"),
    State("rolling-number", "value"),
    prevent_initial_call=True,
)
def update_value(increment, decrement, random_click, value):
    print("value *********", value)
    if ctx.triggered_id == "rn-increment":
        return value + 1
    if ctx.triggered_id == "rn-decrement":
        return value - 1
    return random.randint(1000, 9999)