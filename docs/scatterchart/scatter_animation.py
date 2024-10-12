from random import randint
import dash_mantine_components as dmc
from dash import callback, Input, Output

component = dmc.Box(
    [
        dmc.Button("Update Chart", id="btn-scatterchart-animation"),
        dmc.ScatterChart(
            h=300,
            data=[{"color": "blue.5", "name": "Group 1", "data": [{}]}],
            scatterProps={
                "isAnimationActive": True,
                "animationDuration": 500,
                "animationEasing": "ease-in-out",
                "animationBegin": 500,
            },
            dataKey={"x": "x", "y": "y"},
            xAxisLabel="X data",
            yAxisLabel="Y data",
            id="scatterchart-animation",
        ),
    ]
)


@callback(
    Output("scatterchart-animation", "data"),
    Input("btn-scatterchart-animation", "n_clicks"),
)
def update(n):
    return [
        {
            "color": "blue.5",
            "name": "Group 1",
            "data": [
                {"x": randint(1000, 4000), "y": randint(1000, 4000)} for _ in range(20)
            ],
        }
    ]
