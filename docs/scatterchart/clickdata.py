from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data2

component = dmc.Group(
    [
        dmc.ScatterChart(
            id="figure-scatterchart",
            h=300,
            data=data2,
            dataKey={"x": "age", "y": "BMI"},
            xAxisLabel="Age",
            yAxisLabel="BMI",
        ),
        dmc.Text(id="clickdata-scatterchart1"),
        dmc.Text(id="clickdata-scatterchart2"),
    ]
)

@callback(
    Output("clickdata-scatterchart1", "children"),
    Output("clickdata-scatterchart2", "children"),
    Input("figure-scatterchart", "clickData"),
    Input("figure-scatterchart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"


