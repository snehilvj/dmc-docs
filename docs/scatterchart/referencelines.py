import dash_mantine_components as dmc
from .data import data1

component = dmc.ScatterChart(
    h=300,
    data=data1,
    dataKey={"x": "age", "y": "BMI"},
    xAxisLabel="Age",
    yAxisLabel="BMI",
    referenceLines=[
    {"y": 14, "label": "Underweight ↓", "color": "red.7"},
    {"y": 19, "label": "Normal weight", "color": "teal.7"},
    {"y": 30, "label": "Overweight ↑", "color": "red.7"}
    ]
)

