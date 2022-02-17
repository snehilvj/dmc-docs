import time

import dash_mantine_components as dmc
from dash import callback  # no-prism
from dash import html, Output, Input, dcc

from lib.utils import create_figure

component = html.Div(
    [
        dmc.Skeleton(visible=False, children=dcc.Graph(id="skeleton-graph")),
        dmc.Space(h=10),
        dmc.Button("Update Graph", id="graph-skeleton-button"),
    ]
)


@callback(
    Output("skeleton-graph", "figure"),
    Input("graph-skeleton-button", "n_clicks"),
)
def update_graph(n_clicks):
    time.sleep(2)
    return create_figure()
