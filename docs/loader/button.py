import time

import dash_mantine_components as dmc
from dash import html, Input, Output, callback

component = html.Div([
    dmc.Button("Compute", id="load-btn", loaderProps={"type": "dots"} ),
    dmc.Text(id="load-output"),
])


@callback(
    Output("load-output", "children"),
    Input("load-btn", "n_clicks"),
    running=[(Output("load-btn", "loading"), True, False)],
)
def long_compute(n):
    time.sleep(2)
    return "Done " + str(time.time())
