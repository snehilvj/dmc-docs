import dash_mantine_components as dmc
from .data import data2

component = dmc.ScatterChart(
    h=300,
    data=data2,
    dataKey={"x": "age", "y": "BMI"},
    xAxisLabel="Age",
    yAxisLabel="BMI",
    withLegend=True,
)
