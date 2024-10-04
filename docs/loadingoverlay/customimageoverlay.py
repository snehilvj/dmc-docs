import time

import dash_mantine_components as dmc
from dash import Output, Input, no_update, callback, clientside_callback, dcc, html
from dash_iconify import DashIconify
import numpy as np
import plotly.graph_objs as go

x_data = np.linspace(0, 10, 100)
y_data = np.random.rand(100)

component = dmc.Box(
    children=[
        dmc.Stack(
            pos="relative",
            p=5,
            children=[
                dmc.LoadingOverlay(
                    visible=True,
                    id="loading-overlay",
                    loaderProps={
                        "variant": "custom",
                        "children": html.Img(src="/assets/custom_loadingoverlay.gif", style={"width": "120%", "height": "50%", "position": "relative", "left": "-10%"})
                    },
                    overlayProps={"radius": "sm", "blur": 2},
                ),
                dcc.Graph(
                    id='random-data-graph',
                    figure={
                        'data': [
                            go.Scatter(
                                x=x_data,
                                y=y_data,
                                mode='lines+markers',
                                name='Random Data'
                            )
                        ],
                        'layout': go.Layout(
                            title='Random Data Points',
                            xaxis={'title': 'X-axis'},
                            yaxis={'title': 'Y-axis'},
                            margin={'l': 40, 'b': 40, 't': 40, 'r': 10},
                            hovermode='closest'
                        )
                    },
                )
            ],
        ),
    ]
)

