import dash_mantine_components as dmc
from .data import data1

component = dmc.ScatterChart(
    h=300,
    data=data1,
    dataKey={"x": "age", "y": "BMI"},
    xAxisLabel="Age",
    yAxisLabel="BMI",
    tooltipAnimationDuration=200
)
