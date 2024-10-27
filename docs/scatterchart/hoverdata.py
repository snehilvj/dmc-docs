from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data2

component = dmc.Group(
    [
        dmc.ScatterChart(
            id="figure-scatterchart-hover",
            h=300,
            data=data2,
            dataKey={"x": "age", "y": "BMI"},
            xAxisLabel="Age",
            yAxisLabel="BMI",
            withTooltip=False,
        ),
        dmc.Text(id="hoverdata-scatterchart1"),
        dmc.Text(id="hoverdata-scatterchart2"),
    ]
)

@callback(
    Output("hoverdata-scatterchart1", "children"),
    Output("hoverdata-scatterchart2", "children"),
    Input("figure-scatterchart-hover", "hoverData"),
    Input("figure-scatterchart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"


