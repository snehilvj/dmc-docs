import uuid
from time import sleep

import dash_mantine_components as dmc
from dash import html, callback, Output, Input, clientside_callback
from dash_iconify import DashIconify

component = html.Div(
    [
        dmc.Button(
            "Load from database",
            id="loading-button",
            leftSection=DashIconify(icon="fluent:database-plug-connected-20-filled"),
        ),
        dmc.Text(id="clicked-output", mt=10),
    ]
)

clientside_callback(
    """
    function updateLoadingState(n_clicks) {
        return true
    }
    """,
    Output("loading-button", "loading", allow_duplicate=True),
    Input("loading-button", "n_clicks"),
    prevent_initial_call=True,
)


@callback(
    Output("clicked-output", "children"),
    Output("loading-button", "loading"),
    Input("loading-button", "n_clicks"),
    prevent_initial_call=True,
)
def load_from_db(n_clicks):
    sleep(3)
    return str(uuid.uuid4()), False
