from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data1

component = dmc.Group(
    [
        dmc.ScatterChart(
            id="figure-scatterchart",
            h=300,
            data=data1,
            dataKey={"x": "age", "y": "BMI"},
            xAxisLabel="Age",
            yAxisLabel="BMI"
        ),
        dmc.Text(id="clickdata-scatterchart"),
    ]
)

@callback(
    Output("clickdata-scatterchart", "children"),
    Input("figure-scatterchart", "clickData"),
)
def update(clickdata):
    return str(clickdata)



