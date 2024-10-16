from random import randint
import dash_mantine_components as dmc
from dash import callback, Input, Output


def get_data(values):
    return [
        {"name": "A", "value": values[0], "color": "indigo.6"},
        {"name": "B", "value": values[1], "color": "yellow.6"},
        {"name": "C", "value": values[2], "color": "teal.6"},
        {"name": "C", "value": values[3], "color": "gray.6"},
    ]


component = dmc.Box(
    [
        dmc.Button("Update Chart", id="btn-donutchart-animation", n_clicks=0, mb="md"),
        dmc.DonutChart(
            id="donutchart-animation",
            data=get_data([100, 0, 0, 0]),
            pieProps={"isAnimationActive": True},
        ),
    ]
)


@callback(
    Output("donutchart-animation", "data"),
    Input("btn-donutchart-animation", "n_clicks"),
)
def update(n):
    if n % 2 == 0:
        return get_data([400, 300, 600, 100])
    return get_data([100, 0, 0, 0])
