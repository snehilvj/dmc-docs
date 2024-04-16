import time

import dash_mantine_components as dmc
from dash import Output, Input, no_update, callback, clientside_callback
from dash_iconify import DashIconify

component = dmc.Box(
    children=[
        dmc.Stack(
            pos="relative",
            p=5,
            w=300,
            children=[
                dmc.LoadingOverlay(
                    visible=False,
                    id="loading-overlay",
                    zIndex=1000,
                    overlayProps={"radius": "sm", "blur": 2},
                ),
                dmc.TextInput(
                    label="Username",
                    placeholder="Your username",
                    leftSection=DashIconify(icon="radix-icons:person"),
                    id="dummy-text-box",
                ),
                dmc.TextInput(
                    label="Password",
                    placeholder="Your password",
                    leftSection=DashIconify(icon="radix-icons:lock-closed"),
                ),
                dmc.Checkbox(
                    label="Remember me",
                    checked=True,
                ),
                dmc.Button(
                    "Login", id="load-button", variant="outline", fullWidth=True
                ),
            ],
        ),
    ]
)

clientside_callback(
    """
    function updateLoadingState(n_clicks) {
        return true
    }
    """,
    Output("loading-overlay", "visible", allow_duplicate=True),
    Input("load-button", "n_clicks"),
    prevent_initial_call=True,
)


@callback(
    Output("dummy-text-box", "children"),
    Output("loading-overlay", "visible"),
    Input("load-button", "n_clicks"),
    prevent_initial_call=True,
)
def update(n_clicks):
    time.sleep(3)
    return no_update, False
