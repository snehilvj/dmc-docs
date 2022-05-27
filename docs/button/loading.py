import random
import time

import dash_mantine_components as dmc
from dash import callback, Output, html, Input, no_update

component = html.Div(
    [
        dmc.Text(
            "A random string will come here if you press the below button.",
            id="random-text",
        ),
        dmc.Space(h="md"),
        dmc.Button("Update Contents!", id="load-contents"),
    ]
)


@callback(
    Output("random-text", "children"),
    Output("load-contents", "children"),
    Input("load-contents", "n_clicks"),
    prevent_initial_call=True,
)
def update(n_clicks):
    time.sleep(2)
    return random.choice(["apple", "banana", "strawberry"]), no_update
