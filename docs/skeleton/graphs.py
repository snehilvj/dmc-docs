import time

import dash_mantine_components as dmc
from dash import html, Output, Input, callback

from lib.utils import create_graph

component = html.Div(
    [
        dmc.Skeleton(
            visible=False,
            children=html.Div(id="skeleton-graph-container", children=create_graph()),
            mb=10,
        ),
        dmc.Button("Click Me!", id="graph-skeleton-button"),
    ]
)


@callback(
    Output("skeleton-graph-container", "children"),
    Input("graph-skeleton-button", "n_clicks"),
)
def update_graph(n_clicks):
    time.sleep(2)
    return create_graph()
