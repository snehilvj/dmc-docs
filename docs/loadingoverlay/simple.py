import time

import dash_mantine_components as dmc
from dash import html, Output, Input, no_update, callback
from dash_iconify import DashIconify

component = html.Div(
    style={"width": 200},
    children=dmc.LoadingOverlay(
        dmc.Stack(
            id="loading-form",
            children=[
                dmc.TextInput(
                    label="Username",
                    placeholder="Your username",
                    icon=DashIconify(icon="radix-icons:person"),
                ),
                dmc.TextInput(
                    label="Password",
                    placeholder="Your password",
                    icon=DashIconify(icon="radix-icons:lock-closed"),
                ),
                dmc.Checkbox(
                    label="Remember me",
                    checked=True,
                ),
                dmc.Button(
                    "Login", id="load-button", variant="outline", fullWidth=True
                ),
            ],
        )
    ),
)


@callback(
    Output("loading-form", "children"),
    Input("load-button", "n_clicks"),
    prevent_initial_call=True,
)
def update(n_clicks):
    time.sleep(2)
    return no_update
