import dash_mantine_components as dmc
from .data import data1

component = dmc.ScatterChart(
    h=350,
    data=data1,
    dataKey={"x": "age", "y": "BMI"},
    xAxisLabel="Age",
    yAxisLabel="BMI",
    referenceDots=[{"x": 46, "y": 35, "color": 'red.6', "label": 'Max BMI'}]
)
