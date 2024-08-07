import dash_mantine_components as dmc
from .data import data1

component = dmc.ScatterChart(
    h=300,
    data=data1,
    dataKey={"x": "age", "y": "BMI"},
    tickLine="xy",
    yAxisProps={"tickMargin": 15, "orientation": "right"},
    xAxisProps={"tickMargin": 15, "orientation": "top"},
)
