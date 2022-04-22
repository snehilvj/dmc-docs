import time

import dash_mantine_components as dmc
from dash import html, Output, Input, callback

from lib.utils import create_graph

component = html.Div(
    [
        dmc.LoadingOverlay(
            html.Div(create_graph(), id="loading-customize-output"),
            loaderProps={"variant": "dots", "color": "orange", "size": "xl"},
        ),
        dmc.Button("Click Me!", id="customize-button"),
    ]
)


@callback(
    Output("loading-customize-output", "children"),
    Input("customize-button", "n_clicks"),
)
def func(n_clicks):
    time.sleep(2)
    return create_graph()
